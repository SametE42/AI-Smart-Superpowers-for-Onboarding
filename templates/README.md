# Templates

This folder contains copyable templates for target repositories.

## Core

```text
MASTER_PROMPT.md
MASTER_PROMPT.en.md
```

Use `MASTER_PROMPT.en.md` as the English primary onboarding prompt. Keep `MASTER_PROMPT.md` only when a German workflow prompt is needed.

## Model profiles

```text
MODEL_PROFILES.md
```

Use this file for provider-specific routing notes for DeepSeek, Qwen, Kimi, Mistral, Grok, Xiaomi MiMo, MiniMax and other model families. Do not create one root instruction file per model unless the actual tool supports it.

## Tool entrypoints

Copy only the entrypoints that match the tools used in your project:

| Template | Target path |
|---|---|
| `AGENTS.md` | `AGENTS.md` |
| `CLAUDE.md` | `CLAUDE.md` |
| `GEMINI.md` | `GEMINI.md` |
| `copilot-instructions.md` | `.github/copilot-instructions.md` |
| `tool-entrypoints/AGENTS.md` | `AGENTS.md` |
| `tool-entrypoints/CLAUDE.md` | `CLAUDE.md` |
| `tool-entrypoints/GEMINI.md` | `GEMINI.md` |
| `tool-entrypoints/COPILOT_INSTRUCTIONS.md` | `.github/copilot-instructions.md` |
| `tool-entrypoints/CURSOR_RULES.md` | `.cursor/rules/ai-onboarding.md` |
| `tool-entrypoints/CLINE_RULES.md` | Cline project rules |
| `tool-entrypoints/AIDER_NOTES.md` | Aider repository notes |
| `tool-entrypoints/OPENCODE.md` | `OPENCODE.md` |
| `tool-entrypoints/COMMANDCODE_SKILL.md` | Skill-style workflow template |

Tool entrypoints should stay short. They should link to `/docs/ai/` instead of duplicating long documentation.

The grouped templates live in `templates/tool-entrypoints/` and include localized-structure guidance through File-Maps.

## AI documentation templates

Copy:

```text
templates/docs-ai/
```

to your target repository as:

```text
docs/ai/
```

## Optional templates

Optional templates are available in:

```text
templates/optional/
```

Use them only when the project needs that level of operational, testing, prompt-refinement or governance detail.
Use `optional/MAGICAL_PROMPT_IMPROVER.md` when a broad or ambiguous user request must be converted into safe, scoped and verifiable instructions before execution.

## Skills and subagents

See:

```text
templates/skills/README.md
skills/README.md
```

Skills, subagents, hooks, MCP servers and plugins are optional extensions, not baseline requirements.
