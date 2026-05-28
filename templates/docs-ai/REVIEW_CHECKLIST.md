# REVIEW_CHECKLIST.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Review checklist for AI-assisted changes.  
**Created/updated by:** AI Assistant (Model: [MODEL], Run-ID: [RUN-ID])  
***

## Context

- [ ] Relevant agent instructions read.
- [ ] Relevant documentation read.
- [ ] Affected source files read.
- [ ] Existing tests read.
- [ ] Assumptions documented.
- [ ] Acceptance criteria documented.

## Architecture

- [ ] Layer boundaries respected.
- [ ] Domain/business logic not mixed into UI-only code.
- [ ] UI components do not access low-level storage directly.
- [ ] Shared utilities remain domain-neutral.
- [ ] Repository/service boundaries not bypassed.
- [ ] No unnecessary folder restructuring.
- [ ] No mixed change types without justification.

## Code quality

- [ ] Strict typing preserved.
- [ ] No uncontrolled `any`.
- [ ] No unused imports or dead exports.
- [ ] No duplicated validation/export logic.
- [ ] Null/undefined cases handled.
- [ ] User-facing errors are neutral.
- [ ] No debug output for end users.
- [ ] Comments explain non-obvious behavior only.

## UI and usability

- [ ] Empty state exists.
- [ ] Back/cancel/close actions exist where users could get stuck.
- [ ] Destructive actions require confirmation.
- [ ] Disabled functions are clearly marked as unavailable.
- [ ] Validation is visible and understandable.
- [ ] Text fits target layout.
- [ ] No obvious overlapping UI elements.

## Business logic

- [ ] No business rule invented.
- [ ] Missing rule represented as `not-configured`, warning or blocker.
- [ ] Special cases documented.
- [ ] Calculations based only on approved rules.
- [ ] Exports blocked if required rules or columns are missing.

## Data

- [ ] No real personal, customer, financial or internal data added.
- [ ] Test data synthetic and isolated.
- [ ] No data artifacts committed.
- [ ] Local persistence risks documented if relevant.
- [ ] Snapshot or cross-session risks evaluated if relevant.

## Security

- [ ] No secrets in code.
- [ ] No prototype login treated as production security.
- [ ] No role/permission claim without implementation.
- [ ] No tenant separation claim without implementation.
- [ ] Sensitive values are not logged.
- [ ] CSV/spreadsheet injection protection remains active.
- [ ] Access-control gaps documented if production use is touched.

## Logging and errors

- [ ] Technical errors logged centrally.
- [ ] Error code/category/source set where relevant.
- [ ] End users do not see technical internals.
- [ ] Stacktraces only internal and redacted.
- [ ] Log retention/access not claimed as production-ready unless implemented.
- [ ] Technical errorlog, audit log, change history and export history remain separate.

## Tests

- [ ] Unit/service tests added or updated.
- [ ] Component tests added or updated if UI affected.
- [ ] E2E smoke updated if a core flow changed.
- [ ] Success path tested.
- [ ] Empty state tested.
- [ ] Error path tested.
- [ ] Test data synthetic.
- [ ] Typecheck run or reason documented.
- [ ] Test run executed or reason documented.
- [ ] Build run or reason documented.
- [ ] Full check run or reason documented.

## Documentation

- [ ] README updated if setup, usage or feature changed.
- [ ] CHANGELOG updated if release-relevant.
- [ ] Architecture docs updated if layer or data flow changed.
- [ ] Security docs updated if auth, logging, data or access changed.
- [ ] Testing docs updated if tests or checks changed.
- [ ] Operations docs updated if runtime, deployment or diagnostics changed.
- [ ] Attribution/license docs checked if external material added.
- [ ] Agent instructions checked if workflow rules changed.

## Deployment and operations

- [ ] No new environment variable without documentation.
- [ ] No new external connection without security review.
- [ ] No production deployment recommended while blockers remain.
- [ ] Rollback or recovery impact evaluated.
- [ ] Local reports, exports and test artifacts ignored.

## Breaking changes

- [ ] Route, storage, DTO or data contract changes marked.
- [ ] Migration or reset path documented.
- [ ] Existing local data compatibility evaluated.
- [ ] Tests for old and new structure added or consciously excluded.
