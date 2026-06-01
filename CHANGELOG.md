# Changelog

All notable changes to this project are documented here.

This project follows semantic versioning where practical.

## [Unreleased]

### Added

- Reproducible repository validation script and GitHub Actions workflow.
- Local unit tests for validation behavior.
- Reproducible AI manual scaffold refresh script for English source pages and AI-translated localized batches.
- Blocking validator coverage and tests for old public repository references.
- Optional `MAGICAL_PROMPT_IMPROVER.md` template for safe, verifiable prompt refinement.
- Prompt-intake activation guidance across target-repository system and tool entrypoint templates.
- Blocking validator coverage and tests for unlisted optional template files.

### Changed

- Renamed the public project to AI Smart Superpowers for Onboarding after the GitHub repository rename.
- Replaced old public repository URLs with `https://github.com/SametE42/AI-Smart-Superpowers-for-Onboarding`.
- Expanded all language-folder `README.md` files into complete AI manual entrypoints.
- Added blocking validator checks for language README required sections and standard subfolder coverage.
- Regenerated validation reports after the rebrand and validator update.
- Reworked the root README as the primary GitHub entrypoint.
- Expanded `templates/MASTER_PROMPT.en.md` so it matches the full workflow structure of the German prompt.
- Standardized English template unknown markers to `[UNKNOWN]` and `[ASSUMPTION: ...]`.
- Extended CODEOWNERS coverage to AI documentation and validation files.
- Replaced generic scaffold text in `ai/English/` and matching `ai/German/` pages with practical operating guidance.
- Replaced mirror placeholders in every non-English language folder with AI-translated pages and stable machine-readable quality-pass markers.
- Split validation reporting between English source scaffolds, AI-translated localized pages, legacy unreviewed translations and remaining mirror placeholders.
- Updated publication, contribution, pull request, workflow and i18n documentation to reflect the current validation and reporting workflow.
- Clarified GitHub commit-readiness checks, optional extension paths and AI translation coverage.
- Replaced personal author-name metadata with the public repository handle.
- Published the validated initial repository to GitHub.
- Updated validation workflow actions to current major versions to avoid Node.js 20 deprecation warnings.
- Removed repository-specific completion progress notes from the public tracked tree.

## [0.1.0] - 2026-05-28

### Added

- Initial public version of AI Smart Superpowers for Onboarding.
- Master prompt for multi-model repository onboarding.
- `/docs/ai/` 10-document documentation contract.
- Tool-specific entrypoint strategy for `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and Copilot instructions.
- Review checklist and verification ladder.
- Security, production-readiness and anti-bloat rules.
- Progressive context retrieval guidance.
- Public repository structure with templates, examples and documentation.
- Optional templates for operations, production readiness, testing strategy and protocol boundaries.

### Notes

- The master prompt is considered version `v12`.
- Future changes should avoid expanding the master prompt unless a concrete repeated risk or compatibility issue is proven.
