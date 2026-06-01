# Magical Prompt Improver

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Optional prompt-refinement protocol for turning unclear prompts into precise, safe and verifiable instructions.  
***

## Goal

This template helps humans and AI agents improve a prompt before using it for repository work.

It does not make the prompt automatically correct. It reduces ambiguity, exposes missing context, adds safety boundaries and defines verification criteria.

## When to use

Use this template when a prompt is:

- too broad,
- missing success criteria,
- missing repository context,
- likely to cause invented claims,
- unclear about files, tools, tests or deliverables,
- mixing analysis, implementation, commit or deployment work without gates.

Do not use it to hide uncertainty. If the task is blocked by missing facts, the improved prompt must say so.

## Activation Rules

Run a short intake check on every user request before deciding how much prompt improvement is needed.

Use the lightest effective mode:

- Answer directly when the request is clear, low-risk and does not ask for file changes.
- Use Intake Mode when the request has unclear goals, missing success criteria or broad wording.
- Use Full Rewrite Mode before large work, multi-step repository changes or work that crosses documentation, code, tests and Git.
- Use Verification Mode before claiming completion, passing tests, release readiness or production readiness.
- Use Commit/Push Readiness Mode before staging, committing, pushing or opening a pull request.

Do not run the full protocol for simple status, listing, explanation or lookup requests unless the user asks for prompt improvement.

## Activation Modes

| Mode | Use when | Output |
|---|---|---|
| Intake Mode | The request may be ambiguous, incomplete or risky. | Clarified objective, risks, missing context and safe assumptions. |
| Full Rewrite Mode | The prompt will drive substantial repository work. | A complete rewritten prompt with role, scope, workflow, verification and final report rules. |
| Verification Mode | The task is near completion or makes success claims. | Concrete evidence required before completion can be claimed. |
| Commit/Push Readiness Mode | The task includes Git staging, commit, push, release or PR work. | Scope confirmation, changed-file review, verification commands and final Git action checklist. |

## Decision Tree

```text
1. Is the user asking only for status, a list or a short explanation?
   -> Answer directly unless the request is unclear.

2. Is the requested outcome, scope or success criterion unclear?
   -> Use Intake Mode.

3. Will the work change files, documentation, tests, scripts, CI or repository structure?
   -> Use Intake Mode, then define scope and verification before editing.

4. Does the work involve security, privacy, secrets, production claims, release, commit, push or PR creation?
   -> Use Full Rewrite Mode plus Verification Mode.

5. Is the prompt meant to be reused by another agent or human?
   -> Use Full Rewrite Mode and output the final improved prompt.
```

## Input

```text
Original prompt:
[PASTE ORIGINAL PROMPT]

Known context:
[REPOSITORY, FILES, ISSUE, PR, USER GOAL OR UNKNOWN]

Required output:
[WHAT THE IMPROVED PROMPT SHOULD PRODUCE]

Constraints:
[SECURITY, PRIVACY, APPROVAL, TESTING, COMMIT OR PUSH RULES]
```

## Sequential improvement protocol

### 1. Capture the original prompt

Copy the original prompt exactly before changing it.

Record:

- the original wording,
- who or what the prompt is for,
- whether it asks for analysis, editing, testing, committing, pushing or deployment,
- any explicit constraints that must be preserved.

Do not silently remove user constraints.

### 2. Clarify the goal and success criteria

Rewrite the goal in one or two concrete sentences.

Define success criteria that can be checked:

- expected files or artifacts,
- expected behavior,
- expected commands or tests,
- expected final report,
- required approval gates.

If success cannot be measured, mark the missing criterion as `[UNKNOWN]`.

### 3. Mark risks and ambiguities

List anything that could cause an unsafe or incorrect result:

- missing repository context,
- unclear ownership of files,
- broad refactor scope,
- unsupported tool, model or provider claims,
- security or privacy exposure,
- production-readiness claims without evidence,
- missing test or validation command,
- ambiguity about commit, push or release expectations.

Each risk should include a recommended handling rule.

### 4. Request missing context

If the prompt cannot be executed safely from the available evidence, request only the missing context needed to proceed.

Prefer concrete questions:

```text
Need before execution:
1. Which branch or PR should be targeted?
2. Which verification command proves completion?
3. Should changes be committed and pushed?
```

If reasonable assumptions are safe, state them explicitly instead of blocking.

### 5. Rebuild the prompt into structured sections

Convert the prompt into this structure:

