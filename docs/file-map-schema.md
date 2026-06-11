# File Map Schema

File maps define how canonical AI knowledge-base filenames map to localized output filenames. They are YAML files under `i18n/file-map.<language>.yml`.

## Required Fields

Each file map should include:

```yaml
schema_version: 1
language: de
language_name: German
source_folder: ai/German
docs_directory: docs/ki
agents_filename: AGENTS.md
translation_review_status: machine_generated
canonical_structure: true
localized_structure: true
files:
  CONTEXT_INDEX.md: KONTEXT_INDEX.md
review_notes:
  - German localized filenames require linguistic review before reviewed status.
```

Required keys:

- `schema_version`
- `language`
- `language_name`
- `docs_directory`
- `agents_filename`
- `translation_review_status`
- `files`

Recommended keys:

- `source_folder`
- `canonical_structure`
- `localized_structure`
- `review_notes`

## Allowed Review Values

`translation_review_status` should be one of:

- `reviewed`
- `needs_review`
- `machine_generated`
- `unknown`

## Canonical Keys

The keys under `files` should be canonical Markdown filenames from the generated `docs/ai/` knowledge base. Phase 4 requires all 21 canonical template filenames, from `CONTEXT_INDEX.md` through `HUMAN_REVIEW_GATES.md`.

## Filename Rules

Localized Markdown filenames must:

- be non-empty;
- end with `.md`;
- not contain path separators;
- not have leading or trailing spaces;
- not contain invisible Unicode characters;
- not duplicate another target filename in the same language;
- avoid reserved Windows filenames such as `CON.md`, `PRN.md`, `AUX.md`, `NUL.md`, `COM1.md` and `LPT1.md`.

`agents_filename` should remain `AGENTS.md` by default.

## Docs Directory Rules

`docs_directory` may contain a path such as `docs/ai` or `docs/ki`. It is the only place where a path separator is expected. Individual mapped filenames should not contain directories.

## Validation Rules

Validators should parse every file map, check required fields, verify allowed status values, reject duplicate target filenames and ensure every required canonical file has a mapping.

The repository validator for this layer is:

```bash
python scripts/check_language_support.py --root .
```

Regenerate the human-readable report with:

```bash
python scripts/generate_language_support_report.py --root .
```

## Example

```yaml
schema_version: 1
language: en
language_name: English
source_folder: ai/English
docs_directory: docs/ai
agents_filename: AGENTS.md
translation_review_status: reviewed
canonical_structure: true
localized_structure: true
files:
  CONTEXT_INDEX.md: CONTEXT_INDEX.md
  MASTER_SYSTEM.md: MASTER_SYSTEM.md
  ARCHITECTURE.md: ARCHITECTURE.md
  REVIEW_CHECKLIST.md: REVIEW_CHECKLIST.md
review_notes:
  - Canonical English reference mapping.
```
