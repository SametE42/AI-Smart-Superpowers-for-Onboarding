# AI Smart Superpowers for Onboarding

> Translation status: Initial German translation
> Source file: ../../README.md
> Source language: English
> Last source review: 2026-05-28
> If this translation conflicts with the English source, the English source is authoritative.

Ein strukturierter Master-Prompt- und Dokumentationsstandard für Coding-Projekte in Multi-Model- und AI-unterstützten Entwicklungsworkflows.

Dieses Repository stellt ein wiederverwendbares Framework bereit, mit dem AI Agents sicher, konsistent und mit klaren Dokumentationsgrenzen in Software-Repositories eingearbeitet werden können.

## Warum?

AI Coding Agents scheitern häufig aus ähnlichen Gründen:

- sie übersehen Projektkontext,
- sie leiten Architektur aus unvollständigen Dateien ab,
- sie erfinden Business-Regeln,
- sie ignorieren bestehende Konventionen,
- sie vermischen technische Fehler mit Business-Logs,
- sie erzeugen zu breite Änderungen ohne Verifikation,
- sie behandeln lokale Prototypen als produktionsreife Systeme.

Dieser Standard reduziert diese Risiken durch eine stabile `/docs/ai/`-Wissensbasis, einen klaren Workflow zur Repository-Analyse und kurze tool-spezifische Einstiegspunktdateien wie `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` oder `.github/copilot-instructions.md`.

## Für wen?

Dieses Repository ist nützlich für:

- Entwicklerinnen und Entwickler, die mehrere Coding Agents nutzen,
- Teams mit Claude Code, Codex, Cursor, GitHub Copilot, Gemini, Windsurf oder ähnlichen Tools,
- Projekte, die wiederholbares AI-Onboarding benötigen,
- Maintainer, die AI-generierte Dokumentation strukturiert halten möchten,
- Teams, die klare Grenzen für Security, Produktionsreife und Human Review brauchen.

## Quickstart

1. Kopiere `templates/MASTER_PROMPT.md` oder die englische Variante `templates/MASTER_PROMPT.en.md`, falls vorhanden.
2. Gib den Prompt an deinen Coding Agent.
3. Zeige dem Agent dein Ziel-Repository.
4. Lasse zuerst Phase 0 bis Phase 2 laufen.
5. Prüfe den vorgeschlagenen Dokumentationsplan, bevor Date Änderungen erlaubt werden.

## Sprachen

Englisch ist die Hauptsprache und Quelle der Wahrheit dieses Repositories.

Übersetzungen dienen der Zugänglichkeit. Wenn eine Übersetzung der englischen Quelle widerspricht, gilt die englische Version.

## Unterstützte Modell- und Agent-Ökosysteme

Der Standard ist tool-neutral. Er kann mit OpenAI/Codex, Claude, Gemini, GitHub Copilot, Cursor, Windsurf sowie Modellfamilien wie DeepSeek, Qwen, Kimi, Mistral, Grok, Xiaomi MiMo und MiniMax verwendet werden, sofern das jeweilige Tool die Repository-Kontextdateien aktiv lädt.

Details stehen in:

```text
docs/tool-compatibility.md
```

## Sicherheit

AI-generierte Ergebnisse sind nicht automatisch vertrauenswürdig.

Alle erzeugten Dokumentations- und Codeänderungen müssen vor Commit, Merge oder produktiver Nutzung von Menschen geprüft werden.
