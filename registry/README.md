# registry

- `ids.yaml`: the central ID registry, so permanent rule IDs can never collide across baseline repositories. Provisional (D29). One ID issued so far.
- `sources.yaml`: the official files rules are verified against, each with its version, hash and change detector. Four so far: the NIST SP 800-53 Rev 5 catalog, the DISA CCI list, the DISA Application Security and Development STIG, and the MITRE CWE list.
- `modules.yaml`: the repositories linked into the umbrella and what each one provides and consumes.

`../docs/sources/canonical-sources.md` is the wider human-readable list; an entry moves here once a rule is verified against its file.
