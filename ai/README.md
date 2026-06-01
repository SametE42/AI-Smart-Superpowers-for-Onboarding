# AI Documentation Hub

This repository organizes AI-agent documentation by language.

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

English is the source of truth. Other languages are localized mirrors.

## Start

Open `English/README.md` first.

## Status files

- `LANGUAGE_INDEX.md` lists all language folders.
- `TRANSLATION_STATUS.md` records structure and AI translation status per language.
- `TRANSLATION_POLICY.md` defines translation rules.
- `VALIDATION_REPORT.md` and `VALIDATION_REPORT.json` are generated from `scripts/validate_repository.py`.

Localized AI-translated pages keep the machine-readable `<!-- translation-status: ai-translated; ai-quality-pass -->` status comment. The validator reports any missing AI translation marker or legacy review marker.
