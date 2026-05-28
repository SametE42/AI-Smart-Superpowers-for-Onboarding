# AI Agent Operating Manual

This folder is the English source of truth for the AI documentation. It is designed as a complete operating manual for AI agents, not only as a model list.

## What is included

- Models and providers
- AI coding tools and agent runtimes
- Slash commands, file references and custom command systems
- Prompting and context engineering
- Reusable skills and self-evolving skills
- Three-tier memory and memory safety
- GEPA, DSPy, TextGrad and other optimization approaches
- Evaluation, regression tests and quality gates
- Safety, privacy, permissions and human approval
- Examples and templates

## Core rule

Models usually do not own commands. Commands belong to the host tool or runtime. For example, Codex, Claude Code and Gemini CLI can expose slash commands, while DeepSeek, Qwen, Kimi, Mistral, Grok, MiniMax and Xiaomi MiMo are normally model families or providers that are used through those tools.

## Recommended reading order

1. `agents/agent-architecture.md`
2. `context-engineering/context-engineering-overview.md`
3. `commands/command-taxonomy.md`
4. `skills/skill-design.md`
5. `memory/three-tier-memory.md`
6. `optimization/gepa.md`
7. `evals/evaluation-overview.md`
8. `safety/human-approval.md`
