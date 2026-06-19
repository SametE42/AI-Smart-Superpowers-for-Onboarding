# Magical Prompt Improver

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> ភាសាប្រភព៖ អង់គ្លេស
> ឯកសារប្រភព: ai/English/prompts/magical-prompt-improver.md
> បើមានភាពខុសគ្នា ឯកសារអង់គ្លេសមានអាទិភាព។

ទំព័រនេះពន្យល់ថា `prompts/magical-prompt-improver.md` សមនឹង AI Agent Operating Manual ដូចម្តេច សម្រាប់មនុស្ស និង AI agents ដែលត្រូវរៀបចំ ផ្ទៀងផ្ទាត់ ឬធ្វើឡើងវិញនូវការងារ repository។ Source protocol: [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

## វិសាលភាពអនុវត្ត

ប្រើទំព័រនេះជាមគ្គុទ្ទេសក៍ប្រតិបត្តិការសម្រាប់ `prompt improvement`។ វាមិនជំនួសភស្តុតាង repository ឬសេចក្តីណែនាំគម្រោងទេ។

## គោលការណ៍ធ្វើការ

- រក្សាឈ្មោះឯកសារ commands ឈ្មោះ API និងឈ្មោះ model ដដែល។
- សម្គាល់សន្និដ្ឋានមិនទាន់ផ្ទៀងផ្ទាត់ដោយ `[ASSUMPTION: ...]` និងអង្គហេតុមិនស្គាល់ដោយ `[UNKNOWN]`។
- បញ្ជូនហានិភ័យ security, permissions និង production-readiness ទៅការត្រួតពិនិត្យដោយមនុស្ស។
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

## ការផ្តោត

មុនប្រើក្នុង workflow សូមកំណត់វិសាលភាព ភស្តុតាង commands ដែលអាចផ្ទៀងផ្ទាត់បាន និងព្រំដែនអនុម័តដោយមនុស្ស។

## Examples

### Status/list request

- Mode: direct answer or Intake Mode.
- Output: short answer, evidence and no file edits.

### Repository change request

- Mode: Intake Mode, then Full Rewrite Mode when scope remains broad.
- Output: scoped workflow, files to inspect, verification commands and final report rules.

## ពិនិត្យគុណភាព

- គោលបំណងច្បាស់សម្រាប់ contributor ថ្មី។
- ប្រភពអង់គ្លេសនៅតែជាចំណុចសម្រេចក្នុងជម្លោះ localization។
- The selected activation mode matches the request risk.
- Verification evidence is defined before execution.
