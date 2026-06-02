# Tool Context Loading

## Purpose

Help AI coding agents load the smallest useful `docs/ai/` context for the task at hand.

## General Rule

Keep context minimal but sufficient. Load stable repository rules first, then the affected files. Preserve visible `[UNKNOWN]` and `[ASSUMPTION]` markers instead of silently converting them into facts.

## Bugfix

Load first:

- `docs/ai/ONBOARDING.md`
- `docs/ai/PROJECT_MEMORY.md`
- `docs/ai/ERROR_PATTERNS.md`
- `docs/ai/SECURITY_RULES.md`
- affected source, test, configuration or documentation files

Use this set to recover current state, known errors, safety boundaries and the concrete failing area.

## Feature

Load first:

- `docs/ai/ONBOARDING.md`
- `docs/ai/PROJECT_MEMORY.md`
- `docs/ai/ARCHITECTURE.md`
- `docs/ai/DOMAIN_KNOWLEDGE.md`
- `docs/ai/STYLE_GUIDE.md`
- `docs/ai/REVIEW_CHECKLIST.md`

Use this set before planning scope, data flow, naming, implementation style and review requirements.

## Security

Load first:

- `docs/ai/SECURITY_RULES.md`
- `docs/ai/ARCHITECTURE.md`
- `docs/ai/PROJECT_MEMORY.md`
- relevant authentication, authorization, configuration, secrets-handling or logging files

Do not load, print or summarize secret values. Document security boundaries and redaction rules, not credentials.

## Documentation

Load first:

- `docs/ai/ONBOARDING.md`
- the relevant `docs/ai/` file being created or updated
- `docs/ai/CHANGELOG_AI.md`

Use this set to keep documentation aligned with current onboarding state, durable memory and prior AI-assisted documentation changes.

## Safety Rules

- Do not load or output secrets, credentials, private keys, certificates or real user data.
- Mark missing facts as `[UNKNOWN]`.
- Mark inferences as `[ASSUMPTION]` or `[ASSUMPTION: ...]`.
- Mark incomplete large-repository coverage as `[PARTIALLY REVIEWED]`.
- Ask for human review when missing context affects implementation, security or review decisions.
