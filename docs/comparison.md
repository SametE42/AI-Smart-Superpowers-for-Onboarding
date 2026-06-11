# Comparison

This comparison positions AI Smart Superpowers for Onboarding in the AI-coding-agent ecosystem. It is intentionally cautious: project names, tool categories and high-level roles are used for orientation only. No official compatibility is claimed by this comparison.

Other projects often define how agents work, or provide tools that execute work. This project defines what agents need to understand about a repository before they work.

## Comparison Table

| Project / Approach | Category | Main purpose | Strength | Limit | How this project differs | What this project can learn |
|---|---|---|---|---|---|---|
| AGENTS.md | Entry Point / Format | Provide repository-level instructions for coding agents. | Simple, portable and easy for tools to discover. | A single file can become overloaded in complex repositories. | Uses `AGENTS.md` as a short pointer into a larger evidence-based knowledge base. | Keep the default entrypoint compact and tool-friendly. |
| agentsmd/agents.md | Entry Point / Format | Encourage a shared instruction-file convention for agents. | Helps normalize where agents should look first. | Does not by itself define a complete repository preflight knowledge model. | Treats entrypoint conventions as one layer, not the whole framework. | Preserve a small, predictable first-read file. |
| agentmd/agent.md | Entry Point / Format | Provide an agent-readable project instruction file. | Clear single-file handoff pattern. | Can blur long-term repository knowledge with immediate agent instructions. | Separates tool entrypoints from durable `docs/ai/` knowledge. | Make first-contact instructions easy to scan. |
| agentskills/agentskills | Skill Packaging | Package repeatable agent capabilities or task skills. | Reusable workflows can reduce repeated prompt design. | Skills usually describe how to perform tasks, not the full repository evidence base. | Prepares repository-specific context that skills can consume later. | Keep task workflows modular and bounded. |
| anthropics/skills | Skill Packaging | Define reusable Claude-oriented skills for specialized work. | Encourages scoped instructions and reusable procedures. | Tool-specific skill behavior should not be treated as universal support. | Provides tool-neutral repository preflight context before any skill executes. | Keep reusable procedures concise and explicit about scope. |
| addyosmani/agent-skills | Skill Packaging | Share practical skills and agent workflow patterns. | Practical workflow examples help agents act consistently. | Workflow skill collections may not validate repository evidence or localization. | Focuses on evidence, validation and language-adaptive repository context. | Make workflow guidance concrete enough to execute. |
| obra/superpowers | Workflow Methodology | Define structured development workflows for coding agents. | Strong process discipline for planning, TDD, debugging and verification. | It primarily guides how coding work is performed. | This project focuses on the step before that: a reviewed repository-specific knowledge base before workflows or tools change code. | Keep process guidance explicit and verification-oriented. |
| CommandCode | Agent Workflow / Command Pattern | Organize command-style instructions for repeatable AI-agent work. | Commands can make common actions consistent. | Command catalogs can become detached from repository evidence. | Uses repository evidence and generated knowledge files as the foundation for commands. | Make repeated actions discoverable without duplicating long context. |
| Aider | Execution Agent | Edit code through a coding-agent workflow. | Strong fit for direct repository editing with human-in-the-loop review. | Execution tools still need accurate project context before edits. | Does not replace execution agents; prepares the context they need. | Keep generated context useful for real code-editing sessions. |
| Cline | Execution Agent | Plan and execute coding tasks from an IDE-style agent interface. | Can inspect files, run commands and iterate on tasks. | Tool behavior depends on the active workspace and loaded context. | Supplies structured repository knowledge that Cline-like agents can reference generically. | Keep entrypoints short and workspace-safe. |
| OpenHands | Execution Agent | Run autonomous or semi-autonomous software-engineering tasks. | Broad execution environment for coding workflows. | Autonomous execution increases the need for boundaries and review gates. | Emphasizes preflight evidence, safety rules and human review before execution. | Document governance boundaries for agentic work. |
| Goose | Execution Agent | Connect LLMs to local tools and development workflows. | Flexible tool-connected agent pattern. | Flexibility can increase risk when repository constraints are unclear. | Makes repository constraints explicit before tool use. | Keep tool-use assumptions and permissions visible. |
| OpenCode | Execution Agent | Terminal-oriented coding-agent workflow. | Useful for command-line repository work. | Terminal agents still need scoped documentation and safe defaults. | Provides a portable `docs/ai/` context layer and short entrypoint pattern. | Make CLI-friendly instructions concise. |
| Continue | IDE Assistant / Execution Agent | Bring AI assistance into editor workflows. | Good fit for developer-in-the-loop code assistance. | IDE assistants may receive only partial repository context. | Offers a structured knowledge base that can be selectively loaded. | Support task-specific context retrieval instead of full-context dumping. |
| RepoMaster-like repository-understanding research | Research-Oriented | Study or improve automated understanding of repository structure and tasks. | Highlights the difficulty of reasoning over large codebases. | Research prototypes or papers may not be packaged as reusable repo documentation standards. | Converts repository-understanding concerns into maintainable templates, evidence maps and validation. | Treat repository understanding as an explicit artifact, not an implicit model behavior. |
| GitTaskBench-like benchmark research | Research-Oriented | Evaluate agents on repository tasks or Git-based software-engineering work. | Makes agent performance easier to discuss in controlled tasks. | Benchmarks do not automatically provide deployable repository context or governance docs. | Does not claim benchmark results; focuses on preparing context and review boundaries for real repositories. | Use benchmark thinking to define testable, reviewable onboarding outputs. |

## Abgrenzung Zu `obra/superpowers`

obra/superpowers defines structured development workflows for coding agents. This project focuses on the step before that: a reviewed, repository-specific knowledge base before such workflows or tools change code.

The relationship is complementary, not a claim of official integration. A repository can use this framework to prepare context, then use Superpowers-style workflows, another workflow system or a coding agent runtime to execute scoped work.

## Summary

Entry-point formats are useful because they give agents a predictable first file. Skill systems and workflow methodologies are useful because they define repeatable ways to work. Execution agents are useful because they can inspect files, run commands and make changes.

AI Smart Superpowers for Onboarding addresses a different layer: the evidence-first repository preflight layer. Its core question is not only "How should an agent act?" but "What has been checked, documented and validated about this repository before the agent acts?"

## Comparison Boundaries

- No fake adoption numbers are provided.
- No scientific benchmarks are invented or summarized.
- No official compatibility is claimed unless a tool actually defines and supports the relevant file or mechanism.
- Research-oriented rows are labeled as research-oriented.
- Execution tools are labeled as execution agents.
- Entry files and conventions are labeled as entry points or formats.
