# AI Agent Operating Manual

Dieser Ordner ist die deutsche lokalisierte Version der AI-Dokumentation. Die englische Version unter `ai/English/` bleibt die maßgebliche Quelle.

## Enthaltene Bereiche

- Modelle und Provider
- AI-Coding-Tools und Agent-Runtimes
- Slash Commands, Datei-Referenzen und Custom Commands
- Prompting und Context Engineering
- Wiederverwendbare Skills und Self-Evolving Skills
- Three-Tier Memory und Memory Safety
- GEPA, DSPy, TextGrad und weitere Optimierungsansätze
- Evaluation, Regression Tests und Quality Gates
- Safety, Privacy, Berechtigungen und Human Approval
- Beispiele und Templates

## Grundregel

Modelle besitzen meistens keine eigenen Commands. Commands gehören zum Tool oder zur Agent Runtime. Codex, Claude Code und Gemini CLI können Slash Commands anbieten; DeepSeek, Qwen, Kimi, Mistral, Grok, MiniMax und Xiaomi MiMo sind dagegen meist Modellfamilien oder Provider, die über solche Tools genutzt werden.
