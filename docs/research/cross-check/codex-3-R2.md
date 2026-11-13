1. **CONSISTENT — MCP became stateless.** **UPSTREAM, online:** the [2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) explicitly removes sessions and initialization, requires `server/discover`, and deprecates Roots, Sampling and Logging. Deprecation does **not** mean removal; they remain functional during the transition.

2. **CONSISTENT — elicitation must accompany an existing request.** **UPSTREAM, online:** [MRTR, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr) permits `InputRequiredResult` only for `tools/call`, `prompts/get` and `resources/read`. R2’s proposed routing follows that restriction.

3. **DIVERGENT — “no host surveyed documents both.”** **UPSTREAM, online:** [Cursor’s rolling documentation](https://cursor.com/docs/mcp), checked 2026-11-13, explicitly supports both elicitation and Apps. [VS Code’s documentation](https://code.visualstudio.com/api/extension-guides/ai/mcp) also documents both, although Apps remains experimental. R2’s own matrix contradicts its opening claim.

4. **DIVERGENT — a per-call approval card is guaranteed.** **UPSTREAM, online:** [VS Code’s rolling MCP guide](https://code.visualstudio.com/api/extension-guides/ai/mcp), checked 2026-11-13, explicitly says approval depends on session permissions, organization policy and existing approvals. It warns against assuming every call prompts or `readOnlyHint` bypasses approval.

5. **CONSISTENT — elicitation acceptance does not prove a human clicked.** **UPSTREAM, online:** [Claude Code’s rolling hooks reference](https://code.claude.com/docs/en/hooks), checked 2026-11-13, documents returning `accept` programmatically while skipping the dialog. “Host-reported acceptance” is more precise than implying authenticated human consent.

6. **COULD NOT VERIFY — an MCPL-owned page proves human action.** **UNVERIFIED, online source checked:** [elicitation, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) requires user identification but supplies no human-click attestation. **MCPL assessment:** observing an authenticated request does not establish whether a person or automation initiated it.

7. **CONSISTENT — secrets belong outside form elicitation.** **UPSTREAM, online:** [elicitation, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) prohibits credentials in forms, allows ordinary contact information, and prohibits using URL elicitation to authorize access to the MCP server itself. Treating every OTP identically remains an MCPL policy choice based on its purpose.

8. **CONSISTENT — Apps supplies sandboxed HTML with optional consent hooks.** **UPSTREAM, online:** the [stable Apps specification, 2026-01-26](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx) supports these claims. However, “deny-all” needs qualification: its example permits inline scripts/styles and same-origin access while restricting undeclared external origins.

9. **CONSISTENT, narrowly — a fine-tuned 1B classifier achieved 99%.** **UPSTREAM, online:** [Licardo and Tankovic, v1, 2025-10-24](https://arxiv.org/abs/2510.21970) reports that result for multilingual **e-commerce intent recognition** using synthetic data. **MCPL assessment:** this supports a feasibility experiment, not predicted accuracy on MCPL signals or evolving users.

10. **DIVERGENT — interruption studies establish that purely passive UI is preferable.** **UPSTREAM, online:** [Codellaborator, v4, 2025-09-08](https://arxiv.org/html/2502.18658v4) reports the quoted engagement percentages, but studies proactive assistance and recommends adapting proactivity to programming processes. **MCPL assessment:** it does not establish passive UI as universally preferable or measure the claimed passive-UI/learning trade-off.

**Further incorrect or overstated claims**

- **MCPL assessment, online-verified basis:** “simple retrieval has largely stopped degrading at practical lengths” exceeds [the cited 2026-05-04 study](https://arxiv.org/abs/2605.02173). **UPSTREAM:** its single-needle experiment uses three biographical needles in a classical Chinese corpus; that does not establish general retrieval reliability.
- **MCPL assessment, online-verified basis:** “no upstream exists” for workflows and provenance reflects the inventory’s boundaries, not the wider standards landscape. The sources below directly challenge that conclusion.

**Important omissions**

- **UPSTREAM, online:** [SCXML, W3C Recommendation, 2015-09-01](https://www.w3.org/TR/scxml/) defines event-driven states, transitions and external communications. **MCPL:** compare it before inventing interaction-graph semantics.
- **UPSTREAM, online:** [PROV-O, W3C Recommendation, 2013-04-30](https://www.w3.org/TR/prov-o/) provides interoperable provenance modeling; [CloudEvents’ verifiability extension design](https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/verifiability.md), rolling main checked 2026-11-13, specifies DSSE-signed events. Neither alone supplies a complete trust policy.
- **UPSTREAM, online:** [WebAuthn Level 3, 2026-08-25](https://www.w3.org/TR/webauthn-3/) distinguishes user presence and verification. **MCPL:** evaluate these primitives without equating authentication with informed transaction approval.
- **UPSTREAM, online:** [Claude Code’s MCP guide](https://code.claude.com/docs/en/mcp), rolling, checked 2026-11-13, documents `anthropic/requiresUserInteraction`. It strengthens host-controlled approval, with an Agent SDK callback exception; it is not cryptographic human attestation.

**Recommendations I would not build on yet**

- **MCPL, based on online checks:** #1’s browser-page proof claim and #3’s guaranteed checkpoint need an explicit assurance model.
- **MCPL, based on online checks:** #9’s bespoke workflow/provenance design needs comparison with the omitted standards.
- **MCPL, based on online checks:** #12’s classifier needs representative held-out MCPL data; passive UI and learning outcomes need separate experiments.
- **MCPL next step:** resolve the approval-evidence requirement first, without changing founder decisions.

All checks above used online sources, not recall. No files were edited or shell commands run; newly identified sources remain unregistered under the no-edit instruction.