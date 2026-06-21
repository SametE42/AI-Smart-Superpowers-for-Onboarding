# 5-Minute Repository Onboarding Demo

This demo shows the smallest realistic path from an unknown repository to review-ready AI context.

## Starting Repository

Use a small Python repository with:

```text
README.md
pyproject.toml
example.py
```

## Command

```bash
python scripts/install_ai_onboarding.py \
  --mode standard \
  --language en \
  --structure canonical \
  --detect-stack \
  --target ../target-repo
```

## Expected Output

```text
AGENTS.md
docs/ai/
  AI_ONBOARDING_MANIFEST.yml
  CONTEXT_INDEX.md
  MASTER_SYSTEM.md
  ARCHITECTURE.md
  TECH_STACK.md
  BUILD_AND_TEST.md
  EVIDENCE_MAP.md
  REVIEW_CHECKLIST.md
```

## Human review

Review `AGENTS.md`, `docs/ai/CONTEXT_INDEX.md`, `docs/ai/EVIDENCE_MAP.md`, `docs/ai/SECURITY_RULES.md` and `docs/ai/REVIEW_CHECKLIST.md` before treating the output as trusted project context.

The installer output is review-ready. It is not automatically trusted, production-ready or language-reviewed.
