# Tool Compatibility

This project separates agent support into three layers:

1. Context files
2. Agent runtimes and orchestrators
3. Extension mechanisms

`/docs/ai/` remains the source of truth. Tool-specific files are short references.

Reusable entrypoint templates live in `templates/tool-entrypoints/`. They are copyable guidance for target repositories, not claims of partnership, endorsement or guaranteed behavior by any tool vendor.

## Source Policy

Compatibility rows must have a primary source or an explicitly documented limitation. Do not add a tool-support claim without a source.

`Last checked` dates use the date on which the source was reviewed for this repository.

## 1. Context Files

| Tool / Agent | File or mechanism | Guidance | Source | Last checked | Confidence | Limitations |
|---|---|---|---|---|---|---|
| OpenAI Codex | `AGENTS.md` | Keep a short root entrypoint and link to `/docs/ai/`. | [OpenAI Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) | 2026-06-21 | High | Context behavior is Codex-specific; other runtimes may ignore the file unless they support it. |
| GitHub Copilot | `.github/copilot-instructions.md` | Use repository custom instructions for repo-wide build, test and style context. | [GitHub Copilot repository instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | 2026-06-21 | High | Applies where Copilot custom instructions are enabled and supported by the active surface. |
| GitHub Copilot | `.github/instructions/*.instructions.md` | Use path-specific instructions only for scoped guidance. | [GitHub Copilot repository instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | 2026-06-21 | High | Keep files short; avoid duplicating the full knowledge base. |
| Claude Code | `CLAUDE.md` | Use `CLAUDE.md`; import `AGENTS.md` with `@AGENTS.md` when sharing common instructions. | [Claude Code memory docs](https://code.claude.com/docs/en/memory) | 2026-06-21 | High | Claude Code treats memory as context, not an enforced policy layer. |
| Claude Code | `.claude/rules/*.md` | Use project rules for modular or path-scoped Claude guidance. | [Claude Code memory docs](https://code.claude.com/docs/en/memory) | 2026-06-21 | High | Rules still consume context; use skills for task-specific procedures. |
| Gemini CLI | `GEMINI.md` | Use `GEMINI.md` for instructional context loaded by Gemini CLI. | [Gemini CLI GEMINI.md docs](https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html) | 2026-06-21 | High | Verify the active Gemini client uses the same CLI convention. |
| Cursor | Project rules, `AGENTS.md` | Use Cursor rules for persistent project instructions; keep long context in `/docs/ai/`. | [Cursor rules docs](https://cursor.com/docs/rules) | 2026-06-21 | Medium | Cursor features and file conventions can vary by product version and workspace settings. |
| Windsurf / Cascade | `.devin/rules/*.md`, `.windsurf/rules/*.md`, legacy `.windsurfrules` | Use workspace rules where supported and point back to `/docs/ai/`. | [Cascade memories and rules docs](https://docs.devin.ai/desktop/cascade/memories) | 2026-06-21 | Medium | Documentation identifies `.devin/rules` as preferred and `.windsurf/rules` as fallback; verify the installed client. |
| Continue | `.continue/rules/*.md` | Use Continue rules for system-message instructions; link to `/docs/ai/` for durable context. | [Continue rules docs](https://docs.continue.dev/customize/deep-dives/rules) | 2026-06-21 | Medium | Continue docs note active product changes; validate behavior in the selected extension or CLI. |
| Aider | `CONVENTIONS.md` or `--read <file>` | Load repository conventions as read-only context; point to `/docs/ai/`. | [Aider conventions docs](https://aider.chat/docs/usage/conventions.html) | 2026-06-21 | High | Aider does not require this repository's exact filenames; wire conventions explicitly. |
| OpenCode | `AGENTS.md` | Initialize or maintain concise project instructions and keep durable context in `/docs/ai/`. | [OpenCode docs](https://opencode.ai/docs/) | 2026-06-21 | High | Behavior depends on the OpenCode client version and selected provider/model. |

## 2. Agent Runtimes And Orchestrators

| System | Category | Guidance | Source | Last checked | Confidence | Limitations |
|---|---|---|---|---|---|---|
| OpenAI Codex | Coding-agent runtime | Use `AGENTS.md` and short project instructions that reference `/docs/ai/`. | [OpenAI Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) | 2026-06-21 | High | This is a Codex compatibility note, not a claim about other OpenAI surfaces. |
| Claude Code | Coding-agent runtime | Use `CLAUDE.md`, `.claude/rules/` and optional skills only where justified. | [Claude Code memory docs](https://code.claude.com/docs/en/memory) | 2026-06-21 | High | Human review and hooks remain necessary for enforceable policy. |
| GitHub Copilot | IDE and GitHub assistant | Use repository and path-specific custom instructions. | [GitHub Copilot repository instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | 2026-06-21 | High | Behavior varies by Copilot surface and organization settings. |
| Gemini CLI | Coding-agent runtime | Use `GEMINI.md` for project context and keep detailed docs separate. | [Gemini CLI GEMINI.md docs](https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html) | 2026-06-21 | High | Only applies to Gemini CLI or clients that document the same convention. |
| Cursor | IDE agent | Use project rules and keep rule files compact. | [Cursor rules docs](https://cursor.com/docs/rules) | 2026-06-21 | Medium | Verify active workspace rule settings before relying on them. |
| Windsurf / Cascade | IDE agent | Use workspace rules and keep generated memories separate from reviewed repo context. | [Cascade memories and rules docs](https://docs.devin.ai/desktop/cascade/memories) | 2026-06-21 | Medium | Client naming and rule locations have changed over time; prefer current docs. |
| Continue | CLI / IDE agent | Use `.continue/rules/` or config rules, depending on the selected Continue surface. | [Continue rules docs](https://docs.continue.dev/customize/deep-dives/rules) | 2026-06-21 | Medium | The public docs note a final 2.0.0 release; validate current extension or CLI behavior. |
| Aider | CLI coding assistant | Load conventions explicitly with `/read` or `--read`. | [Aider conventions docs](https://aider.chat/docs/usage/conventions.html) | 2026-06-21 | High | Aider is not assumed to auto-load this repository's full docs. |
| OpenCode | Coding-agent runtime | Use `AGENTS.md` created or maintained for the project. | [OpenCode docs](https://opencode.ai/docs/) | 2026-06-21 | High | Provider/model behavior is separate from OpenCode's repo-context convention. |
| OpenClaw | Self-hosted gateway / orchestrator | Treat `/docs/ai/` as the source of truth and wire it through workspace instructions. | No primary source recorded in this repository. | 2026-06-21 | Low | No official compatibility claim. Document the actual workspace adapter before use. |
| Hermes Agent | Persistent self-hosted agent with memory/skills | Do not persist private or unverified facts automatically. | No primary source recorded in this repository. | 2026-06-21 | Low | No official compatibility claim. Require project-specific integration evidence. |

## 3. Extension Mechanisms

| Mechanism | Use when | Do not use when | Source | Last checked | Confidence | Limitations |
|---|---|---|---|---|---|---|
| Skills / `SKILL.md` | A repeatable task-specific workflow exists. | It is a one-off task or generic best practice. | [OpenAI Codex skills docs](https://developers.openai.com/codex/skills) | 2026-06-21 | Medium | Skill support is runtime-specific; avoid assuming every tool can load skills. |
| Subagents | A clear specialized role needs bounded context. | A normal task can be handled by one agent. | Runtime-specific documentation required. | 2026-06-21 | Low | No cross-tool support claim. Document the active runtime before adding subagents. |
| MCP servers | External tool or data integration is necessary. | Static documentation is enough. | Runtime-specific documentation required. | 2026-06-21 | Low | No official compatibility claim. MCP availability depends on the selected tool and security policy. |
| Hooks | Deterministic pre/post action is needed. | A checklist is sufficient. | [Claude Code memory docs](https://code.claude.com/docs/en/memory) | 2026-06-21 | Medium | Hook semantics are tool-specific and should not be copied blindly. |
| Plugins | Reusable installable capability is needed. | Local repo guidance is enough. | Runtime-specific documentation required. | 2026-06-21 | Low | No official compatibility claim. No generic plugin compatibility claim. |

## Compatibility Rule

Do not add a tool-specific file unless:

- the tool is actually used,
- the file has a clear target path,
- the file stays short,
- it links to `/docs/ai/`,
- it does not duplicate long documentation,
- it does not contradict `MASTER_SYSTEM.md`,
- the compatibility claim is sourced or explicitly marked as project-specific.

## Source-of-truth Rule

Priority order:

1. `/docs/ai/MASTER_SYSTEM.md`
2. Other relevant `/docs/ai/` documents
3. Tool-specific entrypoint files
4. Tool-generated defaults

Conflicts must be marked and reviewed by a human.

## Tool Contract Robustness

Many apparent model failures are tool-contract failures. Treat invalid tool input as a harness design signal before assuming the model is incapable.

Recommended validation flow:

1. Validate the tool input exactly as received.
2. If validation succeeds, do not rewrite the input.
3. If validation fails, inspect the validator issue path and attempt only narrow repairs at that path.
4. Re-validate after repair.
5. Log successful repairs, for example `tool_input_repaired:<toolName>`.
6. On failure, return a short model-readable retry message instead of a raw validator dump.

Common safe shape repairs:

- omit `null` for optional fields when the schema expects absence,
- parse a JSON array that was emitted as a string,
- wrap a bare string in a one-item array when the schema requires an array,
- unwrap degenerate markdown links in path fields only when link text and URL identify the same local path.

Do not apply broad preprocessing before validation. It can silently corrupt valid input, especially file content that happens to look like JSON.

Relational invariants need separate handling. If fields are individually valid but incomplete together, either return a clear retry message or choose a conservative default and report it back to the model. Example: `limit` without `offset` may default to `offset = 0` if the tool documents that behavior.

High-impact tools such as shell, write-file, delete, network and deployment tools require stricter repair rules. Never silently change commands, destructive paths, deployment targets or security-relevant values.

## 4. Model Families And Provider APIs

The following model families can be used with this standard only through an agent runtime, IDE assistant, API wrapper or orchestration layer that actually loads repository context files. These rows are not direct support claims for the model providers themselves.

| Model family / provider | Recommended entrypoint | Source | Last checked | Confidence | Limitations |
|---|---|---|---|---|---|
| OpenAI models | Runtime-defined, commonly `AGENTS.md` in Codex | [OpenAI Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) | 2026-06-21 | High for Codex, Low outside Codex | Provider APIs do not automatically imply repo-context file loading. |
| Anthropic Claude models | Runtime-defined, commonly `CLAUDE.md` in Claude Code | [Claude Code memory docs](https://code.claude.com/docs/en/memory) | 2026-06-21 | High for Claude Code, Low outside Claude Code | Claude API usage is separate from Claude Code memory behavior. |
| Google Gemini models | Runtime-defined, commonly `GEMINI.md` in Gemini CLI | [Gemini CLI GEMINI.md docs](https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html) | 2026-06-21 | High for Gemini CLI, Low outside Gemini CLI | Verify the client before assuming `GEMINI.md` is loaded. |
| DeepSeek | Runtime-defined | No primary context-file source recorded in this repository. | 2026-06-21 | Low | Treat as model-provider compatibility through the selected client only. |
| Qwen / Qwen Code | Runtime-defined | No primary context-file source recorded in this repository. | 2026-06-21 | Low | Add a source before claiming a specific file convention. |
| Kimi / Moonshot | Runtime-defined | No primary context-file source recorded in this repository. | 2026-06-21 | Low | Long-context capability is not the same as repo-context file support. |
| Mistral | Runtime-defined | No primary context-file source recorded in this repository. | 2026-06-21 | Low | Use only through a client that documents how it loads context. |
| Grok / xAI | Runtime-defined | No primary context-file source recorded in this repository. | 2026-06-21 | Low | Verify current-event or web claims with sources. |
| Xiaomi MiMo | Runtime-defined | No primary context-file source recorded in this repository. | 2026-06-21 | Low | Treat as optional model-family mention until a runtime convention is documented. |
| MiniMax | Runtime-defined | No primary context-file source recorded in this repository. | 2026-06-21 | Low | Separate language-model tasks from multimodal/audio/video tasks. |
| Other compatible APIs | Runtime-defined | No primary context-file source recorded in this repository. | 2026-06-21 | Low | Document client/runtime limitations in `MODEL_PROFILES.md`. |

See also:

```text
docs/model-and-agent-ecosystem.md
templates/MODEL_PROFILES.md
```
