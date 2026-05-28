# STYLE_GUIDE.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Code style, architecture style, naming, UI, logging, tests and documentation conventions.  
**Created/updated by:** AI Assistant (Model: [MODEL], Run-ID: [RUN-ID])  
***

## Language

- Documentation language: `[UNBEKANNT]`
- UI language: `[UNBEKANNT]`
- Code identifiers: `[UNBEKANNT]`
- Comments: `[UNBEKANNT]`

## File naming and structure

| Type | Convention |
|---|---|
| Components | `[UNBEKANNT]` |
| Pages/routes | `[UNBEKANNT]` |
| Tests | `[UNBEKANNT]` |
| Types | `[UNBEKANNT]` |
| Services | `[UNBEKANNT]` |
| Repositories | `[UNBEKANNT]` |

## Layer rules

- `[UNBEKANNT]`

## UI rules

- Empty states must be handled.
- Destructive actions should require confirmation.
- Disabled functions should be visibly unavailable.
- User-facing errors should be neutral.
- Technical stacktraces should not be shown to end users.

## Domain and validation rules

- Do not implement domain rules without source evidence.
- Missing rules must be represented as `[UNBEKANNT]`, warning, blocker or `not-configured`.
- Centralize validation where possible.
- Document field, code and severity if the local contract requires it.

## Logging rules

- Use central logging mechanisms where present.
- Do not scatter debug output in production-adjacent code.
- Do not log secrets, tokens, personal data or raw payloads.
- Keep user-facing error messages neutral.

## Export rules

- Use central export helpers where present.
- Export only approved columns.
- Protect against spreadsheet formula injection.
- Document encoding assumptions.
- Log export errors without storing export payloads.

## Test rules

- Prefer test-first for risky changes.
- Add unit/service tests for domain, data and shared logic.
- Add UI tests for validation, dialogs, destructive actions and empty states.
- Add E2E smoke tests for core user flows where relevant.
- Test data must be synthetic.

## DTO and API conventions

- Keep transport DTOs separate from UI/domain types when applicable.
- Model adapter results explicitly: success, not-found, validation, conflict and technical error.
- Treat server-side validation as authoritative in production systems.

## Documentation style

- Name concrete files, risks and decisions.
- Avoid generic filler.
- Document assumptions with reason and risk.
- State production status explicitly.
- Check attribution/license docs when adding external material.
