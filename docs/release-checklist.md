# Release Checklist

Use this checklist before tagging or publishing a release.

## Required Commands

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
python scripts/check_language_support.py --root .
python scripts/check_standard_docs.py --root .
python scripts/check_tool_compatibility.py --root .
python scripts/check_language_review_evidence.py --root .
python scripts/check_external_links.py --root .
python scripts/install_ai_onboarding.py --mode minimal --language en --structure canonical --target /tmp/ai-onboarding-min --dry-run
python scripts/install_ai_onboarding.py --mode standard --language en --structure canonical --target /tmp/ai-onboarding-standard --dry-run
python scripts/install_ai_onboarding.py --mode enterprise --language en --structure canonical --target /tmp/ai-onboarding-enterprise --dry-run
python scripts/install_ai_onboarding.py --mode standard --language de --structure localized --target /tmp/ai-onboarding-de --dry-run
python scripts/generate_language_support_report.py --root . --output docs/language-support-report.md
python scripts/validate_repository.py --root . --json ai/VALIDATION_REPORT.json --markdown ai/VALIDATION_REPORT.md
git diff --exit-code docs/language-support-report.md ai/VALIDATION_REPORT.json ai/VALIDATION_REPORT.md
git diff --check
```

Optional external network gate before publishing:

```bash
python scripts/check_external_links.py --root . --check-network --timeout 8 --retries 1
```

## Required Review Gates

- `CHANGELOG.md` has the target version and date.
- `RELEASE_NOTES.md` matches the tag.
- `docs/tool-compatibility.md` has source, date, confidence and limitations for compatibility claims.
- `scripts/check_tool_compatibility.py --root .` passes.
- Every language marked `reviewed` has matching review evidence under `i18n/review-evidence.<code>.yml`.
- External links pass deterministic inventory validation; run the manual network gate when release-facing URLs changed.
- `docs/language-support-report.md` is regenerated from the current language metadata.
- Known limitations remain visible: installer experimental but functional, generated output review-ready, non-reviewed languages pending linguistic review.
- `main` branch protection requires pull requests, up-to-date required checks and no force pushes.

## Human Review Gates

Do not mark a language as `reviewed` unless a qualified human reviewer checked the README, core terminology, standard output filenames, commands, paths and Markdown rendering.
