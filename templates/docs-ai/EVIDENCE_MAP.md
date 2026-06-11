# EVIDENCE_MAP.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Trace important claims to repository evidence.

## Evidence table

| Claim | Evidence source | Confidence | Last checked | Notes |
|---|---|---|---|---|
| Project appears to use `[UNKNOWN]` | `[UNKNOWN]` | Unknown | YYYY-MM-DD | Verify before relying on this claim |

## Confidence values

- High: direct repository evidence supports the claim.
- Medium: evidence suggests the claim, but some uncertainty remains.
- Low: weak evidence or indirect signal.
- Unknown: evidence is missing or not yet checked.

## Rules

- Confidence may increase only when repository evidence supports the claim.
- Stack detection must be recorded here before it is treated as context.
- Do not use documentation alone as High confidence when current files contradict it.

## Examples

| Claim | Evidence source | Confidence | Last checked | Notes |
|---|---|---|---|---|
| Project appears to use TypeScript | `package.json`, `tsconfig.json` | High | YYYY-MM-DD | Verify package scripts before assuming build commands |
| Project may use Docker | `Dockerfile` | Medium | YYYY-MM-DD | Deployment target still unknown |

