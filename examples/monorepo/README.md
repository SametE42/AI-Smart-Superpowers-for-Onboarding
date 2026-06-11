# Monorepo Example

## Use Case

Multiple packages or services need shared onboarding context plus bounded local context.

## Repository-Typ

Monorepo with `packages/`, `services/` or `apps/`.

## verwendeter Modus

Standard Integration, with Enterprise additions if teams or permissions differ.

## verwendete Sprache

English.

## verwendeter Strukturmodus

Canonical.

## erkannter oder angenommener Stack

Mixed stack; detect per package and document uncertainty.

## verwendete Templates

`CONTEXT_INDEX.md`, `ARCHITECTURE.md`, `TECH_STACK.md`, `BUILD_AND_TEST.md`, `DEPENDENCIES.md`, `EVIDENCE_MAP.md`, `AGENT_ROLES.md` when needed.

## Agent zuerst lesen

1. `docs/ai/CONTEXT_INDEX.md`
2. `docs/ai/ARCHITECTURE.md`
3. `docs/ai/TECH_STACK.md`

## Human Review

Review package boundaries and ownership before cross-package changes.

## Example Layout

```text
packages/
services/
docs/ai/
```
