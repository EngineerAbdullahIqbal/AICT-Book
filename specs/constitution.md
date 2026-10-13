# AICT Course Guide — Book Constitution

**Status**: APPROVED v1.4 (owner approved 2026-10-13)
**Change log**:
- v1.4 (2026-10-13): §1 the book speaks to students directly and never mentions the teacher;
  §2 every step says why you do it, with real-life examples; §4 unconfirmed steps are shown to
  students as an "If your screen looks different" box, and the owner's checks go in a private
  list (owner decision).
- v1.3 (2026-10-12): §1 and §5 make Urdu help optional. The owner explains in Urdu in class.
  A full English/Urdu language switch is planned later with its own spec (owner decision).
- v1.2 (2026-10-11): §3 adds university course pages (for example Stanford CS101) as
  recognised education sources (owner decision).
- v1.1 (2026-10-11): §3 adds which sources count for general computer concepts that have no
  software maker (owner decision).
**Created**: 2026-10-10
**Scope**: The permanent rules for the *content* of the book. Every module spec and every lesson
must follow them.

> **How this relates to `.specify/memory/constitution.md`** (owner decision, 2026-10-10: keep
> both, linked):
> - `.specify/memory/constitution.md` holds the rules for *how we build*: the Spec Kit workflow,
>   Test-First, small steps, and no git by Claude. Spec Kit reads that file for its plan gates.
> - **This file** holds the rules for *what we write*. It is the **single source** for the
>   content rules: audience, tone, verification, UNVERIFIED marking and quality. The other file
>   points here instead of repeating them.

---

## 1. Audience

- **Who**: absolute beginners in Pakistan taking the 1-year AICT computer course.
- Many students have **never used a computer**. Assume no prior knowledge of any kind:
  not of the mouse, not of the screen, not of English computer words.
- Students may be any age. Do not assume school-age examples only.
- **Students read the book directly.** It may be shown in class, but it always speaks to the
  student as "you". The book **never mentions the teacher**: no "teacher", "Teacher Demo",
  "Say: …" lines or "show your teacher". It gives the steps and the reason for each step.
- **Language**: **simple English**. Urdu help may be given in class.
  - The main text is in English.
  - Urdu text is **optional**. New lessons do not need Urdu. Lessons that already have Urdu
    meanings in Key Terms keep them.
  - Any Urdu text that is on a page is reviewed by the owner before the lesson is approved.
  - A full English/Urdu language switch for the whole site is planned for later. It needs its
    own spec. Until then, full translations remain out of scope.

## 2. Tone and Writing Style

- Warm, patient and encouraging. Never make the reader feel slow or foolish.
- Speak to the reader as "you".
- **Say why.** Every step or group of steps says what it is for ("so that…", "This keeps…").
- **Real life first.** Use real examples from daily life in Pakistan to show where the skill is used
  (a shop bill, a school result, a job application, a family budget).
- **Simple English**:
  - One idea per sentence.
  - Most sentences have 15 words or fewer. No sentence is longer than 25 words.
  - Use common words. Prefer "use" over "utilize", "start" over "initiate".
  - Active voice: "Click the button", not "The button should be clicked".
- **Explain every new term** the first time it appears in a lesson, in plain words, and add it to
  that lesson's Key Terms. A term explained in an earlier lesson may be used again. When it is,
  link back to the lesson that explains it.
- Use everyday examples that make sense in Pakistan (home, market, school, mobile phone, family
  shop). Examples must be neutral and respectful: no politics, no religious comparisons, no jokes
  about any group.
- Never use a word like "simply", "just" or "obviously". A step is not simple to a beginner.

## 3. Verification Rule (NON-NEGOTIABLE)

- **Every technical claim must be verified before it is written.** A technical claim is any
  statement about how a computer, program, website or device works, what it is called, or what
  it does.
- Verify through the **Context7 MCP server** first. When Context7 has no coverage (common for
  end-user software such as Windows, Microsoft Office or Adobe apps), use the **official
  documentation** from the company that makes the product (for example Microsoft Support or
  Adobe Help).
- For **general computer concepts** that have no software maker (for example "what is input",
  "what is hardware", or safe use of a computer), these sources count as verified:
  - **Microsoft official pages** (Microsoft Support, Microsoft Learn);
  - **recognised education sites**: well-known public or non-profit education sources (for
    example BBC Bitesize, GCFGlobal, Code.org), and **university course pages** (for example
    Stanford CS101).

  Each source is named and linked in the lesson's Sources section. A personal blog, forum, or
  random website does not count.
- Every lesson ends with a **Sources** section that lists each source used, so the owner can
  check it.
- **Never guess.** If a claim cannot be verified, it does not go in the lesson. If a software
  step cannot be verified, it is marked UNVERIFIED (Section 4).
- **Never invent** menu names, button names, icon names, or keyboard shortcuts.

## 4. The "UNVERIFIED" Marking Rule

Applies to **steps in software** (Microsoft Office, Adobe Photoshop, Adobe Illustrator, InPage,
Windows, and similar).

- A step is **verified** only when it comes from the official documentation for that software.
- If a step cannot be verified, the page shows it inside a student-friendly box that gives a
  **confirmed backup way** to do it, like this:

  ```md
  :::tip[If your screen looks different]

  Your screen may not show this button. Do this instead: (a confirmed way).

  :::
  ```

- Every such step is also listed, with what to check, in the owner's private list
  `specs/unverified-test-list.md`. The page itself never says "test" or "teacher".
- The box covers the **smallest possible part**: the single step or group of steps, never a
  whole lesson.
- After the owner tests the step on a lab computer:
  - If it works, the owner records the software version that was tested, and the marker is
    removed.
  - If it does not work, the step is corrected or removed.
- A module is **fully checked** only when its private list is empty. Until then, the backup way
  in each box keeps students moving.

## 5. Quality Standards

Every lesson must meet all of these before it counts as done:

1. **Complete template**: all lesson-template sections are present, in order (see
   `specs/book-spec.md`, Section 4).
2. **Plain language**: meets Section 2. Any Urdu text on the page has been
   reviewed by the owner (Section 1).
3. **Verified**: every technical claim has a source in the Sources section. Any step that can't
   be confirmed is marked UNVERIFIED (Sections 3–4).
4. **At least one diagram**, following the diagram standards in `specs/book-spec.md`, Section 5.
5. **Accessible**: every diagram has an accessible title and description. Every image has alt
   text.
6. **Builds cleanly**: `npm run build` passes with **zero** broken-link, broken-anchor, or
   broken-Markdown-link messages.
   - Verified Docusaurus behaviour (docs: *API → docusaurus.config.js*): broken page links stop
     the build by default (`onBrokenLinks: 'throw'`). Broken anchors and broken Markdown links
     only print a **warning** by default. So a passing build alone is not enough; the warnings
     must also be zero.
7. **Tested**: the automated tests for the lesson pass (see the Test-First rule in
   `.specify/memory/constitution.md`).
8. **Owner approved**: the owner has reviewed the lesson.

## 6. Out of Scope (until the owner asks)

- Translations, deployment, logins, quizzes that save scores, or any interactive features.

## 7. Changing This Constitution

- Only the owner can approve a change.
- Every change updates the version and date at the top of this file and gets a one-line note
  explaining what changed.
