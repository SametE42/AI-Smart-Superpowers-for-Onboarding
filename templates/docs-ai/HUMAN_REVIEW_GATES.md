# HUMAN_REVIEW_GATES.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Mandatory human review triggers.

## Review gates

| Gate | Human review required when | Evidence to provide |
|---|---|---|
| Security changes | Security rules, secrets, credentials or permissions change | Diff, risk notes, tests |
| Authentication | Login, sessions or identity handling changes | Evidence, tests, rollback notes |
| Authorization | Roles, permissions or tenant boundaries change | Access-control evidence |
| Deployment | Release, hosting, CI/CD or production config changes | Commands, environment notes |
| Data handling | Personal, customer, financial or internal data is touched | Data-flow notes, redaction plan |
| Public claims | README, docs, website or release claims change | Evidence for the claim |
| Licensing | License, attribution or dependency license status changes | License evidence |
| Generated translations | New or changed generated translations are published | Translation status |
| Architecture decisions | Major boundaries, frameworks or data flow change | Decision record |
| Deleting or moving major files | Major files or folders are removed or renamed | Migration plan |
| Major dependency upgrades | Runtime, framework or security-sensitive dependencies change | Dependency review |
| Runtime or deployment changes | Environment variables, containers, cloud or servers change | Runtime evidence |

## Rule

If evidence is incomplete, keep the gate open.

