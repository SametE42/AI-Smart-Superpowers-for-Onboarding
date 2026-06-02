# Tool Context Loading

## Purpose

Help AI coding agents load the smallest useful `docs/ai/` context for the task at hand and avoid loading too much or the wrong context.

## General Rule

Load only the context needed for the task. Start with `docs/ai/ONBOARDING.md` and `docs/ai/PROJECT_MEMORY.md`, then add task-specific files. Do not load secrets or sensitive data. Preserve visible `[UNKNOWN]` gaps instead of silently converting them into facts.

## Bugfix Context

Load first:

- `docs/ai/ONBOARDING.md`
- `docs/ai/PROJECT_MEMORY.md`
- `docs/ai/ERROR_PATTERNS.md`
- `docs/ai/SECURITY_RULES.md`
- affected source, test, configuration or documentation files
- relevant tests

Use this set to recover current state, known errors, safety boundaries and the concrete failing area.

## Feature Context

Load first:

- `docs/ai/ONBOARDING.md`
- `docs/ai/PROJECT_MEMORY.md`
- `docs/ai/ARCHITECTURE.md`
- `docs/ai/DOMAIN_KNOWLEDGE.md`
- `docs/ai/STYLE_GUIDE.md`
- `docs/ai/REVIEW_CHECKLIST.md`

Use this set before planning scope, data flow, naming, implementation style and review requirements.

## Security Context

Load first:

- `docs/ai/SECURITY_RULES.md`
- `docs/ai/ARCHITECTURE.md`
- `docs/ai/PROJECT_MEMORY.md`
- relevant authentication, authorization, configuration, logging or permission files

Do not load, print or summarize secret values. Document security boundaries and redaction rules, not credentials.

## Documentation Context

Load first:

- `docs/ai/ONBOARDING.md`
- the relevant `docs/ai/` file being created or updated
- `docs/ai/CHANGELOG_AI.md`
- existing README or documentation files

Use this set to keep documentation aligned with current onboarding state, durable memory and prior AI-assisted documentation changes.

## Minimal Context Principle

- Keep context minimal but sufficient.
- Do not automatically load all `docs/ai/` files.
- When uncertain, prioritize by task and risk.
- Keep `[UNKNOWN]` and `[ASSUMPTION]` visible.

## Safety Notes

- Do not load or output secrets, credentials, private keys, certificates or real user data.
- Mark missing facts as `[UNKNOWN]`.
- Mark inferences as `[ASSUMPTION]` or `[ASSUMPTION: ...]`.
- Mark incomplete large-repository coverage as `[PARTIALLY REVIEWED]`.
- Ask for human review when missing context affects implementation, security or review decisions.
