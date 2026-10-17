# Practical Upgrade Specification (Phase 1: MS Excel)

**Status**: APPROVED v1.0 (owner approved 2026-10-16)
**Created**: 2026-10-16
**Governed by**: `specs/constitution.md` (v1.4), `specs/book-spec.md` (v1.4),
`specs/module-07-ms-excel/spec.md`

---

## 1. Goal

The book must not be theory only. Every student who comes to the book should **open real files,
build real things, and check their own result** in Word, Excel, PowerPoint and later modules.

The owner's words (2026-10-16): students should "understand and build"; the Excel module needs
"Excel sheets and practical examples I can use and teach".

## 2. Owner Decisions (2026-10-16)

| Question | Decision |
|----------|----------|
| Practice files | **Starter + finished files** for every practical lesson. Small tables may still be typed to build typing skill. |
| Project themes | **All four**: shop & small business; office & jobs; school & tuition centre; home & family. |
| Excel depth | **Add key skills** needed by real projects: absolute references, IF, COUNTIF/SUMIF, XLOOKUP, filters, conditional formatting, freeze panes. |
| Order | **Excel first**, then Word, then PowerPoint (each later phase gets its own section in this spec, approved before work starts). |

## 3. Practice Files (all phases)

**What a lesson gives**: a **Practice files** box with two download links:
- **Starter file**: the data already typed in, ready for the student to work on.
- **Finished file**: the completed work, with the real formulas in the cells, so the student can
  compare and see how it was done.

**Where they live**: `aict-guide/static/files/<app>/<lesson-slug>/`, named
`<short-name>-starter.xlsx` and `<short-name>-finished.xlsx`. Lessons link to them with the
`<PracticeFile href="/files/…">` component (`src/components/PracticeFile.js`). A plain Markdown
link would let the bundler rename the file with a code (e.g. `marks-starter-4dd9….xlsx`); the
component keeps the real file name and adds the site's base address with Docusaurus's
`useBaseUrl` (Docusaurus docs: "Client API › useBaseUrl"; "Static assets").

**How they are made**: by a script kept in the project (`aict-guide/tools/practice-files/`), so
every file can be rebuilt the same way. No macros. Saved as normal `.xlsx` that Excel 2021 opens.

**Content rules**:
- Data is made up, realistic for Pakistan (rupees, Pakistani names, shops, schools, homes),
  neutral and respectful. No real people, companies or phone numbers.
- The layout matches the lesson exactly (same cells, same headings), so every cell address in
  the lesson is right; headings are bold; columns are wide enough to read.
- Finished files contain the **formulas**, not typed answers.

**How they are checked (verification rule for files)**:
1. Expected results are worked out separately in Python.
2. The finished file is recalculated with LibreOffice (headless) and every result cell is compared
   with the expected value. Any difference fails the check.
3. The lesson page states the correct results ("Check your work"), and they must match.
4. Every file uses only features taught in the lesson or earlier, and only features that exist in
   Excel 2021 (confirmed on Microsoft pages that apply to Excel 2021).
5. Functions newer than Excel 2007 are saved with Excel's internal prefixes (for example
   `_xlfn.IFS`, `_xlfn.XLOOKUP`, `_xlfn._xlws.SORT`), otherwise Excel shows `#NAME?` until the
   formula is retyped. The check fails any finished file without them.
6. XLOOKUP, SORT, FILTER and UNIQUE need LibreOffice 24.8 or newer for step 2. The owner
   installed LibreOffice 26.2 (snap) on 2026-10-17; verify.py uses the newest LibreOffice it finds
   and works in `tools/practice-files/recalc-work/` because the snap version cannot use /tmp.
   Any answer cell it cannot calculate is reported as pending, and pending blocks publishing.

## 4. Phase 1: Excel

### 4.1 New skill lessons (Part 2 of Module 7: More Skills)

The owner asked to cover **every important formula** (2026-10-16) and chose all four formula
groups: more logic, more counting and lookups, text and dates, rank/round and Excel 2021's new
formulas. Each lesson fits one 60-minute class.

