# Optional Templates

This folder contains optional AI documentation templates for projects that require deeper production-readiness, testing, protocol, prompt-refinement or governance documentation.

Use these files only when the target repository needs the extra structure. The core `templates/docs-ai/` set remains the baseline.

| Template | Use when |
|---|---|
| `MAGICAL_PROMPT_IMPROVER.md` | A prompt needs to be clarified, safety-scoped and turned into verifiable instructions before execution. |
| `OPERATIONS.md` | Operational ownership, rollout, rollback or support paths need explicit documentation. |
| `PRODUCTION_READINESS.md` | The project needs measurable production-readiness gates. |
| `PROTOCOL_BOUNDARIES.md` | Agent, tool or protocol boundaries need stricter rules. |
| `TESTING_STRATEGY.md` | Automated and manual test strategy needs explicit documentation. |

## Recommended order

1. Start with `MAGICAL_PROMPT_IMPROVER.md` when the request itself is unclear or high-impact.
2. Use `PRODUCTION_READINESS.md`, `OPERATIONS.md`, `PROTOCOL_BOUNDARIES.md` or `TESTING_STRATEGY.md` only when the target repository needs that extra gate.
