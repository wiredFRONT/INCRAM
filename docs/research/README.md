# Research runs

Two research runs were completed on 2026-11-12. **The full report texts are not in this repository yet.** They exist in the claude.ai "MCPL" project and as Google Docs, and need to be exported here as Markdown.

| Run | Title | Words | Google Doc | Project path |
|---|---|---|---|---|
| R1 | Stigops AI umbrella baseline sources | about 6,000 | https://docs.google.com/document/d/1IuhCWDT3DDoRkU1FHQgRR-PQy7QuEQLclV2Zm-955CM/edit | research/R1-stigops-ai-umbrella-baseline-sources.md |
| R2 | MCPL AI interaction specs crosswalk | about 8,300 | https://docs.google.com/document/d/1nHflcsqoQoR20SSBB5uNGuV7wGT4PQEgHOum-XF4t24/edit | research/R2-mcpl-ai-interaction-specs-crosswalk.md |

## How to read them
- Every claim carries a label: [P] read from the owner's own page, [U] unverified, [S] secondary source only, [I] inference. R2 adds [PR] peer-reviewed, [PP] preprint, [VR] vendor-reported.
- Pages were read through a summarizing fetch tool, so short quotes need a spot-check before being reproduced.
- Each report ends with a list of what still needs independent verification.
- Neither report has been cross-checked by a second model.

## To do
- Export both reports into this folder as `R1-stigops-ai-umbrella-baseline-sources.md` and `R2-mcpl-ai-interaction-specs-crosswalk.md`.
- Run the second-model cross-check and record the result beside each report.

The findings that change the plan are summarized in `../decisions/ledger.md`.

## Cross-checks

- `cross-check/brief-1-field-list.md`: the brief given to the second model.
- `cross-check/codex-1-field-list.md`: Codex CLI 0.167.1 review of `schema/rule-fields.md` against NIST IR 7275 Rev 4 (XCCDF 1.2), 2026-11-12. The reviewer reports it opened the specification online.
- `cross-check/codex-1-run1-partial.md`: first run, where the reviewer could not read the repository files.
- R1 and R2 have not been cross-checked yet; their texts are not in this repository.
