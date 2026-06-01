# AI Smart Superpowers for Onboarding

<p align="center">
  <strong>Evidence-first onboarding docs and prompts for AI coding agents.</strong><br>
  A reusable standard for turning an unfamiliar repository into a safe, reviewable working context for humans and AI agents.
</p>

<p align="center">
  <a href="https://github.com/SametE42/AI-Smart-Superpowers-for-Onboarding/actions/workflows/validate.yml"><img alt="Validate repository" src="https://github.com/SametE42/AI-Smart-Superpowers-for-Onboarding/actions/workflows/validate.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/SametE42/AI-Smart-Superpowers-for-Onboarding"></a>
  <img alt="Master prompt: v12" src="https://img.shields.io/badge/master%20prompt-v12-7c3aed">
  <img alt="Language folders: 75" src="https://img.shields.io/badge/language%20folders-75-0f766e">
  <img alt="AI translated files: 19240" src="https://img.shields.io/badge/AI%20translated%20files-19240-2563eb">
  <img alt="Python: 3.x validation" src="https://img.shields.io/badge/python-3.x%20validation-3776ab">
</p>

<p align="center">
  <a href="#start-here">Start Here</a> ·
  <a href="#quickstart">Quickstart</a> ·
  <a href="#language-gateway">Languages</a> ·
  <a href="templates/MASTER_PROMPT.en.md">Master Prompt</a> ·
  <a href="ai/English/README.md">AI Manual</a> ·
  <a href="docs/">Docs</a> ·
  <a href="https://github.com/SametE42/AI-Smart-Superpowers-for-Onboarding/issues">Issues</a>
</p>

---

## Start Here

<table>
  <tr>
    <td width="20%"><a href="ai/English/README.md"><strong>English AI Manual</strong></a><br>Canonical AI-agent operating manual.</td>
    <td width="20%"><a href="ai/German/README.md"><strong>German AI Manual</strong></a><br>Localized German mirror.</td>
    <td width="20%"><a href="ai/LANGUAGE_INDEX.md"><strong>Language Index</strong></a><br>All available language folders.</td>
    <td width="20%"><a href="ai/TRANSLATION_POLICY.md"><strong>Translation Policy</strong></a><br>Source-of-truth and mirror rules.</td>
    <td width="20%"><a href="ai/TRANSLATION_STATUS.md"><strong>Translation Status</strong></a><br>Coverage and quality-pass status.</td>
  </tr>
</table>

## Contents

