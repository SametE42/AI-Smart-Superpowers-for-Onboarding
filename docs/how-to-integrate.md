# How To Integrate

This guide explains how to add AI Smart Superpowers for Onboarding to a target repository.

Use the installer when you want repeatable output, language selection, backups and a manifest. Use manual integration when a repository needs careful review before any generated files are written.

## Manual Integration

1. Choose an integration mode: Minimal, Standard or Enterprise.
2. Copy the matching files from `templates/docs-ai/` into the target knowledge-base directory.
3. Copy only the Tool entrypoints the target repository actually uses.
4. Keep entrypoints short and point them to `docs/ai/CONTEXT_INDEX.md` or the localized equivalent.
5. Review every generated or copied file before treating it as trusted context.

Manual integration is best for sensitive repositories, unusual folder layouts or first-time adoption.

## Installer Integration

Use `scripts/install_ai_onboarding.py` for repeatable setup:

```bash
python scripts/install_ai_onboarding.py --mode standard --language en --structure canonical --target ../target-repo --manifest
```

Important options:

| Option | Purpose |
|---|---|
| `--mode minimal|standard|enterprise` | Select the output size. |
| `--language <code>` | Select any supported language from `i18n/language-support.yml`. |
| `--structure canonical|localized` | Choose English standard filenames or File-Map filenames. |
| `--stack <stack>` | Record an explicit stack hint. |
| `--detect-stack` | Detect conservative stack hints from target files. |
| `--dry-run` | Show planned files without writing. |
| `--force` | Overwrite existing files. |
| `--backup-existing` | Create backups before overwrites. |
| `--manifest` | Generate `AI_ONBOARDING_MANIFEST.yml` or localized manifest. |

## Modes

Minimal is for small projects or quick orientation. It includes the core entrypoint and essential docs.

Standard is the recommended default. It adds stack, dependency, evidence, decisions, review and freshness context.

Enterprise is for larger, regulated, security-sensitive or multi-agent repositories. It adds runtime, agent roles, safety boundaries and human-review gates.

## Language And Structure

Canonical mode uses `docs/ai/` and English standard filenames for the knowledge base. Content still records the selected language.

Localized mode uses the selected language File-Map. German uses `docs/ki/`; other languages use their own `docs_directory` from `i18n/file-map.<code>.yml`.

All supported languages are listed in `i18n/language-support.yml` and summarized in `docs/language-support-report.md`. Use `--list-languages` to see all supported languages before choosing `--language`.

## Stack Selection

Use `--stack` when the stack is already known. Use `--detect-stack` when the installer should inspect files such as `package.json`, `tsconfig.json`, `pyproject.toml`, `go.mod`, `Cargo.toml` or Terraform files.

Stack detection is only a hint. Detected evidence is documented in `EVIDENCE_MAP.md` or the localized equivalent.

## Tool Entrypoints

Tool entrypoints live in `templates/tool-entrypoints/`.

Copy only the entrypoints the target repository needs:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.github/copilot-instructions.md`
- Cursor, Cline, Aider or OpenCode notes where the tool is actually used

Do not copy the full knowledge base into tool-specific files.

## After Installation

1. Read the output summary table.
2. Review `AGENTS.md`.
3. Review `docs/ai/CONTEXT_INDEX.md` or the localized equivalent.
4. Check `SECURITY_RULES.md` and `REVIEW_CHECKLIST.md`.
5. Confirm stack hints in `EVIDENCE_MAP.md`.
6. Review the manifest.
7. Run repository-specific tests or validation.

## What Not To Overwrite

Do not overwrite existing `AGENTS.md`, human-reviewed AI docs, security rules, project decisions or production guidance without review.

Use `--dry-run` first. Use `--backup-existing` with `--force` only after reviewing conflicts.

## Backups And Manifest

Backups preserve overwritten files with timestamp suffixes.

The manifest records mode, language, structure, stack hint, used File-Map, generated files and actions. It helps future migrations between canonical and localized structures.
