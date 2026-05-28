# AI Repo Onboarding Standard

A structured master prompt and documentation standard for coding projects in multi-model and AI-assisted development workflows.

Repository: https://github.com/SametE42/Ai-Repo-Onboarding

This repository provides a reusable framework for onboarding AI agents into software repositories safely, consistently and with explicit documentation boundaries.

## Why?

AI coding agents often fail for the same reasons:

- they miss project context,
- they infer architecture from incomplete files,
- they invent business rules,
- they ignore existing conventions,
- they mix technical errors with business logs,
- they create broad changes without verification,
- they treat local prototypes as production-ready systems.

This standard solves that by creating a stable `/docs/ai/` knowledge base, a clear workflow for repository analysis, and short tool-specific entrypoint files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` or `.github/copilot-instructions.md`.

## For whom?

This repository is useful for:

- developers using multiple coding agents,
- teams working with Claude Code, Codex, Cursor, GitHub Copilot, Gemini, Windsurf or similar tools,
- projects that need repeatable AI onboarding,
- maintainers who want AI-generated documentation to stay structured,
- teams that need clear boundaries around security, production readiness and human review.


## Languages

English is the primary language and source of truth for this repository. The multilingual AI documentation is organized by language directly under `ai/`.

Main entry points:

- [English AI Manual](ai/English/README.md)
- [German AI Manual](ai/German/README.md)
- [Language Index](ai/LANGUAGE_INDEX.md)
- [Translation Policy](ai/TRANSLATION_POLICY.md)

Legacy translations under `i18n/` are kept only for compatibility. New AI documentation should be maintained under `ai/<Language>/`.

## Quickstart

1. Copy `templates/MASTER_PROMPT.md`.
2. Give it to your coding agent.
3. Point the agent at your target repository.
4. Let it run Phase 0 to Phase 2 first.
5. Review the proposed documentation plan before allowing file changes.

For a minimal example, see:

```text
examples/minimal/
```

## What gets created?

The primary output is a `/docs/ai/` folder inside your target repository.

The standard defines 10 core documents:

```text
docs/ai/
├─ MASTER_SYSTEM.md
├─ ARCHITECTURE.md
├─ PROJECT_MEMORY.md
├─ STYLE_GUIDE.md
├─ REVIEW_CHECKLIST.md
├─ DOMAIN_KNOWLEDGE.md
├─ SECURITY_RULES.md
├─ ERROR_PATTERNS.md
├─ CHANGELOG_AI.md
└─ ONBOARDING.md
```

These files are designed to give future AI agents a stable, task-focused and verifiable project context.


## Model and agent ecosystem

This standard is tool-neutral and can be used with model families and agent runtimes such as OpenAI/Codex, Claude, Gemini, GitHub Copilot, Cursor, Windsurf, DeepSeek, Qwen, Kimi, Mistral, Grok, Xiaomi MiMo, MiniMax and other OpenAI-compatible or Anthropic-compatible clients.

Detailed guidance is documented in:

```text
docs/model-and-agent-ecosystem.md
templates/MODEL_PROFILES.md
```

Important: model providers change quickly. Verify provider-specific capabilities against official documentation before publishing compatibility claims.

## Supported tools

This standard separates tool support into three layers:

1. **Context files**
   Short instruction files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Copilot instructions or Cursor rules.

2. **Agent runtimes and orchestrators**
   Systems such as OpenAI Codex, Claude Code, OpenCode, OpenClaw, Hermes Agent or similar agent runtimes.

3. **Extension mechanisms**
   Optional mechanisms such as Skills, Subagents, Hooks, MCP servers or Plugins.

The full compatibility notes are documented in:

```text
docs/tool-compatibility.md
```

## Repository structure

```text
Ai-Repo-Onboarding/
├─ README.md
├─ LICENSE
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ CODE_OF_CONDUCT.md
├─ CITATION.cff
├─ .github/
│  ├─ CODEOWNERS
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ ISSUE_TEMPLATE/
├─ templates/
│  ├─ MASTER_PROMPT.md
│  ├─ AGENTS.md
│  ├─ CLAUDE.md
│  ├─ GEMINI.md
│  ├─ copilot-instructions.md
│  ├─ docs-ai/
│  ├─ optional/
│  └─ skills/
├─ examples/
│  ├─ minimal/
│  ├─ node-typescript/
│  ├─ python-fastapi/
│  └─ multi-agent/
└─ docs/
   ├─ rationale.md
   ├─ design-principles.md
   ├─ tool-compatibility.md
   ├─ publication-checklist.md
   └─ faq.md
```

## Design principles

The standard is built around these principles:

- evidence-first documentation,
- no hallucinated business rules,
- human review before impactful changes,
- strict separation of technical logs, audit logs, change history and export history,
- minimal but useful AI context,
- append-only documentation for multi-model work,
- explicit production-readiness status,
- short tool entrypoints that link to `/docs/ai/` instead of duplicating it.

## Security model

This project does not make AI-generated output automatically trusted.

All generated documentation and code changes must be reviewed by humans before being committed, merged or used in production.

The standard explicitly requires:

- no secrets in documentation,
- no personal or production data in examples,
- no invented security guarantees,
- no production-readiness claims without evidence,
- clear marking of assumptions and unknowns,
- redaction of sensitive values,
- documentation of open risks.

See:

```text
SECURITY.md
templates/docs-ai/SECURITY_RULES.md
templates/optional/PRODUCTION_READINESS.md
```

## Contributing

Contributions are welcome if they improve clarity, safety, tool compatibility or real-world usability.

Please read:

```text
CONTRIBUTING.md
```

before opening a pull request.

## License

MIT License.

## AI documentation hub

This repository includes a central [`ai/`](ai/) folder for all AI-related documentation. The primary manual is [`ai/English/`](ai/English/), and localized manuals are mirrored under language folders such as [`ai/German/`](ai/German/), [`ai/Spanish/`](ai/Spanish/) and [`ai/French/`](ai/French/).

Key English entry points:

- [`ai/English/models/`](ai/English/models/) — model-family profiles for OpenAI, Claude, Gemini, DeepSeek, Qwen, Kimi, Mistral, Grok, MiniMax, Xiaomi MiMo, Llama, Cohere, Perplexity and OpenRouter.
- [`ai/English/tools/`](ai/English/tools/) — command and workflow notes for Codex, Claude Code, Gemini CLI, Cursor, Continue, Aider and OpenCode.
- [`ai/English/commands/`](ai/English/commands/) — command documentation standards and tool-specific command references.
- [`ai/English/skills/`](ai/English/skills/) — reusable skills, skill lifecycle, testing and self-evolving skills.
- [`ai/English/memory/`](ai/English/memory/) — three-tier memory, memory schemas and memory safety.
- [`ai/English/optimization/`](ai/English/optimization/) — GEPA, DSPy, TextGrad and optimization loops.
- [`ai/English/workflows/`](ai/English/workflows/) — reusable workflows for repo onboarding, documentation, model profiles, translations and security review.
- [`ai/English/evals/`](ai/English/evals/) — evaluation tasks for comparing model/tool combinations.

## Multilingual language structure

The repository contains a multilingual AI manual organized directly by language under [`ai/`](ai/). The English manual under [`ai/English/`](ai/English/) is the source of truth. Localized folders such as [`ai/German/`](ai/German/), [`ai/Spanish/`](ai/Spanish/) and [`ai/French/`](ai/French/) mirror the same structure for translated documentation.

See [`ai/LANGUAGE_INDEX.md`](ai/LANGUAGE_INDEX.md) and [`ai/TRANSLATION_POLICY.md`](ai/TRANSLATION_POLICY.md).

