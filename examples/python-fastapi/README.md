# Python/FastAPI Repository Example

This example describes how to apply the AI onboarding standard to a Python FastAPI project.

## Suggested AI documentation

```text
docs/ai/
├─ MASTER_SYSTEM.md
├─ ARCHITECTURE.md
├─ PROJECT_MEMORY.md
├─ STYLE_GUIDE.md
├─ REVIEW_CHECKLIST.md
├─ SECURITY_RULES.md
└─ ONBOARDING.md
```

## Recommended focus areas

- Python version and dependency manager
- application entrypoint
- API routes and schemas
- database migrations
- test strategy
- environment variables and secrets handling
- deployment boundaries

## Example validation commands

```text
python -m venv .venv
python -m pip install -r requirements.txt
pytest
ruff check .
```

Adjust commands to the actual repository before documenting them as authoritative.
