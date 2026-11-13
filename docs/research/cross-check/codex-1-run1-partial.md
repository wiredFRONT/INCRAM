1. **Incorrect or imprecise mappings — UNVERIFIED.** Repository access failed before any file contents returned: the shell launcher failed (`ShellExecuteExW … 1223`), and the alternate reader timed out. I therefore cannot identify what either table claims. No files were edited. I **did open NIST IR 7275 Revision 4 (XCCDF 1.2, September 2011) online**; the specification findings below are verified, not recalled.

2. **Missing properties — UNVERIFIED.** Without `schema/rule-fields.md`, I cannot distinguish omissions from properties already represented.

3. **Inheritance — UPSTREAM; verified against specification text.** Whether the file assumes this correctly remains unverified. `Rule/@extends` requires a visible Rule; cycles fail. Resolution merges properties and removes `@extends`. Table 33 assigns:

   | Model | Properties |
   |---|---|
   | None | abstract, cluster-id, extends, id, signature, status, dc-status |
   | Prepend | source, choices |
   | Append | requires, conflicts, ident, fix, value, complex-value, default, complex-default, lower-bound, upper-bound, match, select, refine-value, refine-rule, set-value, set-complex-value, profile-note |
   | Replace | hidden, prohibitChanges, selected, version, weight, operator, interfaceHint, check, complex-check, role, severity, type, interactive, multiple, note-tag, impact-metric |
   | Override | title, description, platform, question, rationale, warning, reference, fixtext |

   Prepend puts local values first; Append puts inherited values first. Replace substitutes explicit local values. Override appends unless `override="true"`. Different check systems/selectors and different text locales remain distinct properties. [§7.2.2, Tables 32–33](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7275r4.pdf#page=55).

4. **Configuration and classification — MCPL interpretation of verified specification text.** Profiles suit `base`/`cranium` if these mean assessment selections. Nested Groups can encode layer→domain, but not independent overlapping memberships. The repository’s intended semantics remain unverified. [§§6.4.3, 6.5.3](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7275r4.pdf#page=27).

5. **Namespaced metadata — UPSTREAM; verified against specification text.** Valid: `Rule/metadata` permits arbitrary XML. Metadata cannot replace matching native fields or change XCCDF processing. [§6.2.4](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7275r4.pdf#page=16).

6. **Ledger contradictions — UNVERIFIED.** I cannot compare documents I could not read. Attach or paste `schema/rule-fields.md`, `docs/design/library-layout.md`, and `docs/decisions/ledger.md` to complete the cross-check.