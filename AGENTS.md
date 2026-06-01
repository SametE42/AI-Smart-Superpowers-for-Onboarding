# AGENTS.md

This repository contains the AI Repo Onboarding Standard.

Before changing files:

1. Read `README.md` and the relevant files under `docs/`, `templates/`, `scripts/` or `tests/`.
2. Keep repository-specific progress notes out of committed files.
3. Do not document secrets, passwords, tokens, certificates or real user data.

`PROJECT_MEMORY.md` files under `templates/` describe the generated target-repository documentation standard and must stay as reusable templates.

Run relevant verification before claiming completion:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```
