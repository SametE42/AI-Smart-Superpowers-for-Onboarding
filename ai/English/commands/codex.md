# Codex Command Reference

Codex commands are runtime commands. They are not general OpenAI model commands.

## Recommended commands to document

- `/help` — inspect available commands in the current version.
- `/status` — review current session state when available.
- `/model` — switch model when the runtime supports it.
- `/plan` — ask for an implementation plan before edits.
- `/goal` — persist a clear objective across a longer task when available.
- `/mention` — reference files or folders when supported.
- `/fast` — use a faster interaction mode when supported.

## Recommended workflow

1. Check status and available commands.
2. Mention the files or folders that matter.
3. Use plan mode before broad edits.
4. Use goal mode only after the desired end state is clear.
5. Review diffs, tests and documentation before merging.

## Documentation rule

Always verify the exact command list against the installed Codex version or official documentation because slash commands can change over time.
