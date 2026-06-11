# CONTEXT_INDEX.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Task-specific context loading guide.

## How to use this index

Read this file before loading the full knowledge base. Load only the documents needed for the current task.

| Task type | Read first | Optional | Do not load by default |
|---|---|---|---|
| Bug fix | `MASTER_SYSTEM.md`, `ERROR_PATTERNS.md`, `EVIDENCE_MAP.md` | `ARCHITECTURE.md`, `BUILD_AND_TEST.md` | Full history, unrelated decisions |
| Feature implementation | `MASTER_SYSTEM.md`, `TASK_SCOPING.md`, `ARCHITECTURE.md` | `TECH_STACK.md`, `STYLE_GUIDE.md`, `REVIEW_CHECKLIST.md` | All logs or stale notes |
| Refactor | `MASTER_SYSTEM.md`, `ARCHITECTURE.md`, `STYLE_GUIDE.md` | `DECISIONS.md`, `RISK_REGISTER.md` | Unrelated feature docs |
| Security-sensitive change | `MASTER_SYSTEM.md`, `SECURITY_RULES.md`, `SAFETY_BOUNDARIES.md`, `HUMAN_REVIEW_GATES.md` | `RISK_REGISTER.md`, `DEPENDENCIES.md` | Non-security examples |
| Documentation update | `MASTER_SYSTEM.md`, target doc, `FRESHNESS.md` | `PROJECT_MEMORY.md`, `DECISIONS.md` | Unrelated source files |
| Dependency update | `MASTER_SYSTEM.md`, `DEPENDENCIES.md`, `SECURITY_RULES.md` | `BUILD_AND_TEST.md`, `RISK_REGISTER.md` | UI-only docs |
| Test improvement | `MASTER_SYSTEM.md`, `BUILD_AND_TEST.md`, `STYLE_GUIDE.md` | `ERROR_PATTERNS.md` | Deployment docs |
| Build or CI change | `MASTER_SYSTEM.md`, `BUILD_AND_TEST.md`, `TECH_STACK.md` | `RUNTIME_ENVIRONMENT.md`, `DEPENDENCIES.md` | UI-only docs |
| Runtime or deployment change | `MASTER_SYSTEM.md`, `RUNTIME_ENVIRONMENT.md`, `SAFETY_BOUNDARIES.md` | `SECURITY_RULES.md`, `HUMAN_REVIEW_GATES.md` | Test-only notes |
| Release preparation | `MASTER_SYSTEM.md`, `REVIEW_CHECKLIST.md`, `FRESHNESS.md` | `RISK_REGISTER.md`, `DECISIONS.md` | Raw chat history |
| Architecture review | `MASTER_SYSTEM.md`, `ARCHITECTURE.md`, `DECISIONS.md` | `EVIDENCE_MAP.md`, `RISK_REGISTER.md` | Tool-specific entrypoints unless needed |

