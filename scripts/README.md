# Scripts

Repository maintenance scripts live here.

## Available scripts

- `validate_repository.py` checks release-readiness invariants for Markdown structure, local Markdown links, local HTML links, local heading anchors, mirrored AI language files, empty files, README coverage, language README completeness, optional template README coverage, old public repository references, common secret patterns and localization review markers.
- `install_ai_onboarding.py` installs AI onboarding files into a target repository with selectable mode, language, canonical or localized structure, stack hints, dry-run output, overwrite protection, backups and output manifests.
- `check_context_budget.py` warns about oversized, repetitive or duplicated AI documentation.
- `check_evidence_map.py` validates evidence-map table columns, confidence values and high-confidence evidence sources.
- `check_stale_docs.py` validates freshness tables and reports stale or needs-review files.
- `check_tool_entrypoints.py` validates short tool-entrypoint templates.
- `check_localized_output.py` validates localized-output mappings across all supported languages.
- `check_file_map_schema.py` validates file-map schema fields and target filename rules.
- `check_stack_context.py` validates stack-context files in modes, templates and localized mappings.
- `generate_docs_ai_index.py` generates `templates/docs-ai/INDEX.md`.
- `refresh_ai_manual.py` replaces scaffold or mirror-placeholder AI manual pages with practical source content or localized mirror pages. Use `--languages` to target specific language directories, for example `python scripts/refresh_ai_manual.py --root . --languages French Spanish Turkish Arabic`.
- `check_language_support.py` validates `i18n/language-support.yml`, all `i18n/file-map.<code>.yml` files, required canonical keys, review status values, `AGENTS.md` preservation and duplicate localized filenames.
- `check_standard_docs.py` validates `config/standard-docs.yml` against installer modes, language file-map requirements and referenced templates.
- `generate_language_support_report.py` generates `docs/language-support-report.md` from the current language-support matrix and file maps.
