# schema

Owned by the umbrella and used by every baseline repository. Everything here is a draft until it is in the ledger.

| File | What it is | Status |
|---|---|---|
| `rule-fields.md` | The field list for a rule record, mapped to XCCDF 1.2, corrected by the second-model cross-check | draft, revision 2 |
| `rule.schema.json` | The JSON Schema for the header at the top of every `rule.md` | draft 0.1 |

Not yet written: the profile, group and benchmark schemas, and the XCCDF export.

Enforced by `../linter/lint_rules.py`. A worked rule that passes it: `../reference/layers/L2-dev/secrets/r-4k7q2m-no-secrets-in-code/`.

Still open and affecting these files (see `../docs/decisions/ledger.md`): O8 (license, provenance, verification; skill metadata), O12 (tiers), O13 (what CAT I gates), O15 (`extends` across repositories), O16 (the Unified dimension), and the ID format.
