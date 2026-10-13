---
description: "Task list for Module 1 — Computer Basics (with site foundation)"
---

# Tasks: Module 1 — Computer Basics (with site foundation)

**Input**: `specs/module-01-computer-basics/` — plan.md, spec.md, research.md, data-model.md,
contracts/page-contracts.md, quickstart.md. Also `specs/book-spec.md` and
`specs/constitution.md`.

**Tests**: MANDATORY (constitution Principle II). Every change starts with a test that is run
and seen to **fail (RED)**. Then the change is made and the test is run and seen to **pass
(GREEN)**.

**Working directory for all commands**: `book-guide/aict-guide/` unless stated otherwise.

**Rules for every task** (constitution Principles I, IV and the Development Workflow):
- Check Context7 (or the official docs, for lesson facts) **before** writing config or content.
  Never guess. If something can't be confirmed, stop and tell the owner.
- One task at a time. After each task, report what was done, the docs used, how to check it,
  and the files changed. Then **wait for the owner's OK**.
- Claude never runs `git commit` / `git push`. The owner commits.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: could run in parallel (different files, no dependency). In practice tasks run one at
  a time because of the owner-OK rule; [P] only marks where order does not matter.
- **[US1]–[US9]**: user story = one lesson (Lesson 1.1 … 1.9), in teaching order. Priority
  follows the teaching order (US1 = P1 … US9 = P9).

## User Stories (derived from spec.md §3 and book-spec §2.3)

| Story | Lesson | "As the teacher, I can teach…" | Spec criteria |
|-------|--------|--------------------------------|---------------|
| US1 | 1.1 What Is a Computer? Input, Processing, Output and Storage | the four jobs of a computer | LO-1, AC-1.1-a…c |
| US2 | 1.2 Hardware and Software | hardware vs software | LO-2, AC-1.2-a…c |
| US3 | 1.3 Parts of a Computer and Their Jobs | the parts of the lab desktop | LO-3, AC-1.3-a…c |
| US4 | 1.4 Starting Up and Shutting Down Safely | correct start-up and shut-down (Win 10 + 11) | LO-4, AC-1.4-a…c |
| US5 | 1.5 Using the Mouse | the five mouse actions | LO-5, AC-1.5-a…c |
| US6 | 1.6 Keyboard Basics | key groups and common keys | LO-6, AC-1.6-a…c |
| US7 | 1.7 The Operating System and the Desktop | the OS and desktop parts (Win 10 + 11) | LO-7, AC-1.7-a…c |
| US8 | 1.8 Files, Folders, Saving and Deleting | folders, saving in Paint, deleting, Recycle Bin (Win 10 + 11) | LO-8, AC-1.8-a…d |
| US9 | 1.9 Caring for Your Computer | basic safety and care | LO-9, AC-1.9-a…c |

Every story must also meet the common criteria AC-C1 … AC-C10 (spec §4).

---

## Phase 1: Setup — Test harness

**Purpose**: Make it possible to write a failing test before every later change (plan Phase 1,
research R9).

- [X] T001 Check Context7 `/microsoft/playwright` for current install steps, then run
  `npm i -D @playwright/test` in `aict-guide/`. Confirm `@playwright/test` is in
  `aict-guide/package.json` devDependencies and report the installed version.
- [X] T002 Run `npx playwright install chromium` in `aict-guide/`. If it reports missing system
  libraries, **stop** and ask the owner to run `npx playwright install --with-deps chromium`
  themselves (it needs sudo).
- [X] T003 Create `aict-guide/playwright.config.js` (ES module, `defineConfig`):
  `testDir: './tests'`; one project, Chromium only; `use.baseURL: 'http://localhost:3100'`;
  `webServer: { command: 'npm run build && npm run serve -- --port 3100 --no-open',
  url: 'http://localhost:3100', reuseExistingServer: false, timeout: 300000 }`.
  Add `"test": "playwright test"` to `scripts` in `aict-guide/package.json`. Check Context7 for
  the names of Playwright's output folders, then add them to `aict-guide/.gitignore`.
- [X] T004 **RED** Create `aict-guide/tests/site.spec.js` with test `site-title` (contract C1):
  the home page `<title>` contains "AICT Course Guide" and the navbar title is
  "AICT Course Guide". Run `npm test` and confirm it **fails** (title is still "My Site"). This
  proves the harness builds, serves and checks the real site.

