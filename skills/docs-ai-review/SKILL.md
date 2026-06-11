---
name: docs-ai-review
description: Review an existing AI knowledge base against repository evidence, localization mappings and safety rules.
---

# Docs AI Review

Purpose: review an existing AI knowledge base before it is reused by coding agents.

Use when `docs/ai/` or a localized output structure exists and needs evidence, freshness, safety or localization review.

Steps:

1. Check whether the existing AI knowledge base files still match current Repository evidence.
2. Compare claims with source files, tests, configuration and docs.
3. Verify technology context in `TECH_STACK.md`, `BUILD_AND_TEST.md`, `DEPENDENCIES.md` and `RUNTIME_ENVIRONMENT.md` or their localized equivalents.
4. Check local links, file references and expected entrypoints.
5. Check Context Bloat: repeated instructions, excessive generic guidance and stale duplicated rules.
6. Review `SECURITY_RULES.md`, risk notes and human-review boundaries.
7. Mark stale, unsupported or unevidenced claims.
8. Check language and File-Map consistency when localized output is used.

Safety:

- Do not treat documentation as evidence when repository files contradict it.
- Do not claim a language translation is reviewed unless metadata proves it.
- Do not claim vendor support.
