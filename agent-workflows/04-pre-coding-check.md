# Pre-Coding Check Workflow

## Purpose

Confirm that repository context is ready before planning, implementation, testing or review begins.

## When To Use

- Immediately before coding starts.
- Before reviewing code in a repository with new or stale `docs/ai/` context.
- Before executing an implementation plan created by an AI agent.

## Required Inputs

- User request.
- Current repository instructions.
- Reviewed `docs/ai/` files, especially `ONBOARDING.md`, `PROJECT_MEMORY.md`, `SECURITY_RULES.md`, `ARCHITECTURE.md` and `REVIEW_CHECKLIST.md`.
- Current git status and relevant validation commands.

## Process Steps

1. Load the relevant `docs/ai/` files before proposing implementation steps.
2. Check whether the user request fits documented architecture, ownership and security boundaries.
3. Identify required evidence for the requested change.
4. List unresolved `[UNKNOWN]` or `[ASSUMPTION: ...]` items that could affect the work.
5. Confirm which tests, validators or manual checks should run.
6. Decide whether coding can begin or whether more onboarding is required.

## Expected Output

- A short go/no-go decision for coding.
- Required context files and evidence sources.
- Test and validation commands to run.
- Any blockers requiring human decision.

## Security Rules

- Stop before coding if the request conflicts with documented security boundaries.
- Do not bypass human approval for high-risk, destructive, production or sensitive-data changes.
- Keep unknowns visible instead of converting them into assumptions.

## Human Review Checkpoint

A human approves the go/no-go decision when blockers, high-risk changes or unresolved context gaps are present.
