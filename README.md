# INCRAM

Repository: github.com/wiredFRONT/INCRAM. Planning name during research: stigops-AI.

Umbrella project for a normalized, machine-readable library of standards, standard operating procedures and practices for AI-assisted software development, and for **MCPL**, the schema-governed framework that lets an application act as its own subject-matter expert for any AI.

**Status (2026-11-12): planning and research. Nothing is built yet.** This repository currently holds the decisions, designs and research that the build will follow.

## What this is

- **The library.** Practices collated from official sources into one rule format, organized in four layers that inherit from each other:
  1. AI and general AI usage
  2. General software development
  3. Project stack
  4. Dependencies and hosting (self-hosted or managed)
- **MCPL.** An application publishes a governed schema of itself (inputs, actions, rules, workflows, screens). A person speaks plainly, the AI proposes a structured result, and the schema validates it before anything is applied. MCPL lives in its own repository, github.com/wiredFRONT/MCPL, linked here as an optional submodule at `modules/mcpl`.

The structure is modeled on how DISA SRGs and STIGs work: a vendor-neutral base, product-specific guides that inherit from it, tailored profiles, traceable citations, and machine-checkable rules. It never restricts the AI; it gives it a reliable, grouped source to work from.

## Ground rules

1. **Official sources only.** One canonical source per item. Coverage, directories, fan sites and forks are leads, never evidence. See `docs/sources/canonical-sources.md`.
2. **Every statement is labeled** UPSTREAM (fact from a source, with version and date) or MCPL (our recommendation).
3. **Cross-verification is mandatory.** A second AI model checks the work before it is treated as settled.
4. **Small increments.** One decision per pass.

## Where things are

| Path | What it holds |
|---|---|
| `docs/decisions/ledger.md` | Every decision, working assumption, research correction and open item. Authoritative. |
| `docs/vision/mcpl-vision.md` | What MCPL becomes, in the founder's words, plus the reading of it |
| `docs/design/structure-and-profiles.md` | Layers, hierarchy, platform profiles, presentation rules |
| `docs/design/library-layout.md` | Canonical file and folder standard: one rule, one folder |
| `docs/sources/canonical-sources.md` | The single list of official sources, with version pins and status |
| `docs/plan/research-plan.md` | The original research plan (partly superseded; the ledger wins) |
| `docs/research/` | Research runs R1 (umbrella baseline) and R2 (MCPL crosswalk) |
| `schema/` | Rule and profile schemas. Not yet written (pass 0) |
| `registry/` | Central ID registry. Not yet written |
| `modules/mcpl` | Optional submodule: the MCPL repository |

## What happens next

1. Founder rules on the research corrections listed in the ledger.
2. Second-model cross-check of R1 and R2.
3. Pass 0: the rule schema field list, mapped to XCCDF.
4. Turn the canonical sources list into a machine-readable registry with change detection.
5. Import one baseline as proof (research points to NIST SP 800-53).

## Notes

- Public since 2026-11-12 under the wiredFRONT organization. The MCPL repository is private until reviewed, so the submodule is optional and a clone works without it.
- Tailored content derived from DISA STIGs or SRGs is always marked as derived, keeps the original rule ID, and carries no DISA approval.
- Nothing here is legal advice.
