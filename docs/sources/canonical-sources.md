# Canonical sources: one official source per item

Status: DRAFT 2026-11-12. Built from research runs R1 and R2. This is the baseline: the official material frontier AI is already built on, with one clear source for each item.

## Rules
1. One canonical source per item: the owner's own spec, repo or documentation. Never a blog, tracker, directory listing, fan site or fork.
2. Pin a version or date for every source.
3. A secondary source may be kept only as a lead, labeled as such, and never cited as evidence.
4. Status values: READ = opened by a research run (through a summarizing fetch tool, so quotes still need a spot-check); UNREAD = believed official, not yet opened; CONFLICT = the owner's own pages disagree.
5. Nothing here has been cross-checked by a second model yet.

## AI interaction specs (MCPL's upstreams)
| Item | Canonical source | Pin | Status |
|---|---|---|---|
| MCP core specification | modelcontextprotocol.io/specification/2026-07-28 | 2026-07-28; next release targeted 2027-03-30 | READ |
| MCP changelog | modelcontextprotocol.io/specification/2026-07-28/changelog | 2026-07-28 | READ |
| MCP elicitation | modelcontextprotocol.io/specification/2026-07-28/client/elicitation | 2026-07-28 (also 2025-11-25, 2025-06-18) | READ |
| MCP multi-round-trip requests | modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr | 2026-07-28 | READ |
| MCP authorization | modelcontextprotocol.io/specification/2026-07-28/basic/authorization | 2026-07-28 | READ |
| MCP release cadence | modelcontextprotocol.io/seps/3398-release-cycle-updates | accepted 2026-10-14 | READ |
| MCP Apps | github.com/modelcontextprotocol/ext-apps (specification/2026-01-26/apps.mdx) | stable 2026-01-26 | READ (as summary) |
| MCP Registry | modelcontextprotocol.io/registry and github.com/modelcontextprotocol/registry | schema 2025-12-11, API v0.1, preview | READ |
| A2UI | a2ui.org/specification/v1.0-a2ui and github.com/a2ui-project/a2ui | v1.0 per site; v0.9.1 production per repo README | CONFLICT |
| AG-UI | docs.ag-ui.com and github.com/ag-ui-protocol/ag-ui | 1.0; 1.1 draft | READ (one internal conflict) |
| WebMCP | webmachinelearning.github.io/webmcp and github.com/webmachinelearning/webmcp | draft dated 2026-11-11, not standards track | READ |
| WebMCP in Chrome | developer.chrome.com/docs/ai/webmcp | origin trial, Chrome 149+ | UNREAD (page failed to fetch) |
| A2A | a2a-protocol.org/latest/specification and github.com/a2aproject/A2A | 1.0.1 (2026-05-26) | READ (last third unread) |
| OpenAI Apps (MCP Apps in ChatGPT) | developers.openai.com/apps-sdk/mcp-apps-in-chatgpt | compatible since 2026-02-22 | READ |
| Open-JSON-UI | none exists | n/a | No primary source found; dropped |

## Context, skills, discovery, packaging
| Item | Canonical source | Pin | Status |
|---|---|---|---|
| AGENTS.md | agents.md | unversioned | READ |
| Agent Skills | agentskills.io/specification | unversioned | READ |
| llms.txt | llmstxt.org | "v2", modified 2026-08-10 | READ |
| Agent Plugins | agent-plugins.org | 1.0.0 | READ |
| Claude Code (memory, skills, plugins, MCP) | code.claude.com/docs | rolling | READ |
| Lovable (custom MCP, registries) | docs.lovable.dev/integrations | rolling | READ |
| Context7 | github.com/upstash/context7 and context7.com/docs | rolling | READ |

## Baseline standards (the umbrella's upstreams)
| Item | Canonical source | Pin | Status |
|---|---|---|---|
| NIST SP 800-53 | csrc.nist.gov/pubs/sp/800/53/r5/upd1/final and github.com/usnistgov/oscal-content | Rev 5.2.0 (2025-08-27) | READ |
| NIST SSDF | csrc.nist.gov/projects/ssdf | v1.1 final; v1.2 draft | READ |
| NIST AI RMF | nist.gov/itl/ai-risk-management-framework | 1.0, under revision | READ |
| XCCDF | csrc.nist.gov/pubs/ir/7275/r4/upd1/final | 1.2 | READ (partial, via summary) |
| OSCAL | pages.nist.gov/OSCAL and github.com/usnistgov/OSCAL | v1.2.3 (2026-08-07) | READ |
| DISA STIGs and SRGs | cyber.mil (library compilation ZIP at dl.dod.cyber.mil) | quarterly; October 2026 live | Site unreadable by fetch tools; ZIP confirmed live. Jesse is the primary source on this material |
| OWASP ASVS | github.com/OWASP/ASVS | 5.0.0 | READ |
| OWASP Top 10 for LLM Applications | genai.owasp.org/llm-top-10 | 2025 per site; 2026 edition reported in legacy repo | CONFLICT |
| OWASP Cheat Sheets | github.com/OWASP/CheatSheetSeries | rolling | READ |
| OpenSSF Baseline and Scorecard | github.com/ossf/security-baseline and github.com/ossf/scorecard | baseline v2026.08.28 | READ |
| OpenSSF guide for AI code assistant instructions | github.com/ossf/wg-best-practices-os-developers | rolling | READ |
| Project CodeGuard | github.com/cosai-oasis/project-codeguard | rolling | READ |
| MITRE ATLAS | github.com/mitre-atlas/atlas-data | 2026.05 | CONFLICT (license file vs README) |
| MITRE CWE | cwe.mitre.org | version unconfirmed | READ (terms only) |

## Research evidence (cite the paper, not the coverage)
| Item | Canonical source | Type | Status |
|---|---|---|---|
| Context rot | trychroma.com/research/context-rot | vendor report | READ |
| NoLiMa | arxiv.org/abs/2502.05167 | peer-reviewed | READ |
| Multi-turn degradation | arxiv.org/abs/2505.06120 | preprint | READ |
| Context files study (ETH Zurich) | arxiv.org/abs/2602.11988 | preprint, v3 | READ (one figure to re-check) |
| AGENTS.md effect study | arxiv.org/abs/2601.20404 | preprint | READ |
| Small models position paper (NVIDIA) | arxiv.org/abs/2506.02153 | position paper, no experiments | READ |
| ToolOrchestra / Orchestrator-8B | arxiv.org/abs/2511.21689 | preprint | READ |
| ProfiLLM | arxiv.org/abs/2506.13980 | preprint | READ |
| AI crawlers and JavaScript | vercel.com/blog/the-rise-of-the-ai-crawler | vendor analysis of its own traffic | READ (search excerpt only) |

## Tooling mentioned
| Item | Canonical source | Status |
|---|---|---|
| HyperFrames | github.com/heygen-com/hyperframes | UNREAD |
| Remotion license | remotion.pro/license | UNREAD |

## Next
- Turn this into the machine-readable source registry: one row per source with detector, cadence and sanity rule.
- Resolve the three CONFLICT rows and the UNREAD rows.
