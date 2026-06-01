# Pull Request Checklist

## Goal

What does this PR change and why?

## Type of change

- [ ] Clarification
- [ ] Template improvement
- [ ] Example improvement
- [ ] Tool compatibility update
- [ ] Security improvement
- [ ] Documentation structure change
- [ ] Master prompt change
- [ ] Other

## Scope

Affected files:

- 

## Verification

- [ ] No private or sensitive data included.
- [ ] No unsupported tool claim added.
- [ ] No generic best practice added without project-specific value.
- [ ] Existing design principles still apply.
- [ ] Anti-bloat rule respected.
- [ ] README updated if public usage changed.
- [ ] CHANGELOG updated if release-relevant.
- [ ] Templates remain reusable.
- [ ] New optional templates are listed in `templates/optional/README.md`.
- [ ] Repository-specific progress, session, handover or completion notes are not committed.
- [ ] `python -m unittest discover -s tests` passed.
- [ ] `python scripts/validate_repository.py --root .` passed.
- [ ] `ai/VALIDATION_REPORT.md` and `ai/VALIDATION_REPORT.json` regenerated if validation output changed.

## Master prompt impact

- [ ] No master prompt change.
- [ ] Master prompt changed.

If changed, explain why this could not be solved in README, docs or templates:

## Sources / references

List official docs, public repositories or concrete examples used to support the change:

- 

## Risks

Known risks, tradeoffs or open questions:

- 
