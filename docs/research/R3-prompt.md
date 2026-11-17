# R3 research prompt

Written 2026-11-16. Given to an external research tool by Jesse. The cover summary that came back is `R3-summary-as-received.md`.

```text
ROLE
You are a research team producing lessons-learned notes for an open, public library that
normalizes official security and development standards, standard operating procedures and
AI practices into small machine-readable rules that AI assistants consume. The library is
modeled on the DISA pattern: general requirements (the SRG role) and product-specific rules
(the STIG role), each traced to a control. It must stay current without a large staff, must
let many baselines be mixed and matched for one system, and must never reduce what a
language model can do: rules inform and verify, they do not restrict the model.

OBJECTIVE
Find the patterns that mature authorities already use to (1) keep content current,
(2) prevent rot, (3) keep links and identifiers valid, (4) mark content as superseded,
withdrawn or still good, and (5) compose many baselines for one system. For each pattern,
report the authority's own terminology and exact status values. State of the world:
November 2026. Verify current versions; do not rely on memory.

ALREADY ESTABLISHED (do not redo; report only if you find a contradiction)
- NIST SP 800-53 Rev 5.2.0 baselines are cumulative: Low is a subset of Moderate, which is
  a subset of High.
- A STIG rule ID carries a revision; the same ID can return with changed content.
- DISA benchmarks do not use XCCDF "extends"; lineage runs through the SRG ID and the CCI.
- One SRG ID can be a catch-all for many unrelated STIG rules.
- A CVE record often names no CWE.
- Agent skill files have only six portable header fields.
- MCP 2026-07-28 is stateless; a server cannot open a prompt on its own.

THREADS (one notes file each)
A. DISA and DoD. How an SRG becomes a STIG; the official applicability statuses used when
   a product is assessed against an SRG; release cadence, revision histories, sunset and
   retirement of STIGs; what "use the SRG when no STIG exists" means in policy; severity
   override guidance, mitigations and plans of action; CCI lifecycle; how several STIGs
   apply to one system and how conflicts between them are resolved.
B. CVE, CWE, NVD, KEV and related. Record states and rejection; disputes; enrichment
   programs and their gaps; CWE mapping guidance and deprecation; CVSS version
   supersession; exploit-likelihood and known-exploited lists as review triggers; modern
   machine-readable vulnerability formats and how they express aliases, withdrawal and
   affected ranges; machine-readable status statements (for example VEX).
C. Supersession and staleness across standards bodies. How IETF, ISO, NIST, W3C, OWASP,
   CIS and major open-source projects mark a document as current, updated, obsoleted,
   historic, withdrawn or superseded; periodic review outcomes; successor pointers;
   tombstones; persistent identifiers and redirect practice that keep links valid.
D. Composition. How baselines, overlays, profiles, tailoring and inheritance from a
   provider are defined and resolved: NIST tailoring and overlays, OSCAL profile
   resolution, XCCDF profiles and tailoring, CIS levels and implementation groups,
   FedRAMP inheritance and responsibility matrices, shared-responsibility models,
   compliance-as-code projects and policy-as-code bundles. Include how written SOPs are
   structured and combined with technical baselines. Report every precedence rule found.
E. AI itself. Measured evidence on context degradation, instruction overload and
   conflicting instructions; whether instruction or rule files help or harm task success
   and cost; progressive disclosure and on-demand loading; how agent skills, agent
   instruction files and the MCP specification handle versioning, deprecation, discovery
   and size limits; injection through retrieved content; advisory versus blocking designs.
   For every finding say whether the pattern constrains the model.
F. Freshness engineering. Change detection without push notices; dependency-update
   automation as precedent (grouping, cadence, stale handling); documentation freshness
   and link checking; provenance and pinning by content hash; records that keep both the
   authority's effective date and the date read. Include what fails for small teams.

EVIDENCE RULES
- Primary sources only as evidence: the owner's own specification, policy, repository or
  documentation. Blogs, trackers and vendor marketing are leads, never evidence.
- Pin the version and the date read for every source. Give the URL.
- Label every claim: [P] read from the primary source, [S] secondary only, [U] unverified,
  [I] your inference. For studies add [PR] peer-reviewed, [PP] preprint, [VR] vendor-reported.
- Paraphrase. Quote only short phrases, and always for status values and defined terms.
- Where two authorities disagree, report both. Do not reconcile them.

NOTE TEMPLATE (repeat per pattern)
Pattern name | Authority and its own term | Exact status or field values | Problem it solves |
How supersession or staleness is expressed | How it composes with other baselines |
Failure it prevents, and known failure of the pattern itself | Cost to maintain |
Constrains an AI model: yes, no, or only if misused | Source, version, date read, label

FINAL SYNTHESIS (separate file)
1. Required patterns, ranked by how many authorities independently use them.
2. One crosswalk of lifecycle vocabulary across all authorities (current, revised,
   superseded, withdrawn, rejected, deprecated, sunset, historic and equivalents).
3. One crosswalk of composition and precedence rules.
4. Patterns that inform a model versus patterns that restrict it, with the evidence.
5. Contradictions left open, and everything that still needs independent verification.
Do not design the library. Report patterns and evidence only.
```
