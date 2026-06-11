# AGENT_ROLES.md

**Last updated:** YYYY-MM-DD  
**Status:** DRAFT  
**Scope:** Optional AI-agent roles for multi-agent workflows.

## Role table

| Role | Responsibility | Allowed actions | Required input | Output |
|---|---|---|---|---|
| Repository Researcher | Find repository evidence and unknowns | Read files, summarize evidence | Task scope, repository files | Evidence notes |
| Architecture Mapper | Map modules, boundaries and data flow | Read docs and source, update architecture docs | Evidence notes | Architecture summary |
| Stack Analyst | Identify languages, tools and commands | Inspect config and dependency files | Repository files | Stack findings |
| Implementation Planner | Plan scoped changes | Read relevant context, propose steps | Task scope, evidence | Plan |
| Coding Agent | Implement approved changes | Edit scoped files, run checks | Approved plan | Code changes |
| Test Agent | Improve or run tests | Add or run tests | Change scope | Test evidence |
| Security Reviewer | Review secrets, auth, data and dependency risks | Read and report, request human review | Diff and security docs | Security review |
| Documentation Maintainer | Update durable docs | Edit docs, maintain freshness | Verified changes | Documentation updates |
| Human Reviewer | Approve high-impact decisions | Review, approve, reject or request changes | Agent outputs | Review decision |

## Rules

- Roles are optional and do not imply autonomous approval.
- Human Reviewer remains the trust boundary.

