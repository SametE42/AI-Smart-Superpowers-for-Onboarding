# AI Repo Onboarding Standard

<p align="center">
  <a href="https://github.com/SametE42/Ai-Repo-Onboarding/actions/workflows/validate.yml"><img alt="Validate repository" src="https://github.com/SametE42/Ai-Repo-Onboarding/actions/workflows/validate.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/SametE42/Ai-Repo-Onboarding"></a>
  <img alt="Docs first" src="https://img.shields.io/badge/docs-evidence--first-2563eb">
  <img alt="Language folders: 75" src="https://img.shields.io/badge/language%20folders-75-0f766e">
  <img alt="Python: 3.x validation" src="https://img.shields.io/badge/python-3.x%20validation-3776ab">
</p>

<p align="center">
  A reusable documentation and prompt standard for onboarding AI coding agents into software repositories safely, consistently and with clear human-review boundaries.
</p>

<p align="center">
  <a href="#quickstart">Quickstart</a> ·
  <a href="docs/">Docs</a> ·
  <a href="templates/MASTER_PROMPT.en.md">Master Prompt</a> ·
  <a href="ai/English/README.md">AI Manual</a> ·
  <a href="https://github.com/SametE42/Ai-Repo-Onboarding/issues">Issues</a>
</p>

---

## Table Of Contents

