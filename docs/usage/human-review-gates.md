# Human Review Gates

## Purpose

Define the human checkpoints that keep AI-generated onboarding documentation useful, evidence-based and reviewable.

## Gate 1: Documentation Plan Review

### Purpose

Approve the `docs/ai/` creation or update plan before the agent writes durable repository context.

### Required Inputs

- Repository onboarding summary.
- Evidence sources reviewed.
- Proposed `docs/ai/` files to create or update.
- Known `[UNKNOWN]`, `[ASSUMPTION]` and `[PARTIALLY REVIEWED]` markers.

### What Humans Check

- The plan matches the repository and current user goal.
- All relevant target files are named.
- Sensitive areas are recognized.
- Uncertainties are visible.
- The proposed files are necessary and not duplicative.
- The scope is realistic.
- The proposed documentation scope is not unnecessarily large.
- Security-sensitive areas are handled conservatively.

### Pass Criteria

- Scope is clear.
- Missing facts remain visibly marked.
- No secrets, sensitive data or unsupported production claims are included.

### Fail / Revise Criteria

- The plan invents facts, overreaches, duplicates existing docs or omits a required security boundary.

## Gate 2: Knowledge Base Review

### Purpose

Review generated or updated `docs/ai/` files before future sessions use them as reliable context.

### Required Inputs

- Updated `docs/ai/` files.
- Evidence summary or source references.
- Validation or link-check results when available.

### What Humans Check

- Claims are supported by repository evidence.
- `[UNKNOWN]`, `[ASSUMPTION]` and `[PARTIALLY REVIEWED]` markers are accurate.
- No secrets are documented.
- Architecture and security statements are not overstated.
- Unreviewed areas are visibly marked.
- Security rules, review boundaries and sensitive-data handling are explicit.

### Pass Criteria

- The knowledge base is accurate enough to guide future AI sessions.
- Open gaps are marked instead of hidden.
- The reviewed files are safe to reuse as context.

### Fail / Revise Criteria

- The knowledge base contains unsupported claims, stale facts, missing security boundaries or unreviewed sensitive details.

## Gate 3: Pre-Coding Review

### Purpose

Decide whether planning, implementation, tests or review can begin.

### Required Inputs

- User request.
- Current `docs/ai/ONBOARDING.md`.
- Current `docs/ai/PROJECT_MEMORY.md`.
- Current `docs/ai/SECURITY_RULES.md`.
- Current `docs/ai/ARCHITECTURE.md`.
- Current `docs/ai/REVIEW_CHECKLIST.md`.

### What Humans Check

- The request fits documented architecture and ownership boundaries.
- Required context has been loaded.
- Security boundaries are clear.
- Review criteria are known.
- Blocking unknowns are visible.
- Coding remains reasonable despite any unresolved uncertainty.
- Security or privacy-sensitive work has explicit approval.

### Pass Criteria

- The agent has enough reviewed context to proceed.
- Tests and validation commands are known or explicitly marked `[UNKNOWN]`.
- High-risk work has a clear review path.

### Fail / Revise Criteria

- Required context is missing, the request conflicts with security rules or human approval is needed for high-risk work.

## Gate 4: Post-Change Memory Refresh Review

### Purpose

Confirm durable memory is refreshed after significant changes before the session ends.

### Required Inputs

- Final diff or change summary.
- Validation and test results.
- Updated `docs/ai/PROJECT_MEMORY.md` when warranted.
- Updated `docs/ai/CHANGELOG_AI.md` when warranted.

### What Humans Check

- The memory update captures only durable, reusable context.
- Temporary session notes are not committed.
- `PROJECT_MEMORY.md` and `CHANGELOG_AI.md` were updated when warranted.
- New decisions are documented.
- New risks, decisions and open questions are visible.
- Assumptions and risks are current.
- Relevant intentionally unchanged areas are documented.

### Pass Criteria

- Future AI sessions can understand what changed and what remains open.
- No secrets, credentials or real user data are documented.
- Significant changes are reflected without bloating the knowledge base.

### Fail / Revise Criteria

- The update includes temporary progress notes, omits important decisions or treats unreviewed AI output as trusted truth.

## Review Outcomes

| Outcome | Meaning |
|---|---|
| Pass | The agent may proceed to the next workflow step. |
| Revise | The agent must update the plan, documentation or memory and return for review. |
| Block | Work must stop until the blocking issue is resolved. |
| Escalate to human owner | A repository owner or accountable maintainer must decide before work continues. |
