# Model and Agent Ecosystem

This document explains how this standard can be used with different AI model families, coding agents, IDE assistants and API-based model providers.

The important distinction is:

- **Models** are the underlying LLMs, for example DeepSeek, Qwen, Kimi, Mistral, Grok, Xiaomi MiMo or MiniMax.
- **Agent runtimes** are tools that read files, edit repositories, run commands and execute workflows.
- **Context files** are repository files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` or `.github/copilot-instructions.md` that provide stable instructions.

Most model families do not automatically read repository context files by themselves. They need to be used through an IDE, CLI agent, API wrapper or orchestration layer that loads the relevant files into context.

## Baseline recommendation

Use `AGENTS.md` as a portable fallback entrypoint only when the active model client or agent runtime is configured to load it. For source-backed tool-specific compatibility notes, see `docs/tool-compatibility.md`.

Recommended loading order:

```text
AGENTS.md
docs/ai/MASTER_SYSTEM.md
docs/ai/ONBOARDING.md
docs/ai/ARCHITECTURE.md
docs/ai/STYLE_GUIDE.md
docs/ai/REVIEW_CHECKLIST.md
```

For task-specific work, load only the relevant `/docs/ai/` documents instead of the full repository documentation.

## Compatibility matrix

| Model family / provider | Typical use pattern | Recommended repo entrypoint | Notes |
|---|---|---|---|
| OpenAI / GPT / Codex | Coding agent, API, IDE assistant | Runtime-defined; `AGENTS.md` for Codex | Use short, explicit task context and the `/docs/ai/` source-of-truth rule. |
| Anthropic Claude / Claude Code | Coding agent, CLI agent | Runtime-defined; `CLAUDE.md` for Claude Code | Keep `CLAUDE.md` short and avoid duplicating long rules. |
| Google Gemini / Gemini CLI | Coding agent, CLI agent, API | Runtime-defined; `GEMINI.md` for Gemini CLI | Verify the selected Gemini client before relying on `GEMINI.md`. |
| GitHub Copilot | IDE assistant, PR assistant | `.github/copilot-instructions.md` where supported | Add path-specific instructions only when they reduce ambiguity. |
| Cursor | IDE agent | Cursor project rules where supported | Prefer scoped rules for monorepos or framework-specific folders. |
| Windsurf / Cascade | IDE agent | Workspace rules where supported | Root-level instructions should stay concise. |
| DeepSeek | API model, chat/coding model via compatible clients | Runtime-defined | Treat as a model provider unless the chosen client defines a context-file standard. |
| Qwen / Qwen Code | Model family and coding agent | Runtime-defined | Keep repo rules tool-neutral unless the active runtime documents a file convention. |
| Kimi / Moonshot | API model, chat/coding model via compatible clients | Runtime-defined | Long-context capacity is not the same as automatic repository context loading. |
| Mistral | API model, coding model via clients | Runtime-defined | Keep security and privacy boundaries explicit for enterprise or EU-focused setups. |
| Grok / xAI | API model, assistant model | Runtime-defined | Treat web/current-event claims as untrusted unless the active client has live browsing and cites sources. |
| Xiaomi MiMo | API model / research model family | Runtime-defined | Treat as provider/model support unless a dedicated coding-agent context convention is used. |
| MiniMax | API model, agent products, multimodal/audio/video models | Runtime-defined | Use task-specific profiles for language, multimodal or agentic tasks. |
| Other OpenAI-compatible APIs | API model through gateway/router | Runtime-defined | Add provider-specific constraints in `MODEL_PROFILES.md` when needed. |

## Provider-specific profile rule

Provider-specific instructions belong in:

```text
templates/MODEL_PROFILES.md
```

Do not create a new root-level instruction file for every model provider unless the tool explicitly supports that file name.

Bad pattern:

```text
DEEPSEEK.md
QWEN.md
KIMI.md
MISTRAL.md
GROK.md
```

Better pattern:

```text
AGENTS.md
docs/ai/MASTER_SYSTEM.md
templates/MODEL_PROFILES.md
```

Reason: most providers do not automatically discover custom root files. A single universal entrypoint is more portable.

## Model selection guidance

Use model profiles for workflow routing, not for hard-coded superiority claims.

Recommended routing dimensions:

- repository analysis
- small scoped code changes
- large refactoring proposals
- test generation
- security review
- documentation writing
- translation and localization
- long-context review
- multimodal review, if screenshots or diagrams are involved

Avoid claiming that one model is always best. Model behavior changes frequently, and provider capabilities depend on the client, context window, tool access and deployment settings.

## Maintenance rule

Model/provider information changes quickly. Review this document regularly and verify provider-specific claims against official documentation before publishing compatibility claims.

Suggested review cadence:

```text
Quarterly, or before each major repository release.
```

## External references to verify manually

Use official documentation where possible:

- DeepSeek API documentation: https://api-docs.deepseek.com/
- Qwen Code documentation: https://qwenlm.github.io/qwen-code-docs/en/
- Kimi / Moonshot model documentation: https://platform.kimi.ai/docs/models
- Mistral AI documentation: https://docs.mistral.ai/
- xAI documentation: https://docs.x.ai/
- Xiaomi MiMo: https://mimo.mi.com/
- MiniMax API documentation: https://platform.minimax.io/docs/
