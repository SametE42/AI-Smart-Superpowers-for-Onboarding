# Testing Strategy

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Automated and manual test strategy for this project.  
***

## Goal

This document describes how the project is verified.

It should distinguish:

- unit tests,
- service/domain tests,
- component tests,
- integration tests,
- E2E tests,
- manual acceptance checks,
- visual checks,
- production-readiness gates.

## Commands

```bash
[UNBEKANNT]
```

Recommended table:

| Purpose | Command | Notes |
|---|---|---|
| Typecheck | `[UNBEKANNT]` | `[UNBEKANNT]` |
| Unit tests | `[UNBEKANNT]` | `[UNBEKANNT]` |
| E2E smoke | `[UNBEKANNT]` | `[UNBEKANNT]` |
| Build | `[UNBEKANNT]` | `[UNBEKANNT]` |
| Full check | `[UNBEKANNT]` | `[UNBEKANNT]` |

## Current test areas

- `[UNBEKANNT]`

## Manual acceptance scenarios

1. `[UNBEKANNT]`
2. `[UNBEKANNT]`
3. `[UNBEKANNT]`

## Test data

Test data must be:

- synthetic,
- isolated,
- clearly marked,
- not production-like,
- not personal,
- not confidential.

Recommended patterns:

```text
TEST-*
example@example.invalid
Example Customer
Example User
```

## Error-handling tests

Verify:

- neutral user-facing messages,
- central logging,
- no stacktraces in UI,
- no raw payloads in logs,
- not-found states,
- empty states,
- invalid input states.

## Open test gaps

| Gap | Risk | Recommended test |
|---|---|---|
| `[UNBEKANNT]` | `[UNBEKANNT]` | `[UNBEKANNT]` |

## Production-adjacent test gate

The project should not be described as production-ready unless:

- core checks are green,
- core flows are covered,
- test data is synthetic,
- untested areas are listed,
- known risks are documented.
