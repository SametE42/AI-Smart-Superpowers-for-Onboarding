# Magical Prompt Improver

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> Bahasa sumber: Inggeris
> Fail sumber: ai/English/prompts/magical-prompt-improver.md
> Jika terdapat perbezaan, fail Inggeris menjadi rujukan utama.

Use this page when a user request, reusable prompt or agent handoff needs to become clearer before repository work starts. The full source protocol is [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

The improver does not make a prompt automatically correct. It reduces ambiguity, exposes missing context, adds safety boundaries and defines evidence that can prove the task is complete.

## Activation Rules

Run a short intake check on every user request before deciding how much prompt improvement is needed.

- Answer directly when the request is clear, low-risk and does not ask for file changes.
- Use Intake Mode when the request has unclear goals, missing success criteria or broad wording.
- Use Full Rewrite Mode before large work, multi-step repository changes or work that crosses documentation, code, tests and Git.
- Use Verification Mode before claiming completion, passing tests, release readiness or production readiness.
- Use Commit/Push Readiness Mode before staging, committing, pushing or opening a pull request.
- Do not run the full protocol for simple status, listing, explanation or lookup requests unless the user asks for prompt improvement.

## Activation Modes

| Mode | Use when | Output |
|---|---|---|
| Intake Mode | The request may be ambiguous, incomplete or risky. | Clarified objective, risks, missing context and safe assumptions. |
| Full Rewrite Mode | The prompt will drive substantial repository work. | A complete rewritten prompt with role, scope, workflow, verification and final report rules. |
| Verification Mode | The task is near completion or makes success claims. | Concrete evidence required before completion can be claimed. |
| Commit/Push Readiness Mode | The task includes Git staging, commit, push, release or PR work. | Scope confirmation, changed-file review, verification commands and final Git action checklist. |

## Decision Tree

1. If the user asks only for status, a list or a short explanation, answer directly unless the request is unclear.
2. If the requested outcome, scope or success criterion is unclear, use Intake Mode.
3. If the work changes files, documentation, tests, scripts, CI or repository structure, define scope and verification before editing.
4. If the work involves security, privacy, secrets, production claims, release, commit, push or PR creation, use Full Rewrite Mode plus Verification Mode.
5. If the prompt is meant to be reused by another agent or human, use Full Rewrite Mode and output the final improved prompt.

## Intake Output

Return a compact intake when the request needs clarification but can still move forward:

```text
Objective:
[Concrete end state]

Risks and ambiguities:
- [Risk or missing detail]

Safe assumptions:
- [Assumption with reason]

Verification:
[Command, check or evidence required]
```

## Full Rewrite Output

Use this structure for substantial repository work:

```text
Role:
[Who the agent should be]

Objective:
[Concrete end state]

Repository context:
[Files, directories, docs or commands to inspect first]

Scope:
[What is in scope]

Out of scope:
[What must not be changed or claimed]

Workflow:
1. [First action]
2. [Next action]

Verification:
[Commands, manual checks or evidence required]

Final report:
[What to summarize]
```

## Anti-Hallucination Rules

- Work from files, command output, issue text or cited sources.
- Mark unknown facts as `[UNKNOWN]` instead of guessing.
- Mark plausible but unverified conclusions as `[ASSUMPTION: ...]`.
- Do not invent tool capabilities, model capabilities, APIs, business rules or repository URLs.
- Do not claim tests passed unless the exact command was run and read.
- Do not add secrets, real user data, internal URLs or production logs.
- Preserve paths, commands, model names and API names exactly unless the task asks to change them.

## Verification Criteria

| Requirement | Evidence |
|---|---|
| Files changed intentionally | `git diff --name-only` reviewed |
| Tests pass | Exact test command and exit code |
| Documentation links are valid | Repository validator or link checker output |
| No secrets added | Secret scan or validator output |
| Final answer is accurate | Summary matches diff and command output |

If a check is not available, the final report must say so.

## Quality Checklist

- Original intent and explicit constraints are preserved.
- Success criteria are measurable.
- Risks and ambiguities are visible.
- Missing context is requested or safe assumptions are stated.
- Workflow is ordered.
- Anti-hallucination rules are included.
- Verification criteria are concrete.
- Activation mode matches the request.
