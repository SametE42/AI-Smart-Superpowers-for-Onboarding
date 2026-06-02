# Repository Onboarding Workflow

## Purpose

Initialize repository awareness before larger AI-assisted work begins, using `templates/MASTER_PROMPT.en.md` as the primary onboarding prompt.

## When To Use

- Before modifying an unfamiliar repository.
- Before a larger feature, refactor, migration, security review or multi-agent session.
- When existing repository documentation may be stale.

## Required Inputs

- Target repository path.
- User goal or work request.
- `templates/MASTER_PROMPT.en.md`.
- Repository instructions such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` or Copilot instructions when present.
- Existing README, docs, tests, scripts and configuration files.

## Process Steps

1. Read repository instructions before inspecting implementation files.
2. Use `templates/MASTER_PROMPT.en.md` to guide the repository pre-check and documentation plan.
3. Read the README and existing documentation entrypoints.
4. Map the repository structure from tracked files and important directories.
5. For large repositories, prioritize entrypoints, configuration, tests, central modules and existing documentation.
6. Mark any unreviewed or only sampled areas as `[PARTIALLY REVIEWED]`.
7. Identify build, test, validation and review commands from evidence.
8. Identify security boundaries, sensitive-data rules and permission limits.
9. Summarize confirmed facts, `[UNKNOWN]` gaps and `[ASSUMPTION: ...]` inferences.
10. Propose the `docs/ai/` documentation plan before writing files.
11. After human approval, create or update `docs/ai/` according to the reviewed plan.

## Expected Output

- A concise repository-awareness summary.
- A list of evidence sources reviewed.
- A proposed `docs/ai/` creation or update plan.
- Created or updated `docs/ai/` files after human approval.
- Open questions and blockers marked as `[UNKNOWN]`.
- Large-repository coverage gaps marked as `[PARTIALLY REVIEWED]`.

## Security Rules

- Do not copy secrets, tokens, private keys, certificates or real user data into generated documentation.
- Redact sensitive values and describe only the rule or risk.
- Do not claim production readiness, tool support or external integration without repository evidence.

## Human Review Checkpoint

A human review is required before the agent creates or updates `docs/ai/`, and again before coding work starts.
