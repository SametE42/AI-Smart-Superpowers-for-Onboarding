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
[UNKNOWN]
```

Recommended table:

| Purpose | Command | Notes |
|---|---|---|
| Typecheck | `[UNKNOWN]` | `[UNKNOWN]` |
| Unit tests | `[UNKNOWN]` | `[UNKNOWN]` |
| E2E smoke | `[UNKNOWN]` | `[UNKNOWN]` |
| Build | `[UNKNOWN]` | `[UNKNOWN]` |
| Full check | `[UNKNOWN]` | `[UNKNOWN]` |

## Current test areas

- `[UNKNOWN]`

## Manual acceptance scenarios

1. `[UNKNOWN]`
2. `[UNKNOWN]`
3. `[UNKNOWN]`

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
| `[UNKNOWN]` | `[UNKNOWN]` | `[UNKNOWN]` |

## Production-adjacent test gate

The project should not be described as production-ready unless:

- core checks are green,
- core flows are covered,
- test data is synthetic,
- untested areas are listed,
- known risks are documented.
