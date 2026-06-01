# AGENTS.md

This repository uses mandatory continuity mode.

Before any task:

1. Read `PROJECT_STATE.md`.
2. Use `PROJECT_STATE.md` as the continuity source for current state, decisions, risks, open tasks and next step.
3. Update `PROJECT_STATE.md` before handover or final response.
4. Do not document secrets, passwords, tokens, certificates or real user data.

`PROJECT_MEMORY.md` files under `templates/` describe the generated target-repository documentation standard. They do not replace this repository's root `PROJECT_STATE.md`.

Run relevant verification before claiming completion:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```
