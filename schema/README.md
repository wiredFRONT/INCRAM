# schema

Field list drafted in `rule-fields.md` (awaiting review). JSON Schema not yet written. This folder will hold the rule schema and the profile schema (JSON Schema), owned by the umbrella and used by every baseline repository.

Inputs already decided (see `../docs/decisions/ledger.md`):
- Rule record: header (id, layer, title, severity, trigger, source, extends, feedback) plus Simple / How to tell / What to say / Rot guards.
- Opaque permanent IDs; layer is a field.
- Field-mapped to XCCDF, copying its merge behavior for `extends`.
- Pending ruling: extra header fields move inside the standard skill `metadata` field so rules load as skills.
- Pending additions from research: `license` per record, provenance block, verification record.
