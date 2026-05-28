# Gemini CLI Command Reference

Gemini CLI supports command patterns such as slash commands, file references and shell command prefixes depending on version and configuration.

## Recommended command areas

- `/help` and session controls
- `@file` or `@folder` style context references where supported
- `!command` style shell execution where supported
- Custom slash commands for reusable prompts
- `GEMINI.md` as project context

## Empfohlener Workflow

1. Add `GEMINI.md` with project rules.
2. Reference the files required for the task.
3. Use custom commands for recurring docs, tests or review tasks.
4. Keep shell execution gated by human approval.


> Hinweis: Diese Datei ist eine deutsche lokalisierte Version. Bei Abweichungen gilt die englische Datei als maßgeblich.
