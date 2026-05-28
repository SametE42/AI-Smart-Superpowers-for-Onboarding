# Design Principles

## Evidence-first documentation

Repository facts should be grounded in code, tests, configuration or existing documentation.

Use:

- observations for directly visible facts,
- assumptions for plausible but unverified conclusions,
- unknown markers when something cannot be determined.

## Anti-bloat

Agent documentation should contain only information future agents need.

Avoid:

- generic best practices,
- repeated README content,
- long tool-specific files,
- speculative rules,
- style preferences without project impact.

## Human review

AI output is not automatically trusted.

Humans review meaningful changes before commit, merge or production use.

## Multi-model isolation

Multiple AI models may work on the same project. Documentation should support append-only updates, conflict marking and explicit human review instead of overwriting other model entries.

## Progressive context retrieval

Load context in layers:

1. index, headings or summaries,
2. relevant files or time ranges,
3. full details only for selected hits.

Avoid dumping entire repositories, changelogs or memory files into context when targeted retrieval is possible.

## Boundary documentation

AI-generated repository documentation should explicitly separate concepts that are often confused:

- technical error logging,
- functional validation,
- change history,
- export history,
- audit logging,
- security events,
- operational monitoring.

If these concepts are not implemented yet, the documentation must say so explicitly.

## Tool entrypoints as short references

Files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` or Copilot instructions should be short references.

They should point to `/docs/ai/` rather than duplicate long documentation.

## `/docs/ai/` as source of truth

When tool entrypoints and `/docs/ai/` conflict, `/docs/ai/` wins unless a human reviewer decides otherwise.
