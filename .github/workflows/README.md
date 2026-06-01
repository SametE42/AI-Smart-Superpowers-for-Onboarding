# GitHub Workflows

This directory contains GitHub Actions workflows for repository validation.

## Workflows

- `validate.yml` runs unit tests with `python -m unittest discover -s tests`.
- `validate.yml` runs the repository validator with `python scripts/validate_repository.py --root .`.
- `validate.yml` regenerates `ai/VALIDATION_REPORT.md` and `ai/VALIDATION_REPORT.json`.
- `validate.yml` fails if regenerated validation reports differ from committed reports.

The validator blocks broken local Markdown links, missing mirrored AI files, incomplete language README files, unlisted optional templates, old public repository references, common secret patterns and missing translation markers. Generated validation reports are maintained in `ai/VALIDATION_REPORT.md` and `ai/VALIDATION_REPORT.json`; regenerate them locally when validation output changes.
