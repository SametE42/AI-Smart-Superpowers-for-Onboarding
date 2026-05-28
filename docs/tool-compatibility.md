# Tool Compatibility

This project separates agent support into three layers:

1. Context files
2. Agent runtimes and orchestrators
3. Extension mechanisms

`/docs/ai/` remains the source of truth. Tool-specific files are short references.

## 1. Context files

| Tool / Agent | File | Notes |
|---|---|---|
| OpenAI Codex | `AGENTS.md` | Short agent entrypoint; link to `/docs/ai/` |
| GitHub Copilot | `.github/copilot-instructions.md` | Repo-wide Copilot instructions |
| GitHub Copilot | `.github/instructions/*.instructions.md` | Path-specific instructions |
| Claude Code | `CLAUDE.md` | Claude-specific entrypoint |
| Gemini | `GEMINI.md` | Gemini-specific entrypoint |
| Cursor | `AGENTS.md` or `.cursor/rules/*.mdc` | Use rules for scoped behavior |
| Windsurf / Cascade | `AGENTS.md` (root = always active; subdirectory = automatically scoped to files in that folder) or `.windsurf/rules/*.md` | Use scoped placement for monorepos or Rules when more control is needed |

## 2. Agent runtimes and orchestrators

| System | Category | Guidance |
|---|---|---|
| OpenAI Codex | Coding agent runtime | Use `AGENTS.md` and short project instructions |
| Claude Code | Coding agent runtime | Use `CLAUDE.md`; optional skills/subagents where justified |
| OpenCode | Coding agent runtime | Use short entrypoints and `/docs/ai/` references |
| OpenClaw | Self-hosted gateway / agent orchestrator | Uses its own agent workspace and workspace-specific context files. Treat `/docs/ai/` as the source of truth and reference it from OpenClaw workspace instructions instead of copying all documentation into the workspace. |
| Hermes Agent | Persistent self-hosted agent with memory/skills | Do not persist private or unverified facts automatically |
| Gemini CLI / Gemini agents | Coding agent runtime | Use `GEMINI.md` where applicable |

## 3. Extension mechanisms

| Mechanism | Use when | Do not use when |
|---|---|---|
| Skills / `SKILL.md` | A repeatable task-specific workflow exists | It is a one-off task or generic best practice |
| Subagents | A clear specialized role needs bounded context | A normal task can be handled by one agent |
| MCP servers | External tool or data integration is necessary | Static documentation is enough |
| Hooks | Deterministic pre/post action is needed | A checklist is sufficient |
| Plugins | Reusable installable capability is needed | Local repo guidance is enough |

## Compatibility rule

Do not add a tool-specific file unless:

- the tool is actually used,
- the file has a clear target path,
- the file stays short,
- it links to `/docs/ai/`,
- it does not duplicate long documentation,
- it does not contradict `MASTER_SYSTEM.md`.

## Source-of-truth rule

Priority order:

1. `/docs/ai/MASTER_SYSTEM.md`
2. Other relevant `/docs/ai/` documents
3. Tool-specific entrypoint files
4. Tool-generated defaults

Conflicts must be marked and reviewed by a human.

## 4. Model families and provider APIs

The following model families can be used with this standard when they are accessed through an agent runtime, IDE assistant, API wrapper or orchestration layer that loads repository context files.

| Model family / provider | Recommended entrypoint | Notes |
|---|---|---|
| DeepSeek | `AGENTS.md` | Treat as a provider/model family unless the active client defines its own context convention. |
| Qwen / Qwen Code | `AGENTS.md` and Qwen Code project instructions where supported | Use tool-specific instructions only where the runtime supports them. |
| Kimi / Moonshot | `AGENTS.md` | Useful for long-context workflows when the client supports it. |
| Mistral | `AGENTS.md` | Keep privacy and deployment assumptions explicit. |
| Grok / xAI | `AGENTS.md` | Verify current-event or web claims with sources. |
| Xiaomi MiMo | `AGENTS.md` | Treat as optional provider support unless actively used. |
| MiniMax | `AGENTS.md` | Separate language-model tasks from multimodal/audio/video tasks. |
| Other compatible APIs | `AGENTS.md` | Document client/runtime limitations in `MODEL_PROFILES.md`. |

See also:

```text
docs/model-and-agent-ecosystem.md
templates/MODEL_PROFILES.md
```
