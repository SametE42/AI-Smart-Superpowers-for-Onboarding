# AGENTS.md

This repository contains the AI Repo Onboarding Standard.

Before changing files:

1. Read `README.md` and the relevant files under `docs/`, `templates/`, `scripts/` or `tests/`.
2. Keep repository-specific progress, session, handover or completion notes out of committed files.
3. Do not document secrets, passwords, tokens, certificates or real user data.

If temporary progress documents are created while working, delete them before staging, committing or pushing. The public repository should contain the reusable onboarding standard, not internal completion notes.

`PROJECT_MEMORY.md` files under `templates/` describe the generated target-repository documentation standard and must stay as reusable templates.

Run relevant verification before claiming completion:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```
