#!/usr/bin/env python3
"""Verify every rule's links into the official catalogs, against the files pinned in registry/sources.yaml.

Usage: python3 linter/verify_links.py [--cache DIR] [--offline]     (needs: pip install pyyaml)

What it does:
  1. Fetches each pinned source into the cache (unless present) and compares its hash with the pin.
     A different hash, or a newer release found by probing, is reported as UPSTREAM CHANGED: the
     trigger to re-review the rules that cite that source (D49, D50).
  2. For every rule.md under reference/ and layers/:
       references   the control exists in the pinned catalog and the rule's provenance hash is the pin's
       idents       each CCI exists and maps to the stated control and revision; each CWE exists by that name
       associated   each STIG rule exists in the pinned release with that group, rule ID, STIG ID, SRG,
                    severity, title and CCI list
       completeness no rule in a pinned benchmark cites one of the rule's CCIs without being listed

Exit code: 0 all verified and nothing changed upstream; 1 a link failed; 2 links hold but upstream changed.
Downloaded files are data. They are parsed, never executed.
"""
import argparse
import hashlib
import io
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
CCI_SYSTEM = "http://cyber.mil/cci"
CWE_SYSTEM = "https://cwe.mitre.org/"


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def fetch(source, cache, offline):
    target = cache / (source["id"] + pathlib.Path(source["url"]).suffix)
    if not target.exists():
        if offline:
            return None
        with urllib.request.urlopen(source["url"], timeout=120) as response:
            target.write_bytes(response.read())
    return target.read_bytes()


def probe(url):
    try:
        request = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status == 200
    except (urllib.error.URLError, TimeoutError):
        return False


def member(source, data):
    if "member" not in source:
        return data
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        return archive.read(source["member"])


def ns(root):
    return root.tag.split("}")[0].strip("{")


def parse_oscal(data):
    controls = {}

    def walk(items):
        for control in items:
            controls[control["id"]] = control
            walk(control.get("controls", []))

    for group in json.loads(data)["catalog"]["groups"]:
        walk(group.get("controls", []))
    return controls


def parse_cci(data):
    root = ET.fromstring(data)
    n = ns(root)
    items = {}
    for item in root.iter(f"{{{n}}}cci_item"):
        items[item.get("id")] = {(ref.get("index", "").strip(), ref.get("version")) for ref in item.iter(f"{{{n}}}reference")}
    return items


def parse_xccdf(data):
    root = ET.fromstring(data)
    n = ns(root)
    release = ""
    for text in root.findall(f"{{{n}}}plain-text"):
        if text.get("id") == "release-info":
            found = re.search(r"Release:\s*(\d+)", text.text or "")
            release = f"V{root.findtext(f'{{{n}}}version')}R{found.group(1)}" if found else ""
    groups = {}
    for group in root.findall(f"{{{n}}}Group"):
        rule = group.find(f"{{{n}}}Rule")
        groups[group.get("id")] = {
            "rule": rule.get("id"),
            "severity": rule.get("severity"),
            "stig_id": rule.findtext(f"{{{n}}}version"),
            "srg": group.findtext(f"{{{n}}}title"),
            "title": rule.findtext(f"{{{n}}}title"),
            "cci": sorted(i.text for i in rule.findall(f"{{{n}}}ident") if i.get("system") == CCI_SYSTEM),
        }
    return {"id": root.get("id"), "release": release, "groups": groups}


def parse_cwe(data):
    root = ET.fromstring(data)
    n = ns(root)
    return {"CWE-" + w.get("ID"): w.get("Name") for w in root.iter(f"{{{n}}}Weakness")}


PARSERS = {"oscal-catalog": parse_oscal, "cci-list": parse_cci, "xccdf-benchmark": parse_xccdf, "cwe-catalog": parse_cwe}


def rule_headers():
    for base in ("reference", "layers"):
        if not (ROOT / base).exists():
            continue
        for path in sorted((ROOT / base).rglob("rule.md")):
            match = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
            if match:
                yield path.parent.relative_to(ROOT), json.loads(json.dumps(yaml.safe_load(match.group(1)), default=str))


