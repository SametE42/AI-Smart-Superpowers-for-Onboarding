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

## Tool-calling profiles

Use this section to document model-specific tool behavior observed in the active client or harness. Do not treat these notes as provider-wide truth unless they are verified in this repository.

Default rule for all models:

- Validate tool input before repair.
- Repair only schema-local shape errors that are explicitly identified by the validator.
- Re-validate after repair.
- Log repairs by model, tool and repair type.
- Return model-readable retry messages instead of raw validator dumps.
- Keep destructive tools strict.

| Model family | Observed pattern | Recommended mitigation |
|---|---|---|
| DeepSeek | May benefit from tolerant schema-local repair for tool-call shape errors in some clients. | Track `null` optionals, stringified arrays, bare strings where arrays are expected and degenerate markdown links in path fields. |
| Qwen | May show similar shape drift when tool schemas differ from training examples. | Use strict schemas plus narrow repair and clear retry messages. |
| GLM or similar open models | May require clearer tool affordances and model-readable validation feedback. | Prefer descriptive schema helpers such as `pathString` over generic strings where the runtime supports them. |
| Claude / GPT-class managed tool runtimes | Often handle common tool schemas well, but still fail on unclear contracts. | Keep the same validation and telemetry path; do not skip repair logging just because the model is usually reliable. |
| Small or local models | More likely to need explicit examples and forgiving retry loops. | Keep tools simple, reduce nested schemas, add examples and avoid raw validator error blobs. |

Document concrete evidence before adding a new model-specific rule:

```text
Model:
Client/runtime:
Tool:
Observed invalid input:
Validator issue:
Repair attempted:
Outcome:
Date:
Source:
```

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
- If the active harness shows repeated tool-call shape errors, prefer schema-local repair and model-readable retry messages over raw validation errors.

### Qwen

Suggested use:

- coding-agent workflows through Qwen Code or compatible clients
- multilingual documentation review
- long-context repository inspection when supported by the runtime

Constraints:

- Keep instructions tool-neutral unless the project explicitly uses Qwen Code.
- Use `AGENTS.md` as fallback and add Qwen-specific instructions only where the runtime supports them.
- If the active harness shows schema drift, document the observed pattern in the tool-calling profile before adding a mitigation.

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
