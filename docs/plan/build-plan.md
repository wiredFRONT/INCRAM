# INCRAM and MCPL: build plan

Status: PROPOSED 2026-11-16, for Jesse's review. Section 13 evaluates an external review received the same day; section 14 records what three unguided AI builds of the same request show. It replaces the pass list in `research-plan.md`. The ledger wins where they differ. Nothing in this plan changes a decision; where the research argues against a decision, the plan says so and leaves it to Jesse.

How to read it: each phase has a goal, what gets built, an exit test a machine can run, the research it rests on, and the rulings it needs. Work proceeds one increment and one decision per pass.

## 1. Where things stand (checked 2026-11-16)

| Item | Count | Evidence |
|---|---|---|
| Decisions recorded | 52 | `docs/decisions/ledger.md` |
| Open questions | 7 (O8, O12 to O17) plus two tables of cross-check findings | ledger |
| Rules written | 1 (`r-4k7q2m`, CAT I) | `linter/lint_rules.py` passes |
| Links from that rule into official catalogs | 5, all verified | `linter/verify_links.py` |
| Official files pinned by hash | 4 (NIST 800-53 Rev 5.2.0, DISA CCI list, ASD STIG V6R5, MITRE CWE 5.0) | `registry/sources.yaml` |
| MCPL schema parts | 2 of 5 drafted (actions, guards) | `tools/validate.py`, 22 checks pass |
| MCPL extensions | 0 of 4 | `extensions/README.md` |
| MCPL upstream specs read first-hand | 3 of 12 | `upstream/sources.yaml` |
| INCRAM rule enforced by an MCPL guard | 1 | `linter/check_modules.py` |
| Research reports | 2, each cross-checked on ten claims by a second model | `docs/research/` |
| Server, site, accounts, payment | none | |

The honest summary: the method is proven on one rule end to end. Everything else is design.

## 2. What the research says the plan must respect

Each line names its source. "R1", "R2" are the research reports; "X1", "X2" are the second-model cross-checks of them; "files" means read first-hand from the official files on 2026-11-16.

