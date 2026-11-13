# MCPL vision (Jesse, 2026-11-12)

Status: Jesse's statement, plus Claude's reading of it. Jesse repeated the six-point reading back on 2026-11-12 without changes.

## What MCPL becomes (Jesse)
- An API / framework that helps the user understand how to do X, Y, Z inside an application, as a layman-friendly guide.
- It interacts with the user through a myriad of UI. What the user enters is saved. It may be an answer, a sentence, or several items.
- That input is fed to the AI, which works out a proper solution or the proper input to put into the website.
- Example: a layman-friendly firewall system. Existing products let you write rules and permissions in plain language; Jesse dislikes how they do it.
- Schema-driven instead. A request such as "create a rule for ..." is understood from provenance and the technology involved.
- Foundational practices are always applied at minimum, unless the user explicitly states this is a dev prototype ("run free"). If they have not said so, MCPL gets that clarity first, then recommends and builds from there.
- Not just one thing: MCPL can guide the user through navigation, e.g. a link that takes them to another part of the app.
- MCPL is the subject matter expert for that application, within that knowledge boundary.
- Other AI talk to it. It is built to structure frontier AI so it properly adopts and understands the application.
- Schema-based governance throughout. Tested over and over until smooth.
- Jesse has had other AI build this concept, to compare what AI does by default against what the research shows is needed.

## The reading
1. The app publishes a governed schema of itself: its inputs, actions, rules, workflows and screens. That is the "work list", made formal.
2. The user says, in plain words, "block everyone outside the US from the admin page."
3. The AI proposes a structured rule. The schema validates it before anything is applied. The AI proposes; the schema decides what is acceptable.
4. Posture is explicit. Foundational practices apply by default. "Dev prototype, run free" has to be stated. If it is unknown, MCPL asks once, then recommends.
5. Screens and routes are in the schema too, so MCPL can hand the user a link to the right part of the app.
6. The knowledge boundary is closed: it answers from what the app declares, and says so when a question falls outside it. Other AI consult it instead of guessing.

## Two deployment modes
- **Embedded in the application** (the app owns the interface): full UI, approval clicks the server can verify, and the richer UI specs become usable.
- **Reached through someone else's AI app as an MCP server**: the tools-only floor found in research run R2, with richer routes where the host supports them.

## How this maps to research run R2
- The schema of inputs and actions aligns to the MCP tool-definition shape.
- Workflows, chained events and navigation are white space: no upstream spec has them. This is MCPL's core contribution.
- "Understood from provenance" is the second white-space item: signals that record where they came from.
- The clarity question uses the host's form prompt where available, or the app's own UI when embedded.
- Consequential changes (e.g. a firewall rule) need a plain-language preview, an approval the server can verify, and an undo.

## Open
- Jesse's other AI builds of MCPL: where they are, so they can be compared with the same crosswalk method.
