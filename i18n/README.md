# Internationalization

This folder contains machine-readable localization metadata for the AI onboarding framework.

Human-readable AI manual translations still live under `ai/<Language>/`, with `ai/English/` as the source of truth.

## Files

- `language-support.yml`: complete support matrix for all detected language folders.
- `file-map.schema.yml`: schema and filename rules for file maps.
- `file-map.<code>.yml`: per-language canonical-to-localized filename mappings.
- `glossary.yml`: terminology inventory for all supported language codes.
- `de/`: legacy German localization notes retained for compatibility.

## Validation

Run:

```bash
python scripts/check_language_support.py --root .
python scripts/generate_language_support_report.py --root .
```
