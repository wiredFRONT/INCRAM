# R3 (summary only): lifecycle, composition, freshness and AI rule practices

Received from Jesse on 2026-11-16 as a text attachment. It is the cover summary of a research run made in another AI tool from the prompt in `R3-prompt.md`. Reproduced as received.

Status: UNVERIFIED. Three limits apply until the note files themselves are added:

1. The seven note files it lists (threads A to F and the final synthesis) are NOT in this repository. The links below point into the other tool's own workspace and do not open from here.
2. The citation markers in the text are that tool's internal tokens. They carry no URL, so no claim below can be traced to its source from this file alone.
3. Nothing below has been cross-checked by a second model or read first-hand, except where `R3-first-hand-notes.md` says so.

---

# Lessons-Learned Research Package: Lifecycle, Composition, Freshness, and AI Rule Practices

## Deliverables

The requested seven distinct research files are complete. Each thread uses the requested pattern template, records the authority’s terminology and exact status values, distinguishes [P]/[I]/[U] evidence, gives source URLs and version/date information, and uses **November 17, 2026** as the read date.

| File | Scope | Download |
|---|---|---|
| A | DISA and DoD: SRG→STIG, applicability, cadence, sunset, POA&M, severity overrides, CCI, multi-STIG composition | [A — DISA and DoD notes](sandbox:/mnt/data/A_DISA_DoD_notes.md) |
| B | CVE, CWE, NVD, KEV, CVSS, EPSS, CSAF, CycloneDX VEX, OSV | [B — vulnerability ecosystem notes](sandbox:/mnt/data/B_CVE_CWE_NVD_KEV_notes.md) |
| C | IETF, ISO, NIST, W3C, OWASP, CIS, Python, Kubernetes lifecycle and supersession | [C — supersession and staleness notes](sandbox:/mnt/data/C_supersession_staleness_notes.md) |
| D | NIST tailoring/overlays, OSCAL, XCCDF, CIS, FedRAMP, shared responsibility, ComplianceAsCode, OPA, SOP precedence | [D — composition notes](sandbox:/mnt/data/D_composition_notes.md) |
| E | Long-context degradation, conflicting instructions, instruction files, Agent Skills, Codex/Copilot, MCP, prompt injection, advisory vs blocking | [E — AI notes](sandbox:/mnt/data/E_AI_notes.md) |
| F | Conditional polling, Dependabot/Renovate, link checking, hashes/provenance, ETags/TTL, effective/read dates, small-team failure modes | [F — freshness engineering notes](sandbox:/mnt/data/F_freshness_engineering_notes.md) |
| Final | Ranked recurring patterns, lifecycle vocabulary crosswalk, composition/precedence crosswalk, model-informing vs model-restricting patterns, unresolved verification | [Final synthesis](sandbox:/mnt/data/FINAL_synthesis.md) |

## Research coverage and strongest confirmed patterns

Across the authority families reviewed, the most repeated lifecycle structure is **persistent identity + explicit version/state + retained historical record + successor or relationship metadata**, rather than deletion of obsolete material. RFCs preserve immutable numbered publications while recording `Updates`, `Updated By`, `Obsoletes`, and `Obsoleted By`; W3C distinguishes `Superseded Recommendation`, `Obsolete Recommendation`, and `Rescinded Recommendation`; NIST keeps `Withdrawn` publication pages; and Python retains rejected, withdrawn, and superseded PEPs with `Superseded-By`/`Replaces` links. citeturn783498search0turn109123view1turn109123view2turn109123view3

DISA’s product-specialization process is unusually explicit: an SRG requirement assessed against a product receives one of four outcomes—`Not Applicable`, `Applicable – configurable`, `Applicable – inherently meets`, or `Applicable – does not meet`—and the published STIG contains only the configurable-applicable requirements. DISA also visibly uses `Sunset` labels, while its release/support material acknowledges quarterly publication plus out-of-cycle updates and possible lag in derived GPO artifacts. citeturn276090search1turn705296search0turn206860search5

The vulnerability ecosystem supplies several complementary state machines rather than one universal status. CVE uses `PUBLISHED` and `REJECTED`; NVD separately tracks enrichment through states such as `Awaiting Enrichment`, `Undergoing Enrichment`, `Enriched`, `Modified After Enrichment`, `Not Scheduled`, and `Rejected`; CSAF 2.1 supplies nine product-status fields including `known_affected`, `known_not_affected`, `under_investigation`, and `unknown`. citeturn206860search3turn647758search0turn109123view7 EPSS is now on model `v2026.06.15`, making the model version itself part of score interpretation. citeturn772191search2turn772191search3

