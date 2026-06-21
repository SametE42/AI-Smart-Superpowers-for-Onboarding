# Release Notes

## v0.1.0 - 2026-06-21

AI Smart Superpowers for Onboarding v0.1.0 is the first public release target for the reusable repository-preflight standard.

The framework is not a coding agent, SDK or runtime package. The installer is experimental but functional and supports Minimal, Standard and Enterprise modes with canonical or localized output.

## Highlights

- Clear layered output model: Conceptual Core, Minimal, Standard, Enterprise and localized output.
- Central output contract in `config/standard-docs.yml`.
- Installer mode validation through tests and CI.
- Language-aware output with 75 functionally complete language entries.
- Source-backed tool compatibility matrix with confidence and limitation notes.
- Golden E2E installer fixtures for English canonical and German localized standard output.
- Repository validation reports regenerated from the current tree.

## Verification

Release validation should pass:

```bash
python -m unittest discover -s tests
python scripts/check_language_support.py --root .
python scripts/check_standard_docs.py --root .
python scripts/validate_repository.py --root . --json ai/VALIDATION_REPORT.json --markdown ai/VALIDATION_REPORT.md
git diff --exit-code ai/VALIDATION_REPORT.json ai/VALIDATION_REPORT.md
```

## Non-goals

- No claim of official support by external coding-agent tools.
- No claim of production SaaS functionality.
- No claim of adoption metrics, benchmarks or user counts.
- No replacement for human review.
- No claim that non-English language quality is human-reviewed unless the language metadata says `reviewed`.
