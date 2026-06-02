# Tool Usage Guide

## Purpose

Explain how to use this tool-neutral onboarding standard with AI coding agents and IDE assistants.

This guide is not a plugin, official integration, compatibility certification or tool endorsement.

## Minimal Flow

1. Open or copy [`templates/MASTER_PROMPT.en.md`](../../templates/MASTER_PROMPT.en.md).
2. Point the tool at the target repository.
3. Ask it to run repository onboarding before making code changes.
4. Review the proposed `docs/ai/` plan.
5. Approve or revise the plan.
6. Use `docs/ai/` as reviewed context before future coding tasks.

## Recommended Context For Future Sessions

Load these files before planning or coding:

- `docs/ai/ONBOARDING.md`
- `docs/ai/PROJECT_MEMORY.md`
- `docs/ai/SECURITY_RULES.md`
- `docs/ai/ARCHITECTURE.md`
- `docs/ai/REVIEW_CHECKLIST.md`

## Safety Rules

- Do not start implementation before onboarding is reviewed.
- Mark unknowns as `[UNKNOWN]`.
- Mark inferences as `[ASSUMPTION]` or `[ASSUMPTION: ...]`.
- Never expose secrets, credentials, tokens or sensitive data.
- Human review remains required before treating AI-generated documentation as reliable.
- Use minimal sufficient context instead of loading unnecessary files.

## Structured Workflow Files

Use [`agent-workflows/`](../../agent-workflows/README.md) when you want short runbooks for repository onboarding, evidence gathering, `docs/ai/` updates, pre-coding checks and handover refreshes.

## Additional Guides

- [`tool-context-loading.md`](tool-context-loading.md) explains which `docs/ai/` files to load first by task type.
- [`human-review-gates.md`](human-review-gates.md) defines the human checkpoints before documentation, coding and memory refreshes are trusted.

## Not An Integration

This guide describes how to use the onboarding standard with AI coding tools. It does not imply official integration, endorsement, compatibility certification or plugin support for any tool.
