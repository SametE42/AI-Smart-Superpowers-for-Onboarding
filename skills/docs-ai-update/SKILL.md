---
name: docs-ai-update
description: Update durable AI documentation after approved repository changes while keeping localized structures consistent.
---

# Docs AI Update

Purpose: update the AI knowledge base after approved repository changes.

Use only after changes are approved or clearly ready to document as durable repository knowledge.

Steps:

1. Identify approved repository changes that affect durable AI context.
2. Update only relevant files in `docs/ai/` or the localized equivalent.
3. Update `TECH_STACK.md`, `BUILD_AND_TEST.md`, `DEPENDENCIES.md` or `RUNTIME_ENVIRONMENT.md` when stack, build, tests, dependencies or runtime changed.
4. Update `FRESHNESS.md` or the localized equivalent for review cadence.
5. Update `DECISIONS.md` or the localized equivalent when a durable decision changed.
6. Update `EVIDENCE_MAP.md` or the localized equivalent with evidence and confidence.
7. Keep localized file structures consistent with the selected File-Map.
8. Keine temporaeren Sitzungsnotizen als Projektwissen speichern.

Safety:

- Do not overwrite human-reviewed documentation with unreviewed assumptions.
- Do not document secrets or real user data.
- Do not invent undocumented behavior.
