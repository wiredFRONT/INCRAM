# reference

Reference rules. They exist to prove the schema, the folder standard and the linter on real content before any baseline repository is created. Each one moves to its baseline repository when that exists; its ID does not change.

| ID | Rule | Severity | Source | Status |
|---|---|---|---|---|
| `r-4k7q2m` | No passwords, API keys or private keys written into the code | high (CAT I) | NIST SP 800-53 Rev 5.2.0, IA-5(7), read from the official OSCAL catalog | draft 0.1.0; not yet checked by a second model |

Run the linter over everything here:

```
pip install jsonschema pyyaml
python3 linter/lint_rules.py
```
