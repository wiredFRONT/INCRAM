#!/usr/bin/env python3
"""Check for rule r-4k7q2m: no secrets written into the code.

Usage: python3 check.py <project-folder>
Exit code: 0 = none found, 1 = definite finding, 2 = only possible findings (a person must look).
The secret itself is never printed.
"""
import pathlib
import re
import sys

SKIP_DIRS = {".git", "node_modules", "dist", "build", "vendor", ".venv", "__pycache__"}
MAX_BYTES = 1_000_000

DEFINITE = [
    ("private key block", re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY(?: BLOCK)?-----")),
    ("cloud access key ID", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("source-control token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("live payment secret key", re.compile(r"\b[sr]k_live_[0-9A-Za-z]{24,}\b")),
]
SECRET_NAME = r"(?:password|passwd|pwd|secret|token|api[_-]?key|private[_-]?key|access[_-]?key)"
ASSIGNED = re.compile(r"(?i)\b[\w.-]*" + SECRET_NAME + r"[\w.-]*\s*[:=]\s*[\"']([^\"'\s]{8,})[\"']")
ENV_LINE = re.compile(r"(?i)^\s*(?:export\s+)?([A-Z0-9_]*" + SECRET_NAME + r"[A-Z0-9_]*)\s*=\s*(\S+)")
PLACEHOLDER = re.compile(r"(?i)^[\"']?(?:<.*>|\$\{.*\}|\{\{.*\}\}|x{3,}|\*{3,}|change[-_]?me|your[-_].*|example.*|placeholder.*|todo.*|none|null|true|false)[\"']?$")
SAMPLE_ENV = re.compile(r"(?i)\.(?:example|sample|template|dist)$")


def _is_env_file(path):
    return path.name.startswith(".env") and not SAMPLE_ENV.search(path.name)


def scan(root):
    """Return a list of (level, relative path, line number, kind). level is "definite" or "possible"."""
    root = pathlib.Path(root)
    findings = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or SKIP_DIRS.intersection(path.relative_to(root).parts):
            continue
        if path.stat().st_size > MAX_BYTES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        rel = path.relative_to(root).as_posix()
        for number, line in enumerate(text.splitlines(), start=1):
            hit = next((kind for kind, pattern in DEFINITE if pattern.search(line)), None)
            if hit:
                findings.append(("definite", rel, number, hit))
                continue
            match = ASSIGNED.search(line)
            if match and not PLACEHOLDER.match(match.group(1)):
                findings.append(("possible", rel, number, "value assigned to a secret-like name"))
                continue
            if _is_env_file(path):
                match = ENV_LINE.match(line)
                if match and not PLACEHOLDER.match(match.group(2)):
                    findings.append(("possible", rel, number, "real value in an environment file"))
    return findings


def result(findings):
    """pass, fail or review."""
    if any(level == "definite" for level, *_ in findings):
        return "fail"
    return "review" if findings else "pass"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    found = scan(sys.argv[1])
    for level, rel, number, kind in found:
        print(f"{level}: {rel}:{number}: {kind}")
    outcome = result(found)
    print({"pass": "none found", "fail": "definite finding", "review": "possible findings: a person must look"}[outcome])
    sys.exit({"pass": 0, "fail": 1, "review": 2}[outcome])
