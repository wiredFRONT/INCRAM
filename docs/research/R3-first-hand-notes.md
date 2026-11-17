# R3: what has been checked first-hand so far

Written 2026-11-16. Only the cover summary of R3 has been received (`R3-summary-as-received.md`). These notes record what in it agrees or disagrees with material already read first-hand in this repository, and one gap filled from a pinned file.

## A gap the summary left open, filled from the pinned DISA file

The summary says no formal lifecycle state per CCI was verified. The pinned CCI list (`registry/sources.yaml`, `disa-cci`, version 2025-01-23) itself carries a status on every item: 5,137 items, of which 5,046 are `draft` and 91 are `deprecated`. No other status value occurs. Each item also carries a type: 4,415 `policy`, 722 `technical`.

## Agrees with what was already read first-hand

- MCP 2026-07-28 list results carry `ttlMs` and `cacheScope` (seen on the tools page, 2026-11-13).
- Tool annotations are hints that a client must treat as untrusted unless the server is trusted (tools page, 2026-11-13).
- CVE record format is at `dataVersion` 5.1 (one record read, 2026-11-16).

## Differs from this repository's existing record, to be resolved from the note files

| Topic | R3 summary | Already recorded here |
|---|---|---|
| Study of repository instruction files for agents | Such files tended to reduce task success and raised cost by more than 20% | Ledger and R2: no significant change in success, about 20% more cost |
| Conditional requests against DISA's download server | Recommends entity-tag validation first | R1: that server honoured If-Modified-Since but not If-None-Match, so the pin is size plus hash |

## Not checkable from the summary

Every other claim, including the DISA applicability outcomes, the NVD enrichment states, the EPSS model version, the injection study and its numbers, the FedRAMP wording and the CIS wording. They need the thread files and their URLs.
