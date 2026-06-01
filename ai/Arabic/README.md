# AI Agent Operating Manual

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> لغة المصدر: الإنجليزية
> ملف المصدر: ai/English/README.md
> عند وجود تعارض، يكون الملف الإنجليزي هو المرجع.

## Purpose of this language folder

تشرح هذه الصفحة كيف يندرج `README.md` ضمن AI Agent Operating Manual. وهي موجهة إلى الأشخاص ووكلاء الذكاء الاصطناعي الذين يحتاجون إلى تخطيط عمل المستودع أو التحقق منه أو تكراره. This language folder contains the localized AI Agent Operating Manual and mirrors the English folder structure for onboarding, review, prompts, safety, tools, models and templates.

## English source of truth

عند وجود تعارض، يكون الملف الإنجليزي هو المرجع. The English source [`ai/English/README.md`](../English/README.md) remains authoritative, and localized files mirror the English structure.

## How to use this folder

استخدم هذه الصفحة كإرشاد تشغيلي لموضوع `language folder`. لا تحل محل أدلة المستودع أو تعليمات المشروع الخاصة. Use this folder to load the language-specific entrypoint before reading safety guidance, agent patterns, context engineering notes, prompt templates, tool guidance and reusable templates.

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
