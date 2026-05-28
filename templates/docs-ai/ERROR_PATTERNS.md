# ERROR_PATTERNS.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Repeated error patterns, unstable areas and recommended debugging order.  
**Created/updated by:** AI Assistant (Model: [MODEL], Run-ID: [RUN-ID])  
***

## Known repeated patterns

| Pattern | Cause | Prevention |
|---|---|---|
| `[UNBEKANNT]` | `[UNBEKANNT]` | `[UNBEKANNT]` |

## Unstable areas

### [Area name]

**Why unstable:** `[UNBEKANNT]`  
**Affected files:** `[UNBEKANNT]`  
**Affected flows:** `[UNBEKANNT]`  
**Prevention:** `[UNBEKANNT]`

## Typical debugging order

1. Formulate a reproducible test or manual step.
2. Classify the error: UI, routing, validation, export, import, data, auth, logging, build or test.
3. Identify the affected architecture layer.
4. Read existing tests.
5. Add a minimal failing test or correct an outdated test.
6. Document the cause.
7. Fix minimally.
8. Run the narrowest relevant test first.
9. Run broader verification if the area is risky.
10. Update documentation if behavior or risk changed.

## Known open errors

### [Error title]

**Symptom:**  
`[UNBEKANNT]`

**Likely cause:**  
`[ANNAHME: ...]`

**Recommended correction:**  
`[UNBEKANNT]`

**Risk if ignored:**  
`[UNBEKANNT]`