**Checkpoint**: the harness runs, and the first test fails for the right reason. Owner OK.

---

## Phase 2: Foundational — Site foundation (setup tasks d–g) and Module 1 frame

**Purpose**: Everything every lesson needs. **No lesson work starts until this phase is done.**

### Site identity and strict link checks

- [X] T005 **GREEN for `site-title`** In `aict-guide/docusaurus.config.js`: set
  `title: 'AICT Course Guide'` and a one-line `tagline`. Set `navbar.title` to
  'AICT Course Guide' and `navbar.logo.alt` to match. Remove the GitHub navbar item and both
  `editUrl` options. Remove `organizationName` and `projectName` (they are GitHub Pages deploy
  settings; deployment is out of scope). Replace the footer `links` with an empty list and keep
  only a copyright line for "AICT Course Guide". Run `npm test` and confirm `site-title`
  **passes**.
- [X] T006 **Strict links (research R2)**.
  - **RED**: add a temporary broken anchor link (to a heading that does not exist) to
    `aict-guide/docs/intro.mdx`. Run `npm run build` and confirm the build **still passes**,
    printing only a warning. This shows the gap.
  - **GREEN**: add `onBrokenAnchors: 'throw'` and
    `markdown: { hooks: { onBrokenMarkdownLinks: 'throw' } }` to
    `aict-guide/docusaurus.config.js`. Run `npm run build` and confirm it now **fails** on that
    link. Remove the temporary link and confirm `npm run build` passes.

### Remove blog and tutorial — docs-only mode (setup task d, BK-06, research R1)

- [X] T007 **RED** Add tests `home-at-root`, `no-blog` and `no-tutorial` (contract C1) to
  `aict-guide/tests/site.spec.js`. `no-blog` and `no-tutorial` also check that the folders
  `build/blog`, `build/tutorial-basics` and `build/tutorial-extras` do not exist (Node `fs`,
  read after the webServer build). Run `npm test` and confirm all three **fail**.
- [X] T008 **GREEN** Apply docs-only mode:
  - `aict-guide/docusaurus.config.js`: `docs.routeBasePath: '/'`, `blog: false`. Remove the
    navbar `Blog` item. Change the `docSidebar` navbar item to `sidebarId: 'bookSidebar'`,
    `label: 'Book'`.
  - `aict-guide/sidebars.js`: rename `tutorialSidebar` to `bookSidebar` (still
    `{type: 'autogenerated', dirName: '.'}`).
  - Delete `aict-guide/blog/`, `aict-guide/src/pages/` (index.js, index.module.css,
    markdown-page.mdx), `aict-guide/src/components/HomepageFeatures/`,
    `aict-guide/docs/tutorial-basics/`, `aict-guide/docs/tutorial-extras/`, and
    `aict-guide/docs/intro.mdx`.
  - Create `aict-guide/docs/intro.md` with front matter `slug: /`, H1 "AICT Course Guide", and
    a 2–3 sentence welcome (who the book is for, how it is organized). No diagram yet.
  - Run `npm test` and confirm `home-at-root`, `no-blog`, `no-tutorial` and `site-title` all
    **pass**.

### Mermaid and the home-page diagram (setup task e, BK-03, BK-04, research R3, R4, R11)

- [X] T009 **RED** Create `aict-guide/tests/diagrams.spec.js` with `home-diagram`,
  `diagram-accessible` and `diagram-in-words` (contract C2) for `/`. Run `npm test` and confirm
  they **fail**.
- [X] T010 **GREEN**
  - Run `npm install --save @docusaurus/theme-mermaid` in `aict-guide/`. Confirm its version
    equals `@docusaurus/core` (3.10.2). If it does not, **stop** and tell the owner.
  - `aict-guide/docusaurus.config.js`: add `themes: ['@docusaurus/theme-mermaid']`. Add
    `mermaid: true` inside the existing `markdown` object (keep `hooks`). Add
    `themeConfig.mermaid.theme: {light: 'neutral', dark: 'dark'}`.
  - `aict-guide/docs/intro.md`: add the section "How to use this book in class" with a Mermaid
    flowchart (top-to-bottom): Before class → Teacher demo → Student task → Check questions.
    Include `accTitle` and `accDescr`. Directly below it, add a paragraph starting
    "**Diagram in words:**".
  - Run `npm test`; all tests **pass**. Owner checks the diagram in light and dark mode
    (quickstart step 4).

