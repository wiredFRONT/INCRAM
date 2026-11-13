# Decisions and opens ledger

Last updated 2026-11-12. This ledger is authoritative where it differs from any other document.

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

## Context (Jesse)
- Jesse co-authored more than 14 Windows and Linux DISA STIGs. He is the primary source on STIG mechanics, licensing and DISA process.
- Nomen is being built toward: manage your IdP, your secrets, and your layer 2 and 3 zero-trust / tunnel network; integrates with Cloudflare and Tailscale; import and migrate; usable as a backup until proven. Its own project, outside this scope.

## Research runs
| # | Run | Status |
|---|---|---|
| R1 | Stigops AI umbrella baseline sources | DONE 2026-11-12. Not yet cross-checked |
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
| O9 | Run the second-model cross-check on R1 and R2 before pass 0 (schema), or start pass 0 in parallel |
| O10 | What INCRAM stands for, so the README and documents can use the name properly |

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
