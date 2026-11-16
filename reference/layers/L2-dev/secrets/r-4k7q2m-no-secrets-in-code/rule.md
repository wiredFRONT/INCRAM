---
id: r-4k7q2m
title: No passwords, API keys or private keys written into the code
layer: L2-dev
domain: M
config: base
severity: high
status: draft
version: 0.2.0
trigger: The project contains source code, configuration or scripts that are committed to a repository or shipped to users.
references:
  - authority: NIST
    document: SP 800-53 Rev 5.2.0
    locator: IA-5(7) No Embedded Unencrypted Static Authenticators
    pin: "5.2.0; OSCAL catalog last-modified 2026-10-22; usnistgov/oscal-content commit f0de6d8"
    url: https://github.com/usnistgov/oscal-content/blob/f0de6d8d8c059d374f15e0ae07508d82e370fc1d/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json
    source: nist-800-53-r5
idents:
  - system: http://cyber.mil/cci
    value: CCI-004069
    control: IA-5 (7)
    control_revision: "5"
    source: disa-cci
  - system: http://cyber.mil/cci
    value: CCI-002367
    control: IA-5 (7)
    control_revision: "4"
    source: disa-cci
  - system: https://cwe.mitre.org/
    value: CWE-798
    title: Use of Hard-coded Credentials
    source: mitre-cwe
associated:
  - benchmark: Application_Security_Development_STIG
    release: V6R5
    group: V-222642
    rule: SV-222642r961863_rule
    stig_id: APSC-DV-003110
    srg: SRG-APP-000516
    severity: high
    cci: [CCI-002367]
    title: The application must not contain embedded authentication data.
    source: disa-asd-stig
feedback: "on"
origin: MIXED
review:
  last: 2026-11-15
  due: 2027-11-15
mitigations:
  - id: scoped-and-scheduled
    lowers_to: medium
    requires_evidence:
      - The secret is limited to the least access it needs, shown by the provider's own settings page
      - Its use is restricted to named networks or services, shown by the provider's own settings page
      - A dated plan to remove and replace it, no more than 30 days out
provenance:
  imported_from: ia-5.7
  release: 5.2.0
  sha256: 64ca6b4161de51ab6af098a7d101d326f14c95e1abf721396cd8a049e8115eeb
  file: nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json
verification:
  by: Claude (Fable 5.2)
  date: 2026-11-15
  method: Control statement and guidance read from the official OSCAL catalog file in NIST's own repository
  second_check: none yet
---

## Simple

INCRAM: Passwords, API keys, tokens and private keys must not be written into your code, your config files or your scripts. Anyone who can see the code can then use them, and code gets copied to more places than you expect: the repository, every teammate's laptop, build logs, and for web apps the visitor's browser.

Keep the secret outside the code. The code reads it at run time from the place your host provides for secrets.

## Why

UPSTREAM (NIST SP 800-53 Rev 5.2.0, IA-5(7), statement): "Ensure that unencrypted static authenticators are not embedded in applications or other forms of static storage."

UPSTREAM (same control, guidance): other forms of static storage include access scripts and function keys. If an authenticator is used in the same form in which it is stored, it counts as unencrypted.

INCRAM: This is CAT I because one leaked key usually gives direct access to the data or the money behind it, with no further step needed.

## How to tell

INCRAM. `check.py` scans the project and reports:

- Definite findings: a private key block, a cloud access key ID, a source-control token, a live payment secret key.
- Possible findings, which a person must look at: a value assigned to a name such as password, secret, token or api key, and real values in an environment file that is not a sample.

It never prints the secret itself, only the file, the line number and the kind.

By hand:

1. Search the project for the words password, secret, token, key and for "BEGIN" followed by "PRIVATE KEY".
2. Open every environment file. A file with real values must not be in the repository.
3. For a web app, open the built site in a browser, view the page's scripts and search them for the same words. Anything there is public.
4. Check the repository's history, not only the current files. A secret removed last week is still in the history.

Not a finding: a key the provider documents as public by design (for example a publishable or anonymous key), as long as the provider's access rules are what protect the data. State which provider page says so.

## What to say

INCRAM. To the person, in this order:

1. "A secret is written in your code at <file>, line <n>. I have not shown it here."
2. "Treat it as already leaked. Replace it at the provider first: create a new one and turn the old one off."
3. "Then move the new one out of the code, into your host's secrets or environment settings, and have the code read it from there."
4. "Removing the line does not remove it from the repository's history. Replacing the secret is what makes the old copy harmless."

Never ask the person to paste the secret into the chat.

## Mitigation

INCRAM recommendation, for Jesse's review. If the secret cannot be removed yet, the finding may be lowered to CAT II only with all of the evidence listed under `mitigations` in the header. It is never lowered to CAT III and never closed by a mitigation.

## Associated STIGs and SRGs

UPSTREAM. Read from the official files pinned in `registry/sources.yaml` on 2026-11-16 and re-checked by `linter/verify_links.py`.

| Level | Identifier | What it is |
|---|---|---|
| Control | NIST SP 800-53 Rev 5.2.0, IA-5(7) | No Embedded Unencrypted Static Authenticators |
| CCI | CCI-004069 | The Rev 5 mapping of IA-5 (7) in DISA's CCI list |
| CCI | CCI-002367 | The Rev 4 mapping of IA-5 (7): not embedded in applications. This is the one the STIG rule cites |
| SRG | SRG-APP-000516 | The requirement the STIG rule is filed under |
| STIG | Application Security and Development STIG V6R5, V-222642, SV-222642r961863_rule, APSC-DV-003110 | "The application must not contain embedded authentication data." CAT I |
| Weakness | CWE-798 | Use of Hard-coded Credentials (CWE 5.0). CWE-259 and CWE-321 are its children for passwords and cryptographic keys |

INCRAM: The STIG's CAT I and this rule's CAT I agree. The STIG still cites the Rev 4 CCI while the control text used here is Rev 5, so both CCIs are carried. CCI-000202 and CCI-000203 (access scripts, function keys) map to the same control in Rev 4 and are not carried, because no STIG rule read so far cites them for this requirement.

INCRAM: A CVE reaches this rule through its weakness. The CWE list names example CVEs under CWE-798, CWE-259 and CWE-321; those are the verified join. A CVE record itself often names no weakness (the one sampled, CVE-2022-29964, carries none), so the CVE record alone cannot be relied on to route a new CVE here.

## Rot guards

- INCRAM: The patterns in `check.py` go stale as providers change key formats. Review them at each yearly review and whenever a provider announces a new format.
- INCRAM: A scanner that finds nothing has not proved there are no secrets. Say "none found", never "none exist".
- INCRAM: Never copy a found secret into a report, a log, a chat message or a test fixture.
- INCRAM: The STIG rule ID carries a revision. When the pinned STIG release changes, re-read V-222642 and update the release and rule ID together; never keep an old rule ID against a new release.
- INCRAM: Fixtures in this folder contain made-up values only. Do not replace them with real-looking keys; hosting services block pushes that contain them.