### Sidebar with 16 modules (setup task f, BK-01, research R5)

- [X] T011 **RED** Add `sixteen-modules` and `module-placeholders` (contract C1) to
  `aict-guide/tests/site.spec.js`. The expected labels, in order, are: Module 1: Computer Basics;
  Module 2: Typing Skills; Module 3: Internet Essentials; Module 4: MS Word; Module 5: MS
  PowerPoint; Module 6: Presentation Skills; Module 7: MS Excel; Module 8: InPage Urdu; Module
  9: Google Workspace; Module 10: AI Basics; Module 11: HTML & CSS; Module 12: Adobe Photoshop;
  Module 13: Adobe Illustrator; Module 14: Canva; Module 15: Social Media Marketing; Module 16:
  Freelancing Intro. Run `npm test` and confirm both **fail**.
- [X] T012 **GREEN** For each of the 16 modules, create a folder under `aict-guide/docs/` using
  the folder names in `specs/book-spec.md` §3 (`module-01-computer-basics` …
  `module-16-freelancing-intro`). Each folder gets:
  - a `_category_.json` with `label` ("Module N: <Title>") and `position` (N);
  - an `index.md` with front matter `title: "Module N: <Title>"` and only the H1 (placeholder,
    no content).

  Run `npm test` and confirm all tests **pass**. Note from research R5: Modules 2–16 appear as
  links, not expandable sections, until they have lessons.

### Project guidance file (setup task g)

- [X] T013 Create `aict-guide/CLAUDE.md` as a **short pointer only** (owner decision
  2026-10-11). It says the project guide is `../CLAUDE.md` and must be read first, and that the
  rules are in `../.specify/memory/constitution.md` and `../specs/constitution.md`. It repeats
  nothing else. There is no automated test (it is not a site page); the owner reviews it.

### Module 1 frame and lesson test suite (contracts C3, C4)

- [X] T014 **RED** Create the lesson test suite:
  - `aict-guide/tests/lessons.js`: exports an array of `{ url, title }`. It starts **empty**;
    each lesson task adds its entry.
  - `aict-guide/tests/lessons.spec.js`: for every entry in `lessons.js`, runs every check in
    contract C3 (`sections-in-order`, `goal-sentence`, `has-diagram`, `key-terms-table`,
    `student-task-end`, `three-questions`, `common-mistakes`, `sources`, and `version-tabs`
    where tab groups exist).
  - `aict-guide/tests/module-01.spec.js`: `overview-title`, `overview-outcomes` and
    `overview-lesson-links` (contract C4) for `/module-01-computer-basics`.

  Run `npm test` and confirm `overview-outcomes` **fails** (the placeholder has no outcomes).
- [X] T015 **GREEN** Write `aict-guide/docs/module-01-computer-basics/index.md`:
  - H1 "Module 1: Computer Basics";
  - a short summary (spec §1);
  - H2 "Learning Outcomes" with LO-1 … LO-9 (spec §2) in plain words;
  - H2 "Lessons" with an empty list for now (each lesson task adds its link, so the build
    never has a broken link).

  Add the `:lang(ur)` rule to `aict-guide/src/css/custom.css` (slightly larger font size and
  line height; research R8). Run `npm test` and confirm all tests **pass**. The owner reviews
  the summary and outcomes.

**Checkpoint**: foundation done. Setup tasks d–g are complete, the 16-module sidebar works, and
the Mermaid diagram renders and is accessible. Every lesson test is ready and waiting for
entries. Owner OK before lessons start.

---

## How every lesson phase works (US1–US9)

Each lesson has the same 4 tasks:

1. **RED**: add `{ url: '/module-01-computer-basics/<slug>', title: 'Lesson 1.N: <Title>' }` to
   `aict-guide/tests/lessons.js`. Run `npm test` and confirm the new lesson's checks and
   `overview-lesson-links` **fail**.
