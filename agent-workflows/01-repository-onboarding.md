# Repository Onboarding Workflow

## Purpose

Initialize repository awareness before larger AI-assisted work begins.

## When To Use

- Before modifying an unfamiliar repository.
- Before a larger feature, refactor, migration, security review or multi-agent session.
- When existing repository documentation may be stale.

## Required Inputs

- Target repository path.
- User goal or work request.
- Repository instructions such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` or Copilot instructions when present.
- Existing README, docs, tests, scripts and configuration files.

## Process Steps

1. Read repository instructions before inspecting implementation files.
2. Read the README and existing documentation entrypoints.
3. Map the repository structure from tracked files and important directories.
4. Identify build, test, validation and review commands from evidence.
5. Identify security boundaries, sensitive-data rules and permission limits.
6. Summarize confirmed facts, `[UNKNOWN]` gaps and `[ASSUMPTION: ...]` inferences.
7. Propose the `docs/ai/` documentation plan before writing files.

## Expected Output

- A concise repository-awareness summary.
- A list of evidence sources reviewed.
- A proposed `docs/ai/` creation or update plan.
- Open questions and blockers marked as `[UNKNOWN]`.

## Security Rules

- Do not copy secrets, tokens, private keys, certificates or real user data into generated documentation.
- Redact sensitive values and describe only the rule or risk.
- Do not claim production readiness, tool support or external integration without repository evidence.

## Human Review Checkpoint

A human reviews the repository-awareness summary and `docs/ai/` plan before the agent creates documentation or starts coding work.