1. Raw STIG lookup is not the product. Two free STIG servers for AI already exist (R1, confirmed X1). The value has to come from the join, the stack applicability and the plain-language delivery.
2. "Nobody combines these layers" is not proven and must not be assumed. CodeGuard overlaps on guidance and delivery; Gemara and FINOS Common Cloud Controls need a real comparison (X1).
3. DISA's permission to modify STIG text is not confirmed (R1, X1). INCRAM therefore writes its own text and cites DISA identifiers; it never copies check or fix text. `r-4k7q2m` already works this way.
4. NIST SP 800-53 is public domain and CC0 (files). It is the anchor for every rule's control.
5. A STIG rule ID carries a revision, and the same ID can come back with changed content (R1, X1, files). Links are keyed on release plus rule ID and re-verified on every release.
6. The join across catalogs is the control and the CCI. The SRG ID is a catch-all for 57 of 286 ASD rules, and DISA uses no XCCDF inheritance at all (files).
7. A CVE record often names no weakness (files). Routing a new CVE to a rule needs the CWE list's own examples or an enrichment source, not the CVE record alone.
8. Upstreams do not push machine-readable change notices (R1; X1 adds that NIST does send email announcements). Polling with hashes is required, and a fetch that comes back degraded must never replace a good snapshot (R1, from Context7's published policy).
9. Upstream free text reaches users' AI agents, so it must be screened for injected instructions before it is served (R1, from a documented incident at Context7).
10. Tools-only is the only thing every major AI host supports. A host approval prompt is not guaranteed on every call, and an in-chat accept is not proof a person acted (R2, X2, MCP elicitation page read first-hand).
11. A page MCPL serves is stronger than a host report but is not yet proof of a human act. An assurance model has to be written before approval evidence is built (X2).
12. Workflows and provenance are not empty ground. SCXML, PROV-O and the CloudEvents signed-event design exist and must be compared before MCPL defines its own (X2).
13. Passive UI and "learning" are design choices to test, not research findings (X2). The 99% small-classifier result is from e-commerce intent on synthetic data only (X2).
14. Rule records that load as skill files can carry only six portable header fields (R2). This is still an open ruling (O8).
15. OWASP's share-alike licence does not force separate repositories (X1). Repository layout is Jesse's decision (D27) and should not be justified by that licence.

## 3. Phase 0: rulings (blocks everything after Phase 1)

Seven opens and two findings tables are waiting. To cut the typing, each has a recommendation. Reply "accept all", or list the numbers to change.

| # | Question | Recommendation | Basis |
|---|---|---|---|
| O13 | What CAT I "must be satisfied regardless" gates | The status, not the AI. Nothing reports as passing with an open CAT I; the AI keeps working | Keeps D3 and D46 both true; mirrors how an open CAT I blocks an authorization |
| O12 | Tiers versus base and CRANIUM | Three named profiles: foundational, managed, advanced. CRANIUM is the advanced profile. Each profile includes the one below it | XCCDF profiles are selections over one rule set (X on field list); matches D41 |
| O16 | The Unified dimension | A fifth domain value `U`, allowed only on rules in the advanced profile | Smallest change that gives it a representation |
| O17 | Grouping | Two levels: requirement-level and product-level rules. No inheritance between them; both carry the same control and CCI | DISA uses no `extends`; the CCI is the real join (files) |
| O15 | `extends` across repositories | Allowed only inside one repository. Across repositories the link is the shared control and CCI | Follows from O17; avoids cross-repo pins (R1) |
| O14 | Years before a technology gets its own rule set | No research basis exists. Park it; decide when the first technology is a candidate | Avoids locking a number under uncertainty |
| ID format | Prefix, length, issuing | Keep `r-` plus six characters, issued only through `registry/ids.yaml` | Already enforced by the linter |
| O8 | Eleven research corrections | Accept all eleven as proposed in the ledger | Several were confirmed by X2 (approval, delivery on a call in flight, secrets); none was contradicted |
| X1 table | Six findings on R1 | Accept all six adjustments | Each was read at the primary source |
| X2 table | Six findings on R2 | Accept all six adjustments | Each was read at the primary source |

Two of these change earlier decisions and need Jesse to say so explicitly: the approval finding narrows D25, and the correction on signals narrows how "signals trigger prompts" can work.

## 4. Phase 1: make the foundation hold

Goal: the rule record, the checks and the export are stable enough that the next thirty rules do not have to be rewritten.

Build:
1. Accept or amend `schema/rule.schema.json` after Phase 0.
2. Add the fields DISA's own record already has and INCRAM lacks: false positives, false negatives, severity override guidance, responsibility (files). Mitigation is already drafted.
3. Profile schema (selections and overrides, each override with a `why`, D10).
4. XCCDF export of the reference rules, validated against the official XCCDF 1.2 schema file.
5. Continuous checks on every push and on a weekly schedule, in both repositories.
6. A second-model check step for every rule before its status can become `accepted` (D24).

Exit test: `lint_rules.py`, `verify_links.py`, `check_modules.py` and MCPL's `validate.py` all run in continuous integration; the exported XCCDF validates against the official schema; the weekly run reports an upstream change when a pin is altered on purpose.

Research basis: items 5, 6 and 14 above; X on the field list.

## 5. Phase 2: the first baseline, from the ASD STIG's CAT I set

Goal: a real, useful rule set for anyone shipping a web application, each rule traced to its control, CCI and STIG rule.

Why this set: it is DISA's own judgement of what is CAT I for an application, it is small (34 rules), and the first rule already came from it.

First-pass sort of the 34 (for Jesse to correct; he is the authority here):

| Group | Count | STIG rules |
|---|---|---|
| Applies to any shipped web application | 20 | V-222425, V-222430, V-222432, V-222522, V-222542, V-222543, V-222554, V-222577, V-222578, V-222585, V-222596, V-222601, V-222602, V-222604, V-222607, V-222608, V-222609, V-222612, V-222642 (done), V-222662 |
| Applies when the feature is present | 5 | V-222536 (passwords), V-222588 and V-222589 (data at rest), V-222658 and V-222659 (supported components) |
| Specific to DoD environments or to one technology; cite only | 9 | V-222399, V-222400, V-222403, V-222404 (WS-Security and SAML), V-222550, V-222551 (PKI), V-222555, V-222620, V-222643 |

Build:
1. An importer that reads the pinned benchmark and CCI list and creates one stub folder per selected STIG rule, with the header chain filled in and `status: incomplete`. It copies no DISA prose.
2. A release-delta tool: when a new STIG release is pinned, match by rule ID, then by CCI, and report what changed. Design copied from MITRE SAF's delta command (R1).
3. The rules themselves, written in batches of five by control family, each with a check, fixtures and a second-model review.
4. Each rule mapped to its CWE where the CWE list supports it.

Exit test: every rule in the set passes all checks; `verify_links.py` reports no STIG rule in the pinned benchmark that cites a carried CCI and is not listed; each rule has a recorded second-model check.

Needs: Phase 0 rulings O13 and O17; Jesse's correction of the sort above; a decision on whether this baseline gets its own repository now (D27) or stays under `reference/` until there are enough rules to justify it.

## 6. Phase 3: upkeep (D49, D50)

Goal: the library notices upstream change by itself and says which rules are affected.

Build:
1. Extend `registry/sources.yaml` to every source the rules cite, with one detector each. Design from R1: a state file per source committed by a scheduled run, so the history is the audit trail.
2. Two-stage change decision: first a deterministic difference (hash, plus a size or marker sanity rule); only then a model labels the proven difference as substantive, editorial or noise and lists affected rule IDs. The model never decides whether something changed (R1).
3. The DISA library file: pin by size and hash, take the release date from the benchmark inside, never from the server's date (R1).
4. The CVE leg: start from the CWE list's own examples; evaluate an enrichment source for new CVEs before building anything (item 7).
5. The yearly review: the linter already fails a rule whose review is more than twelve months out; add a report of rules due in the next sixty days.
6. Injection screening of every piece of upstream text before it can be served (item 9).
7. Before building a DISA fetcher, evaluate the two existing tools X1 found.

Exit test: altering a pin produces an issue that names the affected rules; a truncated download is refused; a rule past its review date fails the build.

## 7. Phase 4: finish MCPL's core and decide its extensions

Goal: the firewall walk-through runs from request to undo in a test, with nothing hand-waved.

Build:
1. Core parts 3 to 5: posture, screens and routes, boundary.
2. Read the remaining nine upstream specifications first-hand and write their mapping files.
3. For each of the four extensions, a comparison first, then the design:
   - workflows and navigation against SCXML;
   - signal provenance against PROV-O and the CloudEvents signed-event design;
   - approval evidence: write the assurance model, evaluating WebAuthn user presence and user verification;
   - restraint policy: ours; state it and test it.
4. A reference server that speaks tools only, stateless, in both MCP eras (R2).

Exit test: all nine steps of `examples/firewall-rule.md` pass as automated cases; every extension document states what was taken from an existing standard and what is MCPL's own.

Needs: the rulings on D25 and on the X2 table.

## 8. Phase 5: delivery

Goal: a person who is not a developer can reach the library from their AI tool.

Build, in this order: the MCP server over the library (tools only as the floor); a skills listing beside it (R1 found skills are where this audience installs things); server-rendered pages generated from the rule folders, with a Markdown twin, because AI crawlers do not run JavaScript; the STIG viewer (D40) as those pages plus the chain view; then sign-in, the free allowance and payment (D8, D22).

Gate before this phase: a written comparison against CodeGuard, Gemara and FINOS Common Cloud Controls (item 2). If one of them already does the join, the plan changes here, not after launch.

Exit test: a host compatibility table produced by testing each host, not by reading its documentation (L10, L18).

## 9. Phase 6: breadth

The AI layer (L1) and its four domains; stack and dependency layers (L3, L4); platform profiles (D-series decisions on Lovable and Bolt); the advanced profile and CRANIUM; the attachment point for the reasoning governance engine (D38). Planned in detail only when Phase 2 has shown how long a rule really takes to write and verify.

## 10. Phase 7: business

Consulting and training products (D45), pricing and limits (L5), legal review (L2), trademark checks on the names (L6, D36). Not planned further here.

## 11. Risks, stated plainly

| Risk | Why it is real | What the plan does about it |
|---|---|---|
| Scope outruns output | 52 decisions, 1 rule | Phase 2 has a fixed set of 34 with a count as its exit test |
| One person cannot keep a library current | R1: every upstream must be polled | Phase 3 before breadth; nothing is added that the upkeep run cannot watch |
| The differentiation is unproven | X1 | The comparison gate before Phase 5 |
| DISA text rights | R1, X1 | Own text, cited identifiers, no copied prose |
| Approval cannot be proven yet | X2 | Assurance model before any approval feature |
| The name CRANIUM overlaps an existing company | Recorded in D36 as accepted by Jesse | A name check is listed under Phase 7 |
| Rules written by a model drift from the source | This plan depends on model-written rules | Every link machine-verified; a second model checks each rule; Jesse reviews mitigations |

## 12. Working agreement

- One increment and one decision per pass. Commit and push at least hourly.
- No rule is `accepted` without passing all checks and a recorded second-model check.
- Every claim about an upstream is read from the owner's own file and pinned, or marked unverified.
- A decision is Jesse's. Research that argues against one goes in the ledger as a finding, never as an edit.

## 13. External review 1, evaluated (2026-11-16)

Another AI reviewed this plan and made six recommendations (`../research/reviews/external-review-1.md`). Each is judged here against the research and against what is actually built. Nothing below is accepted until Jesse rules.

| # | Recommendation | Verdict | What is taken | What is not, and why |
|---|---|---|---|---|
| 1 | Two time dimensions on everything ingested: when the authority says it applies, and when INCRAM read it | Accept the principle | Every pinned source already carries `published` and `read`. Add the same pair to every rule link, and commit a state file per polling run (Phase 3), so any past state is a git commit that can be checked out | A separate time-travelling database. Git already gives the history at commit granularity, and there is one rule. Revisit when there is a served database (Phase 5) |
| 2 | Structural defence against injected instructions: upstream text is passed only as data, never as instructions | Accept the structural part | Upstream text travels only inside typed result fields, labelled as untrusted, never inside server instructions or tool descriptions. INCRAM already serves its own wording and not DISA prose, which removes most of the exposure | A local 9B model for "toxicity scoring" in front of every read. Injection is not toxicity; the evidence for small models is narrow (cross-check of R2); it adds a second probabilistic layer and a runtime dependency. Keep screening as a later, measured addition |
| 3 | Bind an approval to a hash of exactly what was approved, and void it when the underlying rule changes | Accept, with a correction | The approval record carries a hash of the rule version, the pinned source hashes and the proposal. A change in any of them makes the approval stale. This goes into the assurance model (Phase 4) | "Irrefutable proof of a human act". A signature proves a key was used on a device, not that a person understood and agreed (cross-check of R2). Local PKI and hardware tokens do not fit a non-developer audience (D2); a passkey signing the hash is the candidate to evaluate. Sigstore signs software artifacts, not a person's approval |
| 4 | The AI never writes the enforcement script; it maps a requirement to a declared structure and tested code produces the script | Accept the principle | It is already the design: a rule's check is tested code, the AI's proposal is validated by a schema and guards, and "What to say" is guidance, never an executable fix. Make it a stated rule: no generated script is ever served as a fix | A compiler from a policy language to per-stack scripts, now. That is Phase 6 scope at the earliest. Cedar is an authorization language, not a compliance compiler. "Mathematically verifiable" overstates what unit tests give |
| 5 | Use the six portable skill header fields as pointers and fetch the full join at run time from an in-process columnar engine | Accept the pointer; reject the engine for now | A rule delivered as a skill carries its ID; the MCP server returns the control, CCI, STIG and weakness chain on request. This also settles part of O8 | Arrow or DataFusion. The whole ASD STIG is 286 rules and the full chain for one rule is a few hundred bytes. No measured problem exists. The storage engine is chosen in Phase 5 from measurement |
| 6 | When a CVE arrives with no weakness, have a model assign one offline and store it flagged as synthetic | Accept in part | Enrichment runs offline, never at request time, and every derived mapping is flagged as derived and never labelled UPSTREAM | Doing it before checking whether an official enrichment already supplies the weakness (to be verified first). Model-stated probabilities are not calibrated, so a derived mapping is a candidate for review, never a basis for a CAT I status. Reading exploit code is not needed for a weakness class and adds risk |

Net effect on the plan: Phase 3 gains the state-file history, the data-only rule for upstream text and the offline enrichment step. Phase 4 gains the hash-bound approval. Phase 1 gains the stated rule that no generated script is served as a fix. No phase is reordered.

## 14. What unguided builds show (2026-11-16, corrected the same day)

Jesse asked AI, in plain language, to build what MCPL describes, separately in three of his own products. The three results were compared. They are specimens of what AI produces without the framework. They are not sources for it: nothing is taken from a build into the framework, and the framework repositories name no product. The comparison itself is kept privately with the builds.

An earlier version of this section said pieces would be "lifted" from the builds and that the builds would replace the generic example. That was wrong and is withdrawn. The framework is written from the standards and from general AI practice; builds are measured against it and refined toward it.

What the three builds show: unguided, the AI gets the principles right and is inconsistent on everything a standard should fix.

**Arrived at in all three without being told.** These still have to be written as requirements, because agreement by instinct is not conformance: authored guidance for the AI; a secret never passes through the AI; the human step happens on a surface the application owns, reached by a link; the AI is told what to do next; one implementation for people and for AI; identity from the credential, never from what the AI says.

**Different in each build.** Each row is a place the framework must state one answer.

| Where the builds diverged | What the framework must state | Rests on |
|---|---|---|
| Which protocol revisions the server speaks (three different sets) | The revisions a conforming server serves, and how it serves the stateless and the older era together | MCP 2026-07-28 (R2) |
| Result format (typed in two, JSON packed into text in one) | Results are structured content with an output schema | MCP tool definition, read first-hand |
| Behaviour hints on actions (all, some, none) | Every action declares its hints; MCPL's own consequence level is the authority, because hosts treat hints as untrusted | MCP tool definition, read first-hand |
| How actions are grouped (one step-by-step tool, one flat list, one server per domain) | The surface shapes allowed and when each applies | Nothing upstream; MCPL's own, labelled as such |
| Action names (three conventions) | One naming convention inside the protocol's name rules | MCP tool name rules, read first-hand |
| Approval (three mechanisms; none proves a person acted) | One approval record and a written assurance model | Nothing upstream (cross-check of R2) |
| Asking the person a question (the protocol's own mechanism used in one build of three) | Use the protocol's mechanism when the client declares it; link out for anything secret | MCP elicitation, read first-hand |
| Workflows (a file, a set of tools, a state machine) | One workflow record | Compare with SCXML first (cross-check of R2) |
| When the AI may raise something unasked (a written rule in one build of three) | A restraint policy every conforming application carries | Nothing upstream; MCPL's own |
| Machine-readable self-description (present in one build of three) | The action entry is required, and the interface and the server both read it | `core/action.schema.json` |

Effect on the plan: Phase 4 writes each row as a requirement with a conformance test. A build is then scored against the tests, and its score lives with that build. The generic example in MCPL stays generic.
