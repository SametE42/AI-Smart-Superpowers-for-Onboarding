# MASTER_SYSTEM.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Central working instructions for AI agents operating in this repository.  
**Created/updated by:** AI Assistant (Model: [MODEL], Run-ID: [RUN-ID])  
***

## Purpose

This document is the central instruction file for AI agents working in this project.

It defines:

- project status,
- work order,
- engineering principles,
- change rules,
- review expectations,
- forbidden actions,
- decision principles,
- status language.

It complements short tool entrypoints such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` or `.github/copilot-instructions.md`.

If rules conflict, the stricter rule applies.

## Project status

**Current status:** `[UNKNOWN]`

Allowed status terms:

- `prototype`: local or incomplete functionality.
- `hardened prototype`: locally usable and tested, but still blocked for production.
- `production-adjacent`: architecture or interfaces are prepared, but operational requirements are not complete.
- `production-ready`: only use this term if persistence, validation, access control, logging, business rules and acceptance evidence are complete.

## Production blockers

Document current blockers:

- `[UNKNOWN]`
- `[UNKNOWN]`
- `[UNKNOWN]`

Do not claim production readiness while blockers remain open.

## Required work order

For relevant work, follow this order:

1. Read `PROJECT_MEMORY.md`.
2. Read task-specific context.
3. Identify goal and non-goals.
4. Document assumptions with reason and risk.
5. Define acceptance criteria.
6. Add or identify tests/checks.
7. Implement minimally.
8. Update documentation.
9. Update `PROJECT_MEMORY.md` with current state, decisions, open tasks and next step.
10. Run checks or document why they were not run.
11. State remaining risks and production status.

## Engineering principles

- Respect existing architecture boundaries.
- Do not invent business rules.
- Prefer explicit `not-configured`, warnings or blockers over guessed behavior.
- Keep UI, domain, data, feature and shared technical layers separate.
- Centralize logging and error handling.
- Keep test data synthetic.
- Do not add new dependencies without documented need, license check, bundle/security impact and human review.
- Do not mix refactoring, feature work and documentation updates without clear reason.
- Treat repeated tool-call validation failures as possible contract-design issues. Validate first, repair narrowly only from concrete validator evidence, re-validate, log the repair and report the choice back to the model.

## Change rules

- Do not delete existing content unless explicitly asked.
- Do not overwrite existing documentation if append-only updates are enough.
- Do not make broad formatting-only changes without explicit request.
- Do not add production data, exports, logs, dumps or uploads to the repository.
- Do not add secrets to code, docs, tests or environment examples.
- Do not silently change architecture rules.
- Do not treat local prototype mechanisms as production infrastructure.

## Review process

Every relevant change should check:

- Does it respect the current architecture?
- Are new data flows documented?
- Are validation and error paths covered?
- Are user-facing errors neutral?
- Are technical details logged only after redaction?
- Are tests appropriate for the risk?
- Are README, CHANGELOG and relevant docs updated?
- Does this require attribution, license or dependency review?
- Does this require updating a tool entrypoint?

## Forbidden actions

- Do not claim production readiness without evidence.
- Do not invent billing, tax, security, pricing, legal or domain rules.
- Do not introduce real personal, customer, financial or internal data.
- Do not mix technical error logs with audit logs, change history or export history.
- Do not add hidden external connections.
- Do not bypass central export or logging safeguards.
- Do not make destructive git or file operations without explicit human approval.

## Decision rules

If information is missing:

- Ask at most three critical questions.
- Mark non-critical gaps as `[UNKNOWN]`.
- Mark plausible but unverified conclusions as `[ASSUMPTION: ...]`.
- Default to conservative, blocking and documented behavior.
- For business rules, prefer `not-configured` over invented logic.
- For security, expose the risk rather than silently accepting it.

## Minimum acceptance criteria for new features

A feature is not complete unless the following are covered or explicitly marked as not applicable:

- rendering without runtime errors,
- empty state,
- invalid input handling,
- relevant tests or documented manual checks,
- neutral user-facing error messages,
- documentation of user impact,
- known limitations,
- production status.

## Context loading strategy

Load only what is needed for the task.
For relevant work, `PROJECT_MEMORY.md` is always read first because it contains current state, assumptions, open tasks and handover notes.

| Task type | Required context |
|---|---|
| Bugfix | `MASTER_SYSTEM.md`, `ERROR_PATTERNS.md`, affected files, latest `CHANGELOG_AI.md` entry |
| Feature | `MASTER_SYSTEM.md`, `ARCHITECTURE.md`, `DOMAIN_KNOWLEDGE.md`, `STYLE_GUIDE.md` |
| Refactoring | `MASTER_SYSTEM.md`, `ARCHITECTURE.md`, `STYLE_GUIDE.md`, `REVIEW_CHECKLIST.md` |
| Security | `MASTER_SYSTEM.md`, `SECURITY_RULES.md`, relevant auth/config/logging files |
| Tests | `MASTER_SYSTEM.md`, `STYLE_GUIDE.md`, `REVIEW_CHECKLIST.md`, existing tests |
| Documentation | `MASTER_SYSTEM.md`, relevant `/docs/ai/` file, `CHANGELOG_AI.md` |

## Update rules

When this document changes:

- update the date,
- document why the rule changed,
- avoid adding duplicate rules,
- keep it short enough to remain usable by future agents.