For composition, mature systems generally make precedence explicit or refuse to invent it. CIS states that IG2 builds on IG1 and IG3 contains all Controls and Safeguards. citeturn109123view6 ComplianceAsCode lets a child profile inherit with `extends` and then add, remove, or refine selections. citeturn641321search1 FedRAMP’s 2026 SSP guidance distinguishes agency implementation, provider capability use/reliance, inherited common controls, and tailored-out controls rather than flattening provider and customer responsibilities. citeturn109123view5 OPA takes the opposite approach to ambiguous precedence: it explicitly provides **no ordering guarantee** among conflicting bundle sources and warns that conflicts can drive OPA into an error state. citeturn641321search2

## AI-specific evidence

The AI evidence does not support treating a large pile of rule text as cost-free context. Peer-reviewed work on long contexts found substantial position effects, with relevant information often used less effectively in the middle of long contexts. citeturn647522search0 A 2026 peer-reviewed benchmark of many-tier instruction hierarchies tested as many as twelve levels and found the problem remained difficult for frontier systems. citeturn647522search2 Separately, a 2026 preprint evaluating AGENTS.md-style repository files reported that, in its tested settings, such files tended to reduce task success and raise inference cost by more than 20%, so that result is recorded as [P][PP], not as settled general law. citeturn647522academia7

Agent Skills addresses context cost through “progressive disclosure”: discovery metadata is small, the full `SKILL.md` is loaded when a skill activates, and additional resources are loaded as needed. The thread file records that no portable dedicated lifecycle/deprecation field was found in the current skill specification, rather than inventing one. MCP’s current protocol is dated `2026-07-28`; it gives list/read responses `ttlMs` and `cacheScope`, and explicitly deprecates several older mechanisms with transition periods. citeturn113958search2turn113958search3

Indirect prompt injection remains a measured problem: the peer-reviewed 2026 *IterInject* study reports successful attacks through retrieved external content across several agent settings, including full success on five of nine tested Claude Code targets in its extension experiment. citeturn113958search6 MCP’s own documentation draws an important line between advisory and blocking designs: `ToolAnnotations` are hints, are not enforcement, can be false when supplied by an untrusted server, and do not themselves make a model resist prompt injection. citeturn113958search5 The synthesis therefore separately classifies metadata that merely informs a model from host mechanisms that can actually restrict actions.

## Freshness and rot prevention

The strongest low-cost freshness precedent is ordinary HTTP conditional retrieval. RFC 9110 defines `ETag`, `Last-Modified`, `If-None-Match`, `If-Modified-Since`, and `304 Not Modified`, and explicitly gives entity-tag validation precedence over date validation when both mechanisms are applicable. citeturn113958search0turn113958search1 OPA applies the same pattern to policy bundles and can remember recently superseded ETags to avoid rollback to stale replicas. citeturn641321search2 MCP makes freshness advisory and per-result through `ttlMs`, with an SDK default of immediate staleness (`ttlMs: 0`) and private cache scope. citeturn113958search3

For exact provenance, SLSA’s current approved specification is v1.2 and records artifact/resource digests and dependency provenance, giving a precedent for pinning exact bytes separately from a mutable URL. citeturn641321search3turn641321search5 Dependency automation supplies the small-team operational precedent: Dependabot supports bounded schedules, grouping, separate security-update behavior, and PR limits, while Renovate exposes grouping, schedules, minimum-release-age, dashboards, and concurrency controls. These systems treat reviewer bandwidth—not merely detection—as the scarce resource. citeturn672843search0turn672843search1turn672843search5turn672843search6

## Verification boundaries retained in the files

Several requested points remain deliberately marked [U] rather than being filled by inference. The most material are: no public primary source was found giving a universal mechanical precedence rule for contradictory simultaneously applicable DISA STIGs; no current formal per-CCI lifecycle state enumeration was independently verified; the exact “use the SRG where no STIG exists” wording was confirmed in primary DoD implementation guidance but not re-found verbatim in the current 2022 DoDI 8510.01; and the public DISA schedule material retrieved did not expose a complete set of exact 2026 quarterly dates. The current DoDI does, however, explicitly require maintained POA&Ms for known vulnerabilities and defines POA&M development for unacceptable assessed risk. citeturn276090search7turn276090search8

Other deliberately open pins are the exact repository commit behind the production CVE Record Format page, the release tag underlying the live OSV schema page, the numbered edition metadata behind ISO’s live consolidated directives, the moved canonical URL for NIST’s OSCAL profile-resolution documentation, and a normative standard requiring a consumer-side `date_read` field. ISO’s current directives do independently confirm formal review and disposition processes, while CVE’s production page explicitly says the `main` branch is the production record format and currently exposes schema `dataVersion` 5.1.0. citeturn109123view0turn206860search2turn206860search3

No contradiction was found in the research to the seven facts the brief designated as already established, so they were not repeated as standalone findings in the thread notes.
