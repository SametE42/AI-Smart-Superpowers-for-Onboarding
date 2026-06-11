# Enterprise Example

## Use Case

Governance-heavy repository that needs risk, runtime, agent-role and human-review boundaries.

## Repository-Typ

Security-sensitive service, regulated product or large multi-team repository.

## verwendeter Modus

Enterprise Integration.

## verwendete Sprache

English.

## verwendeter Strukturmodus

Canonical or localized through File-Map.

## erkannter oder angenommener Stack

Fullstack or backend; stack claims require evidence.

## verwendete Templates

All enterprise templates, especially `RISK_REGISTER.md`, `RUNTIME_ENVIRONMENT.md`, `AGENT_ROLES.md`, `SAFETY_BOUNDARIES.md` and `HUMAN_REVIEW_GATES.md`.

## Agent zuerst lesen

1. `docs/ai/CONTEXT_INDEX.md`
2. `docs/ai/HUMAN_REVIEW_GATES.md`
3. `docs/ai/SAFETY_BOUNDARIES.md`
4. `docs/ai/RISK_REGISTER.md`

## Human Review

Human review is mandatory for Risk Register changes, auth, permissions, deployment, data exposure and public claims.

## Governance Signal

Use `HUMAN_REVIEW_GATES.md` to separate AI-suggested changes from changes approved for merge or production.