def verify_rule(header, sources, parsed):
    problems = []

    def need(source_id):
        if source_id not in sources:
            problems.append(f"source {source_id!r} is not in registry/sources.yaml")
            return None
        if source_id not in parsed:
            problems.append(f"source {source_id!r} could not be loaded")
            return None
        return parsed[source_id]

    provenance = header.get("provenance", {})
    for reference in header.get("references", []):
        source_id = reference.get("source")
        if not source_id:
            continue
        catalog = need(source_id)
        if catalog is None:
            continue
        if sources[source_id]["kind"] == "oscal-catalog":
            control = catalog.get(provenance.get("imported_from"))
            if control is None:
                problems.append(f"control {provenance.get('imported_from')!r} is not in {source_id}")
            elif control["title"] not in reference["locator"]:
                problems.append(f"locator does not carry the control's title {control['title']!r}")
            if provenance.get("sha256") != sources[source_id]["sha256"]:
                problems.append(f"provenance hash is not the pinned hash of {source_id}")

    rule_ccis = set()
    for ident in header.get("idents", []):
        catalog = need(ident["source"])
        if catalog is None:
            continue
        if ident["system"] == CCI_SYSTEM:
            rule_ccis.add(ident["value"])
            mappings = catalog.get(ident["value"])
            if mappings is None:
                problems.append(f"{ident['value']} is not in the CCI list")
            elif (ident.get("control"), ident.get("control_revision")) not in mappings:
                problems.append(f"{ident['value']} does not map to {ident.get('control')} revision {ident.get('control_revision')} in the CCI list")
        elif ident["system"] == CWE_SYSTEM:
            name = catalog.get(ident["value"])
            if name is None:
                problems.append(f"{ident['value']} is not in the CWE list")
            elif name != ident.get("title"):
                problems.append(f"{ident['value']} is named {name!r} in the CWE list, not {ident.get('title')!r}")
        else:
            problems.append(f"no verifier for ident system {ident['system']!r}")

    listed = set()
    for item in header.get("associated", []):
        benchmark = need(item["source"])
        if benchmark is None:
            continue
        listed.add((item["source"], item["group"]))
        if benchmark["id"] != item["benchmark"]:
            problems.append(f"{item['group']}: benchmark is {benchmark['id']!r}, not {item['benchmark']!r}")
        if benchmark["release"] != item["release"]:
            problems.append(f"{item['group']}: pinned release is {benchmark['release']}, rule says {item['release']}")
        actual = benchmark["groups"].get(item["group"])
        if actual is None:
            problems.append(f"{item['group']} is not in {item['benchmark']} {benchmark['release']}")
            continue
        for field in ("rule", "severity", "stig_id", "srg", "title"):
            if field in item and actual[field] != item[field]:
                problems.append(f"{item['group']}: {field} is {actual[field]!r} in the STIG, rule says {item[field]!r}")
        if actual["cci"] != sorted(item["cci"]):
            problems.append(f"{item['group']}: CCIs are {actual['cci']} in the STIG, rule says {sorted(item['cci'])}")
        for cci in item["cci"]:
            if cci not in rule_ccis:
                problems.append(f"{item['group']} cites {cci}, which the rule does not carry in idents")

    for source_id, source in sources.items():
        if source["kind"] != "xccdf-benchmark" or source_id not in parsed:
            continue
        for group_id, actual in parsed[source_id]["groups"].items():
            if rule_ccis.intersection(actual["cci"]) and (source_id, group_id) not in listed:
                problems.append(f"{group_id} in {source_id} cites {sorted(rule_ccis.intersection(actual['cci']))} but is not listed under associated")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--cache", default=str(pathlib.Path.home() / ".cache" / "incram-sources"))
    parser.add_argument("--offline", action="store_true", help="use only files already in the cache; skip release probes")
    args = parser.parse_args()
    cache = pathlib.Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)

    registry = yaml.safe_load((ROOT / "registry" / "sources.yaml").read_text(encoding="utf-8"))
    sources = {s["id"]: json.loads(json.dumps(s, default=str)) for s in registry["sources"]}
    parsed, changed = {}, 0
    for source_id, source in sources.items():
        try:
            data = fetch(source, cache, args.offline)
        except (urllib.error.URLError, TimeoutError) as error:
            print(f"UNREACHABLE      {source_id}: {error}")
            continue
        if data is None:
            print(f"NOT CACHED       {source_id}")
            continue
        if sha256(data) != source["sha256"]:
            changed += 1
            print(f"UPSTREAM CHANGED {source_id}: hash differs from the pin ({source['version']})")
        else:
            print(f"pinned           {source_id} {source['version']}")
        if not args.offline:
            for url in source.get("detector", {}).get("next", []):
                if probe(url):
                    changed += 1
                    print(f"UPSTREAM CHANGED {source_id}: a newer release exists at {url}")
        parsed[source_id] = PARSERS[source["kind"]](member(source, data))

    failed = 0
    count = 0
    for folder, header in rule_headers():
        count += 1
        problems = verify_rule(header, sources, parsed)
        links = len(header.get("idents", [])) + len(header.get("associated", [])) + sum(1 for r in header.get("references", []) if r.get("source"))
        if problems:
            failed += 1
            print(f"FAIL  {folder}")
            for problem in problems:
                print(f"        {problem}")
        else:
            print(f"ok    {folder}: {links} links verified")
    print(f"{count} rule(s), {failed} failed, {changed} upstream change(s)")
    sys.exit(1 if failed else (2 if changed else 0))


if __name__ == "__main__":
    main()
