# Magical Prompt Improver

<!-- localization-status: localized-mirror; review-status: tracked-in-language-support -->

> Language status: localized mirror of the English reference. Review status is tracked in the language support metadata.
> উৎস ভাষা: ইংরেজি
> উৎস ফাইল: ai/English/prompts/magical-prompt-improver.md
> পার্থক্য থাকলে ইংরেজি ফাইল প্রাধান্য পাবে।

এই পৃষ্ঠা ব্যাখ্যা করে `prompts/magical-prompt-improver.md` কীভাবে AI Agent Operating Manual-এর মধ্যে ব্যবহৃত হয়। এটি repository কাজ পরিকল্পনা, যাচাই বা পুনরাবৃত্তি করতে হয় এমন মানুষ ও AI agents-এর জন্য লেখা। Source protocol: [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

## ব্যবহারিক পরিসর

এই পৃষ্ঠাকে `prompt improvement` বিষয়ের কার্যকরী নির্দেশিকা হিসেবে ব্যবহার করুন। এটি repository প্রমাণ বা প্রকল্প-নির্দিষ্ট নির্দেশের বিকল্প নয়।

## কাজের নির্দেশিকা

- repository প্রমাণকে প্রধান কর্তৃত্ব হিসেবে ধরুন।
- ফাইলের নাম, commands, API নাম এবং model নাম অপরিবর্তিত রাখুন।
- যাচাইহীন সিদ্ধান্ত `[ASSUMPTION: ...]` এবং অজানা তথ্য `[UNKNOWN]` দিয়ে চিহ্নিত করুন।
- tool-নির্দিষ্ট আচরণকে সেই tool বা runtime-এর সঙ্গে যুক্ত করুন যা সত্যিই তা নিয়ন্ত্রণ করে।
- নিরাপত্তা, permissions এবং production-readiness ঝুঁকি মানব পর্যালোচনায় পাঠান।
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

## ফোকাস

workflow-তে এই পৃষ্ঠা ব্যবহারের আগে পরিসর, প্রয়োজনীয় প্রমাণ, যাচাইযোগ্য commands এবং মানব অনুমোদনের সীমা নির্ধারণ করুন।

## Examples

### Status/list request

- Mode: direct answer or Intake Mode.
- Output: short answer, evidence and no file edits.

### Repository change request

- Mode: Intake Mode, then Full Rewrite Mode when scope remains broad.
- Output: scoped workflow, files to inspect, verification commands and final report rules.

## গুণমান পরীক্ষা

- উদ্দেশ্য নতুন contributor-এর কাছে পরিষ্কার।
- নির্দেশিকা AI agents এবং মানব maintainers উভয়ের জন্য সহায়ক।
- model-নির্দিষ্ট commands বানানো হয় না।
- নিরাপত্তা ও মানব অনুমোদনের সীমা দৃশ্যমান থাকে।
- localization সংঘাতে ইংরেজি উৎস সিদ্ধান্তমূলক থাকে।
- The selected activation mode matches the request risk.
- Verification evidence is defined before execution.
