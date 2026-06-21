# Magical Prompt Improver

<!-- localization-status: localized-mirror; review-status: tracked-in-language-support -->

> Language status: localized mirror of the English reference. Review status is tracked in the language support metadata.
> 原文言語: 英語
> 原文ファイル: ai/English/prompts/magical-prompt-improver.md
> 差異がある場合は英語ファイルを優先します。

このページは `prompts/magical-prompt-improver.md` が AI Agent Operating Manual の中でどのように使われるかを説明します。リポジトリ作業を計画、検証、または再実行する人と AI エージェント向けです。 Source protocol: [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

## 実用範囲

このページを `prompt improvement` テーマの運用ガイドとして使ってください。リポジトリの証拠やプロジェクト固有の指示の代わりにはなりません。

## 作業ガイドライン

- リポジトリの証拠を第一の根拠として扱います。
- ファイル名、コマンド、API 名、モデル名は正確に保持します。
- 未検証の結論は `[ASSUMPTION: ...]`、不明な事実は `[UNKNOWN]` として示します。
- ツール固有の挙動は、それを実際に所有するツールまたは runtime に結び付けます。
- 安全性、権限、本番準備に関するリスクは人間のレビューにエスカレーションします。
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

## 焦点

このページを workflow で使う前に、範囲、必要な証拠、検証可能なコマンド、人間の承認境界を定義します。

## Examples

### Status/list request

- Mode: direct answer or Intake Mode.
- Output: short answer, evidence and no file edits.

### Repository change request

- Mode: Intake Mode, then Full Rewrite Mode when scope remains broad.
- Output: scoped workflow, files to inspect, verification commands and final report rules.

## 品質チェック

- 新しい共同作業者に目的が明確です。
- AI エージェントと人間のメンテナーの両方に役立ちます。
- モデル固有のコマンドを作りません。
- 安全性と人間の承認境界が見える状態です。
- ローカライズの衝突では英語ソースが権威を持ちます。
- The selected activation mode matches the request risk.
- Verification evidence is defined before execution.
