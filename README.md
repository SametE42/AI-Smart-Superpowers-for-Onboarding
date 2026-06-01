# AI Repo Onboarding Standard

<p align="center">
  <a href="https://github.com/SametE42/Ai-Repo-Onboarding/actions/workflows/validate.yml"><img alt="Validation" src="https://github.com/SametE42/Ai-Repo-Onboarding/actions/workflows/validate.yml/badge.svg"></a>
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-111827">
  <img alt="Docs first" src="https://img.shields.io/badge/docs-evidence--first-2563eb">
  <img alt="Languages" src="https://img.shields.io/badge/language%20folders-75-0f766e">
</p>

<p align="center">
  A reusable documentation and prompt standard for onboarding AI coding agents into software repositories safely, consistently and with clear human-review boundaries.
</p>

---

## What This Is

AI coding agents work better when they receive stable repository context instead of a pile of unrelated files. This project defines a practical onboarding standard built around:

- a primary master prompt,
- a structured `docs/ai/` knowledge base for target repositories,
- short tool entrypoints such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and Copilot instructions,
- explicit rules for assumptions, security, production readiness and verification,
- multilingual AI-agent documentation under `ai/<Language>/`.

This repository is documentation-first. It does not ship a production application, backend service or runtime package.

## Quickstart

Use the English prompt as the source-of-truth starting point:

```text
templates/MASTER_PROMPT.en.md
```

1. Copy `templates/MASTER_PROMPT.en.md` into your AI coding agent.
2. Point the agent at the target repository.
3. Let it run the interview and repository pre-check first.
4. Review the analysis report and documentation plan.
5. Approve file changes only after the plan is clear.

Use `templates/MASTER_PROMPT.md` only when you specifically want the German workflow prompt.

## What Gets Created

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

These documents give future agents a compact, verifiable working context. `PROJECT_MEMORY.md` acts as the continuity and handover anchor for current state, assumptions, decisions, open tasks, problems, risks and next steps. Tool-specific files should stay short and point back to `docs/ai/`.

## Repository Map

```text
Ai-Repo-Onboarding/
├─ AGENTS.md
├─ README.md
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ LICENSE
├─ .github/
│  ├─ CODEOWNERS
│  ├─ ISSUE_TEMPLATE/
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ workflows/
├─ ai/
│  ├─ English/
│  ├─ German/
│  ├─ ...
│  ├─ LANGUAGE_INDEX.md
│  ├─ TRANSLATION_POLICY.md
│  └─ VALIDATION_REPORT.md
├─ docs/
├─ examples/
├─ i18n/
├─ scripts/
├─ templates/
└─ tests/
```

## Source Of Truth

| Area | Authoritative source |
|---|---|
| Primary onboarding prompt | `templates/MASTER_PROMPT.en.md` |
| German workflow prompt | `templates/MASTER_PROMPT.md` |
| Public project overview | `README.md` |
| AI manual source language | `ai/English/` |
| Translation rules | `ai/TRANSLATION_POLICY.md` |
| Tool compatibility | `docs/tool-compatibility.md` |
| Security policy | `SECURITY.md` |

If localized documentation conflicts with English, the English source wins until maintainers explicitly decide otherwise.

## Languages And Translation Status

The multilingual manual is organized directly under `ai/`.

- `ai/English/` is the source of truth.
- `ai/German/` is an AI-translated localized mirror.
- Every non-English language folder contains AI-translated pages generated from the shared manual structure.
- Other language folders mirror the English structure and carry the AI quality-pass status marker.
- File names, paths, commands, code blocks, API names and model names should remain unchanged across translations.

Start here:

- [English AI Manual](ai/English/README.md)
- [German AI Manual](ai/German/README.md)
- [Language Index](ai/LANGUAGE_INDEX.md)
- [Translation Policy](ai/TRANSLATION_POLICY.md)
- [Translation Status](ai/TRANSLATION_STATUS.md)

## Supported Agent Ecosystem

The standard is tool-neutral. It can be used with coding-agent runtimes and IDE assistants such as:

- OpenAI Codex
- Claude Code
- GitHub Copilot
- Gemini CLI
- Cursor
- Windsurf
- Continue
- Aider
- OpenCode

It also includes guidance for model families and providers such as OpenAI, Anthropic, Google Gemini, DeepSeek, Qwen, Kimi, Mistral, Grok, MiniMax, Xiaomi MiMo, Llama, Cohere, Perplexity and OpenRouter.

Provider capabilities change quickly. Verify compatibility claims against official documentation before publishing provider-specific updates.

## Validation

This repository includes a reproducible validation script and GitHub Actions workflow.

Run the local checks:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```

Generate reports:

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
- AI translation status markers and legacy unreviewed translation markers.

## Examples

| Example | Use when |
|---|---|
| [`examples/minimal/`](examples/minimal/) | You want the smallest useful setup. |
| [`examples/node-typescript/`](examples/node-typescript/) | You are documenting a Node.js or TypeScript repository. |
| [`examples/python-fastapi/`](examples/python-fastapi/) | You are documenting a Python FastAPI repository. |
| [`examples/multi-agent/`](examples/multi-agent/) | You want researcher, architect, writer and reviewer roles. |

## Design Principles

- Evidence before claims.
- No invented business rules.
- Human review before impactful changes.
- Security and production readiness must be explicit, not implied.
- Tool entrypoints should stay short.
- Multi-model work should be append-only and conflict-aware.
- Documentation should be useful, compact and maintained.

## Security Model

This project does not make AI-generated output automatically trusted.

The standard requires:

- no secrets in documentation,
- no real personal, customer, financial or internal data in examples,
- no production-readiness claims without evidence,
- clear marking of assumptions and unknowns,
- redaction of sensitive values,
- human review before merge or production use.

See [SECURITY.md](SECURITY.md), [templates/docs-ai/SECURITY_RULES.md](templates/docs-ai/SECURITY_RULES.md) and [templates/optional/PRODUCTION_READINESS.md](templates/optional/PRODUCTION_READINESS.md).

## Contributing

Contributions are welcome when they improve clarity, safety, tool compatibility, translation quality or real-world usability.

Before opening a pull request:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) and use the pull request checklist in [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md).

## License

MIT License. See [LICENSE](LICENSE).
