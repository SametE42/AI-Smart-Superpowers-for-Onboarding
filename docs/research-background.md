# Research Background

AI coding agents need repository-specific context. Generic coding ability is not enough when a repository has local architecture, build constraints, historical decisions, safety boundaries, implicit conventions and project-specific review expectations.

A single instruction file is useful because it gives an agent a stable first read. For complex repositories, that file is often not sufficient. If it becomes too long, it can mix durable project knowledge, task-specific instructions, security rules, stale assumptions and tool-specific notes in one place.

Too much context can also hurt. Loading everything into an agent session can make important constraints harder to find, increase cost and make stale documentation look as important as current repository evidence. Context should be structured, reviewed and task-loadable.

Repository understanding is difficult because real projects contain architecture boundaries, dependencies, implicit assumptions, setup steps, historical decisions, generated files, tests, CI conventions and security limits. AI agents need a way to distinguish evidence from assumptions and unknowns.

Technology and stack context matters because build, test, runtime and dependency information varies across programming languages and ecosystems. In other words, technology and stack context is part of the evidence base. A Python repository, a TypeScript monorepo, a Java service, a Rust library, a Swift app and an Infrastructure-as-Code repository have different evidence signals and different verification commands.

Language-dependent output can improve usability for international teams, and language-dependent output should be treated as a design decision rather than a cosmetic translation layer. Fully localized documentation is most useful when every existing language has the same functional support level: selectable language, canonical structure, localized structure, file map, validation and documentation. Functional multilingual support is separate from language quality; functional multilingual support should not imply human-reviewed prose.

Translation quality must be checked and documented honestly. A language can have complete functional support while its `translation_review_status` remains `machine_generated`, `needs_review` or `unknown`. Human-reviewed translation should be claimed only when a human review is documented.

This project addresses the gap through evidence-first documentation, validation, technology-neutral templates and fully localizable output. Its focus is not to replace coding agents, but to prepare the repository knowledge that makes agent work safer and easier to review.

## Design Principles

1. Evidence instead of assumptions

   Repository facts should be grounded in files, tests, configuration, CI or existing documentation. Unknowns should remain explicit.

2. Task-scoped context loading

   Agents should load the documents needed for the current task instead of dumping the entire knowledge base into every session.

3. Human review before trust

   AI-generated documentation, plans and code changes remain proposals until reviewed by a human.

4. Separation of entrypoints and durable knowledge

   Tool entrypoints such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and Copilot instructions should stay short. Durable repository knowledge belongs in `docs/ai/` or the localized equivalent.

5. Traceability of claims

   Important claims should point back to repository evidence, confidence, review status or known unknowns.

6. Freshness and maintenance

   Repository knowledge should be reviewed over time. Stale build commands, old architecture notes and outdated dependency assumptions should be visible.

7. Governance and safety boundaries

   Secrets, production changes, destructive operations, authentication, authorization, deployment and data-handling risks need explicit review boundaries.

8. Tool-compatible entrypoints

   The framework should use known entrypoint filenames where they are useful, while avoiding unsupported claims about official tool integration.

9. Fully localized output for all existing languages

   Existing languages should be treated as first-class output targets, not as a small set of examples.

10. No knowledge duplication between tool files and knowledge base

   Duplicated rules drift. Tool files should point to the knowledge base instead of copying it.

11. Technology and programming-language neutrality

   The generated onboarding structure should work across Python, JavaScript, TypeScript, Java, C#, Go, Rust, PHP, Ruby, Kotlin, Swift, C/C++, monorepos, frontend, backend, fullstack, Infrastructure-as-Code and documentation projects.

12. Build, test, dependency and runtime context as part of repository onboarding

   Agents should not assume how a project installs, builds, tests or runs. These facts need explicit evidence.

13. Same functional support level for all existing languages

   Every detected existing language should be planned for complete functional output support.

14. No permanent fallback treatment for individual languages

   Fallbacks can be temporary during migration, but the target design should not make some languages permanently inferior.

15. Separate evaluation of functional language support and linguistic review quality

   Functional support answers whether the output can be generated and validated. Linguistic review quality answers whether the language has been human-reviewed or needs review.

## Practical Implication

The framework should produce compact, evidence-linked and task-loadable repository context. It should keep entrypoints short, make validation repeatable, document stack uncertainty, support canonical and localized output, and preserve human review as the trust boundary.
