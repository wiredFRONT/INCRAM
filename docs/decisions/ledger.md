# Decisions and opens ledger

Last updated 2026-11-13. This ledger is authoritative where it differs from any other document.

## Decided (Jesse)
| # | Decision | Date |
|---|---|---|
| D1 | Online research first, before any building | 2026-11-12 |
| D2 | Audience is the public end user (vibe coders), not devs | 2026-11-12 |
| D3 | Structure modeled on DISA SRG/STIG; never restricts the AI | 2026-11-12 |
| D4 | Build order: normalized base schema and baseline first; AI-specific layer and per-entity checks after | 2026-11-12 |
| D5 | Layers, not quadrants: AI and general usage > general development > project stack > dependencies and hosting | 2026-11-12 |
| D6 | Guidance is intent-gated; backend guidance stack-agnostic; default advice is ship the prototype | 2026-11-12 |
| D7 | The master umbrella is a public GitHub project named stigops-AI. (Earlier the same day: internal only.) | 2026-11-12 |
| D8 | Behind login; free daily tool-call allowance; payment triggers at the limit | 2026-11-12 |
| D9 | Schemas based on formats AI already uses (Markdown + structured header, JSON Schema) | 2026-11-12 |
| D10 | Layer conflict rule: the more specific layer wins and must record why | 2026-11-12 |
| D11 | Feedback: where the UI supports it, offer a simple thumbs up/down or a quality slider | 2026-11-12 |
| D12 | Every statement labeled UPSTREAM or MCPL recommendation | 2026-11-12 |
| D13 | Rule record shape accepted: header (id, layer, title, severity, trigger, source, extends, feedback) + Simple / How to tell / What to say / Rot guards | 2026-11-12 |
| D14 | Feedback is asked once per rule per user, after they have used the fix, never before and never blocking | 2026-11-12 |
| D15 | File and folder standards must be canonical and follow strict, hyper-modular, co-located code | 2026-11-12 |
| D16 | Rich-UI route may be delivered as a host plugin | 2026-11-12 |
| D17 | Shippin account creation and joining can happen through the user's AI chat via an auth MCP, without a browser if they prefer; well-authored login knowledge, rules, workflows, directions and links; adjustable | 2026-11-12 |
| D18 | Rule IDs are opaque and permanent; layer is a field, not part of the ID | 2026-11-12 |
| D19 | Repos: the umbrella (stigops-AI), then a baseline repo; from a baseline you step to the next | 2026-11-12 |
| D20 | Offer tailored versions of the actual related STIGs so users can opt to harden self-hosted servers or self-managed cloud. UI shows a small "ASSOCIATED STIGS and SRGs" notice for the selected systems | 2026-11-12 |
| D21 | A chat tailored as middleware between the user and frontier AI; mostly premium only | 2026-11-12 |
| D22 | Free experience is extremely limited, just enough to show capability, and requires having joined | 2026-11-12 |
| D23 | Landing and information are mostly open for initial scraping, loosely organized, and make clear the user should get an account. The value sold is centralization | 2026-11-12 |
| D24 | Cross-verification is mandatory. A second model (Codex) runs over the work to catch tunnel vision and recency bias. Other AI will also contribute, to identify what is consistent and what diverges, then align and drill down | 2026-11-12 |
| D25 | The AI may establish the account once it is proven the user clicked the approval in the chat. The information is shown with the offer to use Google auth as well. Sign-in is Shippin auth at auth.shippin.ai, backed by the Nomen IdP | 2026-11-12 |
| D26 | These interactions are experiments: build a variety of ways to test them rather than locking one | 2026-11-12 |
| D27 | Repo strategy: one repo per baseline, linked as OPTIONAL git submodules. One link triggers the next set of avenues; the linked baselines pool together to identify the user's overall work list. Major pieces get their own repo: MCPL is its own repo and a potential submodule of the baseline | 2026-11-12 |
| D28 | Order of work: the umbrella first, then MCPL. Deep research is launched as individual runs; each report is saved with a copy to Google Docs for other AI to scrape | 2026-11-12 |
| D29 | FOR NOW (provisional): the umbrella owns the schema, the linter (shipped as a reusable package or CI action, never copied) and a central ID registry. Rules reference each other by ID only. Submodule pins are bumped by automation. A missing optional submodule must never break a build | 2026-11-12 |
| D30 | Inside each repo: one rule, one folder, with its text, check, test, fixtures and history co-located | 2026-11-12 |
| D31 | One clear, centralized list of official sources is the baseline. Coverage, directories, fan sites and forks are not sources | 2026-11-12 |
| D32 | MCPL is an API / framework that makes an application its own subject-matter expert through a governed schema (see docs/vision/mcpl-vision.md) | 2026-11-12 |
| D33 | The umbrella lives in its own organization as github.com/wiredFRONT/INCRAM, public. (Planning name: stigops-AI.) MCPL is github.com/wiredFRONT/MCPL | 2026-11-12 |
| D34 | MCPL must clearly collapse the existing standards, then extend with our framework, to normalize and be easily adoptable by AI. Repository shape: upstream / core / extensions / routes / examples | 2026-11-12 |
| D35 | The umbrella is named INCRAM: Inference, Neural, Cognitive, Reasoning, Agentic, Machine. Four domains: Inference / Neural (model serving, quantization baselines, runtime behavior); Cognitive / Reasoning (prompt schemas, decision routing, deterministic logic); Agentic / Autonomous (tool-use scoping, least-privilege permissions, orchestration); Model / Machine (deployment pipelines, lifecycle hygiene, basic guardrails) | 2026-11-12 |
| D36 | The advanced configuration is named CRANIUM: the four domains plus a Unified dimension. Jesse accepts the name overlap with the existing company Cranium AI | 2026-11-12 |
| D37 | Positioning: open and non-proprietary. INCRAM standardizes and normalizes existing frameworks across AI implementations and architectures, weaving them together rather than focusing on architecture alone | 2026-11-12 |
| D38 | The structure must leave a clean attachment point for Jesse's reasoning governance engine, to be woven in later | 2026-11-12 |
| D39 | Build order: foundation and schema first; then optimization passes that cut bloat; then the MCP server giving Context7-level access to the library | 2026-11-12 |
| D40 | INCRAM ships its own STIG viewer rather than depending on a third-party one | 2026-11-12 |
| D41 | CRANIUM content lives in the same library and schema as the base, switched on by configuration, not kept as a separate product (closes O11) | 2026-11-12 |
| D42 | Layers and domains are two axes: every rule carries both a layer and a domain, so governance can attach by domain across all four layers (closes O10) | 2026-11-12 |
| D43 | A second-model cross-check of R1, R2 and the rule field list runs before the JSON Schema is written (closes O9) | 2026-11-12 |
| D44 | The problem INCRAM answers: users are sold the false promise that typing "make it better" over and over gets them something secure, with every layer mapped and able to scale, whether infrastructure, code or host. Getting AI to its full potential requires a strong understanding of how it works | 2026-11-13 |
| D45 | INCRAM becomes more than a repository: AI consulting, with products that rival training, built by reverse engineering what the existing offerings do and applying Jesse's STIG, SRG and standard operating procedure expertise | 2026-11-13 |
| D46 | Severity works as it does in real life. CAT I must be satisfied regardless. The checks must actually be done. The only alternative is a proven mitigation, by proven methods, that brings it down to CAT II, because of the risk CAT I represents | 2026-11-13 |
| D47 | A well-organized series of repositories, all interconnected, so an AI has one reliable organized source. All MCPL protocols are woven together into templates that bring them together as a standard | 2026-11-13 |
| D48 | No restricting the AI and no over-governance. Nothing happens behind the scenes without the user's awareness: everything is represented through clear configurations | 2026-11-13 |
| D49 | The library crawls itself repeatedly. Every item is updated and reviewed at least once a year. The most recent material sits in its own section and moves out over time, as in the real world. Decades of CVE and DISA lessons learned are folded in | 2026-11-13 |
| D50 | Dynamic triggers: when a linked source changes, the UI notifies the user. When an alternative starts to trend, users are told a new standard is available. Example: ArkType versus Zod | 2026-11-13 |
| D51 | Maturity rule: a technology such as a JavaScript dependency gets its own STIG only after a set number of years proves it mature. Until then it falls under a generalized SRG, and the choice of technology (X or Y) is a configuration of that SRG. Platform STIGs (Debian, Windows 11) still apply | 2026-11-13 |
| D52 | Everything is tailored for three tiers: foundational, managed, advanced | 2026-11-13 |

