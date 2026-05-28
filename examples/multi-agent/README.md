# Multi-Agent Workflow Example

This example shows how to split repository work across specialized AI agents while keeping a single source of truth.

## Recommended roles

- **Researcher**: reads repository files and summarizes evidence.
- **Architect**: maps structure, boundaries and integration points.
- **Writer**: creates documentation updates.
- **Reviewer**: checks links, contradictions, missing assumptions and safety issues.

## Workflow

1. Start with `templates/MASTER_PROMPT.en.md`.
2. Ask the Researcher to inspect the repository without editing files.
3. Ask the Architect to propose the documentation structure.
4. Ask the Writer to draft only approved files.
5. Ask the Reviewer to validate links, claims, commands and security boundaries.
6. Commit changes only after human review.