2. **VERIFY**: list every technical claim and every software step the lesson needs. Check each
   one in Context7 first, then the maker's official documentation (research R10). Record the
   sources. Report any claim that can't be confirmed, and mark any unconfirmed software step for
   a `:::warning[UNVERIFIED]` box. Windows steps are checked for **both** Windows 10 and
   Windows 11. **Stop and show the owner the verified-claims list before writing.**
3. **GREEN**: write `aict-guide/docs/module-01-computer-basics/<slug>.mdx` following
   data-model.md:
   - front matter `title` and `sidebar_position`;
   - 8 H2 sections in order;
   - Key Terms table with columns Term / Simple meaning / Urdu meaning, with Urdu in
     `<span lang="ur" dir="rtl">`;
   - ≥ 1 Mermaid diagram with `accTitle`/`accDescr` and "**Diagram in words:**";
   - `<Tabs groupId="windows-version">` wherever Windows 10 and 11 differ;
   - Sources.

   Add the lesson's link to the "Lessons" list in
   `aict-guide/docs/module-01-computer-basics/index.md`. Run `npm test` and confirm **all**
   tests pass.
4. **REVIEW** (owner): plain language, Urdu meanings, fits 60 minutes (AC-C10), and the
   lesson-specific criteria. Fix anything the owner raises, run `npm test` again, then the owner
   approves (AC-C9).

---

## Phase 3: User Story 1 — Lesson 1.1 What Is a Computer? (P1) 🎯 MVP

**Goal**: the teacher can teach the four jobs of a computer (LO-1).
**Independent test**: `npm test` passes the C3 checks for `/module-01-computer-basics/what-is-a-computer`, and the owner confirms AC-1.1-a…c.

- [X] T016 [US1] **RED** Add `{ url: '/module-01-computer-basics/what-is-a-computer', title: 'Lesson 1.1: What Is a Computer? Input, Processing, Output and Storage' }` to `aict-guide/tests/lessons.js`; run `npm test`; confirm the new checks fail
- [X] T017 [US1] **VERIFY** the definitions of input, processing, output, storage and data, and every example used (AC-1.1-b); record sources for `aict-guide/docs/module-01-computer-basics/what-is-a-computer.mdx`; stop for owner review
- [X] T018 [US1] **GREEN** Write `aict-guide/docs/module-01-computer-basics/what-is-a-computer.mdx` (`sidebar_position: 1`). The diagram is Input → Processing → Output with Storage linked to Processing. One Check Question asks the student to sort examples into the four jobs (AC-1.1-c). Add its link to `aict-guide/docs/module-01-computer-basics/index.md`; run `npm test`; all pass
- [X] T019 [US1] **REVIEW** Owner checks AC-1.1-a…c, AC-C4, AC-C7 (Urdu), AC-C10 and approves `aict-guide/docs/module-01-computer-basics/what-is-a-computer.mdx`

**Checkpoint**: MVP: the first teachable lesson, on a working site.

---

## Phase 4: User Story 2 — Lesson 1.2 Hardware and Software (P2)

**Goal**: LO-2. **Independent test**: C3 checks pass for `/module-01-computer-basics/hardware-and-software`; the owner confirms AC-1.2-a…c.

- [X] T020 [US2] **RED** Add `{ url: '/module-01-computer-basics/hardware-and-software', title: 'Lesson 1.2: Hardware and Software' }` to `aict-guide/tests/lessons.js`; run `npm test`; confirm failure
- [X] T021 [US2] **VERIFY** the definitions of hardware, software, program and app, and every software example named (AC-1.2-c); record sources for `aict-guide/docs/module-01-computer-basics/hardware-and-software.mdx`; stop for owner review
- [X] T022 [US2] **GREEN** Write `aict-guide/docs/module-01-computer-basics/hardware-and-software.mdx` (`sidebar_position: 2`): ≥ 3 examples each (AC-1.2-a). The Student Task sorts ≥ 6 items (AC-1.2-b). Add the link to `index.md`; run `npm test`; all pass
- [ ] T023 [US2] **REVIEW** Owner checks AC-1.2-a…c and the common criteria, then approves `aict-guide/docs/module-01-computer-basics/hardware-and-software.mdx`

---

## Phase 5: User Story 3 — Lesson 1.3 Parts of a Computer and Their Jobs (P3)

