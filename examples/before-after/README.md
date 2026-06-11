# Before After Example

## Use Case

Show how scattered assumptions become a structured AI knowledge base.

## Repository-Typ

Existing application with informal notes in README files, issue comments and package scripts.

## verwendeter Modus

Standard Integration.

## verwendete Sprache

English.

## verwendeter Strukturmodus

Canonical.

## erkannter oder angenommener Stack

TypeScript hint from `package.json` and `tsconfig.json`; verify before relying on it.

## verwendete Templates

`CONTEXT_INDEX.md`, `ARCHITECTURE.md`, `TECH_STACK.md`, `BUILD_AND_TEST.md`, `EVIDENCE_MAP.md`, `PROJECT_MEMORY.md`.

## Agent zuerst lesen

1. `docs/ai/CONTEXT_INDEX.md`
2. `docs/ai/EVIDENCE_MAP.md`
3. `docs/ai/ARCHITECTURE.md`

## Human Review

Confirm that every migrated assumption has a real evidence source.

## Mini Before

- Build command appears in a README but may be stale.
- Architecture is described in old issue comments.
- Security assumptions are not written down.

## Mini After

- Build and test commands are recorded in `BUILD_AND_TEST.md`.
- Claims are traced in `EVIDENCE_MAP.md`.
- Security boundaries are centralized in `SECURITY_RULES.md`.
