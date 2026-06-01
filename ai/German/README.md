# AI Agent Operating Manual

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> Source language: English
> Source file: ai/English/README.md
> Bei Abweichungen ist die englische Datei maßgeblich.

## Purpose of this language folder

Dieser Sprachordner enthält das deutsch lokalisierte AI Agent Operating Manual. Er erklärt die Standardordner und hilft Menschen sowie KI-Agenten bei Onboarding, Review, Prompts, Safety, Tools, Modellen und wiederverwendbaren Templates.

## English source of truth

Die englische Quelle [`ai/English/README.md`](../English/README.md) ist maßgeblich. Die deutsche Fassung spiegelt die englische Struktur und bewahrt Pfade, Dateinamen, Commands, APIs und Modellnamen.

## How to use this folder

Nutze diesen Ordner als deutschsprachigen Einstieg in die Betriebsanleitung. Lade zuerst Safety, Agentenrollen, Kontextregeln, Prompt-Muster, Tool-Hinweise und Templates, bevor du projektspezifische Schlüsse ziehst.

## Folder overview

| Folder | Purpose |
|---|---|
| `agents/` | Agent patterns and operating models. |
| `commands/` | Command usage and CLI workflows. |
| `context-engineering/` | Context loading, pruning, retrieval and handoff. |
| `evals/` | Evaluation, benchmark and regression testing guidance. |
| `examples/` | Practical workflow examples. |
| `memory/` | Memory models, schemas and safety rules. |
| `models/` | Model-family specific notes. |
| `optimization/` | Prompt, workflow and skill optimization. |
| `prompts/` | Prompt templates and review prompts. |
| `providers/` | Provider-specific documentation. |
| `safety/` | Safety, privacy, approval and prompt-injection rules. |
| `skills/` | Skill design, lifecycle and transfer guidance. |
| `templates/` | Reusable templates. |
| `tools/` | Tool-specific guidance. |

## Recommended reading order

1. `README.md`
2. `safety/README.md`
3. `agents/README.md`
4. `context-engineering/README.md`
5. `prompts/README.md`
6. `tools/README.md`
7. `templates/README.md`

## Safety and human review rules

- Repository evidence is authoritative.
- Do not invent commands, model capabilities or provider behavior.
- Preserve file names, commands, API names and model names.
- Mark assumptions and unknowns.
- Escalate security, permissions and production-readiness risks to human review.

## Localization notes

- File names, folder names, commands, APIs and model names stay unchanged.
- Localized prose may be translated naturally.
- English wins when localized content conflicts with English.

## Quality checklist

- [ ] Purpose is clear.
- [ ] Folder overview is complete.
- [ ] All standard subfolders are listed.
- [ ] Safety boundaries are visible.
- [ ] No unsupported model/tool claims are added.
- [ ] English remains authoritative.
