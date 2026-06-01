# GitHub Configuration

This directory contains the GitHub-facing maintenance files for AI Repo Onboarding Standard.

These files support review, contribution intake and automated validation. They are not part of the target-repository onboarding template that users copy into their own projects.

## Contents

| Path | Purpose |
|---|---|
| `CODEOWNERS` | Assigns review ownership for documentation, templates, scripts and tests. |
| `PULL_REQUEST_TEMPLATE.md` | Guides contributors through scope, verification, security and anti-bloat checks. |
| `ISSUE_TEMPLATE/` | Collects structured bug reports, improvement proposals and tool-compatibility updates. |
| `workflows/validate.yml` | Runs unit tests and repository validation on pushes and pull requests. |

## Maintenance Rules

- Keep GitHub templates short and action-oriented.
- Do not duplicate the main documentation from `README.md`, `docs/` or `templates/`.
- Do not commit repository-specific progress, session, handover or completion notes.
- Do not add secrets, private URLs, personal data or internal operational details.
- Update validation docs when workflow behavior changes.

For public project usage, start with the root [README](../README.md).
