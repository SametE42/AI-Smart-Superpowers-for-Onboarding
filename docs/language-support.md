# Language Support

This repository currently contains 75 language folders under `ai/`. The current evidence is `ai/LANGUAGE_INDEX.md`, `ai/TRANSLATION_STATUS.md`, `i18n/language-support.yml`, `i18n/file-map.*.yml` and the directory structure under `ai/`.

The current functional target state is complete for all detected languages: every existing language is documented, file-mapped, validated and marked for both canonical structure and localized structure output. No language should be treated as a permanent lower-quality fallback.

## Machine-Readable Sources

| File | Purpose |
|---|---|
| `i18n/language-support.yml` | Matrix of all detected language codes, source folders, output support, review status, file maps and docs directories. |
| `i18n/file-map.<code>.yml` | Per-language mapping from canonical `docs/ai/` filenames to localized target filenames. |
| `i18n/file-map.schema.yml` | Required fields, allowed review values and filename rules for file maps. |
| `i18n/glossary.yml` | Cross-language terminology inventory with review notes. |
| `docs/language-support-report.md` | Generated summary report from current language support metadata. |
| `scripts/check_language_support.py` | Validator for the matrix and all file maps. |
| `scripts/generate_language_support_report.py` | Report generator for language support status. |

## Current Language Inventory

| Code | Language | Current evidence |
|---|---|---|
| af | Afrikaans | `ai/Afrikaans/` |
| sq | Albanian | `ai/Albanian/` |
| am | Amharic | `ai/Amharic/` |
| ar | Arabic | `ai/Arabic/` |
| hy | Armenian | `ai/Armenian/` |
| az | Azerbaijani | `ai/Azerbaijani/` |
| eu | Basque | `ai/Basque/` |
| bn | Bengali | `ai/Bengali/` |
| bs | Bosnian | `ai/Bosnian/` |
| bg | Bulgarian | `ai/Bulgarian/` |
| my | Burmese | `ai/Burmese/` |
| ca | Catalan | `ai/Catalan/` |
| zh | Chinese | `ai/Chinese/` |
| hr | Croatian | `ai/Croatian/` |
| cs | Czech | `ai/Czech/` |
| da | Danish | `ai/Danish/` |
| nl | Dutch | `ai/Dutch/` |
| en | English | `ai/English/` |
| et | Estonian | `ai/Estonian/` |
| fi | Finnish | `ai/Finnish/` |
| fr | French | `ai/French/` |
| ka | Georgian | `ai/Georgian/` |
| de | German | `ai/German/`, `i18n/de/` |
| el | Greek | `ai/Greek/` |
| gu | Gujarati | `ai/Gujarati/` |
| ha | Hausa | `ai/Hausa/` |
| he | Hebrew | `ai/Hebrew/` |
| hi | Hindi | `ai/Hindi/` |
| hu | Hungarian | `ai/Hungarian/` |
| is | Icelandic | `ai/Icelandic/` |
| id | Indonesian | `ai/Indonesian/` |
| ga | Irish | `ai/Irish/` |
| it | Italian | `ai/Italian/` |
| ja | Japanese | `ai/Japanese/` |
| kn | Kannada | `ai/Kannada/` |
| kk | Kazakh | `ai/Kazakh/` |
| km | Khmer | `ai/Khmer/` |
| ko | Korean | `ai/Korean/` |
| ku | Kurdish | `ai/Kurdish/` |
| lo | Lao | `ai/Lao/` |
| lv | Latvian | `ai/Latvian/` |
| lt | Lithuanian | `ai/Lithuanian/` |
| mk | Macedonian | `ai/Macedonian/` |
| ms | Malay | `ai/Malay/` |
| ml | Malayalam | `ai/Malayalam/` |
| mr | Marathi | `ai/Marathi/` |
| mn | Mongolian | `ai/Mongolian/` |
| ne | Nepali | `ai/Nepali/` |
| no | Norwegian | `ai/Norwegian/` |
| ps | Pashto | `ai/Pashto/` |
| fa | Persian | `ai/Persian/` |
| pl | Polish | `ai/Polish/` |
| pt | Portuguese | `ai/Portuguese/` |
| pa | Punjabi | `ai/Punjabi/` |
| ro | Romanian | `ai/Romanian/` |
| ru | Russian | `ai/Russian/` |
| sr | Serbian | `ai/Serbian/` |
| si | Sinhala | `ai/Sinhala/` |
| sk | Slovak | `ai/Slovak/` |
| sl | Slovenian | `ai/Slovenian/` |
| so | Somali | `ai/Somali/` |
| es | Spanish | `ai/Spanish/` |
| sw | Swahili | `ai/Swahili/` |
| sv | Swedish | `ai/Swedish/` |
| tl | Tagalog | `ai/Tagalog/` |
| ta | Tamil | `ai/Tamil/` |
| te | Telugu | `ai/Telugu/` |
| th | Thai | `ai/Thai/` |
| ti | Tigrinya | `ai/Tigrinya/` |
| tr | Turkish | `ai/Turkish/` |
| uk | Ukrainian | `ai/Ukrainian/` |
| ur | Urdu | `ai/Urdu/` |
| uz | Uzbek | `ai/Uzbek/` |
| vi | Vietnamese | `ai/Vietnamese/` |
| zu | Zulu | `ai/Zulu/` |

