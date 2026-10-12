# Content Model: Module 1 — Computer Basics

**Date**: 2026-10-11 | **Plan**: [plan.md](./plan.md)

The book has no database. Its "data" is Markdown/MDX files. This file defines each piece of
content, its fields, and the rules a test or review checks.

---

## Book Home

| Field | Rule |
|-------|------|
| File | `aict-guide/docs/intro.md`, front matter `slug: /` |
| Title | "AICT Course Guide" |
| Content | Short welcome, "How to use this book in class" diagram (research R11) |

## Module

| Field | Rule |
|-------|------|
| Folder | `aict-guide/docs/module-NN-<name>/`, names from `specs/book-spec.md` Section 3 |
| `_category_.json` | `label`: "Module N: <Title>"; `position`: N (1–16) |
| Overview page | `index.md` in the folder; H1 = "Module N: <Title>" |
| Overview content (Module 1) | Summary, learning outcomes LO-1…LO-9, ordered lesson list with a link to each lesson |
| Overview content (Modules 2–16) | Title only for now (setup task f) |

**Rules**: exactly 16 module folders; positions 1–16 with no gaps; labels match book-spec.

## Lesson

| Field | Rule |
|-------|------|
| File | `aict-guide/docs/module-01-computer-basics/<slug>.mdx` |
| Front matter | `sidebar_position` (1–9, the lesson number), `title` ("Lesson 1.N: <Title>") |
| Sections | Exactly the 8 sections below, as H2 headings, in this order |

| # | H2 heading (exact text) | Content rule |
|---|-------------------------|--------------|
| 1 | `Goal` | One sentence starting "By the end of this lesson, you can" |
| 2 | `Why It Matters` | 2–4 sentences |
| 3 | `Key Terms` | Key Term table |
| 4 | `Teacher Demo` | Ordered list; may contain Version Tabs and UNVERIFIED blocks |
| 5 | `Student Task` | Ordered list; last item contains "Show your teacher:" |
| 6 | `Check Questions` | Ordered list of exactly 3 items; each contains "Answer:" |
| 7 | `Common Mistakes` | List of 2–5 items, each "Mistake → fix" |
| 8 | `Sources` | List of ≥ 1 item; each item has a link |

A Lesson has 1 or more Diagrams placed anywhere in sections 2–4.

## Key Term (a row of the Key Terms table)

| Column header (exact) | Rule |
|-----------------------|------|
| `Term` | The word or phrase, as used in the lesson |
| `Simple meaning` | Plain English, one sentence |
| `Urdu meaning` | `<span lang="ur" dir="rtl">…</span>`; owner reviews the Urdu |

**Rules**: 3–8 rows per lesson.

## Diagram

| Field | Rule |
|-------|------|
| Form | A ```` ```mermaid ```` code block, flowchart preferred |
| `accTitle` | Required, non-empty |
| `accDescr` | Required, non-empty |
| Size | ≤ 8 boxes; labels 1–4 words |
| Diagram in words | The paragraph right after the diagram starts with "**Diagram in words:**" |

**Rendered form** (what the browser test sees): an `svg` with `aria-roledescription`, containing
a non-empty `<title>` and `<desc>` (research R4).

## Version Tabs (Windows 10 / Windows 11)

| Field | Rule |
|-------|------|
| Form | `<Tabs groupId="windows-version">` |
| Items | `<TabItem value="win10" label="Windows 10">`, `<TabItem value="win11" label="Windows 11">` |
| When used | Only where the steps differ between the versions |

## UNVERIFIED Block

| Field | Rule |
|-------|------|
| Form | `:::warning[UNVERIFIED]` … `:::` |
| Body | Says what to test and on which version(s) |
| State | **Open** (marker present) → **Tested-OK** (owner records version, marker removed) or **Tested-failed** (step fixed or removed) |

## Source

| Field | Rule |
|-------|------|
| Form | List item in the `Sources` section: link + what it verifies |
| Allowed | Context7 result (library ID + topic), or the software maker's official documentation |
