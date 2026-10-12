# Page Contracts (what the automated tests check)

**Date**: 2026-10-11 | **Plan**: [plan.md](./plan.md)

These are the promises each page makes. Each is checked by a Playwright test against the
**production build** served on `http://localhost:3100` (research R9). Test IDs map to the spec's
acceptance criteria. Tests are written **before** the change that makes them pass.

---

## C1. Site (book-spec BK-01, BK-06; setup tasks d, f)

| Test | Check | Spec |
|------|-------|------|
| site-title | Home page `<title>` contains "AICT Course Guide"; navbar title is "AICT Course Guide" | setup |
| home-at-root | `/` shows the book home (H1 "AICT Course Guide") | R1 |
| no-blog | `aict-guide/build/blog` does not exist after build; navbar has no "Blog" link | BK-06, task d |
| no-tutorial | Sidebar has no "Tutorial" items; `build/` has no `tutorial-basics` or `tutorial-extras` folder | BK-06, task d |
| sixteen-modules | Sidebar top-level item labels are exactly the 16 "Module N: <Title>" labels, in order | BK-01, task f |
| module-placeholders | Each module link opens a page whose H1 is its "Module N: <Title>" | task f |

## C2. Diagrams (BK-03, BK-04, AC-C2, AC-C3; setup task e)

| Test | Check |
|------|-------|
| home-diagram | The home page has ≥ 1 `article svg[aria-roledescription]` that is visible |
| diagram-accessible | Every such SVG contains a `<title>` and a `<desc>` with non-empty text |
| diagram-in-words | The element right after each diagram is a paragraph starting "Diagram in words:" |

## C3. Lesson page (AC-C1 … AC-C8; one test set per lesson)

Lessons are listed once in `tests/lessons.js` (URL + expected title). Every listed lesson runs
every check below. A lesson is added to the list **at the start of its task** (red), before
the lesson is written.

| Test | Check | Spec |
|------|-------|------|
| sections-in-order | The article's H2 texts are exactly: Goal, Why It Matters, Key Terms, Teacher Demo, Student Task, Check Questions, Common Mistakes, Sources (in that order) | AC-C1 |
| goal-sentence | First paragraph under Goal starts "By the end of this lesson, you can" | book-spec §4 |
| has-diagram | ≥ 1 visible rendered Mermaid SVG with non-empty `<title>` and `<desc>` | AC-C2, AC-C3 |
| key-terms-table | Under Key Terms: a table with headers Term / Simple meaning (optionally a third column, Urdu meaning) and 3–8 body rows; if the Urdu column is present, every Urdu cell has an element with `lang="ur"` | AC-C7 |
| student-task-end | The last list item under Student Task contains "Show your teacher:" | AC-C8 |
| three-questions | Under Check Questions: one ordered list with exactly 3 items; each contains "Answer:" | AC-C6 |
| common-mistakes | Under Common Mistakes: a list with 2–5 items | book-spec §4 |
| sources | Under Sources: a list with ≥ 1 item, each containing a link | AC-C4 |
| version-tabs (where used) | Every tab group's labels are exactly "Windows 10" and "Windows 11" | module spec §1 |

Build-level (AC-C5): the `webServer` command runs `npm run build` first. With R2's settings any
broken link, anchor or Markdown link fails the build, and then every test fails.

## C4. Module 1 overview (M1-01)

| Test | Check |
|------|-------|
| overview-title | H1 is "Module 1: Computer Basics" |
| overview-outcomes | An H2 "Learning Outcomes" followed by a list of exactly 9 items (LO-1 … LO-9, spec §2) |
| overview-lesson-links | An H2 "Lessons" followed by a list that links to every lesson in `tests/lessons.js`, in order, and each link opens that lesson |

## Not automated (owner review)

AC-C4 (claims really verified), AC-C7 (plain language, Urdu correctness), AC-C9 (approval),
AC-C10 (fits 60 minutes), and every lesson-specific criterion that needs judgement
(for example AC-1.3-a "parts are ones students can see in the lab").
