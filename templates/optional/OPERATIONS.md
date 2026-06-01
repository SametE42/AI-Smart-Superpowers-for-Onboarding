# Operations

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Local operation, diagnostics, updates and handover.  
***

## Local operation

Document required commands:

```bash
[UNKNOWN]
```

Example structure:

```bash
npm install
npm run dev
npm run typecheck
npm run test:run
npm run build
npm run check
```

## Runtime / package manager

| Purpose | Command | Expected result |
|---|---|---|
| Install dependencies | `[UNKNOWN]` | Dependencies installed |
| Start dev server | `[UNKNOWN]` | Local app starts |
| Run tests | `[UNKNOWN]` | Tests pass |
| Build | `[UNKNOWN]` | Build succeeds |
| Full check | `[UNKNOWN]` | All required checks pass |

## Local update

Before updating from Git:

```bash
git status
```

If local changes exist, review, commit or safely store them first.

Recommended update flow:

```bash
git pull --ff-only
[install command]
[build/check command]
```

Do not run destructive commands such as:

```bash
git reset --hard
```

without explicit human approval.

## Diagnostics

Document:

- how to inspect logs,
- how to reproduce errors,
- how to run narrow checks,
- how to clear local test data,
- where generated artifacts are stored,
- which files must not be committed, such as `.env`, generated artifacts, logs, reports or exports.

## Handover

For another person to take over the project, document:

- repository URL,
- required permissions,
- setup commands,
- test commands,
- known limitations,
- production blockers,
- contact or support path,
- current version or tag.

## Non-production status

If the system is not production-ready, state it explicitly:

```text
This project is not production-ready because [reason].
```

Do not hide operational blockers.
