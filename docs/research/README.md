# Research runs

Two research runs were completed on 2026-11-12. The full report texts are in this folder. Copies also exist as Google Docs.

| Run | Title | Words | Google Doc | File |
|---|---|---|---|---|
| R1 | Stigops AI umbrella baseline sources | about 6,000 | https://docs.google.com/document/d/1IuhCWDT3DDoRkU1FHQgRR-PQy7QuEQLclV2Zm-955CM/edit | [R1](R1-stigops-ai-umbrella-baseline-sources.md) |
| R2 | MCPL AI interaction specs crosswalk | about 8,300 | https://docs.google.com/document/d/1nHflcsqoQoR20SSBB5uNGuV7wGT4PQEgHOum-XF4t24/edit | [R2](R2-mcpl-ai-interaction-specs-crosswalk.md) |

## How to read them
- Every claim carries a label: [P] read from the owner's own page, [U] unverified, [S] secondary source only, [I] inference. R2 adds [PR] peer-reviewed, [PP] preprint, [VR] vendor-reported.
- Pages were read through a summarizing fetch tool, so short quotes need a spot-check before being reproduced.
- Each report ends with a list of what still needs independent verification.
- Both reports have been cross-checked by a second model (Codex). Ten claims each were checked, not every claim.

## To do
- "stigops-AI" in R1 is the planning name of INCRAM.

The findings that change the plan are summarized in `../decisions/ledger.md`.

## Cross-checks

- `cross-check/brief-1-field-list.md`: the brief given to the second model.
- `cross-check/codex-1-field-list.md`: Codex CLI 0.167.1 review of `schema/rule-fields.md` against NIST IR 7275 Rev 4 (XCCDF 1.2), 2026-11-12. The reviewer reports it opened the specification online.
- `cross-check/codex-1-run1-partial.md`: first run, where the reviewer could not read the repository files.
- `cross-check/brief-2-R1.md`, `cross-check/codex-2-R1.md`: Codex review of R1, 2026-11-13. Ten load-bearing claims checked online: 6 consistent, 3 divergent, 1 could not be verified. The divergences are listed in the ledger for a ruling.
- `cross-check/brief-3-R2.md`, `cross-check/codex-3-R2.md`: Codex review of R2, 2026-11-13. Ten load-bearing claims checked online: 6 consistent, 3 divergent, 1 could not be verified. Listed in the ledger for a ruling.
