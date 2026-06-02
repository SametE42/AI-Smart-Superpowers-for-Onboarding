# Tool Usage Guide

## Purpose

Explain how to use this onboarding standard with AI coding agents and IDE assistants.

## Minimal Flow

1. Open or copy [`templates/MASTER_PROMPT.en.md`](../../templates/MASTER_PROMPT.en.md).
2. Point the tool at the target repository.
3. Ask it to run repository onboarding before code changes.
4. Review the proposed `docs/ai/` plan.
5. Approve or revise the plan.
6. Use `docs/ai/` as reviewed context before future coding tasks.

## Recommended Context For Future Sessions

- `docs/ai/ONBOARDING.md`
- `docs/ai/PROJECT_MEMORY.md`
- `docs/ai/SECURITY_RULES.md`
- `docs/ai/ARCHITECTURE.md`
- `docs/ai/REVIEW_CHECKLIST.md`

## Safety Rules

- Do not start implementation before onboarding is reviewed.
- Mark unknowns as `[UNKNOWN]`.
- Mark inferences as `[ASSUMPTION: ...]`.
- Never expose secrets, credentials, certificates, private keys or sensitive data.
- Human review remains required before AI-generated documentation is trusted.

## Structured Workflow Files

Use [`agent-workflows/`](../../agent-workflows/README.md) when you want short runbooks for repository onboarding, evidence gathering, `docs/ai/` updates, pre-coding checks and handover refreshes.

## Not An Integration

This guide describes how to use the onboarding standard with AI coding tools. It does not imply official integration, endorsement or compatibility certification with any specific tool.
