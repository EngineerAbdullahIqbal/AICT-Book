# Quickstart: Checking the AICT Course Guide

**Date**: 2026-10-11 | **Plan**: [plan.md](./plan.md)

How the owner (or Claude) proves the work is correct. All commands run in
`~/Abdullah/global-coaching-center/book-guide/aict-guide`.

## Prerequisites

- Node.js ≥ 20 (`node -v` → v24.14.1 on the dev machine).
- Dependencies installed: `npm install`.
- Playwright's Chromium installed once: `npx playwright install chromium`.
  If the tests later fail with a message about missing system libraries, run this yourself
  (it asks for your sudo password): `npx playwright install --with-deps chromium`.

## 1. Build check (AC-C5)

```bash
npm run build
```

Expected: the command finishes without an error and creates the `build/` folder. A broken
link, anchor or Markdown link stops the build with an error (research R2).

## 2. Full automated test run

```bash
npm test
```

Expected: Playwright builds the site, serves it on port 3100, and every test passes. The
summary line shows `passed` and no `failed`. See [contracts/page-contracts.md](./contracts/page-contracts.md)
for what each test checks.

## 3. Look at the site yourself

```bash
npm run start
```

Open http://localhost:3000 and check:
- The home page is "AICT Course Guide" with the "How to use this book in class" diagram drawn as a picture.
- The sidebar shows Module 1 to Module 16 in order. There is no Blog link and no Tutorial.
- Module 1 opens to its overview and lists its lessons.

## 4. Light and dark mode

Use the light/dark mode switch in the navbar. Every diagram must be readable in both modes
(book-spec §5 rule 8).

## 5. Windows tabs (Lessons 1.4, 1.7, 1.8)

Pick "Windows 11" in one tab group. Every other tab group on the page switches to Windows 11
too.

## 6. Urdu text (owner check, needed once)

Open any lesson on the **Windows 11 laptop** and on the **projector**. Check that the Urdu
meanings in Key Terms are readable and in the right direction. If they are not, tell Claude.
A font will then be added (research R8).

## 7. UNVERIFIED steps (before teaching each lesson)

Search the lesson for "UNVERIFIED". Test each step on Windows 11 (laptop) and Windows 10 (lab
computer), as the box says. Tell Claude the result and the Windows version you tested, so the
marker can be removed or the step fixed.
