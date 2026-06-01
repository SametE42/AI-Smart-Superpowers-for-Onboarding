# Magical Prompt Improver

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> 원본 언어: 영어
> 원본 파일: ai/English/prompts/magical-prompt-improver.md
> 차이가 있으면 영어 파일을 기준으로 합니다.

이 페이지는 `prompts/magical-prompt-improver.md`가 AI Agent Operating Manual 안에서 어떻게 쓰이는지 설명합니다. 저장소 작업을 계획, 검증 또는 반복해야 하는 사람과 AI 에이전트를 위한 문서입니다. Source protocol: [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

## 실무 범위

이 페이지를 `prompt improvement` 주제의 운영 지침으로 사용하세요. 저장소 증거나 프로젝트 고유 지침을 대체하지 않습니다.

## 작업 지침

- 저장소 증거를 기본 권위로 다룹니다.
- 파일 이름, 명령, API 이름, 모델 이름을 정확히 보존합니다.
- 검증되지 않은 결론은 `[ASSUMPTION: ...]`, 알 수 없는 사실은 `[UNKNOWN]`으로 표시합니다.
- 도구별 동작은 실제로 그 동작을 소유한 도구 또는 runtime에 연결합니다.
- 보안, 권한, 프로덕션 준비 위험은 사람 검토로 에스컬레이션합니다.
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

## 초점

이 페이지를 workflow에서 사용하기 전에 범위, 필요한 증거, 검증 가능한 명령, 사람 승인 경계를 정의하세요.

## Examples

### Status/list request

- Mode: direct answer or Intake Mode.
- Output: short answer, evidence and no file edits.

### Repository change request

- Mode: Intake Mode, then Full Rewrite Mode when scope remains broad.
- Output: scoped workflow, files to inspect, verification commands and final report rules.

## 품질 점검

- 새 기여자가 목적을 이해할 수 있습니다.
- 지침이 AI 에이전트와 사람 유지관리자 모두에게 유용합니다.
- 모델별 명령을 만들어내지 않습니다.
- 보안과 사람 승인 경계가 계속 보입니다.
- 현지화 충돌에서는 영어 원본이 권위를 가집니다.
- The selected activation mode matches the request risk.
- Verification evidence is defined before execution.
