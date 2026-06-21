# FAQ

## Is this a coding agent?

No. This is a standard for onboarding coding agents into repositories.

## Does every project need all 10 `/docs/ai/` files?

The standard has a 10-file Conceptual Core for the prompt model and three installable contracts: Minimal with 7 docs, Standard with 17 docs and Enterprise with 21 docs. `config/standard-docs.yml` is the machine-readable source for the installable contracts.

## Should I put everything into `AGENTS.md`?

No. `AGENTS.md` should stay short and link to `/docs/ai/`.

## Can I use this with only one tool?

Yes. Use only the entrypoint relevant to your tool.

## Does this replace human review?

No. Human review remains required before important changes are merged or used in production.

## Does this make a project production-ready?

No. It helps document production readiness and blockers. It does not certify production readiness.

## Can I add Skills, Subagents or MCP?

Yes, but only when they solve a repeated, bounded and verifiable workflow. They are optional extensions.
