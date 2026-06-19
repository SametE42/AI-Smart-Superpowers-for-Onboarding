# Integration Modes

The framework supports three integration modes. The same modes work in canonical and localized structure because localized filenames come from File-Maps. The machine-readable source of truth is [`../standard-docs.yml`](../standard-docs.yml).

| Modus | Fuer wen | Dateien | Aufwand | Empfehlung |
| ----- | ------- | ------- | ------- | ---------- |
| Minimal Integration | Small projects or first orientation | `AGENTS.md` plus 7 core knowledge-base files | Low | Use when a repository needs a lightweight start. |
| Standard Integration | Normal application, library or documentation repositories | `AGENTS.md` plus 17 knowledge-base files | Medium | Recommended default. |
| Enterprise Integration | Large, regulated, multi-agent or security-sensitive repositories | Tool entrypoints plus 21 knowledge-base files | Higher | Use when governance, runtime and human-review boundaries matter. |

## Minimal Integration

Canonical English:

```text
AGENTS.md
docs/ai/
├─ CONTEXT_INDEX.md
├─ MASTER_SYSTEM.md
├─ ARCHITECTURE.md
├─ BUILD_AND_TEST.md
├─ PROJECT_MEMORY.md
├─ SECURITY_RULES.md
└─ REVIEW_CHECKLIST.md
```

Localized German:

```text
AGENTS.md
docs/ki/
├─ KONTEXT_INDEX.md
├─ SYSTEMREGELN.md
├─ ARCHITEKTUR.md
├─ BUILD_UND_TESTS.md
├─ PROJEKTWISSEN.md
├─ SICHERHEITSREGELN.md
└─ PRUEFCHECKLISTE.md
```

## Standard Integration

Canonical English:

```text
AGENTS.md
docs/ai/
├─ CONTEXT_INDEX.md
├─ MASTER_SYSTEM.md
├─ ONBOARDING.md
├─ ARCHITECTURE.md
├─ TECH_STACK.md
├─ BUILD_AND_TEST.md
├─ DEPENDENCIES.md
├─ EVIDENCE_MAP.md
├─ PROJECT_MEMORY.md
├─ DECISIONS.md
├─ STYLE_GUIDE.md
├─ SECURITY_RULES.md
├─ RISK_REGISTER.md
├─ REVIEW_CHECKLIST.md
├─ ERROR_PATTERNS.md
├─ TASK_SCOPING.md
└─ FRESHNESS.md
```

Localized German:

```text
AGENTS.md
docs/ki/
├─ KONTEXT_INDEX.md
├─ SYSTEMREGELN.md
├─ EINARBEITUNG.md
├─ ARCHITEKTUR.md
├─ TECHNOLOGIE_STACK.md
├─ BUILD_UND_TESTS.md
├─ ABHAENGIGKEITEN.md
├─ NACHWEISUEBERSICHT.md
├─ PROJEKTWISSEN.md
├─ ENTSCHEIDUNGEN.md
├─ STILRICHTLINIEN.md
├─ SICHERHEITSREGELN.md
├─ RISIKOREGISTER.md
├─ PRUEFCHECKLISTE.md
├─ FEHLERMUSTER.md
├─ AUFGABENABGRENZUNG.md
└─ AKTUALITAET.md
```

## Enterprise Integration

Canonical English:

```text
AGENTS.md
CLAUDE.md
GEMINI.md
.cursor/rules/ai-onboarding.md
.github/copilot-instructions.md

docs/ai/
├─ CONTEXT_INDEX.md
├─ MASTER_SYSTEM.md
├─ ONBOARDING.md
├─ ARCHITECTURE.md
├─ TECH_STACK.md
├─ BUILD_AND_TEST.md
├─ DEPENDENCIES.md
├─ RUNTIME_ENVIRONMENT.md
├─ EVIDENCE_MAP.md
├─ PROJECT_MEMORY.md
├─ DECISIONS.md
├─ STYLE_GUIDE.md
├─ SECURITY_RULES.md
├─ RISK_REGISTER.md
├─ REVIEW_CHECKLIST.md
├─ ERROR_PATTERNS.md
├─ TASK_SCOPING.md
├─ FRESHNESS.md
├─ AGENT_ROLES.md
├─ SAFETY_BOUNDARIES.md
└─ HUMAN_REVIEW_GATES.md
```

Localized German:

```text
AGENTS.md
CLAUDE.md
GEMINI.md
.cursor/rules/ki-onboarding.md
.github/copilot-instructions.md

docs/ki/
├─ KONTEXT_INDEX.md
├─ SYSTEMREGELN.md
├─ EINARBEITUNG.md
├─ ARCHITEKTUR.md
├─ TECHNOLOGIE_STACK.md
├─ BUILD_UND_TESTS.md
├─ ABHAENGIGKEITEN.md
├─ LAUFZEITUMGEBUNG.md
├─ NACHWEISUEBERSICHT.md
├─ PROJEKTWISSEN.md
├─ ENTSCHEIDUNGEN.md
├─ STILRICHTLINIEN.md
├─ SICHERHEITSREGELN.md
├─ RISIKOREGISTER.md
├─ PRUEFCHECKLISTE.md
├─ FEHLERMUSTER.md
├─ AUFGABENABGRENZUNG.md
├─ AKTUALITAET.md
├─ AGENTENROLLEN.md
├─ SICHERHEITSGRENZEN.md
└─ MENSCHLICHE_PRUEFPUNKTE.md
```

## Other Languages

Other languages use the same mode definitions. Their localized paths come from each language File-Map in `i18n/file-map.<code>.yml`.

Canonical mode keeps English standard filenames. Localized mode uses `docs_directory` and mapped target filenames from the File-Map.

## Stack Context By Mode

| File | Minimal | Standard | Enterprise |
|---|---|---|---|
| `BUILD_AND_TEST.md` | Yes | Yes | Yes |
| `TECH_STACK.md` | No | Yes | Yes |
| `DEPENDENCIES.md` | No | Yes | Yes |
| `RUNTIME_ENVIRONMENT.md` | No | No | Yes |