## Context (Jesse)
- Jesse co-authored more than 14 Windows and Linux DISA STIGs. He is the primary source on STIG mechanics, licensing and DISA process.
- Nomen is being built toward: manage your IdP, your secrets, and your layer 2 and 3 zero-trust / tunnel network; integrates with Cloudflare and Tailscale; import and migrate; usable as a backup until proven. Its own project, outside this scope.

## Research runs
| # | Run | Status |
|---|---|---|
| R1 | Stigops AI umbrella baseline sources | DONE 2026-11-12. Text in docs/research. Cross-checked by Codex 2026-11-13: of ten load-bearing claims, 6 consistent, 3 divergent, 1 could not be verified |
| R2 | MCPL AI interaction specs crosswalk (14 specs, crosswalk table, host matrix, evidence review) | DONE 2026-11-12. Not yet cross-checked |

## Research corrections awaiting Jesse (R2). His decisions above are unchanged until he rules.
| Affects | What the research found | Proposed adjustment |
|---|---|---|
| D25 | An in-chat "accept" is reported by the host app; nothing in the protocol proves a human clicked. One host documents a hook that auto-answers; another cancels prompts in autonomous mode. Only a page we serve lets the server see the click | Label in-chat approval "host-attested". Use a link to a page we control for any approval that must be a human act. An account created in chat stays limited until that step |
| D17 | Name and email in a chat form are allowed. Passwords are not. One-time codes are best treated as secrets. The spec forbids using link-mode prompts as the sign-in to the server itself | Sign-in to MCPL is MCP authorization (OAuth). Verification leaves the chat (emailed link). Some major hosts have no documented chat forms, so there the in-chat step is an app button or text |
| D16 | No plugin format carries UI. Plugins carry skills and server config | Rich UI ships from the MCP server through MCP Apps; the plugin installs skills and the server |
| D13 | Only six skill header fields are portable; one major host rejects any other | If rules are to load as skills, put layer, severity, trigger, source, extends, feedback inside the standard `metadata` field |
| D8, D22 | Some hosts require a paid plan for custom connections; vibe-coding platforms reach only the build chat | Day-one promise is tools-only: guidance through tool descriptions and results |
| "Signals trigger prompts" | Since MCP 2026-07-28 a server cannot open a prompt on its own; a question can only ride a call the AI already made | Signals decide whether to attach a question to a call in flight |
| "Without them realizing" (skill profile) | One small study: people accept seeing inferences about them, dislike wrong ones. Misjudging someone as a beginner produces condescension. A stored profile is profiling under EU law (secondary sources) | Make the inferred level visible and correctable; only ever add explanation, never withhold |
| "Desire to learn" | No study infers or validates it | Let the user say it (user-triggered) |
| Small companion model | Supported: a small fine-tuned classifier. Not shown: a small model tracking a user unattended. The best-known trained small model is the reverse topology (it drives, frontier models are its tools) | Scope the companion to narrow classification |
| Upkeep cadence | No source gives a calendar interval; guidance is trigger-based. Nobody has measured periodic normalization | State the cadence as our default with event triggers first; treat it as a hypothesis to test |
| Learning goal | Explanation alone is not shown to teach; gains come when the user does some of the work. Passive UI is supported by interruption studies. The two pull against each other | Run it as an experiment (D26) |

