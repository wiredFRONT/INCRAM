# Grouping: how INCRAM ties a rule into the official chain

Status: the chain below is BUILT and machine-verified for one rule. The grouping model at the end is PROPOSED and waits on Jesse (ledger O17). Jesse is the primary source on STIG mechanics; this document records only what was read from the official files and what INCRAM does with it.

## The chain, read from the official files on 2026-11-16

Worked for rule `r-4k7q2m` (no secrets in code):

```
NIST SP 800-53 Rev 5.2.0  IA-5(7)                       control
        |
DISA CCI list 2025-01-23  CCI-004069 (Rev 5 mapping)    one testable statement per CCI
                          CCI-002367 (Rev 4 mapping)
        |
SRG-APP-000516                                          requirement for a class of technology
        |
ASD STIG V6R5  V-222642 / SV-222642r961863_rule         rule for a product class, CAT I
               APSC-DV-003110
        |
INCRAM r-4k7q2m                                         plain-language rule, check, fix, CAT I

MITRE CWE 5.0  CWE-798  (children CWE-259, CWE-321)     weakness class
        |
CVE records that name those weaknesses                  instances; each is a reason to re-review
```

The pinned files and their hashes are in `registry/sources.yaml`. `linter/verify_links.py` re-reads them and fails if any link in a rule does not hold.

## What the files themselves showed

- A STIG rule ID carries a revision (`SV-222642r961863_rule`). The link is keyed on release plus rule ID, and both move together.
- The STIG rule still cites the Rev 4 CCI (CCI-002367) while a Rev 5 CCI (CCI-004069) exists for the same control. A rule has to carry both to join the control side and the STIG side.
- One control fans out to several CCIs (four for IA-5 (7) across revisions). Not every CCI is cited by a STIG rule.
- The Group title in the benchmark is the SRG ID. That is the join between a STIG rule and its SRG requirement.
- ASD STIG V6R5 has 286 rules: 34 CAT I, 230 CAT II, 22 CAT III.
- A STIG rule keeps its old identifiers as legacy idents, so history stays traceable after renumbering.
- CWE is a tree. CWE-798 is the base; CWE-259 (password) and CWE-321 (cryptographic key) are children. A CVE attaches to the rule through whichever of them it names.

## What INCRAM does with it today

| DISA or MITRE practice | INCRAM today |
|---|---|
| Control to CCI | `idents` with the CCI system URI DISA's own benchmarks use, the control and its revision; verified |
| SRG and STIG rule | `associated` (D20): benchmark, release, V-number, rule ID, STIG ID, SRG, severity, CCIs; verified |
| Completeness | the verifier fails if a pinned STIG rule cites one of the rule's CCIs and is not listed |
| New release | each source has a detector; a changed hash or a newer release file is reported as UPSTREAM CHANGED |
| CVE to weakness | `idents` with the CWE; verified by name |
| Severity | CAT I in the STIG, `high` here; a mismatch fails verification |

Not built: reading CVE records themselves (only the CWE they would name), the SRG document (only its ID, as carried by the STIG), and any STIG other than ASD.

## PROPOSED grouping model (O17)

Mirror the two DISA levels inside INCRAM, using fields that already exist:

1. **Requirement level (the SRG role).** A technology-neutral rule, such as `r-4k7q2m`. It carries the control, the CCIs and the weakness.
2. **Product level (the STIG role).** A rule for one stack or product that `extends` a requirement-level rule and adds the product's own check and fix, for example "no service key in a browser bundle" for one hosting platform.
3. **Maturity (D51).** A technology starts as a configuration of the requirement-level rule (`maturity: srg-config`). When it has been stable for the agreed number of years it gets its own product-level rule set (`maturity: own-stig`).
4. **Groups.** The XCCDF Group stays the layer (D5, D42). The requirement a product-level rule belongs to is its `extends` parent, the same join the SRG ID gives DISA.

This needs O15 settled, because product-level rules will live in other repositories than their requirement-level parents.
