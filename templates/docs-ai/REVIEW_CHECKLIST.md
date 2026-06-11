# REVIEW_CHECKLIST.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Review checklist before final agent output or merge.

## Evidence checked

- [ ] Current repository files were read.
- [ ] Claims are backed by `EVIDENCE_MAP.md` or direct repository evidence.
- [ ] Unknowns are listed.
- [ ] Assumptions use `[ASSUMPTION: ...]`.

## Tests considered

- [ ] Relevant automated tests identified.
- [ ] Relevant manual checks identified.
- [ ] Test gaps documented.
- [ ] Verification result recorded.

## Security boundaries checked

- [ ] No secrets or credentials exposed.
- [ ] No production configuration changed without review.
- [ ] Auth, permissions and data handling risks reviewed.
- [ ] Dependency risks reviewed where relevant.

## Documentation updates

- [ ] `PROJECT_MEMORY.md` updated only for durable knowledge.
- [ ] `DECISIONS.md` updated for formal decisions.
- [ ] `FRESHNESS.md` updated if review cadence changed.
- [ ] User-facing docs updated if behavior changed.

## Unknowns listed

- `[UNKNOWN]`

## Human review gates checked

- [ ] Security-sensitive changes.
- [ ] Authentication or authorization.
- [ ] Deployment or runtime changes.
- [ ] Data handling.
- [ ] Public claims.
- [ ] Licensing.
- [ ] Generated translations.
- [ ] Major dependency upgrades.
