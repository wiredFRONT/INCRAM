# r-4k7q2m changelog

## 0.2.0 (2026-11-16)
- Added the chain from official files: two CCIs, the SRG, the Application Security and Development STIG V6R5 rule V-222642, and CWE-798. Each is verified by `linter/verify_links.py` against the files pinned in `registry/sources.yaml`.
- Still not done: second-model check; history scanning in `check.py`; the mitigation needs Jesse's review.

## 0.1.0 (2026-11-15)
- First draft. Source: NIST SP 800-53 Rev 5.2.0 IA-5(7), read from the official OSCAL catalog.
- Not yet done: second-model check of this rule; a CCI and CWE identifier (not added because neither was read from its official source); history scanning in `check.py`; the mitigation needs Jesse's review.