```text
Role:
[WHO THE AGENT SHOULD BE FOR THIS TASK]

Objective:
[THE CONCRETE END STATE]

Repository context:
[FILES, DIRECTORIES, DOCS OR COMMANDS TO READ FIRST]

Scope:
[WHAT IS IN SCOPE]

Out of scope:
[WHAT MUST NOT BE CHANGED OR CLAIMED]

Workflow:
1. [FIRST ACTION]
2. [SECOND ACTION]
3. [NEXT ACTION]

Verification:
[COMMANDS, MANUAL CHECKS OR EVIDENCE REQUIRED]

Final report:
[WHAT TO SUMMARIZE]
```

Keep the prompt direct and executable. Remove motivational filler.

### 6. Add anti-hallucination rules

Add rules that keep the agent grounded:

- Work from files, command output, issue text or cited sources.
- Mark unknowns as `[UNKNOWN]` instead of guessing.
- Do not invent tool capabilities, model capabilities, APIs, business rules or repository URLs.
- Do not claim tests passed unless the exact command was run and read.
- Do not add secrets, real user data, internal URLs or production logs.
- Preserve paths, commands, model names and API names exactly unless the task asks to change them.

### 7. Add verification criteria

Define what proves the task is complete.

Use concrete evidence:

| Requirement | Evidence |
|---|---|
| Files changed intentionally | `git diff --name-only` reviewed |
| Tests pass | Exact test command and exit code |
| Documentation links are valid | Repository validator or link checker output |
| No secrets added | Secret scan or validator output |
| Final answer is accurate | Summary matches diff and command output |

If a check is not available, require the final report to say so.

### 8. Output the final improved prompt

Return the improved prompt as a ready-to-use block.

It should include:

- the objective,
- evidence to inspect first,
- ordered workflow,
- safety and privacy boundaries,
- verification commands,
- final report requirements,
- unresolved questions or assumptions.

Do not include hidden reasoning. Do not claim the improved prompt is guaranteed to be correct.

## Example

Original prompt:

```text
Make this repo better and push it.
```

Improved prompt:

```text
Role:
Act as a repository maintenance assistant.

Objective:
Review the repository for clear, low-risk documentation, validation and workflow improvements. Apply only changes that are supported by repository evidence, then verify, commit and push if all checks pass.

Repository context:
Read `README.md`, `AGENTS.md`, relevant files under `docs/`, `templates/`, `scripts/` and `tests/`, plus the current Git status.

Scope:
- Fix clear documentation, validation, link, naming or workflow consistency issues.
- Update tests when validator behavior changes.
- Regenerate committed validation reports if output changes.

Out of scope:
- Do not add unsupported tool, model or provider claims.
- Do not add secrets, real user data, internal URLs or production logs.
- Do not create progress, audit, session or handover files.

Workflow:
1. Inspect current repository state and relevant docs.
2. Identify concrete issues with evidence.
3. Add failing tests before validator behavior changes.
4. Implement focused fixes.
5. Run required tests and validation.
6. Review the final diff.
7. Commit and push only if verification passes.

Verification:
Run `python -m unittest discover -s tests` and `python scripts/validate_repository.py --root .`. Regenerate reports when needed and rerun the validator.

Final report:
Summarize what changed, what was verified, the commit hash and whether push succeeded.
```

## Ready-to-copy prompt

```text
You are improving a prompt before it is used for repository work.

Original prompt:
[PASTE ORIGINAL PROMPT]

Known context:
[PASTE AVAILABLE CONTEXT OR WRITE UNKNOWN]

Improve the prompt by following this sequence:

1. Preserve the original intent and explicit constraints.
2. Restate the objective in concrete, verifiable terms.
3. Identify risks, ambiguities and missing context.
4. Ask only for missing context that is required; otherwise state safe assumptions.
5. Rewrite the prompt into structured sections: Role, Objective, Repository context, Scope, Out of scope, Workflow, Verification and Final report.
6. Add anti-hallucination rules: work from evidence, mark unknowns, do not invent tools/models/APIs/business rules/URLs, do not claim verification without command output, and do not include sensitive data.
7. Add verification criteria that prove completion.
8. Output only the final improved prompt plus a short list of unresolved questions, if any.

The improved prompt must be precise, safe, concise and executable. It must not add unsupported claims or remove required constraints.
```

## Quality checklist

- [ ] Original intent is preserved.
- [ ] Success criteria are measurable.
- [ ] Risks and ambiguities are visible.
- [ ] Missing context is requested or safe assumptions are stated.
- [ ] Workflow is ordered.
- [ ] Anti-hallucination rules are included.
- [ ] Verification criteria are concrete.
- [ ] Final prompt is ready to use.
- [ ] Activation mode is appropriate for the request.
