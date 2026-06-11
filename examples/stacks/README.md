# Stack Examples

## Use Case

Show that the framework is technology-neutral and not Python-only.

## Repository-Typ

Any repository with detectable stack evidence.

## verwendeter Modus

Standard Integration for most projects; Enterprise when runtime or security boundaries matter.

## verwendete Sprache

English by default; any supported language can be selected.

## verwendeter Strukturmodus

Canonical by default; localized through File-Maps when desired.

## erkannter oder angenommener Stack

Stack hints only. Evidence must be recorded in `EVIDENCE_MAP.md`.

## verwendete Templates

`TECH_STACK.md`, `BUILD_AND_TEST.md`, `DEPENDENCIES.md`, `RUNTIME_ENVIRONMENT.md`, `EVIDENCE_MAP.md`.

## Agent zuerst lesen

1. `docs/ai/TECH_STACK.md`
2. `docs/ai/BUILD_AND_TEST.md`
3. `docs/ai/EVIDENCE_MAP.md`

## Human Review

Review stack hints before using generated build, test or deployment commands.

## Stack Hints

| Stack | Evidence examples | Notes |
|---|---|---|
| Python | `pyproject.toml`, `requirements.txt`, `setup.py` | Python is an internal automation option, not the framework target only. |
| TypeScript | `package.json`, `tsconfig.json` | Verify package scripts before assuming commands. |
| Java | `pom.xml`, `build.gradle` | Gradle may also indicate Kotlin; document ambiguity. |
| C# | `.csproj`, `.sln` | Treat as .NET hint until verified. |
| Go | `go.mod` | Verify test commands from repo files. |
| Rust | `Cargo.toml` | Verify workspace layout before commands. |
| Infrastructure-as-Code | `*.tf`, `terraform/` | Human review required for deployment-impacting changes. |
