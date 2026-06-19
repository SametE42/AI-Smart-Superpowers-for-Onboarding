# Magical Prompt Improver

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> මූලාශ්‍ර භාෂාව: ඉංග්‍රීසි
> මූලාශ්‍ර ගොනුව: ai/English/prompts/magical-prompt-improver.md
> වෙනසක් තිබේ නම් ඉංග්‍රීසි ගොනුව ප්‍රමුඛ වේ.

මෙම පිටුව `prompts/magical-prompt-improver.md` AI Agent Operating Manual තුළ කෙසේ ගැළපෙන්නේද යන්න පැහැදිලි කරයි; repository වැඩ සැලසුම් කරන, සත්‍යාපනය කරන හෝ නැවත කරන පුද්ගලයින් සහ AI agents සඳහායි. Source protocol: [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

## ප්‍රායෝගික විෂය පථය

මෙම පිටුව `prompt improvement` සඳහා මෙහෙයුම් මාර්ගෝපදේශයක් ලෙස භාවිත කරන්න. මෙය repository සාක්ෂි හෝ ව්‍යාපෘති උපදෙස් වෙනුවට නොවේ.

## වැඩ මාර්ගෝපදේශ

- ගොනු නම්, commands, API නම් සහ model නම් අකුරටම රකින්න.
- තහවුරු නොකළ නිගමන `[ASSUMPTION: ...]` ලෙසත් නොදන්නා කරුණු `[UNKNOWN]` ලෙසත් ලකුණු කරන්න.
- security, permissions සහ production-readiness අවදානම් මිනිස් සමාලෝචනයට යොමු කරන්න.
- Keep `Intake Mode`, `Full Rewrite Mode`, `Verification Mode` and `Commit/Push Readiness Mode` as stable mode names.
- Use concrete evidence before success, release, commit or push claims.

## Activation Modes

| Mode | Use when | Output |
|---|---|---|
| Intake Mode | Ambiguous or incomplete request. | Clarified objective, risks, missing context and safe assumptions. |
| Full Rewrite Mode | Substantial repository work. | Role, scope, workflow, verification and final report rules. |
| Verification Mode | Success or readiness claim. | Concrete evidence required before completion can be claimed. |
| Commit/Push Readiness Mode | Git, release or PR action. | Scope confirmation, diff review, checks and final Git action list. |

## Decision Tree

1. status/list/explanation -> direct answer unless the request is unclear.
2. unclear objective/scope/success criterion -> Intake Mode.
3. file, documentation, test, script, CI or structure change -> scope and verification before editing.
4. security, privacy, secrets, production, release, commit, push or PR -> Full Rewrite Mode plus Verification Mode.
5. reusable prompt or agent handoff -> Full Rewrite Mode.

## Workflow order

1. Preserve the original request and explicit constraints.
2. Select the lightest safe activation mode.
3. Define objective, scope, non-goals, risks and missing context.
4. Rewrite only when the work is broad, high-impact or reusable.
5. Define verification evidence before execution.
6. Make the final report match the diff and command output.

## Intake Output

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

- Use files, command output, issue text or cited sources as evidence.
- Mark unknown facts as `[UNKNOWN]`.
- Mark unverified conclusions as `[ASSUMPTION: ...]`.
- Do not invent tool capabilities, model capabilities, APIs, business rules or repository URLs.
- Do not claim tests passed without the exact command output.
- Do not add secrets, real user data, internal URLs or production logs.
- Preserve paths, commands, model names and API names unless the task asks to change them.

## Verification Criteria

| Requirement | Evidence |
|---|---|
| Intentional file changes | `git diff --name-only` reviewed |
| Tests pass | Exact command and exit code |
| Documentation links are valid | Repository validator or link checker output |
| No secrets added | Secret scan or validator output |
| Final answer is accurate | Summary matches diff and command output |

If a check is unavailable, the final report must say so.

## අවධානය

workflow තුළ භාවිතයට පෙර විෂය පථය, සාක්ෂි, සත්‍යාපනය කළ හැකි commands සහ මිනිස් අනුමැතියේ සීමා නිර්වචනය කරන්න.

## Examples

### Status/list request

- Mode: direct answer or Intake Mode.
- Output: short answer, evidence and no file edits.

### Repository change request

- Mode: Intake Mode, then Full Rewrite Mode when scope remains broad.
- Output: scoped workflow, files to inspect, verification commands and final report rules.

## ගුණාත්මක පරීක්ෂාව

- අරමුණ නව contributor සඳහා පැහැදිලිය.
- localization ගැටුම්වලදී ඉංග්‍රීසි මූලාශ්‍රය තීරණාත්මක වේ.
- The selected activation mode matches the request risk.
- Verification evidence is defined before execution.
