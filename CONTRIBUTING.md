# Contributing

Thank you for considering a contribution.

This repository is a documentation and prompt standard for AI-assisted repository onboarding. Contributions should improve practical usefulness, safety, clarity or tool compatibility without making the standard unnecessarily heavy.

## Accepted contribution types

Good contributions include:

- clearer wording,
- safer default rules,
- better templates,
- improved examples,
- verified tool-compatibility updates,
- security improvements,
- anti-bloat improvements,
- better review or testing guidance.

## Not accepted

Please avoid:

- generic best practices without project-specific value,
- unverified claims about tool behavior,
- long agent instructions that duplicate existing docs,
- speculative rules without a concrete failure case,
- automatic memory systems without privacy and security design,
- examples containing real personal, customer, financial or internal data.

## Pull request rules

Every pull request should have exactly one clear purpose.

Avoid:

- bulk PRs,
- unrelated formatting changes,
- opportunistic refactors,
- adding a new rule without explaining what risk it reduces.

Each PR should explain:

- what changed,
- why it changed,
- which files were affected,
- whether the master prompt changed,
- whether README, templates or docs need updates,
- what verification was performed.

## Tool-specific claims

If a contribution adds or changes tool compatibility information, use official documentation or a clearly identified public repository as support.

Examples:

- official vendor documentation,
- official GitHub repository,
- release notes,
- maintained public examples.

Do not add support claims based only on assumptions.

## Anti-bloat rule

New agent rules are allowed only if they do at least one of the following:

- reduce a concrete risk,
- prevent a repeated failure pattern,
- improve tool compatibility,
- improve verification,
- reduce context usage,
- clarify human review boundaries.

Do not add rules that are only stylistic preference.

## Security and privacy

Do not include:

- real API keys,
- passwords,
- tokens,
- certificates,
- real customer data,
- real personal data,
- internal URLs,
- production logs,
- exported business data.

Use placeholders instead.

## Branch and commit guidance

Recommended branch naming:

```text
docs/<short-topic>
template/<short-topic>
fix/<short-topic>
compat/<tool-name>
```

Recommended commit style:

```text
docs: clarify production readiness template
template: add protocol boundaries optional document
fix: correct Copilot target path note
```

## Review checklist

Before opening a pull request:

- [ ] The change has one clear purpose.
- [ ] No private or sensitive data is included.
- [ ] Tool claims are supported by reliable sources.
- [ ] No duplicated long-form documentation was added.
- [ ] The master prompt was not expanded without strong reason.
- [ ] README or docs were updated if the public usage changed.
- [ ] Templates remain reusable and project-neutral.
- [ ] Repository-specific progress notes are not committed.

## Verification commands

Run these checks before opening a pull request:

```bash
python -m unittest discover -s tests
python scripts/validate_repository.py --root .
```

When the change affects validation output, language folders or release readiness, regenerate the reports too:

```bash
python scripts/validate_repository.py --root . --json ai/VALIDATION_REPORT.json --markdown ai/VALIDATION_REPORT.md
```
