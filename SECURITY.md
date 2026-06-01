# Security Policy

## Scope

This repository contains documentation, prompts and templates for AI-assisted software development.

It does not contain a production application, backend service or runtime system.

Relevant security issues include:

- unsafe agent instructions,
- missing redaction rules,
- dangerous default permissions,
- prompt-injection risks,
- incorrect production-readiness guidance,
- misleading authentication or authorization claims,
- insecure logging, audit or export guidance,
- examples that contain sensitive data.

## Reporting security issues

Please do not open a public issue for sensitive security reports.

Use GitHub Private Vulnerability Reporting if enabled, or contact the maintainers through the repository contact method.

Report privately if the issue involves:

- leaked secrets,
- real personal data,
- internal URLs,
- dangerous agent permissions,
- instructions that could cause destructive changes,
- prompt-injection vulnerabilities,
- incorrect handling of logs or exports.

## What is not a vulnerability

The following are usually not security vulnerabilities by themselves:

- a missing example for a specific tool,
- incomplete optional templates,
- wording improvements,
- unsupported third-party tools,
- non-sensitive documentation typos.

Please open a normal issue for those.

## Security principles

This project follows these principles:

- never document secrets in cleartext,
- mark assumptions explicitly,
- avoid invented production guarantees,
- keep tool entrypoints short,
- require human review before impactful changes,
- keep technical logs, audit logs, export history and change history separate,
- treat local browser storage as non-production unless proven otherwise,
- require explicit verification before claiming production readiness.

## Sensitive data policy

Do not include:

- API keys,
- passwords,
- tokens,
- private certificates,
- personal data,
- customer data,
- billing data,
- internal logs,
- local machine paths containing real usernames,
- real phone numbers,
- real email addresses,
- confidential organization names.

Use placeholders such as:

```text
[REDACTED]
example@example.invalid
Example Organization
/path/to/project
```

## Supported versions

Security fixes apply to the latest tagged release.

Until the first public release after the repository rename is published, security fixes apply to the default branch `main`.

Early versions below `1.0.0` may change structure as the standard stabilizes.
