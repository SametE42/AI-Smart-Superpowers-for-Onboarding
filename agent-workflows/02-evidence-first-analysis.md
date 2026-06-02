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
- Relevant files from README, docs, configuration, scripts, tests and source directories.
- Any user-supplied constraints or exclusions.

## Process Steps

1. Define the analysis scope and note excluded areas.
2. Read primary docs and configuration before drawing conclusions.
3. Inspect files, tests, scripts, configuration and representative source files for behavioral evidence.
4. Record direct evidence with file paths and short rationale.
5. Mark missing facts as `[UNKNOWN]`.
6. Mark inferred claims as `[ASSUMPTION]` or `[ASSUMPTION: ...]`.
7. For large repositories, prioritize core areas and mark incomplete coverage as `[PARTIALLY REVIEWED]` or `[PARTIALLY REVIEWED: ...]`.
8. Separate confirmed facts from recommendations and open questions.

## Expected Output

- Evidence-backed findings with source paths.
- Explicit `[UNKNOWN]`, `[ASSUMPTION]` and, when needed, `[PARTIALLY REVIEWED]` markers.
- A short list of risks, gaps and next files to review.

## Security Rules

- Do not expose secret values found during inspection.
- Summarize sensitive patterns without copying sensitive data.
- Treat private, customer, financial or personal data as out of scope unless the user explicitly approves safe redacted handling.

## Human Review Checkpoint

A human reviews the evidence summary and uncertainty markers before those findings become `docs/ai/` source material.
