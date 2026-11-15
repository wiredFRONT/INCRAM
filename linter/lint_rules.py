#!/usr/bin/env python3
"""INCRAM rule linter. Enforces the folder standard in docs/design/library-layout.md.

Usage: python3 linter/lint_rules.py [folder ...]      (needs: pip install jsonschema pyyaml)
With no folder it lints every rule under reference/ and layers/.
Exit code 0 only if every rule passes every check.

Checks, per rule folder:
  1. Required files exist: rule.md, check.py, check.test.py, CHANGELOG.md, fixtures/pass, fixtures/fail.
  2. rule.md starts with a header that matches schema/rule.schema.json.
  3. The folder name starts with the rule's ID, and the ID is in registry/ids.yaml exactly once.
  4. extends, requires and conflicts point only at IDs in the registry.
  5. Required sections exist, in order: Simple, How to tell, What to say, Rot guards.
  6. Every paragraph and list item in the body carries a label: UPSTREAM or INCRAM (D12).
  7. The next review is at most twelve months after the last (D49).
  8. check.py passes fixtures/pass and fails fixtures/fail.
  9. check.test.py passes.
"""
import datetime
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED_FILES = ["rule.md", "check.py", "check.test.py", "CHANGELOG.md"]
REQUIRED_DIRS = ["fixtures/pass", "fixtures/fail"]
REQUIRED_SECTIONS = ["Simple", "How to tell", "What to say", "Rot guards"]
LABEL = re.compile(r"^(?:[-*]\s+|\d+\.\s+)?(UPSTREAM|INCRAM)\b")

schema = json.loads((ROOT / "schema" / "rule.schema.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema, format_checker=FormatChecker())
registry = yaml.safe_load((ROOT / "registry" / "ids.yaml").read_text(encoding="utf-8"))["ids"]
registered = [entry["id"] for entry in registry]


def split_rule(text):
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        return None, text
    header = json.loads(json.dumps(yaml.safe_load(match.group(1)), default=str))
    return header, match.group(2)


def unlabeled_blocks(section_text):
    """Each section must state its label once at the start, or label every block."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n", section_text) if b.strip()]
    if blocks and LABEL.match(blocks[0]) and not blocks[0].startswith(("-", "*")) and not re.match(r"\d+\.", blocks[0]):
        section_label = True
    else:
        section_label = False
    missing = []
    for block in blocks:
        lines = [l for l in block.splitlines() if l.strip()]
        is_list = all(re.match(r"^\s*(?:[-*]|\d+\.)\s+", l) for l in lines)
        if LABEL.match(lines[0]):
            continue
        if section_label:
            continue
        if is_list and all(LABEL.match(l.strip()) for l in lines):
            continue
        missing.append(lines[0][:60])
    return missing


def lint(folder):
    problems = []
    for name in REQUIRED_FILES:
        if not (folder / name).is_file():
            problems.append(f"missing file {name}")
    for name in REQUIRED_DIRS:
        if not (folder / name).is_dir() or not any((folder / name).iterdir()):
            problems.append(f"missing or empty folder {name}")
    if problems:
        return problems

    header, body = split_rule((folder / "rule.md").read_text(encoding="utf-8"))
    if header is None:
        return ["rule.md has no header block"]
    for error in sorted(validator.iter_errors(header), key=lambda e: list(e.path)):
        problems.append(f"header: {'/'.join(map(str, error.path)) or '(top)'}: {error.message}")
    rule_id = header.get("id", "")
    if not folder.name.startswith(rule_id + "-"):
        problems.append(f"folder name must start with the rule ID {rule_id!r}")
    if registered.count(rule_id) != 1:
        problems.append(f"ID {rule_id!r} appears {registered.count(rule_id)} times in registry/ids.yaml; it must appear once")
    for field in ("extends", "requires", "conflicts"):
        value = header.get(field, [])
        for target in [value] if isinstance(value, str) else value:
            if target not in registered:
                problems.append(f"{field} points at unknown ID {target!r}")
            if target == rule_id:
                problems.append(f"{field} points at the rule itself")

    sections = re.findall(r"^## (.+?)\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    names = [name.strip() for name, _ in sections]
    present = [name for name in names if name in REQUIRED_SECTIONS]
    if present != REQUIRED_SECTIONS:
        problems.append(f"required sections, in order, are {REQUIRED_SECTIONS}; found {present}")
    for name, text in sections:
        for start in unlabeled_blocks(text):
            problems.append(f"section {name!r}: no UPSTREAM or INCRAM label on: {start!r}")

    review = header.get("review")
    if review:
        try:
            last = datetime.date.fromisoformat(review["last"])
            due = datetime.date.fromisoformat(review["due"])
            if due <= last:
                problems.append("review.due must be after review.last")
            if (due - last).days > 366:
                problems.append("review.due is more than twelve months after review.last")
        except (ValueError, KeyError, TypeError):
            problems.append("review dates are not valid dates")

    spec = importlib.util.spec_from_file_location(f"check_{rule_id.replace('-', '_')}", folder / "check.py")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        if module.result(module.scan(folder / "fixtures" / "pass")) != "pass":
            problems.append("check.py does not pass fixtures/pass")
        if module.result(module.scan(folder / "fixtures" / "fail")) != "fail":
            problems.append("check.py does not fail fixtures/fail")
    except Exception as error:  # a broken check is a lint failure, not a crash
        problems.append(f"check.py could not run: {error}")

    tests = subprocess.run([sys.executable, str(folder / "check.test.py")], capture_output=True, text=True)
    if tests.returncode != 0:
        problems.append("check.test.py failed: " + tests.stderr.strip().splitlines()[-1])
    return problems


def find_rules():
    found = []
    for base in ("reference", "layers"):
        found += [p.parent for p in (ROOT / base).rglob("rule.md")] if (ROOT / base).exists() else []
    return sorted(found)


if __name__ == "__main__":
    folders = [pathlib.Path(a).resolve() for a in sys.argv[1:]] or find_rules()
    failed = 0
    seen = {}
    for folder in folders:
        problems = lint(folder)
        header, _ = split_rule((folder / "rule.md").read_text(encoding="utf-8")) if (folder / "rule.md").is_file() else (None, "")
        label = folder.relative_to(ROOT) if folder.is_relative_to(ROOT) else folder
        if header and header.get("id") in seen:
            problems.append(f"ID already used by {seen[header['id']]}")
        elif header:
            seen[header.get("id")] = label
        if problems:
            failed += 1
            print(f"FAIL  {label}")
            for problem in problems:
                print(f"        {problem}")
        else:
            print(f"ok    {label}")
    print(f"{len(folders)} rule(s) linted, {failed} failed")
    sys.exit(1 if failed else 0)
