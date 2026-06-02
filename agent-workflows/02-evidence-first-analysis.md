# Evidence-First Analysis Workflow

## Purpose

Gather repository facts from evidence and keep uncertainty visible.

## When To Use

- Before documenting architecture, security, domain behavior or workflows.
- When repository knowledge is scattered across files.
- When a large repository cannot be reviewed completely in one pass.

## Required Inputs

- Target repository path.
- Scope of the analysis.
- Relevant files from README, docs, configuration, build files, scripts, tests and source directories.
- Any user-supplied constraints or exclusions.

## Process Steps

1. Define the analysis scope and note excluded areas.
2. Read primary docs and configuration before drawing conclusions.
3. Inspect files, tests, scripts, build files, configuration and representative source files for behavioral evidence.
4. Record direct evidence with file paths and short rationale.
5. Separate observed facts from derived conclusions.
6. Derive dependencies only from manifest or lockfiles.
7. State dependency or runtime versions only when they are available in evidence.
8. Mark missing facts as `[UNKNOWN]`.
9. Mark inferred claims as `[ASSUMPTION]` or `[ASSUMPTION: ...]`.
10. For large repositories, prioritize core areas and mark incomplete coverage as `[PARTIALLY REVIEWED]` or `[PARTIALLY REVIEWED: ...]`.
11. Separate confirmed facts from recommendations and open questions.

## Expected Output

- Evidence-backed findings with source paths.
- Explicit `[UNKNOWN]`, `[ASSUMPTION]` and, when needed, `[PARTIALLY REVIEWED]` markers.
- Clear distinction between observed facts and derived conclusions.
- A short list of risks, gaps and next files to review.

## Security Rules

- Do not expose secret values found during inspection.
- Summarize sensitive patterns without copying sensitive data.
- Treat private, customer, financial or personal data as out of scope unless the user explicitly approves safe redacted handling.

## Human Review Checkpoint

A human reviews the evidence summary and uncertainty markers before those findings become `docs/ai/` source material.
