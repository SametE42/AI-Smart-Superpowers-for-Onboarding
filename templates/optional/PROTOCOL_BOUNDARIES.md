# Protocol Boundaries

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Separation of technical logging, validation, change history, export history and audit logging.  
***

## Goal

This document prevents different types of protocol data from being mixed.

Technical errors, business validation, change history, export history and audit logs have different purposes and must remain separate.

## Technical error logging

Purpose: technical diagnostics.

Examples:

- runtime errors,
- rendering errors,
- export failures,
- storage failures,
- network failures,
- unexpected service exceptions.

Must not contain:

- raw business objects,
- full export payloads,
- unredacted personal data,
- secrets,
- authorization headers.

## Validation / review center

Purpose: business or functional checks.

Examples:

- missing required business data,
- inconsistent fields,
- unconfigured business rules,
- warnings requiring human review.

This is not a technical error log.

## Change history

Purpose: user-readable record of local or business changes.

Examples:

- record created,
- record edited,
- status changed,
- setting changed.

This is not a secure audit log unless explicitly implemented as such.

## Export history

Purpose: trace business export events.

Examples:

- filename,
- export timestamp,
- number of exported rows,
- export type,
- user display name if approved.

Must not contain full export payloads unless explicitly approved and secured.

## Audit log

Purpose: security-relevant and compliance-relevant traceability.

An audit log requires explicit requirements for:

- what must be audited,
- retention,
- access control,
- tamper resistance,
- deletion rules,
- legal or compliance constraints.

If those requirements are missing, document audit as `[UNBEKANNT]` or `not implemented`.

## Boundary rule

Keep these areas separate:

```text
technical error log
functional validation
change history
export history
audit log
operational monitoring
```

Do not reuse one mechanism for another without explicit design review.