[`Overview`](#overview) · [`Quickstart`](#quickstart) · [`Workflow`](#workflow) · [`Target Output`](#what-gets-created-in-target-repositories) · [`Languages`](#language-gateway) · [`Validation`](#validation) · [`Examples`](#examples) · [`Security`](#security-model) · [`Contributing`](#contributing)

## Overview

AI coding agents work best when they receive stable repository context, explicit boundaries and verifiable documentation instead of scattered files and guesses. This repository provides a documentation-first onboarding standard built around:

| Standard layer | What it gives you |
|---|---|
| **Master prompt** | A structured interview, repository pre-check, analysis flow and output contract. |
| **`docs/ai/` templates** | Ten target-repository documents for architecture, memory, style, review, security and onboarding. |
| **Magical Prompt Improver** | An optional prompt-refinement protocol for turning unclear requests into safe, verifiable instructions. |
| **Tool entrypoint guidance** | Short references for agent files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and Copilot instructions. |
| **Multilingual AI manual** | A mirrored AI-agent operating manual under `ai/<Language>/`. |
| **Validation tooling** | Unit tests and a repository validator for Markdown, links, language mirrors, secrets and translation markers. |

This is not a production app, backend service, SDK, runtime package or replacement for human review. It is a reusable standard for making AI-assisted repository work safer and easier to audit.

## Quickstart

<table>
  <tr>
    <td width="33%">
      <strong>1. Start with the prompt</strong><br>
      Use <a href="templates/MASTER_PROMPT.en.md"><code>templates/MASTER_PROMPT.en.md</code></a> as the primary English onboarding prompt.
    </td>
    <td width="33%">
      <strong>2. Point it at a repository</strong><br>
      Let the agent run the interview, repository pre-check and analysis report before it edits files.
    </td>
    <td width="33%">
      <strong>3. Review before changes</strong><br>
      Approve the documentation plan before generated files are created or updated.
    </td>
  </tr>
</table>

Use [`templates/MASTER_PROMPT.md`](templates/MASTER_PROMPT.md) when you specifically want the German workflow prompt.

```text
Primary prompt:  templates/MASTER_PROMPT.en.md
German prompt:   templates/MASTER_PROMPT.md
Target output:   docs/ai/
Local checks:    python -m unittest discover -s tests
                 python scripts/validate_repository.py --root .
```

No package installation is required to use the prompt standard. Python is only needed for this repository's maintenance checks.

## Workflow

```mermaid
flowchart LR
    A["Master prompt"] --> B["Interview + repo pre-check"]
    B --> C["Evidence-based analysis"]
    C --> D["Documentation plan"]
    D --> E["Human approval"]
    E --> F["docs/ai/ knowledge base"]
    F --> G["Validation + review"]
```

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

## Language Gateway

<table>
  <tr>
    <td width="20%"><a href="ai/English/README.md"><strong>English</strong></a><br>Source of truth</td>
    <td width="20%"><a href="ai/German/README.md"><strong>German</strong></a><br>Localized mirror</td>
    <td width="20%"><a href="ai/LANGUAGE_INDEX.md"><strong>Language Index</strong></a><br>All 75 folders</td>
    <td width="20%"><a href="ai/TRANSLATION_POLICY.md"><strong>Translation Policy</strong></a><br>Rules and invariants</td>
    <td width="20%"><a href="ai/TRANSLATION_STATUS.md"><strong>Translation Status</strong></a><br>Coverage table</td>
  </tr>
</table>

The multilingual manual is organized under `ai/`. English is authoritative. Non-English folders mirror the English structure and carry the AI quality-pass status marker.

<details>
<summary><strong>Browse all language mirrors</strong></summary>

|  |  |  |  |  |
|---|---|---|---|---|
| [Afrikaans](ai/Afrikaans/README.md) | [Albanian](ai/Albanian/README.md) | [Amharic](ai/Amharic/README.md) | [Arabic](ai/Arabic/README.md) | [Armenian](ai/Armenian/README.md) |
| [Azerbaijani](ai/Azerbaijani/README.md) | [Basque](ai/Basque/README.md) | [Bengali](ai/Bengali/README.md) | [Bosnian](ai/Bosnian/README.md) | [Bulgarian](ai/Bulgarian/README.md) |
| [Burmese](ai/Burmese/README.md) | [Catalan](ai/Catalan/README.md) | [Chinese](ai/Chinese/README.md) | [Croatian](ai/Croatian/README.md) | [Czech](ai/Czech/README.md) |
| [Danish](ai/Danish/README.md) | [Dutch](ai/Dutch/README.md) | [English](ai/English/README.md) | [Estonian](ai/Estonian/README.md) | [Finnish](ai/Finnish/README.md) |
| [French](ai/French/README.md) | [Georgian](ai/Georgian/README.md) | [German](ai/German/README.md) | [Greek](ai/Greek/README.md) | [Gujarati](ai/Gujarati/README.md) |
| [Hausa](ai/Hausa/README.md) | [Hebrew](ai/Hebrew/README.md) | [Hindi](ai/Hindi/README.md) | [Hungarian](ai/Hungarian/README.md) | [Icelandic](ai/Icelandic/README.md) |
| [Indonesian](ai/Indonesian/README.md) | [Irish](ai/Irish/README.md) | [Italian](ai/Italian/README.md) | [Japanese](ai/Japanese/README.md) | [Kannada](ai/Kannada/README.md) |
| [Kazakh](ai/Kazakh/README.md) | [Khmer](ai/Khmer/README.md) | [Korean](ai/Korean/README.md) | [Kurdish](ai/Kurdish/README.md) | [Lao](ai/Lao/README.md) |
| [Latvian](ai/Latvian/README.md) | [Lithuanian](ai/Lithuanian/README.md) | [Macedonian](ai/Macedonian/README.md) | [Malay](ai/Malay/README.md) | [Malayalam](ai/Malayalam/README.md) |
| [Marathi](ai/Marathi/README.md) | [Mongolian](ai/Mongolian/README.md) | [Nepali](ai/Nepali/README.md) | [Norwegian](ai/Norwegian/README.md) | [Pashto](ai/Pashto/README.md) |
| [Persian](ai/Persian/README.md) | [Polish](ai/Polish/README.md) | [Portuguese](ai/Portuguese/README.md) | [Punjabi](ai/Punjabi/README.md) | [Romanian](ai/Romanian/README.md) |
| [Russian](ai/Russian/README.md) | [Serbian](ai/Serbian/README.md) | [Sinhala](ai/Sinhala/README.md) | [Slovak](ai/Slovak/README.md) | [Slovenian](ai/Slovenian/README.md) |
| [Somali](ai/Somali/README.md) | [Spanish](ai/Spanish/README.md) | [Swahili](ai/Swahili/README.md) | [Swedish](ai/Swedish/README.md) | [Tagalog](ai/Tagalog/README.md) |
| [Tamil](ai/Tamil/README.md) | [Telugu](ai/Telugu/README.md) | [Thai](ai/Thai/README.md) | [Tigrinya](ai/Tigrinya/README.md) | [Turkish](ai/Turkish/README.md) |
| [Ukrainian](ai/Ukrainian/README.md) | [Urdu](ai/Urdu/README.md) | [Uzbek](ai/Uzbek/README.md) | [Vietnamese](ai/Vietnamese/README.md) | [Zulu](ai/Zulu/README.md) |

</details>

## Source Of Truth

| Area | Authoritative source |
|---|---|
| Primary onboarding prompt | [`templates/MASTER_PROMPT.en.md`](templates/MASTER_PROMPT.en.md) |
| German workflow prompt | [`templates/MASTER_PROMPT.md`](templates/MASTER_PROMPT.md) |
| Target-repository document templates | [`templates/docs-ai/`](templates/docs-ai/) |
| Optional prompt-refinement template | [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](templates/optional/MAGICAL_PROMPT_IMPROVER.md) |
| Public project overview | [`README.md`](README.md) |
| AI manual source language | [`ai/English/`](ai/English/) |
| Language index | [`ai/LANGUAGE_INDEX.md`](ai/LANGUAGE_INDEX.md) |
| Translation rules | [`ai/TRANSLATION_POLICY.md`](ai/TRANSLATION_POLICY.md) |
| Translation status | [`ai/TRANSLATION_STATUS.md`](ai/TRANSLATION_STATUS.md) |
| Tool compatibility | [`docs/tool-compatibility.md`](docs/tool-compatibility.md) |
| Contribution rules | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Security policy | [`SECURITY.md`](SECURITY.md) |

If localized documentation conflicts with English, the English source wins until maintainers explicitly decide otherwise.

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

## Validation

This repository includes local maintenance checks and a GitHub Actions workflow.

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```

Generate validation reports:

```bash
python scripts/validate_repository.py --root . --json ai/VALIDATION_REPORT.json --markdown ai/VALIDATION_REPORT.md
```

The validator checks local Markdown file targets, H1 headings, empty files, directory README coverage, mirrored AI language files, language sorting, legacy AI links, old public repository references, optional template README coverage, common secret patterns, translation status markers and language README completeness. It does not currently validate external URLs or heading anchors.

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
