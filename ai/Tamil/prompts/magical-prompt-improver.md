# Magical Prompt Improver

<!-- localization-status: localized-mirror; review-status: tracked-in-language-support -->

> Language status: localized mirror of the English reference. Review status is tracked in the language support metadata.
> மூல மொழி: ஆங்கிலம்
> மூல கோப்பு: ai/English/prompts/magical-prompt-improver.md
> வேறுபாடு இருந்தால் ஆங்கில கோப்பே முன்னுரிமை பெறும்.

இந்த பக்கம் `prompts/magical-prompt-improver.md` AI Agent Operating Manual-இல் எப்படி பொருந்துகிறது என்பதை விளக்குகிறது; repository பணியை திட்டமிடும், சரிபார்க்கும் அல்லது மீண்டும் செய்யும் மனிதர்கள் மற்றும் AI agents க்காக. Source protocol: [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

## நடைமுறை வரம்பு

இந்த பக்கத்தை `prompt improvement` க்கான செயல்பாட்டு வழிகாட்டியாகப் பயன்படுத்துங்கள். இது repository ஆதாரங்கள் அல்லது திட்ட வழிமுறைகளை மாற்றாது.

## பணி வழிகாட்டிகள்

- கோப்பு பெயர்கள், commands, API பெயர்கள் மற்றும் model பெயர்களை அப்படியே வைத்திருங்கள்.
- சரிபார்க்காத முடிவுகளை `[ASSUMPTION: ...]` என்றும் தெரியாத உண்மைகளை `[UNKNOWN]` என்றும் குறிக்கவும்.
- security, permissions மற்றும் production-readiness அபாயங்களை மனித மதிப்பாய்வுக்கு உயர்த்தவும்.
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

## கவனம்

workflow-இல் பயன்படுத்துவதற்கு முன் வரம்பு, ஆதாரம், சரிபார்க்கக்கூடிய commands மற்றும் மனித ஒப்புதல் எல்லைகளை வரையறுக்கவும்.

## Examples

### Status/list request

- Mode: direct answer or Intake Mode.
- Output: short answer, evidence and no file edits.

### Repository change request

- Mode: Intake Mode, then Full Rewrite Mode when scope remains broad.
- Output: scoped workflow, files to inspect, verification commands and final report rules.

## தரச் சரிபார்ப்பு

- புதிய contributor-க்கு நோக்கம் தெளிவாக உள்ளது.
- localization முரண்பாடுகளில் ஆங்கில மூலமே தீர்மானிக்கிறது.
- The selected activation mode matches the request risk.
- Verification evidence is defined before execution.
