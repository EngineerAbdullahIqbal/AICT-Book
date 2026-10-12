# Site Design Specification: Front Page and Book Look

**Status**: APPROVED v1.0 (owner approved 2026-10-13; colours and fonts wait for the screenshots)
**Created**: 2026-10-13
**Governed by**: `specs/constitution.md` (v1.3), `specs/book-spec.md` (v1.1),
`.specify/memory/constitution.md` (v1.2.0)

---

## 1. Goal

Give the book a modern, book-like look in the style of the **AI Agent Factory** book
(agentfactory.panaversity.org): a proper front page and polished reading pages.

**Own branding, not a copy.** We follow the *layout and style* of that site. We do not copy its
code, name, logo, text, images or Panaversity branding. The book shows its own name:
**AICT Course Guide**, by **Global Coaching Center**.

**Reference**: the owner's screenshots of the Agent Factory front page and a chapter page
(project root, added 2026-10-13). Colours, spacing and fonts follow them where they suit our
readers.

## 2. Users and Constraints

- The main use is **on a projector in class**. Text must be large and high-contrast, readable
  from the back of a classroom. Where the Agent Factory style and projector readability
  conflict, readability wins.
- Absolute beginners will later read it themselves: simple English on the front page, same
  rules as the lessons (constitution §2).
- Works in light and dark mode, and on a phone.
- Static site only (GitHub Pages). No servers, no accounts.

## 3. Front Page (new, at `/`)

Sections, top to bottom:

| # | Section | Content |
|---|---------|---------|
| 1 | **Hero** | Book title "AICT Course Guide"; subtitle "A one-year computer course for complete beginners"; "Global Coaching Center"; buttons **Start Reading** (to the book start page) and **See the Modules** (to section 3); an own-design book cover picture. |
| 2 | **At a glance** | Short facts: 16 modules · 1 year · one lesson = one 60-minute class · lessons ready so far. |
| 3 | **The 16 modules** | One card per module, in course order: number, name, short line, icon. Each card links to the module's overview page. Modules with lessons show "Ready"; others show "Coming soon". |
| 4 | **How every lesson works** | The class flow as 4 cards: Goal → Teacher Demo → Student Task → Check Questions. |
| 5 | **For teachers and students** | Two cards: how the teacher uses the book in class; how students use it to practise and revise. |
| 6 | **Start call** | "Start with Module 1" button. |

The current book home page (the "How to use this book in class" page) moves from `/` to
`/start` and stays the first page in the sidebar. All lesson addresses stay the same.

## 4. Book Look (all pages)

- **Colours**: a new primary colour palette for light and dark mode (chosen from the
  screenshots), replacing the Docusaurus default green.
- **Fonts**: one clean sans-serif font for text and headings; a larger base font size for the
  projector.
- **Navbar**: own logo, book title, Book link, dark/light switch.
- **Footer**: Global Coaching Center, the book title, the year. No social links unless the owner
  gives them.
- **Lesson pages**: styled section headings, Key Terms tables, callout boxes (UNVERIFIED,
  Screenshot to add), and previous/next cards. Breadcrumbs stay on.
- **Logo and favicon**: own simple design. All Docusaurus sample images are removed.

## 5. Out of Scope

AI tutor or chat, sign-in, leaderboard, progress tracking, learner counts, language switch
(Urdu comes later with its own spec), social media links. Each needs its own spec.

## 6. Acceptance Criteria

- **D-01**: `/` shows the front page with the book title as its main heading, and "Global
  Coaching Center".
- **D-02**: **Start Reading** opens the book start page (`/start`), which has the docs sidebar.
- **D-03**: The front page shows 16 module cards in course order. Each links to its module
  page, and that page opens.
- **D-04**: Module cards for modules with lessons say "Ready"; the rest say "Coming soon".
- **D-05**: The book start page still draws its diagram (existing diagram tests move there).
- **D-06**: No Docusaurus sample images are used anywhere (logo, favicon, social card).
- **D-07**: All existing lesson and module tests still pass; the build has zero broken-link
  warnings, both locally and with the GitHub Pages address.
- **D-08**: Light and dark mode both readable (owner checks on the projector).
- **D-09**: The front page works on a phone width without sideways scrolling (owner checks).

## 7. Open Questions

Answered by the owner on 2026-10-13:
1. Search: **later**, with its own small spec after delivery.
2. Front-page sections in §3: **approved**.
