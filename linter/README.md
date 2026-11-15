# linter

`lint_rules.py` makes the folder standard machine-enforced (layout rule 10). It fails when a rule folder is missing a required file, its header does not match `../schema/rule.schema.json`, its ID is not in `../registry/ids.yaml` exactly once, a reference points at an unknown ID, a required section is missing, a statement carries no UPSTREAM or INCRAM label, the next review is more than twelve months out, the check does not pass and fail its fixtures, or the rule's own tests fail.

```
pip install jsonschema pyyaml
python3 linter/lint_rules.py            # every rule under reference/ and layers/
python3 linter/lint_rules.py <folder>   # one rule
```

Not yet done: packaging as a reusable CI action (D29), a check that a profile override carries a `why`, and a check that the source URL is on the canonical sources list.