**Goal**: LO-3. **Independent test**: C3 checks pass for `/module-01-computer-basics/parts-of-a-computer`; the owner confirms AC-1.3-a…c.

- [X] T024 [US3] **RED** Add `{ url: '/module-01-computer-basics/parts-of-a-computer', title: 'Lesson 1.3: Parts of a Computer and Their Jobs' }` to `aict-guide/tests/lessons.js`; run `npm test`; confirm failure
- [X] T025 [US3] **VERIFY** Ask the owner to confirm which parts are on the lab desktops (AC-1.3-a). Verify each part's name and job and record sources for `aict-guide/docs/module-01-computer-basics/parts-of-a-computer.mdx`; stop for owner review
- [X] T026 [US3] **GREEN** Write `aict-guide/docs/module-01-computer-basics/parts-of-a-computer.mdx` (`sidebar_position: 3`): each part linked to one of the four jobs from Lesson 1.1 (AC-1.3-b). In the Student Task, students point to each part (AC-1.3-c). Add the link to `index.md`; run `npm test`; all pass
- [ ] T027 [US3] **REVIEW** Owner checks AC-1.3-a…c and the common criteria, then approves `aict-guide/docs/module-01-computer-basics/parts-of-a-computer.mdx`

---

## Phase 6: User Story 4 — Lesson 1.4 Starting Up and Shutting Down Safely (P4)

**Goal**: LO-4. **Independent test**: C3 checks, including `version-tabs`, pass for `/module-01-computer-basics/starting-up-and-shutting-down`; the owner confirms AC-1.4-a…c.

- [X] T028 [US4] **RED** Add `{ url: '/module-01-computer-basics/starting-up-and-shutting-down', title: 'Lesson 1.4: Starting Up and Shutting Down Safely' }` to `aict-guide/tests/lessons.js`; run `npm test`; confirm failure
- [X] T029 [US4] **VERIFY** Start-up, sign-in and shut-down steps for **Windows 10 and Windows 11** from Microsoft official pages, plus why a correct shut-down matters (AC-1.4-a, -b). Ask the owner whether the lab uses sign-in. Record sources and any UNVERIFIED steps for `aict-guide/docs/module-01-computer-basics/starting-up-and-shutting-down.mdx`; stop for owner review
- [X] T030 [US4] **GREEN** Write `aict-guide/docs/module-01-computer-basics/starting-up-and-shutting-down.mdx` (`sidebar_position: 4`): `<Tabs groupId="windows-version">` where the versions differ. Common Mistakes includes switching off at the wall without shutting down (AC-1.4-c). Add the link to `index.md`; run `npm test`; all pass
- [ ] T031 [US4] **REVIEW** Owner checks AC-1.4-a…c and the common criteria, and tests any UNVERIFIED step on Windows 11 (laptop) and Windows 10 (lab). Then the owner approves `aict-guide/docs/module-01-computer-basics/starting-up-and-shutting-down.mdx`

---

## Phase 7: User Story 5 — Lesson 1.5 Using the Mouse (P5)

**Goal**: LO-5. **Independent test**: C3 checks pass for `/module-01-computer-basics/using-the-mouse`; the owner confirms AC-1.5-a…c.

- [X] T032 [US5] **RED** Add `{ url: '/module-01-computer-basics/using-the-mouse', title: 'Lesson 1.5: Using the Mouse' }` to `aict-guide/tests/lessons.js`; run `npm test`; confirm failure
- [X] T033 [US5] **VERIFY** the names and descriptions of the mouse parts and the five actions (point, click, double-click, right-click, drag) and scrolling. If an online practice page is proposed, check that it works and list it (AC-1.5-c). Record sources for `aict-guide/docs/module-01-computer-basics/using-the-mouse.mdx`; stop for owner review
- [X] T034 [US5] **GREEN** Write `aict-guide/docs/module-01-computer-basics/using-the-mouse.mdx` (`sidebar_position: 5`): one demo step and one practice step per action (AC-1.5-a). Common Mistakes includes moving while clicking and slow double-clicks (AC-1.5-b). The task works without installing anything. Add the link to `index.md`; run `npm test`; all pass
- [ ] T035 [US5] **REVIEW** Owner checks AC-1.5-a…c and the common criteria, then approves `aict-guide/docs/module-01-computer-basics/using-the-mouse.mdx`

