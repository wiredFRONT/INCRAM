# Rule record: field list (pass 0, revision 2)

Status: DRAFT for Jesse's review. Nothing here is accepted until it is in the ledger.

Revision 2 applies the second-model cross-check of 2026-11-12 (`../docs/research/cross-check/codex-1-field-list.md`), which the reviewer reports it verified against NIST IR 7275 Rev 4 (XCCDF 1.2). Marks used below:

- PROVISIONAL: waits on an open item in the ledger.
- PROPOSED: added in this revision from a decision or the cross-check; not yet ruled on.

## Header fields

| Field | Required | Values | XCCDF 1.2 mapping | Merge on `extends` | Basis |
|---|---|---|---|---|---|
| `id` | yes | opaque, permanent, never reused | `Rule/@id`, encoded on export as `xccdf_<namespace>_rule_<id>` (required pattern) | not inherited | D18 |
| `title` | yes | short plain sentence | `Rule/title` | override | D13 |
| `layer` | yes | `L1-ai`, `L2-dev`, `L3-stack`, `L4-deps` | `Group` membership (the one structural axis) | n/a | D5 |
| `domain` | yes | `IN`, `CR`, `A`, `M` | `Rule/metadata`. Groups form a tree, so a second independent axis cannot also be Groups | INCRAM rule needed | D35, D42 |
| `config` | yes | `base`, `cranium` | membership in a named `Profile` (`base`, `cranium`). `select/@selected` is only true or false | n/a | D36, D41 |
| `severity` | yes | `high`, `medium`, `low` | `Rule/@severity`. XCCDF also allows `unknown` and `info`. CAT I, II, III is the DISA convention for high, medium, low, not part of XCCDF | replace | D13, D46 |
| `status` | yes | `incomplete`, `draft`, `interim`, `accepted`, `deprecated` | `Rule/status`. `retired` is not an XCCDF value; a retired rule exports as `deprecated` with a retirement date in metadata | not inherited | layout rule 5 |
| `version` | yes | rule's own revision | `Rule/version` | replace | layout |
| `trigger` | yes | when the rule applies | CPE platform applicability only fits `Rule/platform`; every other trigger goes in `Rule/metadata` | INCRAM rule needed | D13 |
| `references` | yes | list: authority, document, pin, URL | `Rule/reference` | override | D13, D31 |
| `idents` | no | list: naming-system URI plus value (CCI, CVE, CWE) | `Rule/ident` with `@system` | append | cross-check |
| `extends` | no | one rule ID | `Rule/@extends`. The parent must be a Rule visible in the same Benchmark | not inherited | D13 |
| `requires` / `conflicts` | no | rule or group IDs | `Rule/requires`, `Rule/conflicts`. These constrain selection, not execution order. IDs in one `requires` are alternatives; separate `requires` are each required | append | layout rule 4 |
| `feedback` | yes | `on`, `off` (ask once, after the fix is used) | `Rule/metadata` | INCRAM rule needed | D13, D14 |
| `origin` | PROPOSED | `UPSTREAM`, `INCRAM` | `Rule/metadata` | INCRAM rule needed | D12 |
| `override_why` | PROPOSED | text, required when a rule overrides a less specific layer | `Rule/metadata`; in a profile, `Profile/.../remark` | n/a | D10 |
| `review` | PROPOSED | last reviewed date, next review due (at most 12 months apart) | dated `Rule/status` plus `Rule/metadata` | not inherited | D49 |
| `mitigation` | PROPOSED | the mitigation, its evidence, resulting severity | `Rule/metadata`; result side belongs in the assessment record, not the rule | n/a | D46 |
| `maturity` | PROPOSED | `srg-config` (under the generalized SRG) or `own-stig` | `Rule/metadata` | n/a | D51 |
| `tier` | PROVISIONAL | `foundational`, `managed`, `advanced` | named `Profile` per tier | n/a | D52, open O12 |
| `license` | PROVISIONAL | SPDX identifier per record | `Rule/metadata` (`dc:rights`). A permitted representation, not a native licensing field | INCRAM rule needed | research, open O8 |
| `provenance` | PROVISIONAL | imported-from ID, release, content hash | `Rule/metadata` | not inherited | research, open O8 |
| `verification` | PROVISIONAL | who or what checked it, when | `Rule/metadata` | not inherited | research, open O8 |

"INCRAM rule needed": XCCDF's inheritance table assigns no merge model to `metadata`, so INCRAM must state one for each of these fields.

## Body sections

| Section | Required | XCCDF 1.2 mapping | Merge on `extends` |
|---|---|---|---|
| Simple | yes | `Rule/description` | override |
| Why | no | `Rule/rationale` | override |
| How to tell | yes | prose: `Rule/check/check-content`. The script: a second `Rule/check` with its own `@system` URI and `check-content-ref/@href` pointing at `check.py` | replace, per check system |
| What to say | yes | `Rule/fixtext`, for the remediation guidance only. Executable remediation, if ever added, belongs in `Rule/fix` | override |
| Rot guards | yes | user-facing cautions fit `Rule/warning`; the upkeep meaning stays in `Rule/metadata` | override / INCRAM rule needed |

XCCDF "override" means the child's value is appended to the parent's unless the child sets `override="true"`, which replaces it.

## Outside the rule record

The cross-check listed XCCDF properties with no place here. They belong to other schemas, not to each rule:

- Benchmark: identity, release version and status, platform, notices, scoring model.
- Group: ID, title, description, references.
- Profile: identity, title, selections, refinements, value settings, `remark`.
- Rule properties left at XCCDF defaults for now: `weight`, `selected`, `role`, `multiple`, complex checks, check exports.

## Custom fields in XCCDF

Namespaced XML inside `Rule/metadata` is valid XCCDF. It must not replace a native field or change how XCCDF assessment is processed. A consumer may display or skip it.

## Design gaps for Jesse (ledger opens)

- O15: `extends` across repositories. XCCDF requires the parent in the same Benchmark, and INCRAM is one repository per baseline.
- O16: how the Unified dimension of CRANIUM is represented.
- O12: tiers versus `base` and `cranium`, including whether base rules stay selected in CRANIUM.
- O8: `license`, `provenance`, `verification`, and whether extra header fields move inside the skill `metadata` field.
- ID format (prefix, length, issuing) is still open in the layout document.

## Not in this pass

The JSON Schema file, the profile, group and benchmark schemas, and the linter.
