# Rationale

AI-assisted coding works best when agents have stable, verifiable and scoped repository context.

This standard exists because many AI coding failures are not caused by model capability alone. They are caused by missing project context, unclear boundaries, weak verification and overloaded instruction files.

## Goals

- Create a stable `/docs/ai/` knowledge base.
- Keep tool-specific entrypoints short.
- Make assumptions and unknowns explicit.
- Prevent invented business logic.
- Keep security and production-readiness claims evidence-based.
- Support multiple AI models without letting them overwrite each other's work.

## Non-goals

- This is not an automatic memory system.
- This is not a replacement for human code review.
- This is not a production-readiness certification.
- This is not a universal architecture standard.
- This does not require every optional template in every project.

## Why `/docs/ai/`?

Tool entrypoint files are useful, but they should stay short. Large instruction files increase context cost and can make agent behavior worse.

`/docs/ai/` provides a structured source of truth that can be loaded selectively based on task type.
