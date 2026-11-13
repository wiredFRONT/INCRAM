# Rule record: field list (pass 0)

Status: DRAFT for Jesse's review. Nothing here is accepted until it is in the ledger. Fields marked PROVISIONAL depend on an open item.

## Header fields

| Field | Required | Values | XCCDF 1.2 mapping | Basis |
|---|---|---|---|---|
| `id` | yes | opaque, permanent, never reused | `Rule/@id` | D18 |
| `title` | yes | short plain sentence | `Rule/title` | D15 |
| `layer` | yes | `L1-ai`, `L2-dev`, `L3-stack`, `L4-deps` | `Group` membership | D5 |
| `domain` | PROVISIONAL | `IN`, `CR`, `A`, `M` | second `Group` axis, or `metadata` | D35, open O10 |
| `config` | yes | `base`, `cranium` | `Profile` selection (`select/@selected`) | D36, D41 |
| `severity` | yes | `high`, `medium`, `low` (CAT I, II, III) | `Rule/@severity` | D15 |
| `status` | yes | `draft`, `accepted`, `deprecated`, `retired` | `Rule/status` | layout rule 5 |
| `version` | yes | rule's own revision | `Rule/version` | layout (CHANGELOG per rule) |
| `trigger` | yes | when the rule applies | none; partial fit `Rule/platform`. INCRAM extension | D15 |
| `source` | yes | list: authority, document, pin, URL | `Rule/reference`, `Rule/ident` (CCI) | D15, canonical sources |
| `extends` | no | one rule ID | `Rule/@extends`, Table 33 merge behavior | D15 |
| `requires` / `conflicts` | no | rule IDs | `Rule/requires`, `Rule/conflicts` | layout rule 4 |
| `feedback` | yes | `on`, `off` (ask once, after the fix is used) | none. INCRAM extension | D15 |
| `license` | PROVISIONAL | SPDX identifier per record | `metadata` (`dc:rights`) | research, open O8 |
| `provenance` | PROVISIONAL | imported-from ID, release, content hash | `metadata` | research, open O8 |
| `verification` | PROVISIONAL | who or what checked it, when | `metadata` | research, open O8 |

## Body sections

| Section | Required | XCCDF 1.2 mapping |
|---|---|---|
| Simple | yes | `Rule/description` |
| Why | no | `Rule/rationale` |
| How to tell | yes | `Rule/check/check-content` (points at `check.py`) |
| What to say | yes | `Rule/fixtext` |
| Rot guards | yes | none; nearest `Rule/warning`. INCRAM extension |

## What has no XCCDF home

`trigger`, `feedback` and Rot guards. They export inside `Rule/metadata` under an INCRAM namespace so an XCCDF consumer ignores them without breaking.

## Depends on open items

- O10: whether `domain` is required on every rule (two axes) or only on `L1-ai` rules (breakdown).
- O8: whether `license`, `provenance` and `verification` are added, and whether every field except `name` and `description` moves inside the skill `metadata` field so a rule loads as a skill.
- ID format (prefix, length, issuing) is still open in the layout document.

## Not in this pass

The JSON Schema file, the profile schema, and the linter. Those follow once this list is ruled on.