# Magical Prompt Improver

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> שפת מקור: אנגלית
> קובץ מקור: ai/English/prompts/magical-prompt-improver.md
> במקרה של סתירה, הקובץ באנגלית הוא הקובע.

דף זה מסביר כיצד `prompts/magical-prompt-improver.md` משתלב ב-AI Agent Operating Manual. הוא מיועד לאנשים ול-AI agents שצריכים לתכנן, לאמת או לחזור על עבודה ב-repository. Source protocol: [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

## היקף מעשי

השתמש בדף זה כהנחיה תפעולית לנושא `prompt improvement`. הוא אינו מחליף ראיות מה-repository או הוראות ייחודיות לפרויקט.

## הנחיות עבודה

- התייחס לראיות מה-repository כסמכות העיקרית.
- שמור בדיוק על שמות קבצים, commands, שמות API ושמות מודלים.
- סמן מסקנות לא מאומתות עם `[ASSUMPTION: ...]` ועובדות לא ידועות עם `[UNKNOWN]`.
- קשר התנהגות ייחודית לכלי אל ה-tool או runtime שבאמת מחזיק בה.
- העבר סיכוני security, permissions ו-production-readiness לביקורת אנושית.
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

## מיקוד

לפני שימוש בדף זה ב-workflow, הגדר היקף, ראיות נדרשות, commands ניתנים לאימות וגבולות אישור אנושי.

## Examples

### Status/list request

- Mode: direct answer or Intake Mode.
- Output: short answer, evidence and no file edits.

### Repository change request

- Mode: Intake Mode, then Full Rewrite Mode when scope remains broad.
- Output: scoped workflow, files to inspect, verification commands and final report rules.

## בדיקת איכות

- המטרה ברורה ל-contributor חדש.
- ההנחיה מועילה גם ל-AI agents וגם ל-maintainers אנושיים.
- לא ממציאים commands ייחודיים למודלים.
- גבולות security ואישור אנושי נשארים גלויים.
- המקור האנגלי נשאר מכריע בסכסוכי localization.
- The selected activation mode matches the request risk.
- Verification evidence is defined before execution.