---

## Phase 8: User Story 6 — Lesson 1.6 Keyboard Basics (P6)

**Goal**: LO-6. **Independent test**: C3 checks pass for `/module-01-computer-basics/keyboard-basics`; the owner confirms AC-1.6-a…c.

- [ ] T036 [US6] **RED** Add `{ url: '/module-01-computer-basics/keyboard-basics', title: 'Lesson 1.6: Keyboard Basics' }` to `aict-guide/tests/lessons.js`; run `npm test`; confirm failure
- [ ] T037 [US6] **VERIFY** every key group and key name and what each key does (AC-1.6-a). Record sources for `aict-guide/docs/module-01-computer-basics/keyboard-basics.mdx`; stop for owner review
- [ ] T038 [US6] **GREEN** Write `aict-guide/docs/module-01-computer-basics/keyboard-basics.mdx` (`sidebar_position: 6`): no keyboard shortcuts (AC-1.6-b), and a clear note that typing practice is in Module 2 (AC-1.6-c). Add the link to `index.md`; run `npm test`; all pass
- [ ] T039 [US6] **REVIEW** Owner checks AC-1.6-a…c and the common criteria, then approves `aict-guide/docs/module-01-computer-basics/keyboard-basics.mdx`

---

## Phase 9: User Story 7 — Lesson 1.7 The Operating System and the Desktop (P7)

**Goal**: LO-7. **Independent test**: C3 checks, including `version-tabs`, pass for `/module-01-computer-basics/operating-system-and-desktop`; the owner confirms AC-1.7-a…c.

- [X] T040 [US7] **RED** Add `{ url: '/module-01-computer-basics/operating-system-and-desktop', title: 'Lesson 1.7: The Operating System and the Desktop' }` to `aict-guide/tests/lessons.js`; run `npm test`; confirm failure
- [X] T041 [US7] **VERIFY** what an operating system does, and the names and places of the desktop, icons, Start menu, taskbar and window buttons, for **Windows 10 and Windows 11**, plus the steps to open and close a program (AC-1.7-a, -b). Record sources and any UNVERIFIED steps for `aict-guide/docs/module-01-computer-basics/operating-system-and-desktop.mdx`; stop for owner review
- [X] T042 [US7] **GREEN** Write `aict-guide/docs/module-01-computer-basics/operating-system-and-desktop.mdx` (`sidebar_position: 7`): Tabs where the versions differ, and no untaught technical words (AC-1.7-c). Add the link to `index.md`; run `npm test`; all pass
- [ ] T043 [US7] **REVIEW** Owner checks AC-1.7-a…c and the common criteria, and tests any UNVERIFIED step on both versions. Then the owner approves `aict-guide/docs/module-01-computer-basics/operating-system-and-desktop.mdx`

---

## Phase 10: User Story 8 — Lesson 1.8 Files, Folders, Saving and Deleting (P8)

**Goal**: LO-8. **Independent test**: C3 checks, including `version-tabs`, pass for `/module-01-computer-basics/files-folders-saving-deleting`; the owner confirms AC-1.8-a…d.

