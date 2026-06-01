# Scripts

Repository maintenance scripts live here.

## Available scripts

- `validate_repository.py` checks release-readiness invariants for Markdown structure, local links, mirrored AI language files, empty files, README coverage and common secret patterns.
- `refresh_ai_manual.py` replaces scaffold or mirror-placeholder AI manual pages with practical source content or AI-translated localized pages. Use `--languages` to target specific language directories, for example `python scripts/refresh_ai_manual.py --root . --languages French Spanish Turkish Arabic`.
