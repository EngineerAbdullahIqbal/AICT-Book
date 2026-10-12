<!--
Sync Impact Report
- Version change: 1.1.0 → 1.2.0 (MINOR: review cadence changed; deployment setup allowed)
- Modified principles:
  IV. Small Steps with Owner Approval → lesson work is reviewed per module; the owner still
  approves every spec and lesson list before writing (owner decision 2026-10-12)
- Modified sections:
  Technical Constraints & Scope → site may be configured for GitHub Pages; owner publishes
  Development Workflow → per-module review
- Previous: 1.0.0 → 1.1.0 moved content rules to specs/constitution.md (2026-10-11)
- Added sections: none
- Removed sections: none
- Templates: no template changes needed (tasks-template already has mandatory tests)
- Follow-up TODOs: none
-->

# AICT Course Guide Constitution

The AICT Course Guide is a Docusaurus teaching book for a 1-year computer course (AICT) for
absolute beginners in Pakistan. The website lives in `aict-guide/`; the Spec Kit project root
is `book-guide/`.

## Core Principles

### I. Verify Before You Write (NON-NEGOTIABLE)

- Before every setup step, configuration change, or technical claim, Claude MUST fetch the
  current official documentation through the Context7 MCP server and use the exact commands
  and configuration it gives.
- Claude MUST NOT guess. If Context7 or the official documentation cannot confirm something,
  Claude MUST stop and tell the owner instead of continuing.
- Every report MUST name the documentation pages that were used.

Rationale: the book teaches beginners who cannot spot a wrong step; one invented step
breaks trust in the whole course.

### II. Test-First (NON-NEGOTIABLE)

- Every change follows Red → Green → Refactor: write the automated test first, run it and
  confirm it fails, make the change, run it and confirm it passes, then refactor.
- The test suite is:
  - `npm run build` in `aict-guide/` — MUST succeed (broken links fail the build).
  - Playwright end-to-end tests in a real browser — required for anything visible on the
    page, including proof that Mermaid diagrams actually render.
- A task is not done until its tests pass and the full suite still passes.

Rationale: tests prove each step works and stop later steps from silently breaking it.

### III. Spec-Driven Development

- Every change MUST trace to an approved spec → plan → tasks under `specs/`.
- No implementation starts until the owner has approved the spec and plan.
- If work reveals the spec is wrong or incomplete, the spec is updated first, then the code.

Rationale: the owner decides what is built; the spec is the record of that decision.

### IV. Small Steps with Owner Approval

- Claude works on one task at a time.
- Claude MUST wait for the owner's OK on every spec, plan and lesson list before writing
  lessons from it.
- Lesson work (RED → VERIFY → GREEN for each lesson) runs through a whole module without
  stopping. When the module is done, Claude reports: what was done, which docs were used, how
  the owner can check it, and which files changed. Then Claude MUST wait for the owner's
  review of the module.
- If something can't be verified, Claude marks it UNVERIFIED or leaves it out, and lists it in
  the module report (Principle I).

Rationale: small, checked steps keep mistakes small and easy to undo.

### V. Beginner-First Content

- All rules for *what we write* (audience, language and Urdu help, tone, lesson template,
  diagrams, quality standards) live in **`specs/constitution.md`**, which is the single source
  for content rules. They are not repeated here.
- Every lesson MUST meet that file's quality standards before it is reported as done.

Rationale: the teacher reads from this book in class; it must work for the weakest student.
One source of content rules prevents the two files from drifting apart.

### VI. Official-Source Software Steps

- The verification rule and the **UNVERIFIED** marking rule for software steps are defined in
  `specs/constitution.md`, Sections 3–4, and MUST be followed.
- Menu names, buttons, and keyboard shortcuts MUST NOT be invented.

Rationale: software menus change between versions; only official sources are reliable.

## Technical Constraints & Scope

- Docusaurus 3 (currently 3.10.2), classic template, JavaScript variant, npm.
- Node.js >= 20.0 (Docusaurus requirement). Dev machine: Node v24.14.1, Ubuntu 24.04.
- Lesson content is written only for modules whose spec the owner has approved.
- The site may be configured for GitHub Pages (`EngineerAbdullahIqbal/AICT-Book`). Only the
  owner publishes. No translations until the owner asks for them.

## Development Workflow

- Spec Kit flow: constitution → specify → (clarify) → plan → tasks → implement.
- Within implement, each task runs Red → Green → Refactor (Principle II). Owner review
  happens per module (Principle IV).
- Claude MUST NOT run `git commit`, `git push`, or publish anything. The owner commits and
  publishes to their own GitHub. Claude lists the changed files at the end of each step.

## Governance

- This constitution overrides all other practices and guidance files, including CLAUDE.md.
- Amendments require the owner's approval, an updated Sync Impact Report, and a version bump:
  - MAJOR: a principle is removed or redefined incompatibly.
  - MINOR: a principle or section is added or materially expanded.
  - PATCH: wording, clarification, or typo fixes.
- Every plan MUST pass the Constitution Check gate before work starts, and every report to
  the owner is a compliance check against Principles I, II, and IV.

**Version**: 1.2.0 | **Ratified**: 2026-10-10 | **Last Amended**: 2026-10-12
