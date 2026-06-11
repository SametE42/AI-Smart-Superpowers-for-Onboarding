# MASTER_SYSTEM.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Central working rules for AI agents in this repository.

## Purpose

This file defines the baseline behavior for AI-assisted work. Tool entrypoints such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and Copilot instructions should stay short and point here or to `CONTEXT_INDEX.md`.

## Evidence-first behavior

- Prefer current repository evidence over stale documentation.
- Mark missing facts as `[UNKNOWN]`.
- Mark plausible but unverified conclusions as `[ASSUMPTION: ...]`.
- Do not invent business, security, architecture or deployment rules.
- Confidence may increase only when repository evidence supports the claim.

## Required context flow

1. Use `CONTEXT_INDEX.md` first.
2. Load only the documents needed for the current task.
3. Check `SECURITY_RULES.md` before sensitive work.
4. Check `HUMAN_REVIEW_GATES.md` before high-impact changes.
5. Record important claims in `EVIDENCE_MAP.md`.

## Stack and language rules

- Do not assume project language or stack without evidence.
- Treat Python, JavaScript, TypeScript, Java, C#, Go, Rust, PHP, Ruby, Kotlin, Swift, C/C++, monorepos, frontend, backend, fullstack, Infrastructure-as-Code and documentation projects as valid targets.
- Python may be used for local installer, validation or test automation, but target repositories are not assumed to be Python projects.

## Safety rules

- Do not expose secrets, credentials, tokens, certificates or private user data.
- Do not make destructive changes without explicit human approval.
- Do not claim production readiness without evidence.
- Require human review for security, auth, deployment, data handling, licensing, generated translations and public claims.

## Completion rule

Before final status, state what was changed, what was verified, what remains unknown and which human review gates still apply.
