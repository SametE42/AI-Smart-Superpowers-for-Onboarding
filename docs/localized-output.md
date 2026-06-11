# Localized Output

Localized output lets the installer generate AI onboarding files in a selected language while keeping tool compatibility explicit.

The source of truth for supported languages is `i18n/language-support.yml`. Per-language output paths and filenames come from `i18n/file-map.<code>.yml`. The generated language report is `docs/language-support-report.md`.

## Structure Modes

`canonical` structure keeps the standard English file and folder names. Content is generated for the selected language target, but files stay under `docs/ai/`.

Example German canonical output:

```text
AGENTS.md
docs/ai/CONTEXT_INDEX.md
docs/ai/MASTER_SYSTEM.md
docs/ai/ARCHITECTURE.md
docs/ai/TECH_STACK.md
docs/ai/EVIDENCE_MAP.md
docs/ai/AI_ONBOARDING_MANIFEST.yml
```

`localized` structure uses the selected language file map. German uses `docs/ki/` and German ASCII-safe filenames.

Example German localized output:

```text
AGENTS.md
docs/ki/KONTEXT_INDEX.md
docs/ki/SYSTEMREGELN.md
docs/ki/ARCHITEKTUR.md
docs/ki/TECHNOLOGIE_STACK.md
docs/ki/NACHWEISUEBERSICHT.md
docs/ki/KI_ONBOARDING_MANIFEST.yml
```

Other languages also support localized structure. When a language has not received human-reviewed localized filenames, its file map may use stable ASCII-safe names such as `FR_CONTEXT_INDEX.md`. This is functional support, not a claim of human-reviewed translation quality.

## Why AGENTS.md Stays Untranslated

`AGENTS.md` remains the default entrypoint filename because many AI coding tools look for that exact file. Its content may point to localized folders, but the filename stays stable unless a future compatibility decision changes the standard.

## When To Use Each Mode

Use `canonical` when tool compatibility, searchability and cross-team consistency matter most. English standard filenames are easier for many agents, IDEs, validators and documentation workflows to discover.

Use `localized` when target-repository readers expect localized documentation paths, or when repository policy favors language-specific filenames. Review localized filenames carefully before relying on them in automation.

Use `--no-localized-filenames` with `--structure localized` when you want the localized docs directory but still want canonical filenames.

## Installer Examples

```bash
python scripts/install_ai_onboarding.py --mode standard --language de --structure canonical
python scripts/install_ai_onboarding.py --mode standard --language de --structure localized
python scripts/install_ai_onboarding.py --mode standard --language <any-supported-language-code> --structure localized
```

List supported languages:

```bash
python scripts/install_ai_onboarding.py --list-languages
```

The language table includes Sprachcode, Sprachname, output support, translation review status and docs directory.

## Stack Hints

`--stack` records an explicit stack hint such as `typescript`, `python`, `java`, `go`, `rust`, `iac` or `docs`.

`--detect-stack` scans target-repository files and records a conservative hint. Examples:

| Evidence | Hint |
|---|---|
| `package.json` | `javascript` |
| `tsconfig.json` | `typescript` |
| `pyproject.toml`, `requirements.txt`, `setup.py` | `python` |
| `pom.xml`, `build.gradle` | `java` |
| `.csproj`, `.sln` | `csharp` |
| `go.mod` | `go` |
| `Cargo.toml` | `rust` |
| `composer.json` | `php` |
| `Gemfile` | `ruby` |
| `Package.swift` | `swift` |
| `CMakeLists.txt`, `Makefile` | `cpp` |
| `*.tf`, `terraform/` | `iac` |

Detection is only a hint. If evidence is ambiguous or missing, the installer uses `generic`. Detected stack evidence is written to `EVIDENCE_MAP.md` or the localized equivalent.

## Output Manifest

`--manifest` writes an output manifest beside the generated docs. Standard and enterprise installations also generate a manifest by default.

The manifest records:

- selected mode;
- selected language;
- structure mode;
- docs directory;
- `AGENTS.md` preservation;
- translation review status;
- stack hint and evidence;
- generated file actions.

The manifest supports later migration, auditing and comparison between canonical and localized structures.

## Migrations

To migrate from canonical to localized structure, run a dry run first and compare the planned paths:

```bash
python scripts/install_ai_onboarding.py --mode standard --language de --structure localized --dry-run
```

Then install with `--backup-existing` and `--force` only after reviewing conflicts:

```bash
python scripts/install_ai_onboarding.py --mode standard --language de --structure localized --backup-existing --force
```

For broader migration guidance, see `docs/migration-guide.md`.

## Adding Languages

Add new languages through mappings rather than installer code:

1. Add or refresh the language evidence under `ai/`.
2. Add the language to `i18n/language-support.yml`.
3. Add `i18n/file-map.<code>.yml`.
4. Set `output_support`, `translation_review_status`, `canonical_structure` and `localized_structure`.
5. Run `python scripts/check_language_support.py --root .`.

The installer reads those files at runtime, so new languages become selectable when the metadata validates.

## Risks Of Localized Filenames

Localized filenames can make repositories easier for local teams to read, but they can reduce compatibility with tools that expect English names, ASCII paths, fixed prompt-entrypoint names or simple path matching. RTL scripts, Unicode normalization and shell quoting can also create avoidable friction.

For this reason, canonical structure is usually the safest default for mixed-tool AI workflows. Localized structure is best when the repository team has reviewed the file map and accepts the tooling tradeoffs.
