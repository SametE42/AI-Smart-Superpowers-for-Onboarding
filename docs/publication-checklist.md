# Publication Checklist

Use this before publishing or releasing the repository.

## Required release gate

- [ ] `README.md` explains purpose, quickstart and limits.
- [ ] `LICENSE` exists.
- [ ] `CHANGELOG.md` includes the release-relevant changes.
- [ ] `CONTRIBUTING.md` exists.
- [ ] `SECURITY.md` exists.
- [ ] Repository-specific progress, session, handover or completion notes are deleted or left untracked before commit and push.
- [ ] `templates/MASTER_PROMPT.md` is present.
- [ ] `templates/MASTER_PROMPT.en.md` is present and treated as the primary English prompt.
- [ ] `config/standard-docs.yml` defines Conceptual Core plus Minimal, Standard and Enterprise mode file lists.
- [ ] `templates/docs-ai/` contains every file referenced by `config/standard-docs.yml`.
- [ ] Every file in `templates/optional/` is listed in `templates/optional/README.md`.
- [ ] `docs/tool-compatibility.md` is present.
- [ ] `examples/minimal/` exists.
- [ ] `scripts/validate_repository.py` is present.
- [ ] `scripts/refresh_ai_manual.py` is present.
- [ ] `tests/` contains validation tests.
- [ ] GitHub validation workflow exists at `.github/workflows/validate.yml`.
- [ ] GitHub Actions permissions stay minimal; current workflows use `contents: read`.
- [ ] GitHub Actions versions are either pinned to commit SHAs or deliberately kept on reviewed major versions with this decision documented in `CHANGELOG.md`.
- [ ] `scripts/check_standard_docs.py --root .` passes.
- [ ] `ai/VALIDATION_REPORT.md` and `ai/VALIDATION_REPORT.json` are regenerated from the current tree.
- [ ] `git status --short` was reviewed and every new or modified file is intentionally included or intentionally left out.
- [ ] All GitHub-critical files are staged and committed before pushing: `.github/`, `AGENTS.md`, `scripts/`, `tests/`, `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md` and `LICENSE`.
- [ ] No real personal data is included.
- [ ] No internal URLs are included.
- [ ] No secrets are included.
- [ ] No old public repository names or repository URLs remain outside clearly scoped changelog history.
- [ ] Local machine paths are removed or anonymized.
- [ ] Golden installer E2E fixtures pass for `standard en canonical` and `standard de localized`.
- [ ] `docs/tool-compatibility.md` has `Source`, `Last checked`, `Confidence` and `Limitations` for every compatibility row.
- [ ] GitHub branch protection for `main` requires PR review, up-to-date branches, `Validate repository` and `Validate AI docs`, and disallows force pushes.
- [ ] No open conflict-heavy PR remains visible unless it is intentionally retained with a clear comment.
- [ ] A GitHub release exists for the intended tag, and `CHANGELOG.md` plus `RELEASE_NOTES.md` match that tag.

## Required commands

Run before release:

```bash
python -m unittest discover -s tests
python scripts/check_language_support.py --root .
python scripts/check_standard_docs.py --root .
python scripts/validate_repository.py --root . --json ai/VALIDATION_REPORT.json --markdown ai/VALIDATION_REPORT.md
git diff --exit-code ai/VALIDATION_REPORT.json ai/VALIDATION_REPORT.md
```

Expected result:

- unit tests pass,
- validator status is `PASS`,
- generated validation reports reflect the current file counts and findings,
- optional template README coverage is complete,
- old public repository reference hits are `0`,
- `legacy_localization_term_hits` is `0`.

## Localization status gate

- [ ] `ai/English/` remains the source of truth.
- [ ] Every non-English language folder mirrors the English structure.
- [ ] Every localized file includes `<!-- localization-status: localized-mirror; review-status: tracked-in-language-support -->`.
- [ ] `ai/VALIDATION_REPORT.md` shows `localized_mirror_files` above zero, `missing_localization_status_marker_files: 0`, `legacy_localization_term_hits: 0` and `unreviewed_translation_files: 0`.

## Optional later

- [ ] Release automation beyond validation.
- [ ] Security or scorecard workflows.
- [ ] More examples.
- [ ] Additional translation quality audits for high-traffic languages.
- [ ] Project-specific skills, subagents, hooks, MCP servers or plugins when a repeated workflow justifies them.
- [ ] More target-repository examples for common stacks.
- [ ] External link checking with timeout, retry and allowlist.
