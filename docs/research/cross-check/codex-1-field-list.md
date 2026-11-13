1. **Wrong or imprecise mappings**

**UPSTREAM — confidence: verified against specification text.** I opened [NIST IR 7275 Revision 4, XCCDF 1.2, September 2011](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7275r4.pdf) online. The XML schema link failed to render. Section/table references below refer to that specification.

| Field | File’s claim | Correction and authority |
|---|---|---|
| `id` | Opaque ID → `Rule/@id` | Exported IDs must follow `xccdf_namespace_rule_name`, with the prescribed namespace and NCName constraints. An opaque internal ID needs compliant encoding. §6.2.3, Table 3. |
| `status` | `draft`, `accepted`, `deprecated`, `retired` → `Rule/status` | `retired` is invalid. Permitted values are `incomplete`, `draft`, `interim`, `accepted`, `deprecated`. §6.2.8. |
| `severity` | Three levels, equated with CAT I–III | Those three values are valid; XCCDF also supports `unknown` and `info`. The CAT equivalence is not defined here. Table 9. |
| `source` | References and CCI identifiers bundled together | `reference` describes resources; `ident` asserts an identified issue/control relationship and requires a naming-system URI. Authority/document/pin/URL does not explicitly capture identifier value plus system. §§6.2.6, 6.4.4.3. |
| `requires` / `conflicts` | Lists of rule IDs | These constrain **selection**, not execution order or prerequisite success. Targets may also be Groups. One `requires/@idref` list means OR; separate `requires` elements impose separate requirements. Each `conflicts` names one target. Table 6. |
| How to tell | `check-content` “points at `check.py`” | `check-content` embeds checking content. An external file uses `check-content-ref/@href`, optionally `@name`, with required `check/@system`. Table 11. |
| What to say | `fixtext` | Correct only for remediation guidance. Generic conversational text is not necessarily a fix description. Executable remediation belongs in `fix`. §6.4.4.5. |
| `trigger` | Partial fit with `platform` | Only platform applicability fits: CPE names or applicability expressions referenced by `@idref`, not arbitrary intent/event conditions. §6.2.5. |
| `extends`, `layer`, `domain`, `config` | Direct mappings | Conditional mappings; see points 3–4. |

**MCPL — confidence: verified against specification text:** `metadata/dc:rights` is a permissible representation, not a native SPDX licensing contract. Rot guards map to `warning` only insofar as they contain user cautions; automated maintenance semantics remain custom. §§6.2.4, 6.4.2.

2. **Missing properties**

**MCPL — confidence: verified against specification text for the properties; inclusion is a recommendation, not a claim about DISA usage frequency.** The list lacks explicit representation for:

- Rule/Group `weight`, default `selected`; Rule `role`, `multiple`, and ordinary warnings with categories.
- Independent identifier/system pairs; `fix` scripts and their system/platform attributes; fixtext associations and remediation attributes.
- Checking-system URI, external check location/name, selectors, alternative checks, complex checks, and check exports to parameter Values.
- Explicit platform applicability; dated status history; version timestamp/update URL.
- Group IDs, titles, descriptions and references, beyond classification labels.
- Profile identity, title, selection references, refinements, parameter settings and explanatory `remark`.
- Benchmark identity, release version/status, platform, notices and scoring model.

These need places in the overall model, though not necessarily in every rule record. [Tables 4–6, 8–9, 11, 15–16, 21–22](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7275r4.pdf).

3. **Inheritance**

**UPSTREAM — confidence: verified against specification text.** One parent is correct, but it must be a **visible Rule within the Benchmark**; arbitrary cross-Group or cross-repository references are insufficient. Cycles fail resolution. Inheritance copies XCCDF properties, not Python implementation logic. §§6.3.1, 7.2.2.

[Table 33](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7275r4.pdf#page=57) specifies:

| Model | Behavior and properties |
|---|---|
| None | Not inherited: `abstract`, `cluster-id`, `extends`, `id`, `signature`, `status`, `dc-status`. |
| Prepend | Child values precede inherited values: `source`, `choices`. |
| Append | Inherited values precede child values: `requires`, `conflicts`, `ident`, `fix`, `value`, `complex-value`, `default`, `complex-default`, `lower-bound`, `upper-bound`, `match`, `select`, `refine-value`, `refine-rule`, `set-value`, `set-complex-value`, `profile-note`. |
| Replace | Explicit child replaces inherited value: `hidden`, `prohibitChanges`, `selected`, `version`, `weight`, `operator`, `interfaceHint`, `check`, `complex-check`, `role`, `severity`, `type`, `interactive`, `multiple`, `note-tag`, `impact-metric`. |
| Override | Append unless `override="true"` requests replacement: `title`, `description`, `platform`, `question`, `rationale`, `warning`, `reference`, `fixtext`. |

Checks are distinguished by system/selector; localized properties by language. Table 33’s `source` is the Value property, not this proposed bibliography field. **MCPL:** custom fields need explicit merge rules; Table 33 does not assign `metadata` a model.

4. **Configurations and classification**

**MCPL — confidence: verified against specification text; design conclusion.** Profiles are sound for generating base/cranium selections, but `select/@selected` is Boolean—not either configuration name. Define named Profiles and membership rules, including whether base rules remain selected in cranium.

Groups form a tree, not two independent membership axes. Nested layer/domain Groups can encode both, but repeat domain groupings across layers. Prefer one structural axis plus explicit metadata for the other. Rules may also sit directly under Benchmark. [§§6.3.1, 6.4.3, 6.5.3](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7275r4.pdf).

5. **Custom metadata**

**UPSTREAM — confidence: verified against specification text.** Yes: namespaced XML inside `Rule/metadata` is valid. However, metadata must not replace applicable native fields or change XCCDF assessment processing. “Consumers ignore it” overstates the guarantee: they may display/process extensions, but core assessment semantics remain unchanged. [§6.2.4](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7275r4.pdf).

6. **Ledger consistency**

**MCPL — confidence: verified against supplied texts, not recalled.**

- D12’s statement-level UPSTREAM/MCPL distinction is absent.
- D36’s Unified dimension has no explicit representation; this is an unresolved gap, not proof it must become a fifth domain.
- D10 requires override reasons; no explicit `why` representation appears.
- D13, not D15, supports the accepted record shape.
- Added draft fields do not themselves contradict D13. O8-dependent changes remain explicitly provisional.