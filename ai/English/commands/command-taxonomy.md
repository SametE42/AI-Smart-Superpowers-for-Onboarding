# Command Taxonomy

Command systems, slash commands, file references and repeatable workflow commands.

## Practical Scope

This page explains how `commands/command-taxonomy.md` fits into the AI Agent Operating Manual. Use it when an agent or maintainer needs repeatable guidance for this topic without loading the entire repository.

## Operating Guidance

- Treat repository evidence as authoritative and documentation as secondary.
- Preserve file names, commands, API names and model names exactly.
- Mark unverified conclusions as `[ASSUMPTION: ...]` and unknown facts as `[UNKNOWN]`.
- Keep tool-specific behavior tied to the runtime that actually owns it.
- Escalate security, permission and production-readiness risks to human review.

## Focus

Separate model capabilities from host-tool commands and document only commands the runtime owns.


## Quality Checklist

- The purpose is clear to a new repository user.
- The guidance is useful for both AI agents and human maintainers.
- No model-specific commands are invented unless they belong to the host tool.
- Safety and human-approval boundaries remain visible.
- English remains the authoritative source for localization.
