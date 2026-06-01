# AI Repo Onboarding Standard GitHub Configuration

AI Repo Onboarding Standard is a reusable documentation and prompt standard for onboarding AI coding agents into software repositories safely, consistently and with clear human-review boundaries.

This `.github/` directory contains the repository-facing GitHub configuration for that standard: review ownership, issue intake, pull request guidance and automated validation. It is maintenance infrastructure for this repository, not part of the target-repository `docs/ai/` template that users copy into their own projects.

For the public project overview, start with the root [README](../README.md).

## Project Snapshot

| Area | Entry point |
|---|---|
| Primary onboarding prompt | [`templates/MASTER_PROMPT.en.md`](../templates/MASTER_PROMPT.en.md) |
| German workflow prompt | [`templates/MASTER_PROMPT.md`](../templates/MASTER_PROMPT.md) |
| Generated target-repository docs | [`templates/docs-ai/`](../templates/docs-ai/) |
| Multilingual AI manual | [`ai/English/`](../ai/English/) |
| Tool compatibility notes | [`docs/tool-compatibility.md`](../docs/tool-compatibility.md) |
| Contribution rules | [`CONTRIBUTING.md`](../CONTRIBUTING.md) |
| Security policy | [`SECURITY.md`](../SECURITY.md) |

The repository is documentation-first. It does not provide a production application, backend service, runtime package or automatic replacement for human review.

## GitHub Files

| Path | Purpose |
|---|---|
| [`CODEOWNERS`](CODEOWNERS) | Assigns review ownership for documentation, templates, scripts and tests. |
| [`PULL_REQUEST_TEMPLATE.md`](PULL_REQUEST_TEMPLATE.md) | Guides contributors through scope, verification, security and anti-bloat checks. |
| [`ISSUE_TEMPLATE/`](ISSUE_TEMPLATE/) | Collects structured bug reports, improvement proposals and tool-compatibility updates. |
| [`workflows/README.md`](workflows/README.md) | Explains repository validation workflows. |
| [`workflows/validate.yml`](workflows/validate.yml) | Runs unit tests and repository validation on pushes and pull requests. |

## Validation Gate

The GitHub workflow mirrors the local checks documented in the root README:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```

The validator checks Markdown structure, local links, mirrored AI language files, README coverage, empty files, common secret patterns and AI translation status markers.

## Maintenance Rules

- Keep GitHub templates short, specific and action-oriented.
- Keep long-form project guidance in [`README.md`](../README.md), [`docs/`](../docs/) or [`templates/`](../templates/).
- Do not commit repository-specific progress, session, handover or completion notes.
- Do not add secrets, private URLs, personal data or internal operational details.
- Update workflow documentation when validation behavior changes.
