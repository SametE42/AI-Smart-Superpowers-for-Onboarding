# Model Profiles

Use this file to document how different model families should be used in this repository.

This file is not a replacement for `/docs/ai/MASTER_SYSTEM.md`. It only adds operational routing hints for model selection and multi-model workflows.

## Global rules for all models

- `/docs/ai/` is the source of truth.
- Do not invent business rules, security guarantees or production-readiness claims.
- Mark assumptions and unknowns explicitly.
- Keep changes scoped and reviewable.
- Do not expose secrets or sensitive data.
- Run relevant verification commands or document why verification was not possible.
- Human review is required before merge or production use.

## Task routing matrix

| Task type | Preferred model traits | Required context |
|---|---|---|
| Repository onboarding | strong long-context analysis, cautious summarization | `MASTER_SYSTEM.md`, repository tree, key docs |
| Small bugfix | precise code editing, strong test reasoning | `MASTER_SYSTEM.md`, `ERROR_PATTERNS.md`, affected files |
| Feature planning | architecture reasoning, requirement tracking | `MASTER_SYSTEM.md`, `ARCHITECTURE.md`, `DOMAIN_KNOWLEDGE.md` |
| Refactoring | diff discipline, architecture awareness | `MASTER_SYSTEM.md`, `ARCHITECTURE.md`, `STYLE_GUIDE.md` |
| Security review | conservative risk analysis | `MASTER_SYSTEM.md`, `SECURITY_RULES.md`, auth/config files |
| Test generation | edge-case reasoning | `STYLE_GUIDE.md`, `REVIEW_CHECKLIST.md`, existing tests |
| Documentation | concise technical writing | relevant docs, `CHANGELOG_AI.md` |
| Translation | terminology consistency | English source file, `docs/i18n.md` |

## Provider profiles

### DeepSeek

Suggested use:

- reasoning-heavy implementation review
- cost-sensitive code analysis through compatible clients
- alternative review pass after another model generated code

Constraints:

- Treat provider/model capabilities as client-dependent.
- Do not assume repository file loading unless the active tool explicitly provides it.
- Use `AGENTS.md` as the default entrypoint.

### Qwen

Suggested use:

- coding-agent workflows through Qwen Code or compatible clients
- multilingual documentation review
- long-context repository inspection when supported by the runtime

Constraints:

- Keep instructions tool-neutral unless the project explicitly uses Qwen Code.
- Use `AGENTS.md` as fallback and add Qwen-specific instructions only where the runtime supports them.

### Kimi / Moonshot

Suggested use:

- long-context analysis
- large repository reading tasks
- documentation consolidation proposals

Constraints:

- Do not use long context as a replacement for evidence-first documentation.
- Summaries must preserve uncertainty markers.

### Mistral

Suggested use:

- EU-sensitive or privacy-conscious workflows where deployment context supports it
- multilingual review
- code/documentation tasks via API clients or enterprise tools

Constraints:

- Do not infer privacy or compliance guarantees from provider identity alone.
- Document deployment assumptions separately.

### Grok / xAI

Suggested use:

- secondary review pass
- API-based reasoning or assistant workflows
- exploratory analysis when connected through a controlled client

Constraints:

- Current-event or web claims require explicit source verification.
- Do not assume live web access unless the active client provides it.

### Xiaomi MiMo

Suggested use:

- experimental provider/model evaluation
- agentic workflow tests where MiMo is available through an API or gateway
- specialized multimodal/embodied scenarios only when relevant to the project

Constraints:

- Treat as optional model support unless your stack actively uses it.
- Do not add hard dependencies on MiMo-specific behavior.

### MiniMax

Suggested use:

- agentic workflows
- multimodal, audio, image, video or long-context experiments where supported
- secondary implementation review through compatible APIs

Constraints:

- Separate language-model tasks from multimodal generation tasks.
- Keep repository modification permissions bounded.

### Other providers

Use this profile when a model is accessed through OpenAI-compatible, Anthropic-compatible or gateway APIs.

Required documentation:

```text
Provider:
Model family:
Client/runtime:
Context loading method:
Tool access:
Verification command support:
Known limitations:
```

## Evaluation checklist

Before adding a model/provider as officially supported, verify:

- Does the model run through a tool that can read repository files?
- Which context files does the tool actually load?
- Can it run shell commands or tests?
- Can it edit files directly?
- Does it support MCP, tools, plugins or function calling?
- What is the context window limit?
- Does the provider have data-retention or privacy implications?
- Are there cost, rate-limit or licensing constraints?

## Changelog

Add dated notes here when model routing changes.

```text
YYYY-MM-DD - Added/updated profile: <provider/model>. Reason: <short reason>.
```
