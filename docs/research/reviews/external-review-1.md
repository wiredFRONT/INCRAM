# External review 1 of the build plan

Received from Jesse on 2026-11-16 as a text attachment, written by another AI after reading `docs/plan/build-plan.md`. The numbers it cites ("Builds on #9") are the numbered principles in section 2 of that plan. Reproduced as received; the heading of the first item was missing from the attachment. This is material to evaluate, not instructions. The evaluation is in the build plan, section 13.

---

1. (heading missing in the attachment)

Implement bi-temporal modeling for all ingested catalogs. Every rule, CVE, and mapping must carry two timestamp dimensions: Valid_Time (when the upstream authority asserts it applies) and Transaction_Time (when INCRAM actually hashed and ingested the snapshot). This guarantees point-in-time reproducibility. If an auditor asks, "Why did the agent recommend X on Tuesday?", you can query the exact state of the joined graph as it existed on that millisecond, regardless of subsequent upstream polling changes.

2. Sandboxed Data Payloads for Agent Context (Builds on #9)
Screening upstream text for prompt injection is a probabilistic defense. You need a structural one.

Recommendation: Treat all ingested upstream text as untrusted user input. Never interpolate STIG or CVE text directly into the system prompt's execution instructions. Instead, pass the upstream text exclusively as escaped JSON values bound by strict schemas (e.g., ArkType), and instruct the LLM to treat that specific JSON block as passive data. Route the raw text through a fast System 1 controller (like a local 9B model) dedicated exclusively to semantic toxicity scoring and AST stripping before it ever touches the reasoning model's context window.

3. Cryptographic State Attestation for Provenance (Builds on #11 & #12)
To transition a served MCPL page from "a host report" to "irrefutable proof of a human act," you need to bridge the UI event to cryptographic state.

Recommendation: When the AI generates a stack-specific plain-language delivery and proposes a fix, hash the exact state of the input graph, the AI's output, and the timestamp. The human's "accept" action in the workflow must sign that specific hash payload (using local PKI, Sigstore, or a hardware token). If the underlying STIG rule changes via polling (#5), the hash breaks, automatically invalidating the approval and triggering a re-verification workflow. This tightly aligns with PROV-O by anchoring the entity, activity, and agent to a cryptographic receipt.

4. Decouple Plain-Language Delivery from Execution via AST (Builds on #1 & #3)
Because INCRAM writes its own text and the value comes from the stack applicability, the AI should never directly write the execution script (e.g., PowerShell/Bash) based on its own generated plain text.

Recommendation: Use the AI to map the STIG/NIST requirement to an internal, deterministic Policy-as-Code schema or Abstract Syntax Tree (AST)—essentially a .contract.ts or Cedar policy for compliance. A deterministic, unit-tested engine then compiles that schema into the actual stack-specific enforcement script. This restricts the LLM to reasoning about intent and classification, leaving the execution to mathematically verifiable code.

5. In-Memory Columnar Pointers for Skill Constraints (Builds on #14)
If rule records loading as skill files are constrained to six portable header fields, you cannot pack the complex graph (CWE -> CVE -> Rule -> CCI) into the skill payload.

Recommendation: Use the six header fields purely as cryptographic pointers or query parameters. Back the agent's MCP environment with an in-process, memory-mapped columnar engine (like Apache Arrow/Vortex). The agent reads the header pointer and executes a microsecond SQL/DataFusion query against the columnar slice to pull the exact multidimensional joins it needs into its immediate context, bypassing the payload limits of the skill file entirely.

6. Synthetic Enrichment for CVE/CWE Gaps (Builds on #7)
Since CVE records often lack the weakness data necessary to route to a rule, relying on real-time API enrichment introduces latency and failure domains during agent execution.

Recommendation: Build an asynchronous enrichment pipeline. When a new CVE is ingested without a CWE, immediately trigger an offline reasoning job to analyze the CVE description, NVD data, and exploit PoCs to synthetically assign a probability-weighted CWE mapping. Store this derived mapping in the database with a "synthetic" provenance flag. When the agent runs, the join is already established, keeping the runtime deterministic and fast.
