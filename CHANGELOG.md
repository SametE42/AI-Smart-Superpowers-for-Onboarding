# Changelog

All notable changes to this project are documented here.

This project follows semantic versioning where practical.

## [Unreleased]

### Added

- Deterministic external link inventory check with optional timeout/retry network validation.
- Manual GitHub Actions workflow for release-time external URL checks.
- Tool compatibility matrix contract validation.
- Language review evidence validation for languages marked `reviewed`.
- Review evidence metadata for the canonical English language source.

### Changed

- Expanded release, publication, workflow, config, i18n and test documentation for the new quality gates.

## [v0.1.0] - 2026-06-21

### Added

- Central machine-readable output contract in `config/standard-docs.yml`.
- Contract validation through `scripts/check_standard_docs.py`, unit tests and CI.
- Golden installer E2E fixtures for `standard en canonical` and `standard de localized`.
- Reproducible repository validation script and GitHub Actions workflow.
- Local unit tests for validation behavior.
- Reproducible AI manual scaffold refresh script for English source pages and localized mirror batches.
- Blocking validator coverage and tests for old public repository references.
- Optional `MAGICAL_PROMPT_IMPROVER.md` template for safe, verifiable prompt refinement.
- Multilingual AI manual page for the Magical Prompt Improver across all language folders.
- Prompt-intake activation guidance across target-repository system and tool entrypoint templates.
- Blocking validator coverage and tests for unlisted optional template files.
- Blocking validator coverage and tests for prompt README link consistency and unlocalized Magical Prompt Improver body text.

### Changed

- Clarified the README output model: Conceptual Core, Minimal, Standard, Enterprise and localized output.
- Rebuilt `docs/tool-compatibility.md` as a source-backed compatibility matrix with last-checked dates, confidence and limitations.
- Expanded publication gates for release checks, branch protection, source-backed compatibility and E2E fixtures.
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
- Replaced mirror placeholders in every non-English language folder with localized mirror pages and stable machine-readable review-status markers.
- Split validation reporting between English source scaffolds, localized mirror pages, legacy unreviewed translations and remaining mirror placeholders.
- Updated publication, contribution, pull request, workflow and i18n documentation to reflect the current validation and reporting workflow.
- Clarified GitHub commit-readiness checks, optional extension paths and AI translation coverage.
- Replaced personal author-name metadata with the public repository handle.
- Published the validated initial repository to GitHub.
- Updated validation workflow actions to current major versions to avoid Node.js 20 deprecation warnings; workflows keep minimal `contents: read` permissions.
- Removed repository-specific completion progress notes from the public tracked tree.
- Linked prompt manual pages from every language's `prompts/README.md` for easier discovery.
- Localized the Magical Prompt Improver manual body with workflow order, examples and quality gates for language-folder mirrors.

## Pre-release baseline - 2026-05-28

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
