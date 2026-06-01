# AI Agent Operating Manual

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> ພາສາຕົ້ນສະບັບ: ອັງກິດ
> ໄຟລ໌ຕົ້ນສະບັບ: ai/English/README.md
> ຖ້າມີຄວາມແຕກຕ່າງ ໃຫ້ຍຶດໄຟລ໌ອັງກິດ.

## Purpose of this language folder

ໜ້ານີ້ອະທິບາຍວ່າ `README.md` ເຂົ້າກັບ AI Agent Operating Manual ແນວໃດ ສໍາລັບຄົນ ແລະ AI agents ທີ່ຕ້ອງວາງແຜນ ກວດສອບ ຫຼືເຮັດຊໍ້າວຽກ repository. This language folder contains the localized AI Agent Operating Manual and mirrors the English folder structure for onboarding, review, prompts, safety, tools, models and templates.

## English source of truth

ຖ້າມີຄວາມແຕກຕ່າງ ໃຫ້ຍຶດໄຟລ໌ອັງກິດ. The English source [`ai/English/README.md`](../English/README.md) remains authoritative, and localized files mirror the English structure.

## How to use this folder

ໃຊ້ໜ້ານີ້ເປັນຄູ່ມືປະຕິບັດສໍາລັບ `language folder`. ມັນບໍ່ແທນຫຼັກຖານ repository ຫຼືຄໍາແນະນໍາໂຄງການ. Use this folder to load the language-specific entrypoint before reading safety guidance, agent patterns, context engineering notes, prompt templates, tool guidance and reusable templates.

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
