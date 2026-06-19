# Magical Prompt Improver

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> Source language: English
> Source file: ai/English/prompts/magical-prompt-improver.md
> Bei Abweichungen ist die englische Datei maßgeblich.

Nutze diese Seite, wenn eine Benutzeranfrage, ein wiederverwendbarer Prompt oder eine Agenten-Übergabe vor Repository-Arbeit präziser werden muss. Source protocol: [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

## Praktischer Scope

Der Magical Prompt Improver reduziert Mehrdeutigkeit, macht fehlenden Kontext sichtbar, setzt Sicherheitsgrenzen und definiert prüfbare Abschlusskriterien.

## Arbeitsleitlinien

- Wähle immer den leichtesten Modus, der das Risiko der Anfrage zuverlässig abdeckt.
- Bewahre Dateipfade, Commands, Modellnamen, API-Namen und Nutzergrenzen unverändert.
- Markiere unbekannte Fakten mit `[UNKNOWN]` und unbestätigte Annahmen mit `[ASSUMPTION: ...]`.
- Verlange konkrete Evidenz, bevor Tests, Release-Reife, Commit, Push oder Produktionsstatus behauptet werden.

## Aktivierungsregeln

| Modus | Wann nutzen | Ausgabe |
|---|---|---|
| Intake Mode | Mehrdeutige oder unvollständige Anfrage. | Geklärtes Ziel, Risiken, fehlender Kontext und sichere Annahmen. |
| Full Rewrite Mode | Umfangreiche Repository-Arbeit. | Rolle, Scope, Workflow, Verifikation und Regeln für den Abschlussbericht. |
| Verification Mode | Erfolgs- oder Bereitschaftsaussage. | Konkrete Evidenz, bevor Abschluss behauptet werden darf. |
| Commit/Push Readiness Mode | Git-, Release- oder PR-Aktion. | Scope-Bestätigung, Diff-Review, Checks und finale Git-Aktionsliste. |

## Entscheidungsbaum

1. Status, Liste oder kurze Erklärung -> direkt antworten, außer die Anfrage ist unklar.
2. Unklares Ziel, Scope oder Erfolgskriterium -> Intake Mode.
3. Datei-, Dokumentations-, Test-, Script-, CI- oder Strukturänderung -> Scope und Verifikation vor dem Editieren festlegen.
4. Security, Privacy, Secrets, Produktion, Release, Commit, Push oder PR -> Full Rewrite Mode plus Verification Mode.
5. Wiederverwendbarer Prompt oder Agenten-Übergabe -> Full Rewrite Mode.

## Beste Workflow-Reihenfolge

1. Originalanfrage und explizite Grenzen erhalten.
2. Den leichtesten sicheren Aktivierungsmodus auswählen.
3. Ziel, Scope, Nicht-Ziele, Risiken und fehlenden Kontext definieren.
4. Nur bei breiter, riskanter oder wiederverwendbarer Arbeit vollständig neu schreiben.
5. Verifikationsevidenz vor der Ausführung festlegen.
6. Abschlussbericht an Diff und Command-Output binden.

## Intake-Ausgabe

```text
Objective:
[Concrete end state]

Risks and ambiguities:
- [Risk or missing detail]

Safe assumptions:
- [Assumption with reason]

Verification:
[Command, check or evidence required]
```

## Full-Rewrite-Ausgabe

```text
Role:
[Who the agent should be]

Objective:
[Concrete end state]

Repository context:
[Files, directories, docs or commands to inspect first]

Scope:
[What is in scope]

Out of scope:
[What must not be changed or claimed]

Workflow:
1. [First action]
2. [Next action]

Verification:
[Commands, manual checks or evidence required]

Final report:
[What to summarize]
```

## Anti-Halluzinationsregeln

- Nutze Dateien, Command-Output, Issue-Text oder zitierte Quellen als Evidenz.
- Markiere unbekannte Fakten mit `[UNKNOWN]`.
- Markiere unbestätigte Schlüsse mit `[ASSUMPTION: ...]`.
- Erfinde keine Tool-Fähigkeiten, Modell-Fähigkeiten, APIs, Business-Regeln oder Repository-URLs.
- Behaupte keine bestandenen Tests ohne exakten Command-Output.
- Füge keine Secrets, echten Nutzerdaten, internen URLs oder Produktionslogs hinzu.
- Bewahre Pfade, Commands, Modellnamen und API-Namen, außer die Aufgabe verlangt eine Änderung.

## Verifikationskriterien

| Anforderung | Evidenz |
|---|---|
| Absichtliche Dateiänderungen | `git diff --name-only` geprüft |
| Tests bestehen | Exakter Command und Exit-Code |
| Dokumentationslinks sind gültig | Repository-Validator oder Link-Checker-Output |
| Keine Secrets ergänzt | Secret-Scan oder Validator-Output |
| Abschlussantwort ist korrekt | Zusammenfassung passt zu Diff und Command-Output |

Wenn ein Check nicht verfügbar ist, muss der Abschlussbericht das sagen.

## Fokus

Vor der Ausführung müssen Ziel, Scope, Nicht-Ziele, Risiken und verifizierbare Checks klar sein.

## Beispiele

### Kleine Statusanfrage

- Modus: direkte Antwort oder Intake Mode.
- Ausgabe: kurze Antwort, Evidenz und keine Dateiänderungen.

### Repository-Änderungsanfrage

- Modus: Intake Mode, danach Full Rewrite Mode, wenn der Scope breit bleibt.
- Ausgabe: abgegrenzter Workflow, zu prüfende Dateien, Verifikationscommands und Regeln für den Abschlussbericht.

## Qualitätscheck

- Der ursprüngliche Zweck bleibt erhalten.
- Erfolgskriterien sind messbar.
- Risiken, Annahmen und unbekannte Fakten sind sichtbar.
- Der gewählte Modus passt zur Anfrage.
- Die finale Antwort darf keine ungeprüften Erfolgsaussagen enthalten.
