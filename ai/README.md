# AI Documentation Hub

This repository organizes the multilingual AI Manual for AI Smart Superpowers for Onboarding.

The manual supports an evidence-first Pre-Development Onboarding layer for AI coding agents. Language folders help agents and maintainers prepare repository context, safety boundaries, prompts and workflows before planning, coding, testing or review begins.

## Language folders

Each language folder mirrors the same structure:

- `models/`
- `providers/`
- `tools/`
- `commands/`
- `prompts/`
- `skills/`
- `memory/`
- `context-engineering/`
- `workflows/`
- `optimization/`
- `evals/`
- `agents/`
- `safety/`
- `examples/`
- `templates/`

English is the source of truth. Other languages are localized mirrors. Each language `README.md` must keep the same core structure: Overview, Where This Fits, Target Output, Quickstart, Source Of Truth And Links, Workflow, When To Use, When Not To Use, Manual Structure, safety rules, localization notes and quality checklist.

## Start

Open `English/README.md` first. It links the primary master prompt, `docs/ai/` templates, the AI Manual entrypoint and the Magical Prompt Improver.

## Status files

- `LANGUAGE_INDEX.md` lists all language folders.
- `TRANSLATION_STATUS.md` records structure and AI translation status per language.
- `TRANSLATION_POLICY.md` defines translation rules.
- `VALIDATION_REPORT.md` and `VALIDATION_REPORT.json` are generated from `scripts/validate_repository.py`.

Localized AI-translated pages keep the machine-readable `<!-- translation-status: ai-translated; ai-quality-pass -->` status comment. The validator reports any missing AI translation marker or legacy review marker.
