# Tasks: Module 7: MS Excel

**Spec**: `specs/module-07-ms-excel/spec.md` (approved 2026-10-12). **Plan**: same stack and tests as
`specs/module-01-computer-basics/plan.md`; lesson tests are data-driven from `aict-guide/tests/lessons.js`.
**Review**: per module (build constitution v1.2.0, Principle IV).

## Setup

- [X] E001 **RED** Add all lessons to `aict-guide/tests/lessons.js` and the overview to `aict-guide/tests/module-overviews.spec.js`; run the tests; confirm the new checks fail
- [X] E002 Write `aict-guide/docs/module-07-ms-excel/index.md` (outcomes + lesson links)

## Lessons (each: VERIFY on support.microsoft.com for Office 2016/2019 → GREEN write the page)

- [X] E003 Lesson 7.1: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/starting-excel.mdx`
- [X] E004 Lesson 7.2: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/entering-editing-saving-data.mdx`
- [X] E005 Lesson 7.3: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/rows-and-columns.mdx`
- [X] E006 Lesson 7.4: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/formatting-cells.mdx`
- [X] E007 Lesson 7.5: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/number-formats.mdx`
- [X] E008 Lesson 7.6: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/first-formulas.mdx`
- [X] E009 Lesson 7.7: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/fill-handle.mdx`
- [X] E010 Lesson 7.8: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/sum-and-average.mdx`
- [X] E011 Lesson 7.9: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/min-max-count.mdx`
- [X] E012 Lesson 7.10: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/sorting-data.mdx`
- [X] E013 Lesson 7.11: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/simple-chart.mdx`
- [X] E014 Lesson 7.12: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/page-setup-and-printing.mdx`
- [X] E015 Lesson 7.13: VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/project-result-sheet.mdx`

## Module check

- [X] E016 Run the full `npm test` and `npm run build`; all pass with zero warnings
- [X] E017 List every UNVERIFIED box for the owner to test on a lab computer (Office 2016/2019)
- [ ] E018 **REVIEW** Owner reviews the whole module and approves it

## Practical upgrade (specs/practical-upgrade/spec.md, approved 2026-10-16)

- [X] E-P01 Toolkit: `aict-guide/tools/practice-files/` (build.py, verify.py, xlsxkit.py) and `src/components/PracticeFile.js`
- [X] E-P02 **RED** `tests/practice-files.spec.js` + `tests/practice-files.js`; new lessons in `tests/lessons.js`
- [X] E-P03 Pilot: Lesson 7.8 files (marks, weekly-sales) built, verified, linked
- [X] E-P04 Files for Lessons 7.2–7.7
- [X] E-P05 Files for Lessons 7.9–7.13
- [X] E-P06 Lesson 7.14: Fixed Cells: Absolute References — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/absolute-references.mdx` + files
- [X] E-P07 Lesson 7.15: Making Decisions With IF — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/if-function.mdx` + files
- [X] E-P08 Lesson 7.16: More Decisions: IFS, AND and OR — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/ifs-and-or.mdx` + files
- [X] E-P09 Lesson 7.17: Counting: COUNTA, COUNTBLANK, COUNTIF and COUNTIFS — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/counting-functions.mdx` + files
- [X] E-P10 Lesson 7.18: Adding With Conditions: SUMIF, SUMIFS and AVERAGEIF — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/sumif-sumifs-averageif.mdx` + files
- [X] E-P11 Lesson 7.19: Finding Data: VLOOKUP and XLOOKUP — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/vlookup-and-xlookup.mdx` + files
- [X] E-P12 Lesson 7.20: Errors and Rounding: IFERROR and ROUND — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/iferror-and-round.mdx` + files
- [X] E-P13 Lesson 7.21: Positions: RANK.EQ — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/rank-eq.mdx` + files
- [X] E-P14 Lesson 7.22: Joining and Changing Text — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/joining-and-changing-text.mdx` + files
- [X] E-P15 Lesson 7.23: Parts of Text: LEFT, RIGHT, MID and LEN — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/parts-of-text.mdx` + files
- [X] E-P16 Lesson 7.24: Dates: TODAY, NOW, Days Between Dates and DATEDIF — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/working-with-dates.mdx` + files
- [X] E-P17 Lesson 7.25: Excel 2021 Formulas: SORT, FILTER and UNIQUE — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/sort-filter-unique.mdx` + files
- [X] E-P18 Lesson 7.26: Filtering Data — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/filtering-data.mdx` + files
- [X] E-P19 Lesson 7.27: Conditional Formatting — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/conditional-formatting.mdx` + files
- [X] E-P20 Lesson 7.28: Freeze Panes for Long Lists — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/freeze-panes.mdx` + files
- [X] E-P21 Lesson 7.29: Project: Shop Stock and Sales Register — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/project-stock-and-sales.mdx` + files
- [X] E-P22 Lesson 7.30: Project: Customer Bill With Discount — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/project-customer-bill.mdx` + files
- [X] E-P23 Lesson 7.31: Project: Monthly Salary Sheet — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/project-salary-sheet.mdx` + files
- [X] E-P24 Lesson 7.32: Project: Staff Attendance Sheet — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/project-attendance-sheet.mdx` + files
- [X] E-P25 Lesson 7.33: Project: Result Card With Grades — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/project-result-card.mdx` + files
- [X] E-P26 Lesson 7.34: Project: Tuition Fee Record and Unpaid List — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/project-fee-record.mdx` + files
- [X] E-P27 Lesson 7.35: Project: Monthly Family Budget — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/project-family-budget.mdx` + files
- [X] E-P28 Lesson 7.36: Project: Electricity Bill Calculator — VERIFY + GREEN `aict-guide/docs/module-07-ms-excel/project-electricity-bill.mdx` + files
- [X] E-P29 Module 7 overview: three parts, new outcomes and links
- [X] E-P30 Install LibreOffice 24.8+ (owner) and verify XLOOKUP / SORT / FILTER / UNIQUE files
- [X] E-P31 Full `npm test` + `verify.py` pass; owner reviews
