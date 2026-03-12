<!--
Sync Impact Report
- Version change: 0.0.0 → 1.0.0
- List of modified principles:
  - Initialized from template with concrete values.
  - Added "I. Open Source & Free Software Only" (User Directive).
  - Added "II. Portuguese Language Focus" (Project Context).
  - Added "III. Modular & Testable" (Best Practice).
  - Added "IV. Documentation as Code" (Best Practice).
  - Added "V. Simple & Maintainable" (Best Practice).
- Added sections:
  - Technical Constraints
  - Workflow & Quality
- Removed sections: None.
- Templates requiring updates:
  - .specify/templates/plan-template.md (✅ updated/checked)
  - .specify/templates/spec-template.md (✅ updated/checked)
  - .specify/templates/tasks-template.md (✅ updated/checked)
- Follow-up TODOs: None.
-->

# pt-tts Constitution

## Core Principles

### I. Open Source & Free Software Only
The project MUST exclusively use open source or free software. This applies to all libraries, frameworks, tools, and dependencies used in development, testing, and production. No proprietary software is allowed. All dependencies must have licenses compatible with open-source redistribution (e.g., MIT, Apache 2.0, GPL, BSD).

### II. Portuguese Language Focus
The primary focus of the project is the Portuguese language, specifically for Text-to-Speech (TTS) applications. All phonetic rules, linguistic models, and datasets must prioritize Portuguese linguistic accuracy and regional variations where applicable.

### III. Modular & Testable
Every component must be modular and independently testable. We follow a library-first approach where core logic is decoupled from any specific interface (CLI, Web, etc.). High test coverage is mandatory for core linguistic logic.

### IV. Documentation as Code
Documentation, including this constitution, specifications, and implementation plans, must be maintained alongside the code in the repository. Documentation is the single source of truth for project governance and requirements.

### V. Simple & Maintainable
We prioritize simplicity and long-term maintainability over complex "just-in-case" features. The YAGNI (You Ain't Gonna Need It) principle is strictly enforced to avoid over-engineering.

## Technical Constraints

### License Compliance
All third-party dependencies must be audited for license compliance. Tools used in the CI/CD pipeline must also be open source or free for use in open-source projects.

### Language & Compatibility
Core libraries should be written in languages that offer broad cross-platform compatibility and strong performance for audio processing.

## Workflow & Quality

### Spec-First Development
No feature implementation may begin without a verified and approved specification (`spec.md`) and implementation plan (`plan.md`).

### Automated Validation
The CI/CD pipeline must enforce linting, type-checking, and automated testing for every pull request. Failure to meet these quality gates blocks merging.

## Governance

### Amendment Procedure
This constitution is a living document. Amendments require a version bump and an update to the `LAST_AMENDED_DATE`. Changes must be documented in the Sync Impact Report at the top of this file.

### Compliance Review
All implementation plans and task lists must include a "Constitution Check" to ensure alignment with these core principles.

**Version**: 1.0.0 | **Ratified**: 2026-03-12 | **Last Amended**: 2026-03-12
