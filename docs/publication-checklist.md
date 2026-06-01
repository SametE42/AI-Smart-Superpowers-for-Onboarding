# Publication Checklist

Use this before publishing or releasing the repository.

## Required release gate

- [ ] `README.md` explains purpose, quickstart and limits.
- [ ] `LICENSE` exists.
- [ ] `CHANGELOG.md` includes the release-relevant changes.
- [ ] `CONTRIBUTING.md` exists.
- [ ] `SECURITY.md` exists.
- [ ] Repository-specific progress notes are not committed.
- [ ] `templates/MASTER_PROMPT.md` is present.
- [ ] `templates/MASTER_PROMPT.en.md` is present and treated as the primary English prompt.
- [ ] `templates/docs-ai/` contains all 10 core document templates.
- [ ] `docs/tool-compatibility.md` is present.
- [ ] `examples/minimal/` exists.
- [ ] `scripts/validate_repository.py` is present.
- [ ] `scripts/refresh_ai_manual.py` is present.
- [ ] `tests/` contains validation tests.
- [ ] GitHub validation workflow exists at `.github/workflows/validate.yml`.
- [ ] `ai/VALIDATION_REPORT.md` and `ai/VALIDATION_REPORT.json` are regenerated from the current tree.
- [ ] `git status --short` was reviewed and every new or modified file is intentionally included or intentionally left out.
- [ ] All GitHub-critical files are staged and committed before pushing: `.github/`, `AGENTS.md`, `scripts/`, `tests/`, `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md` and `LICENSE`.
- [ ] No real personal data is included.
- [ ] No internal URLs are included.
- [ ] No secrets are included.
- [ ] Local machine paths are removed or anonymized.

## Required commands

Run before release:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root . --json ai/VALIDATION_REPORT.json --markdown ai/VALIDATION_REPORT.md
```

Expected result:

- unit tests pass,
- validator status is `PASS`,
- generated validation reports reflect the current file counts and findings.

## Translation status gate

- [ ] `ai/English/` remains the source of truth.
- [ ] Every non-English language folder mirrors the English structure.
- [ ] Every localized file includes `<!-- translation-status: ai-translated; ai-quality-pass -->`.
- [ ] `ai/VALIDATION_REPORT.md` shows `ai_translated_files: 19166`, `missing_ai_translation_marker_files: 0` and `unreviewed_translation_files: 0`.

## Optional later

- [ ] Release automation beyond validation.
- [ ] Security or scorecard workflows.
- [ ] More examples.
- [ ] Additional translation quality audits for high-traffic languages.
- [ ] Project-specific skills, subagents, hooks, MCP servers or plugins when a repeated workflow justifies them.
- [ ] More target-repository examples for common stacks.
- [ ] Branch protection and required status checks configured in GitHub repository settings.
