# Architecture Of This Project

AI Smart Superpowers for Onboarding is organized as a modular Repository Preflight Framework. Its job is to turn repository evidence into reviewed AI context before coding agents make changes.

The project is intentionally modular because AI-agent onboarding in complex repositories needs more than a single instruction file. The framework separates entrypoints, persistent knowledge, technology and stack context, build and test context, evidence tracking, governance, tool compatibility, validation, examples, translations and language-dependent output for all existing languages.

## Module Map

| Module | Purpose | Main files |
|---|---|---|
| Core Onboarding | Main process and master prompt | `README.md`, `templates/` |
| AI Knowledge Base | Persistent repository context | `templates/docs-ai/` |
| Technology & Stack Context | Programming languages, build, tests, dependencies and runtime | `TECH_STACK.md`, `BUILD_AND_TEST.md`, `DEPENDENCIES.md`, `RUNTIME_ENVIRONMENT.md` |
| Localized Output | Language-dependent output for all existing languages | `i18n` file maps, installer |
| Language Support Matrix | Status and mappings for all languages | `i18n/language-support.yml`, `docs/language-support.md` |
| Localization Quality | Review status, glossary and translation rules | `i18n/glossary.yml`, `docs/localization-guidelines.md` |
| Evidence & Traceability | Sources and confidence for claims | `EVIDENCE_MAP.md`, `DECISIONS.md` |
| Governance & Safety | Security and review boundaries | `SECURITY_RULES.md`, `RISK_REGISTER.md` |
| Tool Entrypoints | Integration with agents | `templates/tool-entrypoints/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Copilot instructions |
| Skill Packaging | Reusable agent workflows | `skills/`, `templates/skills/` |
| Validation & CI | Quality checks | `scripts/`, `tests/`, `.github/workflows/` |
| Examples | Realistic usage examples | `examples/` |
| Translations | Language mirrors and localization metadata | `ai/`, `i18n/` |

## How The Modules Work Together

Tool entrypoints stay short and point agents toward the knowledge base. The master prompt guides the initial repository preflight. The `templates/docs-ai/` files define what should be created inside a target repository. Validation scripts check that this repository and the generated standard remain coherent. The multilingual manual under `ai/` explains the broader AI-agent operating model, while `i18n/` is the planned home for machine-readable language support, file maps and terminology.

## Source Of Truth

English source material is the canonical reference for framework behavior. The current authoritative sources are:

- `README.md` for public positioning.
- `templates/MASTER_PROMPT.en.md` for the primary onboarding workflow.
- `templates/docs-ai/` for target-repository knowledge-base templates.
- `ai/English/` for the AI manual source language.
- `ai/LANGUAGE_INDEX.md` and `ai/TRANSLATION_STATUS.md` for current language-folder evidence.
- `scripts/validate_repository.py` and tests for current release-readiness invariants.

Localized files should not introduce unique normative requirements. If a rule changes, update the English source first, then mirror or map it.

## Duplication Boundaries

The README should explain the project and link to deeper documentation. It should not contain every template, schema rule, migration case or language mapping. Tool entrypoints should also remain compact because coding agents load them frequently and because long duplicated rules become stale quickly.

## Localized Filenames

Localized filenames are supported so target repositories can present an AI knowledge base in the language their maintainers use. This requires explicit file maps instead of guessing translated filenames. File maps make localized output auditable, testable and reversible.

`AGENTS.md` is not localized by default. Many tools and agent runtimes look for that exact filename, so changing it would reduce interoperability.

## Technology Neutrality

The framework must remain technology- and programming-language-neutral. Python is acceptable for this repository's installer, validation and tests, but generated onboarding output must work for Python, JavaScript, TypeScript, Java, C#, Go, Rust, PHP, Ruby, Kotlin, Swift, C/C++, monorepos, frontend, backend, fullstack, Infrastructure-as-Code and documentation projects.

## Language Support And Review Quality

All existing languages should reach the same functional support level: selectable language, canonical structure, localized structure, file map, validation and documentation. Translation quality is tracked separately because a language can be technically supported before a human review has happened.
