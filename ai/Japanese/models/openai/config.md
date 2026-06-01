# Config

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> 原文言語: 英語
> 原文ファイル: ai/English/models/openai/config.md
> 差異がある場合は英語ファイルを優先します。

このページは `models/openai/config.md` が AI Agent Operating Manual の中でどのように使われるかを説明します。リポジトリ作業を計画、検証、または再実行する人と AI エージェント向けです。

## 実用範囲

このページを `models` テーマの運用ガイドとして使ってください。リポジトリの証拠やプロジェクト固有の指示の代わりにはなりません。

## 作業ガイドライン

- リポジトリの証拠を第一の根拠として扱います。
- ファイル名、コマンド、API 名、モデル名は正確に保持します。
- 未検証の結論は `[ASSUMPTION: ...]`、不明な事実は `[UNKNOWN]` として示します。
- ツール固有の挙動は、それを実際に所有するツールまたは runtime に結び付けます。
- 安全性、権限、本番準備に関するリスクは人間のレビューにエスカレーションします。

## 焦点

このページを workflow で使う前に、範囲、必要な証拠、検証可能なコマンド、人間の承認境界を定義します。

## 品質チェック

- 新しい共同作業者に目的が明確です。
- AI エージェントと人間のメンテナーの両方に役立ちます。
- モデル固有のコマンドを作りません。
- 安全性と人間の承認境界が見える状態です。
- ローカライズの衝突では英語ソースが権威を持ちます。