- [What This Is](#what-this-is)
- [What This Is Not](#what-this-is-not)
- [Quickstart](#quickstart)
- [Features](#features)
- [What Gets Created In Target Repositories](#what-gets-created-in-target-repositories)
- [Repository Map](#repository-map)
- [Source Of Truth](#source-of-truth)
- [Languages And Translation Status](#languages-and-translation-status)
- [Validation](#validation)
- [Examples](#examples)
- [GitHub And Community Files](#github-and-community-files)
- [Security Model](#security-model)
- [Contributing](#contributing)
- [License](#license)

## What This Is

AI Repo Onboarding Standard helps humans and AI coding agents share a stable, evidence-based repository context. It defines a master prompt, reusable `docs/ai/` templates, short tool entrypoints, validation scripts and multilingual AI-agent documentation.

Use it when you want an AI agent to inspect a repository, ask the right setup questions, document what is known, mark what is unknown and keep future work reviewable.

## What This Is Not

This repository is documentation-first. It is not:

- a production application,
- a backend service,
- an SDK or runtime package,
- a framework that must be installed and started,
- a replacement for human review,
- a guarantee that every AI provider or tool behaves the same way.

Provider and tool capabilities change quickly. Verify provider-specific claims against official documentation before publishing them.

## Quickstart

Use the English master prompt as the primary starting point:

```text
templates/MASTER_PROMPT.en.md
```

1. Copy [`templates/MASTER_PROMPT.en.md`](templates/MASTER_PROMPT.en.md) into your AI coding agent.
2. Point the agent at the target repository.
3. Let it run the interview and repository pre-check first.
4. Review the analysis report.
5. Review the documentation plan.
6. Approve file changes only after the plan is clear.

Use [`templates/MASTER_PROMPT.md`](templates/MASTER_PROMPT.md) when you specifically want the German workflow prompt.

No package installation is required to use the prompt standard. Python is only needed when you run this repository's validation scripts.

## Features

| Feature | Description |
|---|---|
| `MASTER_PROMPT.en.md` | Primary English onboarding prompt for repository analysis and AI documentation setup. |
| `templates/docs-ai/` | Ten reusable target-repository documents for architecture, memory, style, review, security and onboarding. |
| Short tool entrypoints | Guidance for files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and Copilot instructions without duplicating long docs. |
| Multilingual AI manual | `ai/<Language>/` folders mirror the English AI-agent manual structure across 75 language folders. |
| Validation script | `scripts/validate_repository.py` checks Markdown links, headings, mirrors, README coverage, secret patterns and translation markers. |
| Example setups | Minimal, Node/TypeScript, Python/FastAPI and multi-agent examples show how the standard can be applied. |

## What Gets Created In Target Repositories

The standard creates or updates a `docs/ai/` folder inside the target repository:

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

`PROJECT_MEMORY.md` is the target repository's continuity and handover anchor for current state, assumptions, decisions, open tasks, problems, risks and next steps. Tool-specific entrypoint files should stay short and point back to `docs/ai/`.

## Repository Map

```text
.
├─ AGENTS.md                     # Short repository instructions for coding agents
├─ README.md                     # Public GitHub entrypoint
├─ templates/                    # Master prompts and target-repository templates
├─ ai/                           # Multilingual AI-agent manual
├─ docs/                         # Supporting project documentation
├─ examples/                     # Minimal, stack-specific and multi-agent examples
├─ scripts/                      # Validation and AI manual refresh scripts
├─ tests/                        # Unit tests for maintenance scripts
├─ .github/                      # GitHub workflow, issue and PR configuration
└─ SECURITY.md                   # Security policy and reporting guidance
```

## Source Of Truth

| Area | Authoritative source |
|---|---|
| Primary onboarding prompt | [`templates/MASTER_PROMPT.en.md`](templates/MASTER_PROMPT.en.md) |
| German workflow prompt | [`templates/MASTER_PROMPT.md`](templates/MASTER_PROMPT.md) |
| Target-repository document templates | [`templates/docs-ai/`](templates/docs-ai/) |
| Public project overview | [`README.md`](README.md) |
| AI manual source language | [`ai/English/`](ai/English/) |
| Language index | [`ai/LANGUAGE_INDEX.md`](ai/LANGUAGE_INDEX.md) |
| Translation rules | [`ai/TRANSLATION_POLICY.md`](ai/TRANSLATION_POLICY.md) |
| Translation status | [`ai/TRANSLATION_STATUS.md`](ai/TRANSLATION_STATUS.md) |
| Tool compatibility | [`docs/tool-compatibility.md`](docs/tool-compatibility.md) |
| Contribution rules | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Security policy | [`SECURITY.md`](SECURITY.md) |

If localized documentation conflicts with English, the English source wins until maintainers explicitly decide otherwise.

## Languages And Translation Status

The multilingual manual is organized directly under `ai/`.

- [`ai/English/`](ai/English/) is the source of truth.
- [`ai/German/`](ai/German/) is a localized AI-translated mirror.
- Other non-English language folders mirror the English structure.
- Localized files carry the AI quality-pass status marker.
- File names, paths, commands, code blocks, API names and model names should remain stable across translations.

Start here:

- [English AI Manual](ai/English/README.md)
- [German AI Manual](ai/German/README.md)
- [Language Index](ai/LANGUAGE_INDEX.md)
- [Translation Policy](ai/TRANSLATION_POLICY.md)
- [Translation Status](ai/TRANSLATION_STATUS.md)

## Validation

This repository includes local maintenance checks and a GitHub Actions workflow.

Run the local checks:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```

Generate validation reports:

```bash
python scripts/validate_repository.py --root . --json ai/VALIDATION_REPORT.json --markdown ai/VALIDATION_REPORT.md
```

The validator checks:

- local Markdown links,
- first-level Markdown headings,
- empty files,
- directory README coverage,
- mirrored files across `ai/<Language>/`,
- language folder sorting,
- legacy AI links,
- common secret patterns,
- AI translation status markers,
- legacy unreviewed translation markers.

CI uses Python `3.x` through [`actions/setup-python`](.github/workflows/validate.yml). The exact minimum Python patch version is not pinned in this repository.

## Examples

| Example | Use when |
|---|---|
| [`examples/minimal/`](examples/minimal/) | You want the smallest useful setup before expanding to the full template set. |
| [`examples/node-typescript/`](examples/node-typescript/) | You are documenting a Node.js or TypeScript repository. |
| [`examples/python-fastapi/`](examples/python-fastapi/) | You are documenting a Python FastAPI repository. |
| [`examples/multi-agent/`](examples/multi-agent/) | You want researcher, architect, writer and reviewer roles. |

## GitHub And Community Files

| File | Purpose | Status |
|---|---|---|
| [`.github/ISSUE_TEMPLATE/bug_report.yml`](.github/ISSUE_TEMPLATE/bug_report.yml) | Structured bug reports | Present |
| [`.github/ISSUE_TEMPLATE/improvement.yml`](.github/ISSUE_TEMPLATE/improvement.yml) | Focused improvement proposals | Present |
| [`.github/ISSUE_TEMPLATE/tool_compatibility.yml`](.github/ISSUE_TEMPLATE/tool_compatibility.yml) | Tool compatibility reports or suggestions | Present |
| [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) | Pull request checklist | Present |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution process | Present |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Contributor behavior expectations | Present |
| [`SECURITY.md`](SECURITY.md) | Security policy | Present |
| [`.github/workflows/validate.yml`](.github/workflows/validate.yml) | Unit tests and repository validation | Present |

## Supported Agent Ecosystem

The standard is tool-neutral. It can be used with coding-agent runtimes and IDE assistants documented in [`docs/tool-compatibility.md`](docs/tool-compatibility.md), including Codex, Claude Code, GitHub Copilot, Gemini CLI, Cursor, Windsurf, Continue, Aider and OpenCode.

It also includes cautious guidance for model families and providers such as OpenAI, Anthropic, Google Gemini, DeepSeek, Qwen, Kimi, Mistral, Grok, MiniMax, Xiaomi MiMo, Llama, Cohere, Perplexity and OpenRouter. Treat those as compatibility notes, not support guarantees.

## Design Principles

| Principle | Meaning |
|---|---|
| Evidence before claims | Ground facts in files, tests, configuration or existing documentation. |
| No invented business rules | Mark unknowns instead of filling gaps with guesses. |
| Human review before impact | AI output is a proposal until reviewed and approved. |
| Explicit security boundaries | Do not imply production readiness or safety without evidence. |
| Short tool entrypoints | Keep agent-specific files compact and point to `docs/ai/`. |
| Maintained documentation | Prefer compact, useful docs over duplicated long-form guidance. |

## Security Model

This project does not make AI-generated output automatically trusted.

The standard requires:

- no secrets in documentation,
- no real personal, customer, financial or internal data in examples,
- no production-readiness claims without evidence,
- clear marking of assumptions and unknowns,
- redaction of sensitive values,
- human review before merge or production use.

See [`SECURITY.md`](SECURITY.md), [`templates/docs-ai/SECURITY_RULES.md`](templates/docs-ai/SECURITY_RULES.md) and [`templates/optional/PRODUCTION_READINESS.md`](templates/optional/PRODUCTION_READINESS.md).

## Contributing

Contributions are welcome when they improve clarity, safety, tool compatibility, translation quality or real-world usability.

Before opening a pull request:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```

Keep pull requests focused. Avoid speculative tool claims, generic best-practice additions and unnecessary prompt expansion. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and use the checklist in [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md).

## License

This project is licensed under the [MIT License](LICENSE).
