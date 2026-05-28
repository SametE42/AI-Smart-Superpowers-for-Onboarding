# Skills and Subagents

This project does not require skills, subagents, hooks, MCP servers or plugins by default.

Use this folder only for optional task-specific workflows that are:

- repeatable,
- safe to run,
- clearly scoped,
- documented with inputs and outputs,
- explicit about permissions,
- verifiable.

## When to create a skill

Create a skill only if:

- the same workflow is repeated often,
- normal documentation is not enough,
- the workflow has clear steps,
- the workflow has clear success criteria,
- the workflow has clear safety limits.

## Do not create a skill for

- generic best practices,
- one-off tasks,
- broad coding style preferences,
- vague productivity improvements,
- workflows that require secrets,
- workflows that can make destructive changes without review.

## Required structure

Each skill or subagent workflow should document:

- purpose,
- inputs,
- outputs,
- allowed actions,
- forbidden actions,
- verification steps,
- risks,
- human review requirements.

`/docs/ai/` remains the source of truth.
