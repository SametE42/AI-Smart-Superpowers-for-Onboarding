# Migration Guide

This guide describes planned migration paths for repositories adopting AI Smart Superpowers for Onboarding. It is guidance, not an installer guarantee.

## Old `docs/ai/` To Modular Structure

Start by inventorying existing AI documentation. Preserve useful project-specific evidence, assumptions, decisions, build/test commands and safety rules. Move reusable context into the closest canonical template file instead of creating duplicate long-form files.

## Canonical To Localized

For canonical to localized migration:

1. Select the target language.
2. Load the language file map.
3. Keep `AGENTS.md` unchanged unless a human explicitly accepts tool compatibility risk.
4. Move or copy canonical files into the localized docs directory.
5. Rename files only according to the file map.
6. Create or update the Output Manifest.
7. Run localized-output validation.

## Localized To Canonical

For localized to canonical migration:

1. Load the same file map in reverse.
2. Map localized filenames back to canonical names.
3. Preserve localized content where it is still useful.
4. Record unknown or conflicting mappings.
5. Update the Output Manifest to show migrated, skipped and conflicting files.

## Existing `AGENTS.md`

Do not overwrite an existing `AGENTS.md` without review. Prefer to keep it short and add links to `docs/ai/CONTEXT_INDEX.md` or the localized equivalent.

## Existing AI Documents

Existing AI documents may contain repository-specific evidence that should not be lost. If the installer later supports backup behavior, use it before overwrite operations. Without an installer, copy manually and review diffs.

## Multiple Languages

Multiple language outputs should be treated as peer structures. English may remain the canonical reference, but localized output should not permanently fall back to English filenames unless the file map documents that choice.

## Tool Entrypoints

Tool entrypoints such as `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` and `.cursor/rules/ai-onboarding.md` should stay short. They should point to the knowledge base instead of duplicating it.

## Conflict Cases

Common conflicts include existing files with different meanings, missing file-map entries, filename collisions, stale translated content and unclear review status. Mark unresolved items as unknown and require human review before destructive changes.

## Backup Strategy

Before migration, copy existing AI documentation to a backup location outside the generated output path or use the future `--backup-existing` installer option. Do not store secrets or private user data in migration notes.

## Output Manifest

The Output Manifest should record installation mode, language, structure mode, file map, generated files, skipped files, overwritten files, warnings and translation review status. It is the audit trail for migration decisions.