## Cross-check findings awaiting Jesse (R1, Codex 2026-11-13). Full text: docs/research/cross-check/codex-2-R1.md
| R1 claim | What the second model found at the primary source | Proposed adjustment |
|---|---|---|
| OWASP share-alike content must be kept physically separate, in its own repositories, away from paid offerings | CC BY-SA 4.0 requires attribution and same-licence sharing of adaptations. It permits commercial use and collections and prescribes no repository boundary. A per-record licence field alone does not settle database rights | Do not choose repository architecture from this. Keep the per-record licence field; get the packaging question answered properly (L2) |
| No upstream offers a push channel | NIST offers subscribed email announcements. They are not a machine-readable change feed | Narrow the claim: polling is still required; subscribe to the announcements as an extra signal |
| No downstream tool automates DISA retrieval or update detection | STIGhub advertises nightly synchronization; stigcli documents downloading the latest compilation. Owner claims, not tested | Drop this as a differentiator; evaluate both before building our own fetcher |
| Nobody combines the layers and applicability model | Cannot be established by keyword search. CodeGuard overlaps on guidance and MCP delivery; Gemara connects requirements to technical evidence | Treat "unclaimed" as unproven; compare against Gemara and FINOS Common Cloud Controls |
| XCCDF export is lossy | XCCDF permits arbitrary XML metadata, so custom fields can survive export; standard consumers need not act on them | Already reflected in schema/rule-fields.md revision 2 |
| OSCAL set aside | Compliance Trestle supports smaller OSCAL structures, Markdown authoring and Git workflows | Prototype one round trip before treating OSCAL as too heavy (A1 stays an assumption) |

## White space: no upstream exists, MCPL must define
1. Workflows and chained events (a declared interaction graph for an app)
2. Signed signal provenance and a trust level
3. Anti-nag policy
4. Approval evidence a server can verify

