# Security policy

Codex-Guidas is a public engineering knowledge repository. Security reports must be handled privately so that vulnerabilities, credentials or exploit details are not exposed in public discussions.

## Reporting a vulnerability

**Please do not disclose suspected vulnerabilities, exploit steps, credentials, private data or sensitive logs in public GitHub issues, discussions or pull requests.**

The preferred channel is GitHub's **Report a vulnerability** function in the repository's Security area, but only after the repository maintainer has explicitly enabled **Private vulnerability reporting** in the repository's Security and analysis settings and confirmed that the option is available.

**Configuration status:** The presence of this file does not enable private vulnerability reporting. The feature's enabled status has not been independently verified as of 2026-11-19. Until the maintainer enables and verifies it, do not assume that the private reporting form is available. Use a separately verified private contact route agreed with the maintainer; do not send sensitive details through a public issue.

## Scope

The policy covers the Codex-Guidas repository and its maintained components, including:

- the Python knowledge search and validation CLI;
- GitHub Actions workflows and repository automation;
- templates, manifests and other repository-managed artefacts that could expose sensitive information or enable unsafe execution.

This policy does not make Codex-Guidas the incident authority for other projects. Report vulnerabilities in ScoutSA, SoulSync, SoulSyncMobile, NAVIGRE or another owning repository through that project's designated security process.

## What to include in a report

Where safe to do so, include:

- affected repository path and branch/commit;
- concise description of the security impact;
- reproduction steps that do not expose real user data or harm a service;
- relevant logs or proof of concept with secrets, tokens and personal information removed;
- any suggested containment action.

Do not test against systems or data you do not own or have explicit permission to assess.

## Response and disclosure

The maintainer should acknowledge receipt, assess severity and affected scope, coordinate a fix and agree on a disclosure timeline with the reporter. Do not publish details until affected users have had a reasonable opportunity to update and the maintainer and reporter agree disclosure is safe.

This policy is a reporting process, not a security certification or warranty that every vulnerability will be detected or remedied.