- [X] T044 [US8] **RED** Add `{ url: '/module-01-computer-basics/files-folders-saving-deleting', title: 'Lesson 1.8: Files, Folders, Saving and Deleting' }` to `aict-guide/tests/lessons.js`; run `npm test`; confirm failure
- [X] T045 [US8] **VERIFY** for **Windows 10 and Windows 11**: that Paint is available (AC-1.8-b; if this can't be confirmed for either version, **stop and tell the owner** before writing). Also verify the steps to open Paint and save a drawing with a name into a chosen folder, make a folder in File Explorer, find and open the file, delete it, and restore it from the Recycle Bin (AC-1.8-a, -d). Record sources and any UNVERIFIED steps for `aict-guide/docs/module-01-computer-basics/files-folders-saving-deleting.mdx`; stop for owner review
- [X] T046 [US8] **GREEN** Write `aict-guide/docs/module-01-computer-basics/files-folders-saving-deleting.mdx` (`sidebar_position: 8`): Tabs where the versions differ. Common Mistakes includes saving without choosing a folder (AC-1.8-c). Add the link to `index.md`; run `npm test`; all pass. **If the draft does not fit 60 minutes** (AC-C10), stop and propose the split from spec §5 (1.8 Files/Saving, 1.9 Deleting, Caring becomes 1.10). A split needs the owner's approval and a spec update before continuing
- [ ] T047 [US8] **REVIEW** Owner checks AC-1.8-a…d and the common criteria, and tests any UNVERIFIED step on both versions. Then the owner approves `aict-guide/docs/module-01-computer-basics/files-folders-saving-deleting.mdx`

---

## Phase 11: User Story 9 — Lesson 1.9 Caring for Your Computer (P9)

**Goal**: LO-9. **Independent test**: C3 checks pass for `/module-01-computer-basics/caring-for-your-computer`; the owner confirms AC-1.9-a…c.

- [X] T048 [US9] **RED** Add `{ url: '/module-01-computer-basics/caring-for-your-computer', title: 'Lesson 1.9: Caring for Your Computer' }` to `aict-guide/tests/lessons.js`; run `npm test`; confirm failure
- [X] T049 [US9] **VERIFY** every safety and health statement against an official or recognised source (AC-1.9-a). Ask the owner about lab rules (AC-1.9-b). Record sources for `aict-guide/docs/module-01-computer-basics/caring-for-your-computer.mdx`; stop for owner review
- [X] T050 [US9] **GREEN** Write `aict-guide/docs/module-01-computer-basics/caring-for-your-computer.mdx` (`sidebar_position: 9`): the Student Task is a short checklist (AC-1.9-c). Add the link to `index.md`; run `npm test`; all pass
- [ ] T051 [US9] **REVIEW** Owner checks AC-1.9-a…c and the common criteria, then approves `aict-guide/docs/module-01-computer-basics/caring-for-your-computer.mdx`

---

## Phase 12: Polish — Module check

- [ ] T052 Run the full `npm test` and `npm run build` in `aict-guide/`, and confirm all tests pass and the build is clean (M1-03, BK-02…BK-05). Walk through `specs/module-01-computer-basics/quickstart.md` steps 3–6 with the owner
- [ ] T053 Search `aict-guide/docs/module-01-computer-basics/` for "UNVERIFIED" and give the owner the full list, each with the lesson, step and Windows version(s) to test (M1-04). The module is "ready for teaching" only when the list is empty
- [ ] T054 Mark every task done in `specs/module-01-computer-basics/tasks.md` and list the changed files for the owner to commit

---

## Dependencies & Execution Order

- **Phase 1 (Setup)** → **Phase 2 (Foundational)** → **Phases 3–11 (US1–US9)** → **Phase 12**.
- Phase 2 blocks all lessons: the lesson tests (T014), the overview page (T015) and Mermaid
  (T010) must exist first.
- **Lessons are taught in order and written in order.** US1→US9 have no code dependency on
  each other, but:
  - US3 (parts) reuses the four jobs from US1;
  - US7 and US8 assume the mouse skills from US5;
  - so they are written in teaching order to keep cross-references correct.
- Inside each lesson: RED → VERIFY → GREEN → REVIEW, strictly.
- Every task ends with the owner's OK (constitution Principle IV).

## Parallel Opportunities

Because of the owner-OK rule, tasks run one at a time. Where order technically does not
matter:
- The VERIFY tasks for lessons with no Windows steps (T017, T021, T033, T037, T049) could be
  researched ahead of their phase. They still have to be presented to the owner one at a time.
- T013 (`aict-guide/CLAUDE.md`) does not depend on T011–T012.

## Implementation Strategy

1. **Foundation first**: Phases 1–2. The site is a clean, tested book with 16 modules, but no
   lessons yet.
2. **MVP = US1 (Lesson 1.1)**: the first lesson you can teach. Stop and check it in a real class
   if you want before continuing.
3. **Incremental**: one lesson at a time, US2 → US9. Each adds a teachable lesson without
   breaking earlier ones, because the whole suite runs every time.
4. **Ready for teaching** after T053, when no UNVERIFIED markers are left.

## Notes

- RED must be seen failing for the right reason before GREEN.
- Never invent menu names, buttons or shortcuts. Unconfirmed software steps go in
  `:::warning[UNVERIFIED]` boxes.
- The owner commits after each task or group. Claude never runs git.
