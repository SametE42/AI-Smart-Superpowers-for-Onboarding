# SAFETY_BOUNDARIES.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Actions agents must not take without explicit human approval.

## Boundaries

- Secrets: do not reveal, copy or commit secrets.
- Credentials: do not create, rotate or expose credentials.
- Production configuration: do not edit without approval.
- Security-sensitive files: do not change without review.
- Destructive commands: do not run without explicit approval.
- License changes: do not change without review.
- Dependency upgrades: do not perform major or security-sensitive upgrades without review.
- Generated translations: do not mark as human-reviewed unless reviewed.
- Compliance claims: do not make legal, regulatory or certification claims without evidence.
- User or customer data: do not inspect, store or document real private data.

## Escalation

If a task touches a boundary, pause and require human review before proceeding.

