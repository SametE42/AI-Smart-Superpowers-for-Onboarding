# AI Smart Superpowers for Onboarding

<p align="center">
  <strong>Evidence-first Pre-Development Onboarding docs and prompts for AI coding agents.</strong><br>
  Repository governance, issue intake, pull request guidance and validation workflows for this standard.
</p>

<p align="center">
  <a href="https://github.com/SametE42/AI-Smart-Superpowers-for-Onboarding/actions/workflows/validate.yml"><img alt="Validate repository" src="https://github.com/SametE42/AI-Smart-Superpowers-for-Onboarding/actions/workflows/validate.yml/badge.svg"></a>
  <a href="../LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/SametE42/AI-Smart-Superpowers-for-Onboarding"></a>
  <img alt="Master prompt: v12" src="https://img.shields.io/badge/master%20prompt-v12-7c3aed">
  <img alt="Language folders: 75" src="https://img.shields.io/badge/language%20folders-75-0f766e">
  <img alt="Localized mirror files: 19240" src="https://img.shields.io/badge/localized%20mirror%20files-19240-2563eb">
  <img alt="Python: 3.x validation" src="https://img.shields.io/badge/python-3.x%20validation-3776ab">
</p>

<p align="center">
  <a href="../README.md#start-here">Start Here</a> ·
  <a href="../README.md#quickstart">Quickstart</a> ·
  <a href="../README.md#multilingual-ai-manual">Languages</a> ·
  <a href="../templates/MASTER_PROMPT.en.md">Master Prompt</a> ·
  <a href="../ai/English/README.md">AI Manual</a> ·
  <a href="../docs/">Docs</a>
</p>

---

## Start Here

<table>
  <tr>
    <td width="20%"><a href="../ai/English/README.md"><strong>English AI Manual</strong></a><br>Canonical AI-agent operating manual.</td>
    <td width="20%"><a href="../ai/German/README.md"><strong>German AI Manual</strong></a><br>Localized German mirror.</td>
    <td width="20%"><a href="../ai/LANGUAGE_INDEX.md"><strong>Language Index</strong></a><br>All available language folders.</td>
    <td width="20%"><a href="../ai/TRANSLATION_POLICY.md"><strong>Translation Policy</strong></a><br>Source-of-truth and mirror rules.</td>
    <td width="20%"><a href="../ai/TRANSLATION_STATUS.md"><strong>Localization Status</strong></a><br>Coverage and review status.</td>
  </tr>
</table>

## Overview

AI Smart Superpowers for Onboarding is a reusable evidence-first Pre-Development Onboarding layer for preparing AI coding agents to work in software repositories safely, consistently and with clear human-review boundaries.

For the complete public project page, open the root [README](../README.md). This `.github/` directory is the repository operations layer: it keeps contribution intake structured, review ownership explicit and validation automatic.

| Standard layer | Entry point |
|---|---|
| **Primary onboarding prompt** | [`templates/MASTER_PROMPT.en.md`](../templates/MASTER_PROMPT.en.md) |
| **German workflow prompt** | [`templates/MASTER_PROMPT.md`](../templates/MASTER_PROMPT.md) |
| **Generated target-repository docs** | [`templates/docs-ai/`](../templates/docs-ai/) |
| **Multilingual AI manual** | [`ai/English/`](../ai/English/) |
| **Tool compatibility notes** | [`docs/tool-compatibility.md`](../docs/tool-compatibility.md) |
| **Contribution rules** | [`CONTRIBUTING.md`](../CONTRIBUTING.md) |
| **Security policy** | [`SECURITY.md`](../SECURITY.md) |

## GitHub Configuration

| File | Purpose |
|---|---|
| [`CODEOWNERS`](CODEOWNERS) | Assigns review ownership for documentation, templates, scripts and tests. |
| [`PULL_REQUEST_TEMPLATE.md`](PULL_REQUEST_TEMPLATE.md) | Guides contributors through scope, verification, security and anti-bloat checks. |
| [`ISSUE_TEMPLATE/`](ISSUE_TEMPLATE/) | Collects structured bug reports, improvement proposals and tool-compatibility updates. |
| [`workflows/README.md`](workflows/README.md) | Explains repository validation workflows. |
| [`workflows/validate.yml`](workflows/validate.yml) | Runs unit tests and repository validation on pushes and pull requests. |

## Validation Gate

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
python scripts/validate_repository.py --root . --json ai/VALIDATION_REPORT.json --markdown ai/VALIDATION_REPORT.md
git diff --exit-code ai/VALIDATION_REPORT.json ai/VALIDATION_REPORT.md
```

The validator checks Markdown structure, local Markdown links, local HTML links, local heading anchors, mirrored AI language files, README coverage, language README completeness, optional template README coverage, prompt README link consistency, Magical Prompt Improver localization markers, old public repository references, empty files, common secret patterns and localization review markers. It does not currently validate external URLs.

## Maintenance Rules

| Rule | Why it matters |
|---|---|
| Keep GitHub templates short, specific and action-oriented. | Contributors should know what to submit without reading duplicated long-form guidance. |
| Keep project guidance in [`README.md`](../README.md), [`docs/`](../docs/) or [`templates/`](../templates/). | The public documentation stays discoverable and maintainable. |
| Do not commit progress, session, handover or completion notes. | The repository stays reusable instead of exposing internal work history. |
| Do not add secrets, private URLs, personal data or internal operational details. | Public docs remain safe to publish and copy. |
| Update workflow documentation when validation behavior changes. | CI, local checks and docs stay aligned. |

## Scope Boundary

This folder is maintenance infrastructure for this repository. It is not part of the target-repository `docs/ai/` template that users copy into their own projects.
