# Library layout: canonical file and folder standard

Status: ACCEPTED by Jesse 2026-11-12 (ledger D15, D30). Principle: strict, hyper-modular, co-located. Applies inside each baseline repository.

## Layout
```
library/
  schema/                      rule and profile schemas (JSON Schema)
  layers/
    L1-ai/
      exec/
        <id>-skill-is-text-file/
          rule.md              the record (header + Simple / How to tell / What to say / Rot guards)
          check.py             scanner check for this rule
          check.test.py        test for the check
          fixtures/pass/       sample inputs that must pass
          fixtures/fail/       sample inputs that must fail
          CHANGELOG.md         history of this rule only
    L2-dev/
    L3-stack/
      tanstack-start/
    L4-deps/
  profiles/
    lovable/profile.yaml       selections and overrides only
  hosts/
    <host>-plugin/             per-host adapters only
  build/                       generated output, never hand-edited
```

## Canonical rules
1. One rule, one folder. The folder is the unit of change, review and reuse.
2. Co-located: everything about a rule (text, check, test, fixtures, history) lives in its folder.
3. No shared helpers folder. If two rules need the same logic, one extends the other, or the logic moves into the scanner core.
4. Rules reference each other by ID only, never by path. Moving a folder breaks nothing.
5. IDs are opaque and permanent (ledger D18). Layer is a field. A retired rule keeps its ID; IDs are never reused.
6. A profile holds only selections and overrides. Every override carries a `why` (ledger D10).
7. build/ is generated: simple view, index, discovery files, XCCDF export. Never edited by hand.
8. Votes and usage data never live in the repo.
9. Host adapters contain no rules. Rules contain no host-specific code.
10. Strict means machine-enforced: a linter fails the build when a rule folder is missing a required file, a reference points to an unknown ID, or an override has no `why`.

## Across repositories (ledger D27, D29)
- One repository per baseline, linked as optional git submodules.
- The umbrella owns the schema, the linter (shipped as a reusable package or CI action, never copied) and a central ID registry. Provisional.
- Submodule pins are bumped by automation. A missing optional submodule must never break a build.

## From research
- Rules that are to load as skill files can carry only six portable header fields. Extra fields (layer, severity, trigger, source, extends, feedback) belong inside the standard `metadata` field. Awaiting Jesse's ruling.
- Every record needs a `license` field, and share-alike content (OWASP) must stay separable.
- Imported DISA rules are keyed on Rule ID plus release or content hash.

## Open
- ID format details (prefix, length, how IDs are issued).
- Whether this convention is later published as a layer 2 guide for users' own projects.