| # | Lesson | Formulas / skills |
|---|--------|-------------------|
| 7.14 | Fixed Cells: Absolute References | `$A$1`, mixed `$A1` (only if sourced) |
| 7.15 | Making Decisions With IF | IF with numbers and text |
| 7.16 | More Decisions: IFS, AND and OR | IFS (grades), AND, OR inside IF |
| 7.17 | Counting: COUNTA, COUNTBLANK, COUNTIF and COUNTIFS | counting filled, empty and matching cells |
| 7.18 | Adding With Conditions: SUMIF, SUMIFS and AVERAGEIF | totals and averages that match a rule |
| 7.19 | Finding Data: VLOOKUP and XLOOKUP | look up a price, marks or salary by name or code |
| 7.20 | Errors and Rounding: IFERROR and ROUND | clean error messages; rupees to 0 or 2 decimals |
| 7.21 | Positions: RANK.EQ | 1st, 2nd, 3rd position in a result sheet |
| 7.22 | Joining and Changing Text: &, CONCAT, UPPER, LOWER, PROPER, TRIM | full names, clean lists |
| 7.23 | Parts of Text: LEFT, RIGHT, MID, LEN | codes, phone-number parts (made up) |
| 7.24 | Dates: TODAY, NOW, Days Between Dates, DATEDIF | due days, age, days late |
| 7.25 | Excel 2021 Formulas: SORT, FILTER and UNIQUE | lists that update themselves |
| 7.26 | Filtering Data | show only the rows you need |
| 7.27 | Conditional Formatting | colours that change with the numbers |
| 7.28 | Freeze Panes for Long Lists | headings stay visible |

### 4.2 Real projects (Part 3 of Module 7: Real Projects)

Each project is one lesson page (same template), with a starter and finished file, a real
story, the steps, and the correct results.

| # | Project | Theme | Main skills |
|---|---------|-------|-------------|
| 7.29 | Shop Stock and Sales Register | Shop | SUM, IF (low-stock alert), conditional formatting, filter |
| 7.30 | Customer Bill With Discount | Shop | multiply, SUM, absolute reference for discount %, ROUND, number formats |
| 7.31 | Monthly Salary Sheet | Office | basic + allowances − deductions, absolute reference, IF (bonus), SUM |
| 7.32 | Staff Attendance Sheet | Office | COUNTIF (P / A / L), percentage, conditional formatting, freeze panes |
| 7.33 | Result Card With Grades | School | SUM, percentage, IFS grades, RANK.EQ, COUNTIF passes, XLOOKUP, chart |
| 7.34 | Tuition Fee Record and Unpaid List | Tuition centre | SUMIF, COUNTIF, FILTER or filters, conditional formatting, dates |
| 7.35 | Monthly Family Budget | Home | SUM, percentage share, chart, conditional formatting for overspending |
| 7.36 | Electricity Bill Calculator | Home | units = new − old reading, rate × units, IF for a higher rate above a limit (**made-up practice rates**, clearly labelled, not the real tariff) |

### 4.3 Files for the existing lessons (Part 1)

Lessons 7.2–7.13 get starter and finished files for their Step by Step and Practice data.
Lesson 7.1 needs no file. Small tables are still typed in Step by Step; the starter file is
offered for Practice.

### 4.4 Module page

The Module 7 overview groups lessons under three headings: **Part 1: Excel Basics (7.1–7.13)**,
**Part 2: More Skills (7.14–7.28)**, **Part 3: Real Projects (7.29–7.36)**. Lesson addresses do
not change.

## 5. Acceptance Criteria

- **PU-01**: Every Excel lesson that uses data has a Practice files box with a starter and a
  finished file link; both links download successfully (automated test).
- **PU-02**: Every finished file passes the LibreOffice recalculation check against independently
  computed results (automated check run before each publish).
- **PU-03**: New lessons and projects meet all common lesson criteria (template, student voice,
  sources, diagrams, Show answer, etc.) and AC-E1…E3 of the Module 7 spec, for Excel 2021.
- **PU-04**: Every Excel 2021 step and function cites a Microsoft page whose "Applies to" list
  includes Excel 2021, or sits in an "If your screen looks different" box.
- **PU-05**: The electricity calculator says clearly that its rates are made up for practice.

## 6. Later Phases (outline only; each gets its own section and owner approval)

- **Phase 2, Word**: starter + finished `.docx` files, and real projects (shop invoice, office
  notice, job application, CV, school certificate, event invitation, newsletter).
- **Phase 3, PowerPoint**: starter + finished `.pptx` files and real projects (shop products,
  school event, office report, health-awareness talk).
- **Later modules** (Internet, InPage, Google Workspace, …): practical tasks in each module spec.

## 7. Open Questions

Answered by the owner on 2026-10-16:
1. New skill lessons: **approved, and cover every important formula** (all four formula groups).
2. Projects: **all 8 approved**.
3. Electricity calculator: **made-up simple practice rates**, clearly labelled.
4. Files for existing lessons 7.2–7.13: **in this phase**.
