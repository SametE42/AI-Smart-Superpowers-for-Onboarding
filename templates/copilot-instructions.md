# GitHub Copilot Instructions

This file is intended to be copied to:

```text
.github/copilot-instructions.md
```

## Project context

The full AI documentation lives in:

```text
docs/ai/
```

Use these documents as the primary source of truth:

- `docs/ai/MASTER_SYSTEM.md`
- `docs/ai/ARCHITECTURE.md`
- `docs/ai/STYLE_GUIDE.md`
- `docs/ai/REVIEW_CHECKLIST.md`
- `docs/ai/ONBOARDING.md`

## Rules

- Follow existing code style and architecture.
- Do not invent business logic.
- Do not add dependencies without review.
- Do not expose secrets or private data.
- Keep suggestions minimal and project-specific.
- Prefer existing patterns over new abstractions.
- Include tests or verification steps for meaningful changes.
