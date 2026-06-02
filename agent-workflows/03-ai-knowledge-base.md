# AI Knowledge Base Workflow

## Purpose

Create or update the target repository's reviewed `docs/ai/` knowledge base.

## When To Use

- After repository onboarding and evidence-first analysis.
- When future AI sessions need stable project context.
- When significant repository changes make existing `docs/ai/` content stale.

## Required Inputs

- Approved documentation plan.
- Evidence summary from repository onboarding.
- Target `docs/ai/` templates or existing `docs/ai/` files.
- Repository security and review constraints.
- README `docs/ai/` overview for conceptual target output.

## Process Steps

1. Create or update only the `docs/ai/` files approved in the plan.
2. Treat the README file list as a conceptual overview of the target output, not a mandatory creation order.
3. Choose the safest creation or update order for the current repository and reviewed plan.
4. Prefer the target repository's existing documentation style.
5. Ground architecture, workflow and security claims in repository evidence.
6. Preserve `[UNKNOWN]`, `[ASSUMPTION: ...]` and `[PARTIALLY REVIEWED: ...]` markers where facts remain unverified.
7. Keep tool entrypoints short and link them to `docs/ai/` instead of duplicating long guidance.
8. Update `CHANGELOG_AI.md` when AI documentation changes are significant.
9. Run available documentation validation or link checks when the repository provides them.

## Expected Output

- A reviewed `docs/ai/` knowledge base, commonly including `ONBOARDING.md`, `PROJECT_MEMORY.md`, `SECURITY_RULES.md`, `ARCHITECTURE.md` and `REVIEW_CHECKLIST.md`.
- Clear evidence notes, uncertainty markers and human-review requirements.
- A short summary of changed files and validation results.

## Security Rules

- Never document secrets, credentials, private keys, certificates or real user data.
- Do not make unsupported production-readiness or compliance claims.
- Keep security boundaries explicit and conservative.

## Human Review Checkpoint

A human reviews the generated or updated `docs/ai/` files before they are treated as reusable context for future coding sessions.
