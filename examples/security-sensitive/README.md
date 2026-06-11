# Security Sensitive Example

## Use Case

Repository where secrets, authentication, deployment or sensitive data handling are central risks.

## Repository-Typ

Backend service, infrastructure repository or internal platform.

## verwendeter Modus

Enterprise Integration.

## verwendete Sprache

English.

## verwendeter Strukturmodus

Canonical.

## erkannter oder angenommener Stack

Backend or Infrastructure-as-Code; verify from files such as `Dockerfile`, Terraform files or service manifests.

## verwendete Templates

`SECURITY_RULES.md`, `SAFETY_BOUNDARIES.md`, `HUMAN_REVIEW_GATES.md`, `RISK_REGISTER.md`, `RUNTIME_ENVIRONMENT.md`.

## Agent zuerst lesen

1. `docs/ai/SECURITY_RULES.md`
2. `docs/ai/SAFETY_BOUNDARIES.md`
3. `docs/ai/HUMAN_REVIEW_GATES.md`

## Human Review

Human review is required before auth, permissions, deployment, secrets, logging or data-retention changes.

## Boundary

Do not include real secrets, customer data or internal incident details in examples.