## Alignment summary (R2)
- Align: MCP elicitation (choices, non-secret details, link-out for secrets); MCP Apps (rich inline UI, thumbs/slider); AGENTS.md (always-on context); Agent Skills (on-demand guidance); MCP tool-definition shape (work-list entries); MCP Registry server.json (discovery); Agent Plugins 1.0.0 plus a Claude-format plugin (distribution)
- Optional route: A2UI, only where a host can render it or inside our own app
- Out of reach for a guest server: AG-UI (relevant to our own chat surface, D21, and to the embedded mode)
- Dropped: Open-JSON-UI (no spec exists); OpenAI Apps SDK as a separate item (folded into MCP Apps); A2A (multi-agent only)
- Build the server to speak both the pre-July and post-July 2026 MCP revisions
- Routing is chosen per request from the capabilities the host declares, never from the host's name

## Findings from R1 that change the plan
- Schema: lean schema mapped to XCCDF judged sound. Copy XCCDF's merge behavior for `extends`. layer, trigger, feedback and rot guards have no XCCDF home.
- Import: key imported STIG rules on Rule ID plus release or content hash. SRG lineage must be rebuilt from the SRG ID. No XCCDF-to-Markdown converter exists.
- Rule size budget: borrow the skill-file limits.
- Sources: NIST SP 800-53 Rev 5.2.0 is the cleanest first import. OWASP is CC BY-SA (per-record license field, keep separable). CIS, PCI and the Secure Controls Framework are cite-only. No language-specific or AI-specific STIG or SRG was found.
- Competition: free STIG lookup servers for AI already exist, so raw STIG lookup cannot carry the price. No project found combines cited standards, an AI layer, stack profiles, machine-checkable rules and delivery to non-developers.
- Regulations: unverified leads until read from official sources.
- Upstream text must be screened for injected instructions before it reaches a user's AI.

## Working assumptions (not yet confirmed)
| # | Assumption |
|---|---|
| A1 | Lean schema field-mapped to XCCDF, rather than adopting OSCAL (supported by R1) |
| A2 | Dials (hosting mode; depth) treated as an experiment per D26 |
| A5 | Feedback routing by host capability; votes stored outside the rule file |
| A7 | Sign-up routes to test: in-chat approval with later verification; in-chat details plus email link; Google via link; passkey via link |
| A8 | Verification is recorded per rule: who or what verified it against the primary source, and when |
| A9 | Tailored STIG content is marked as derived, with the original rule ID |
| A10 | Unverified accounts get only the tiny free tier until identity is proven |
| A13 | Site: one source (the rule folders) generates server-rendered pages, a Markdown twin, the MCP data and the index. Public: each rule's plain summary and source. Behind login: check, fix text, tailored profiles |

## Open
| # | Question |
|---|---|
| O8 | Rule on the research corrections above (accept, change or reject each) |
| O12 | How the three tiers (D52) relate to the base and CRANIUM configurations (D36, D41), including whether base rules stay selected in CRANIUM |
| O13 | What CAT I "must be satisfied regardless" (D46) gates, given D3 (never restricts the AI) and D6 (default advice is ship the prototype) |
| O14 | The number of years for the maturity rule (D51) |
| O15 | `extends` across repositories: XCCDF requires the parent rule inside the same Benchmark, and INCRAM is one repository per baseline (D27). Raised by the cross-check |
| O16 | How the Unified dimension of CRANIUM (D36) is represented in the schema. Raised by the cross-check |

## Later, not blocking
| # | Item |
|---|---|
| L1 | Where the skill profile lives and the consent flow |
| L2 | Legal review: jurisdiction content and data handling |
| L3 | First baseline to import as proof (R1 points to NIST SP 800-53) |
| L4 | Upkeep cadence value |
| L5 | Free limit and price |
| L6 | Trademark check on "STIG" in a public repo name; collision check for MCPL |
| L7 | Small-model selection and training |
| L8 | Cross-language work-list extractor scripts (no existing extractor found) |
| L10 | Own a tested host compatibility table (R2 has the first draft; no official one exists) |
| L11 | Video tooling |
| L12 | Whether the layout convention is published as a layer 2 guide |
| L13 | What Nomen must support for each sign-up route |
| L14 | ID format details |
| L15 | Differentiation now that STIG lookup is free elsewhere |
| L16 | Sign-up experiment measures |
| L17 | A fetch path that can read cyber.mil and official legal texts |
| L18 | Hands-on test per host: does the server's guidance text reach the AI |
| L19 | Listing in a skills directory alongside the MCP registry |
| L20 | Compare Jesse's other AI builds of MCPL against the research |
| L21 | Scope and timing of the consulting and training-rival products (D45), relative to the build order in D39 |
