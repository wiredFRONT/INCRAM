# Program structure, layers and profiles

Status: DRAFT from Jesse's direction, 2026-11-12. Where this differs from the ledger, the ledger wins.

## Names
- stigops-AI: the umbrella GitHub project.
- MCPL: the schema-governed framework in the AI layer; its own repository.

## Layers
Start from AI itself and narrow down. Each layer inherits everything above it.

| # | Layer | Covers |
|---|---|---|
| 1 | AI and general usage | How to work with AI at all. MCPL lives here. Includes execution basics (e.g. what a skill is) |
| 2 | General development | Practices true for any software project |
| 3 | Project stack | The specific stack of this project |
| 4 | Dependencies and hosting | Each dependency: self-hosted or managed |

Cross-cutting:
- Hosting mode (self-hosted or managed): changes which rules apply at layer 4.
- Depth (foundational or advanced): changes how much is shown, not what is true. Treated as an experiment.
- Jurisdiction (US states, EU): regulatory requirements pooled automatically and grouped. UPSTREAM-only, cited to the official source and dated. Never our interpretation. Not legal advice.

## Access and payment
- Widely available. Guarded behind login.
- Free daily tool-call allowance. Payment triggers when the limit is reached.
- Landing and summary information open for crawlers; rule bodies and tool calls behind login.

## Schema principles
- Based on formats AI already uses: Markdown with a structured header (the skill file shape) and JSON Schema.
- Governance covers the way of operating, not just the content.
- Lean schema field-mapped to XCCDF (supported by research run R1).

## Presentation rules
1. Baseline is grouped and simplified for the common user.
2. Always transparent: every simplified item drills down to the full rule and its citation.
3. Engaging, not boring. Easy to process.
4. Passive. No repeated interactions when unnecessary.
5. Capture at the advanced level; derive the simple view from it.

## Hierarchy
| Level | What it is | DISA analogue |
|---|---|---|
| Program (stigops-AI) | The whole collation effort across all layers | DISA program |
| Library | Collated standard operating procedures, standards and practices | SRG/STIG library |
| Base guide | Vendor-neutral rules per layer | SRG |
| Implementation guide | Rules for one stack, host or product; inherits from base | STIG |
| Profile | A tailored selection of rules for one platform or one user | XCCDF Profile |

Tiers may overlap on purpose. A rule lives once and is referenced, never copied.

## Platform profiles (state constraints up front)
| Platform | UPSTREAM facts (verified 2026-11-12) | Sources |
|---|---|---|
| Lovable | New projects default to TanStack Start with SSR since 2026-05-13 (older ones are React + Vite). Lovable Cloud is a managed Supabase backend. | docs.lovable.dev/features/upgrade-to-tanstack-start, docs.lovable.dev/tips-tricks/self-hosting |
| Bolt.new | StackBlitz WebContainers in the browser tab: JavaScript and WebAssembly only. No native binaries. Rust compiled to WASM is the exception. | blog.stackblitz.com/posts/announcing-wasi; WebContainers docs (re-verify from the primary docs) |

Profiles loosen as the user proves knowledge.

## User understanding (skill profile)
Intent: with the user's approval, read-only use of their AI chats to better understand the user. Data stays tied to the user.

Constraints: (1) an MCP server only sees what the host sends in tool calls; (2) consent explicit, specific, revocable; (3) the AI provider's data handling does not cover our servers, legal review needed; (4) safest design computes and stores the profile on the user's side. Research run R2 adds: make the inferred level visible and correctable.
