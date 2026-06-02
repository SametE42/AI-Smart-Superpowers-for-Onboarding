# Handover And Memory Refresh Workflow

## Purpose

Refresh handover notes and project memory after significant changes so future AI sessions inherit reviewed context.

## When To Use

- After a completed feature, migration, refactor, documentation update or incident follow-up.
- When architecture, workflows, validation commands or security rules changed.
- When important assumptions were resolved or new unknowns were discovered.

## Required Inputs

- Final diff or change summary.
- Validation and test results.
- Existing `docs/ai/PROJECT_MEMORY.md` and `docs/ai/CHANGELOG_AI.md`.
- Any human review notes or follow-up decisions.

## Process Steps

1. Confirm the change is significant enough to update memory; skip tiny corrections unless they affect future sessions.
2. Review the final diff and validation output.
3. Update `PROJECT_MEMORY.md` with durable context, decisions, open points, assumptions, risks and next steps.
4. Update `CHANGELOG_AI.md` with the documentation or onboarding change and rationale.
5. Remove temporary progress notes before staging or sharing changes.
6. Preserve unresolved facts as `[UNKNOWN]`, `[ASSUMPTION]` or `[ASSUMPTION: ...]`.

## Expected Output

- Updated project memory and AI changelog when warranted.
- Clear handover notes for future AI sessions.
- Visible open points, decisions, assumptions, risks and next steps.
- No temporary progress, session or completion notes left in committed files.

## Security Rules

- Do not write secrets, credentials, certificates, private keys or real user data into memory files.
- Redact sensitive paths, identifiers or values when they are not needed for future work.
- Do not present unreviewed AI output as trusted project truth.

## Human Review Checkpoint

A human reviews memory and handover updates before they are accepted as durable context for future sessions.
