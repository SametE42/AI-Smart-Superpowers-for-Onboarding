# GitHub Workflows

This directory contains GitHub Actions workflows for repository validation.

## Workflows

- `validate.yml` runs unit tests with `python -m unittest discover -s tests`.
- `validate.yml` runs the repository validator with `python scripts/validate_repository.py --root .`.

Generated validation reports are maintained in `ai/VALIDATION_REPORT.md` and `ai/VALIDATION_REPORT.json`; regenerate them locally when validation output changes.
