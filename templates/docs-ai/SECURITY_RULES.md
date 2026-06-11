# SECURITY_RULES.md

**Last updated:** YYYY-MM-DD
**Status:** DRAFT
**Scope:** Security rules for AI-assisted work.

## Secrets

- Do not expose secrets, tokens, certificates, private keys or credentials.
- Record only redacted locations and required remediation.
- Do not add real secrets to examples, tests or documentation.

## Credentials

- Authentication credentials: `[UNKNOWN]`
- Authorization model: `[UNKNOWN]`
- Production credential handling: `[UNKNOWN]`

## Production configuration

- Do not edit production configuration without human approval.
- Do not infer production readiness from local setup.
- Document unknown deployment and runtime assumptions.

## Data exposure

- Do not add real personal, customer, financial or internal data.
- Keep test data synthetic.
- Redact logs, payloads and screenshots before documentation.

## Auth

- Authentication evidence: `[UNKNOWN]`
- Authorization evidence: `[UNKNOWN]`
- Role or permission evidence: `[UNKNOWN]`

## Permissions

- Destructive operations require explicit human approval.
- Permission changes require human review.
- Access-control claims require implementation evidence.

## Dependency risk

- Security-sensitive dependency updates require review.
- Unknown licenses or supply-chain risk must be flagged.
- Do not add dependencies without evidence of need.

## Human review requirements

Human review is required for secrets, credentials, auth, permissions, production configuration, data exposure, dependency risk, deployment and public security claims.
