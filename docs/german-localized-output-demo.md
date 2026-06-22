# German Localized Output Demo

This demo shows German localized file paths while keeping the review status honest.

German localized output is functionally supported. Its language quality remains pending linguistic review until a qualified human review is documented in the language metadata.

## Dry Run

```bash
python scripts/install_ai_onboarding.py \
  --mode standard \
  --language de \
  --structure localized \
  --target ../target-repo \
  --dry-run
```

## Expected Structure

```text
AGENTS.md
docs/ki/
├─ KONTEXT_INDEX.md
├─ SYSTEMREGELN.md
├─ EINARBEITUNG.md
├─ ARCHITEKTUR.md
├─ TECHNOLOGIE_STACK.md
├─ BUILD_UND_TESTS.md
├─ NACHWEISUEBERSICHT.md
├─ SICHERHEITSREGELN.md
└─ PRUEFCHECKLISTE.md
```

## Review Rule

Do not change `de` to `reviewed` unless the German README, core terminology, standard output filenames, commands, paths and Markdown rendering have been checked by a qualified human reviewer.
