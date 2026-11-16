#!/usr/bin/env python3
"""Check the links between the INCRAM umbrella and the repositories in registry/modules.yaml.

Usage: python3 linter/check_modules.py [--module NAME=PATH ...]     (needs: pip install pyyaml)

For each module:
  1. It is declared in .gitmodules at the path the registry gives, with the same repository.
  2. If a checkout is available (the submodule itself, or a path given with --module):
       - its link file names this umbrella;
       - every INCRAM rule ID it says it implements exists in registry/ids.yaml and is active;
       - the commit pinned here is reported against the checkout's commit.
A module that is not checked out is reported and skipped, never failed: modules are optional.
Prints which rule is enforced where, and which rules nothing enforces yet.
Exit code 0 unless a link is broken.
"""
import argparse
import configparser
import json
import pathlib
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent


def git(args, cwd):
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def same_repo(a, b):
    norm = lambda u: u.lower().removesuffix(".git").rstrip("/")
    return norm(a) == norm(b)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--module", action="append", default=[], metavar="NAME=PATH")
    args = parser.parse_args()
    overrides = dict(item.split("=", 1) for item in args.module)

    modules = yaml.safe_load((ROOT / "registry" / "modules.yaml").read_text(encoding="utf-8"))["modules"]
    ids = {e["id"]: e for e in yaml.safe_load((ROOT / "registry" / "ids.yaml").read_text(encoding="utf-8"))["ids"]}
    gitmodules = configparser.ConfigParser()
    gitmodules.read(ROOT / ".gitmodules", encoding="utf-8")
    declared = {gitmodules[s]["path"]: gitmodules[s]["url"] for s in gitmodules.sections()}

    problems, enforced = [], {}
    for module in modules:
        name, path = module["name"], module["path"]
        if path not in declared:
            problems.append(f"{name}: {path} is not declared in .gitmodules")
        elif not same_repo(declared[path], module["repo"]):
            problems.append(f"{name}: .gitmodules points at {declared[path]}, the registry says {module['repo']}")
        pinned = git(["ls-files", "-s", path], ROOT).split()
        pinned = pinned[1] if len(pinned) > 1 else ""
        print(f"module {name}: pinned at {pinned[:7] or 'nothing'}")

        checkout = pathlib.Path(overrides.get(name, ROOT / path)).resolve()
        if not (checkout / module["link_file"]).is_file():
            print(f"module {name}: not checked out at {checkout}; links not checked (modules are optional)")
            continue
        head = git(["rev-parse", "HEAD"], checkout)
        if head and pinned and head != pinned:
            print(f"module {name}: checkout is at {head[:7]}, which is not the pinned commit")
        link = yaml.safe_load((checkout / module["link_file"]).read_text(encoding="utf-8"))
        if not same_repo(link["umbrella"]["repo"], "https://github.com/wiredFRONT/INCRAM"):
            problems.append(f"{name}: its link file names {link['umbrella']['repo']} as the umbrella")
        for provided in module.get("provides", []):
            if not (checkout / provided).is_file():
                problems.append(f"{name}: the registry says it provides {provided}, which does not exist")
        for guard_file in sorted(checkout.rglob("*.guard.json")):
            guard = json.loads(guard_file.read_text(encoding="utf-8"))
            for rule_id in guard.get("implements", []):
                where = f"{name}:{guard_file.relative_to(checkout).as_posix()}"
                if rule_id not in ids:
                    problems.append(f"{where} implements {rule_id}, which is not in registry/ids.yaml")
                elif ids[rule_id]["state"] != "active":
                    problems.append(f"{where} implements {rule_id}, which is {ids[rule_id]['state']}")
                else:
                    enforced.setdefault(rule_id, []).append(where)

    for rule_id in sorted(ids):
        if rule_id in enforced:
            print(f"link   {rule_id} is enforced by {', '.join(enforced[rule_id])}")
        else:
            print(f"       {rule_id} is not enforced by any module yet")
    for problem in problems:
        print(f"FAIL   {problem}")
    print(f"{len(modules)} module(s), {len(problems)} broken link(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
