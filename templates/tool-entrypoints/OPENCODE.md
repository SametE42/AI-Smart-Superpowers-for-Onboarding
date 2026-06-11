# OPENCODE.md

Use this short entrypoint for OpenCode-style coding-agent sessions.

Start with `docs/ai/CONTEXT_INDEX.md`. For localized structures, use the localized equivalent such as `docs/ki/KONTEXT_INDEX.md` or the path from the selected File-Map.

Load only task-relevant files:

- `TECH_STACK.md`, `BUILD_AND_TEST.md`, `DEPENDENCIES.md` and `RUNTIME_ENVIRONMENT.md` for stack, build, test, dependency or runtime questions.
- `SECURITY_RULES.md` before security, secrets, auth, permissions, production or data-handling changes.
- `REVIEW_CHECKLIST.md` before final output.
- `PROJECT_MEMORY.md` and `DECISIONS.md` only for durable changes.

Repository evidence wins over stale documentation. Mark assumptions and unknowns. Do not invent undocumented behavior. This template is tool-neutral and does not claim vendor support.
