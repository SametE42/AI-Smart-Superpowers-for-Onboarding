# PROJECT_MEMORY.md

**Last updated:** YYYY-MM-DD
**Status:** DRAFT
**Scope:** Durable project state, continuity handover, assumptions, decisions, risks, workarounds and open questions.
**Created/updated by:** AI Assistant (Model: [MODEL], Run-ID: [RUN-ID])
***

## Continuity protocol

`PROJECT_MEMORY.md` is the continuity anchor inside `/docs/ai/`.

For every relevant task:

1. Read `PROJECT_MEMORY.md` before changing files.
2. Read the task-specific documents listed in `MASTER_SYSTEM.md`.
3. Record analyzed context, decisions, assumptions, uncertainties, problems, risks and open tasks.
4. Update the current state and next step before handover.
5. Do not document secrets, passwords, tokens, certificates or real user data.

If relevant information is not documented here, future agents must treat it as unknown.

### Label rules

- Session timestamps: `YYYY-MM-DDTHH:MM:SSZ`.
- Document header date: `YYYY-MM-DD`.
- Work status: `OPEN` / `IN_PROGRESS` / `BLOCKED` / `DONE`.
- Analysis status: `COMPLETE` / `PARTIALLY_ANALYZED` / `OPEN`.
- Unknown facts: `[UNKNOWN]`.
- Unverified conclusions: `[ASSUMPTION: ...]`.
- Missing source: `[SOURCE UNKNOWN]`.

## Current state

| Field | Value |
|---|---|
| Goal | `[UNKNOWN]` |
| Phase | `[UNKNOWN]` |
| Progress | `[UNKNOWN]` |
| Next step | `[UNKNOWN]` |
| Last handover | `[UNKNOWN]` |

## Analyzed context

| Timestamp | Status | Source | Notes |
|---|---|---|---|
| YYYY-MM-DDTHH:MM:SSZ | `OPEN` | `[UNKNOWN]` | `[UNKNOWN]` |

## Durable assumptions

### Assumption: [Title]

**Assumption:** `[ASSUMPTION: ...]`
**Reason:** `[Why this assumption currently exists]`
**Risk:** `[What can go wrong if it is false]`

## Architecture decisions

| Date | Decision | Reason | Risk / Tradeoff |
|---|---|---|---|
| YYYY-MM-DD | `[UNKNOWN]` | `[UNKNOWN]` | `[UNKNOWN]` |

## Session decisions

Use this section for task-level decisions that affect handover but do not need a full ADR.

| Timestamp | Decision | Reason | Source |
|---|---|---|---|
| YYYY-MM-DDTHH:MM:SSZ | `[UNKNOWN]` | `[UNKNOWN]` | `[SOURCE UNKNOWN]` |

## Technical debt

| Area | Problem | Risk | Recommended action |
|---|---|---|---|
| `[UNKNOWN]` | `[UNKNOWN]` | `[UNKNOWN]` | `[UNKNOWN]` |

## Dangerous areas

List files, modules or concepts where changes can have broad effects:

- `[UNKNOWN]`

For each area, document:

```markdown
### [Area]

**Why risky:**  
**Affected flows:**  
**Required tests/checks before change:**  
```

## Known workarounds

| Workaround | Reason | Risk | Remove when |
|---|---|---|---|
| `[UNKNOWN]` | `[UNKNOWN]` | `[UNKNOWN]` | `[UNKNOWN]` |

## Problems

| Problem | Status | Source | Notes |
|---|---|---|---|
| `[UNKNOWN]` | `OPEN` | `[SOURCE UNKNOWN]` | `[UNKNOWN]` |

## Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| `[UNKNOWN]` | `UNKNOWN` | `[UNKNOWN]` | `[UNKNOWN]` |

## Refactoring decisions

Use this format for accepted or rejected refactorings:

```markdown
## Decision [YYYY-MM-DD]: [Title]

**Context:**  
[What triggered the decision]

**Decision:**  
[What was decided]

**Not adopted:**  
[What was explicitly not adopted]

**Reason:**  
[Why]

**Risk:**  
[Remaining risk]

**Follow-up:**  
[Next task]
```

## Open project questions

- `[UNKNOWN]`
- `[UNKNOWN]`
- `[UNKNOWN]`

## Open tasks

| Priority | Task | Status | Dependencies |
|---|---|---|---|
| P1 | `[UNKNOWN]` | `OPEN` | `[UNKNOWN]` |
| P2 | `[UNKNOWN]` | `OPEN` | `[UNKNOWN]` |
| P3 | `[UNKNOWN]` | `OPEN` | `[UNKNOWN]` |

## Next step

- `[UNKNOWN]`

## Handover

At the end of each session or before context loss, append a dated handover entry:

```markdown
### Handover [YYYY-MM-DDTHH:MM:SSZ]

**Current state:** `[UNKNOWN]`
**Open tasks:** `[UNKNOWN]`
**Decisions:** `[UNKNOWN]`
**Problems:** `[UNKNOWN]`
**Uncertainties:** `[UNKNOWN]`
**Next step:** `[UNKNOWN]`
```

## Validation before handover

- [ ] `PROJECT_MEMORY.md` was read.
- [ ] `PROJECT_MEMORY.md` was updated.
- [ ] Relevant decisions were documented.
- [ ] Unknowns and assumptions were marked.
- [ ] Next step is defined.
- [ ] No secrets, passwords, tokens, certificates or real user data are included.