## Structure Modes

`canonical structure` means the target repository uses canonical English paths and filenames such as `docs/ai/ARCHITECTURE.md`, even when content or guidance may be language-aware.

`localized structure` means the target repository uses language-specific documentation folders and filenames defined by a file map. For example, German may use a localized docs directory and localized Markdown filenames.

`AGENTS.md` is not localized by default because many AI coding tools look for that exact entrypoint filename.

## File Maps

File maps live under `i18n/file-map.<language>.yml`. A file map declares the language, docs directory, `AGENTS.md` entrypoint, localization review status and the mapping from canonical filenames to localized filenames.

File maps should be maintained as source-controlled evidence. Localized filenames must not be guessed at install time.

English maps canonical filenames to themselves. German has a localized example such as `KONTEXT_INDEX.md` and `SYSTEMREGELN.md`, but its language quality remains pending linguistic review until human review is documented. Other non-English languages currently use stable ASCII-safe, language-code-prefixed filenames, for example `FR_CONTEXT_INDEX.md`, to provide complete functional localized structure without pretending that linguistic filename review has happened.

## Adding A Language

To add a language, maintainers should:

1. Add the language folder under `ai/` only when source material exists.
2. Add the language to `ai/LANGUAGE_INDEX.md` and `ai/TRANSLATION_STATUS.md`.
3. Add an entry to `i18n/language-support.yml`.
4. Add `i18n/file-map.<language>.yml`.
5. Document whether language quality is human-reviewed, pending linguistic review or unknown.
6. Run language-support validation and repository validation.

## Localization Review Status

`translation_review_status` tracks language quality separately from functional support. Public docs and reports should describe automated or draft language states as `pending linguistic review`, while the machine-readable source remains in the language metadata.

The current non-English language mirrors have complete structural coverage according to `ai/TRANSLATION_STATUS.md`; they should not be described as human-reviewed unless a human review is documented. Their machine-readable review state remains tracked in the current matrix.

## Filename Validation

Localized filenames should be validated for empty names, duplicate targets, path separators, missing `.md` extensions, invisible characters and reserved platform names. RTL languages such as Arabic, Hebrew, Persian, Pashto and Urdu may use documented ASCII-safe filenames when that is safer for tooling.

## Validation

Run:

```bash
python scripts/check_language_support.py --root .
python scripts/generate_language_support_report.py --root .
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```

The language-support validator checks every detected language folder, every support entry, every file map, required canonical keys, duplicate target filenames, `AGENTS.md` preservation, review status values and localized/canonical structure flags.

## Updating Translations

Update English source first. Reuse existing translations where possible. When translation quality changes, update language metadata and keep the status honest.
