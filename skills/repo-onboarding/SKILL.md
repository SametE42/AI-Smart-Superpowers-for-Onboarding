---
name: repo-onboarding
description: Use before working in an unfamiliar repository to create or update reviewed docs/ai context from repository evidence.
---

# Repo Onboarding

Purpose: prepare a repository knowledge base before planning, coding, testing or reviewing changes.

Use when the repository is unfamiliar or the current `docs/ai/` or localized knowledge base is missing, stale or incomplete.

Steps:

1. Inspect Repository evidence first: files, tests, configuration, docs and existing entrypoints.
2. Identify Programmiersprachen, frameworks, package managers, build systems and test commands only when evidence supports them.
3. Identify architecture, constraints, risks, assumptions and unknowns.
4. Create or update `docs/ai/` or the localized knowledge base selected by the File-Map.
5. Document evidence sources and confidence in `EVIDENCE_MAP.md` or the localized equivalent.
6. Mark assumptions explicitly and keep unknowns visible.
7. Require Human Review before generated documentation is treated as trusted context.

Safety:

- Do not document secrets, real user data or private operational details.
- Do not claim production readiness without evidence.
- Do not invent undocumented behavior.
- Keep tool entrypoints short and point them to the knowledge base.
