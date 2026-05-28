# Production Readiness Gates

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Measurable gates required before the project can be described as production-ready.  
***

## Goal

This document defines measurable requirements that must be fulfilled before the project can move beyond prototype or pre-production status.

It does not replace business approval and does not invent domain rules.

## Current classification

**Current status:** `[UNBEKANNT]`

Allowed status terms:

- `prototype`
- `hardened prototype`
- `production-adjacent`
- `production-ready`

Do not use `production-ready` unless every required gate is met or explicitly documented as externally fulfilled.

## Gate 1: Backend and persistence contract

Acceptance criteria:

- [ ] Production persistence is documented.
- [ ] Repository/API contracts are defined.
- [ ] UI/domain types are separated from transport DTOs where needed.
- [ ] Not-found, validation, conflict and technical error states are modeled.
- [ ] Migration, backup, restore and deletion are documented.
- [ ] Tests cover adapter contracts without production data.

Status: `[UNBEKANNT]`

## Gate 2: Server-side validation

Acceptance criteria:

- [ ] Required fields are validated server-side.
- [ ] Date ranges and allowed values are validated server-side.
- [ ] State transitions are validated server-side.
- [ ] Client validation remains a usability helper only.
- [ ] Error responses are neutral for users and loggable for operators.
- [ ] Tests cover valid input, invalid input and conflicts.

Status: `[UNBEKANNT]`

## Gate 3: Business-rule approval

Acceptance criteria:

- [ ] Relevant pricing, billing, tax, status, export or workflow rules are approved.
- [ ] Rules are versioned.
- [ ] Example calculations or examples are tested.
- [ ] Missing rules block affected outputs.
- [ ] Exports remain disabled if required rules are missing.

Status: `[UNBEKANNT]`

## Gate 4: Access control and operational frame

Acceptance criteria:

- [ ] Access to deployment target is defined.
- [ ] Authentication is implemented or external access control is documented.
- [ ] Authorization or explicit non-requirement is documented.
- [ ] No secret is stored in frontend code.
- [ ] Secret scanning is enabled in CI or has been checked manually.
- [ ] Operational ownership, support path and rollback are documented.

Status: `[UNBEKANNT]`

## Gate 5: Logging, audit and export history

Acceptance criteria:

- [ ] Technical logs have transport, access control, retention and deletion rules.
- [ ] Audit log is separated from technical error logs.
- [ ] Export history is tamper-resistant if required.
- [ ] Sensitive values are redacted before log storage.
- [ ] Tests cover redaction, error codes and protocol boundaries.

Status: `[UNBEKANNT]`

## Gate 6: Production-adjacent test and acceptance basis

Acceptance criteria:

- [ ] Full project check is green.
- [ ] Browser-based E2E tests cover core flows.
- [ ] Visual checks exist for important screens where relevant.
- [ ] Test data is synthetic and isolated.
- [ ] Acceptance report lists status, risks and untested areas.

Status: `[UNBEKANNT]`

## Final production status rule

The project may be called production-ready only when all required gates are fulfilled or explicitly documented as externally fulfilled.

Until then, use a precise status such as:

```text
Hardened prototype, production-adjacent in some areas, not production-ready.
```
