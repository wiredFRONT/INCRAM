---
id: r-4k7q2m
title: No passwords, API keys or private keys written into the code
layer: L2-dev
domain: M
config: base
severity: high
status: draft
version: 0.1.0
trigger: The project contains source code, configuration or scripts that are committed to a repository or shipped to users.
references:
  - authority: NIST
    document: SP 800-53 Rev 5.2.0
    locator: IA-5(7) No Embedded Unencrypted Static Authenticators
    pin: "5.2.0; OSCAL catalog last-modified 2026-10-22; usnistgov/oscal-content commit f0de6d8"
    url: https://github.com/usnistgov/oscal-content/blob/f0de6d8d8c059d374f15e0ae07508d82e370fc1d/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json
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

## Rot guards

- INCRAM: The patterns in `check.py` go stale as providers change key formats. Review them at each yearly review and whenever a provider announces a new format.
- INCRAM: A scanner that finds nothing has not proved there are no secrets. Say "none found", never "none exist".
- INCRAM: Never copy a found secret into a report, a log, a chat message or a test fixture.
- INCRAM: Fixtures in this folder contain made-up values only. Do not replace them with real-looking keys; hosting services block pushes that contain them.
