# Module 7 Specification: MS Excel

**Status**: APPROVED v1.0 (owner approved 2026-10-12)
**Created**: 2026-10-12
**Module folder**: `module-07-ms-excel`
**Governed by**: `specs/constitution.md` (v1.3), `specs/book-spec.md` (v1.1)

---

## 1. Module Summary

Students learn to keep records and do calculations in Microsoft Excel: typing data, making it
easy to read, adding totals and averages with formulas, sorting, making a chart and printing.
The module ends with a project: a student result sheet.

**Prerequisites**: Module 1 (mouse, keyboard, files and saving). Module 4 (Word) taught the
ribbon, saving and printing; Excel lessons link back to those lessons instead of teaching them
again in full.

**Target software**: **Microsoft Excel 2016 / Excel 2019** on Windows (the lab computers).
- Every step comes from a Microsoft Support page whose "Applies to" list includes Excel 2016
  or Excel 2019.
- A step that can't be confirmed for these versions goes in an UNVERIFIED box
  (constitution §4). The owner tests it on a lab computer.

**Formulas and function names** (SUM, AVERAGE, MIN, MAX, COUNT): exact spelling and behaviour
come from Microsoft Support function pages.

**Keyboard shortcuts**: allowed only when a Microsoft Support page lists them for Excel.

**Money**: examples use Pakistani rupees, written as "Rs" in the text. Excel's currency format
for rupees is taught only if the steps can be verified; otherwise the lesson uses plain
numbers with a "Rs" column heading.

**Pictures**: no screenshots tonight; `:::info[Screenshot to add]` boxes where useful.

**Practice data**: small tables shown on the page (5–10 rows) that students type themselves.

## 2. Learning Outcomes

By the end of Module 7, the student can:

- **LO-1**: Open Excel and name the workbook, worksheet, row, column, cell and cell address.
- **LO-2**: Type text and numbers into cells, edit and clear a cell, and save the workbook.
- **LO-3**: Change column width and row height, and insert and delete rows and columns.
- **LO-4**: Make a table easy to read with font, fill colour, borders and alignment.
- **LO-5**: Apply number formats (number, currency or plain number with "Rs", percentage, date).
- **LO-6**: Write a formula with +, −, × and ÷ using cell addresses.
- **LO-7**: Copy a formula down a column with the fill handle.
- **LO-8**: Use SUM and AVERAGE, including AutoSum.
- **LO-9**: Use MIN, MAX and COUNT.
- **LO-10**: Sort a list from A to Z and from smallest to largest.
- **LO-11**: Make a column chart from a small table.
- **LO-12**: Set up a worksheet for printing and print it.
- **LO-13**: Build a result sheet with totals, averages, percentages and a chart.

## 3. Lesson List (for owner approval)

| # | Lesson | Main outcome |
|---|--------|--------------|
| 7.1 | Starting Excel: Workbooks, Worksheets and Cells | LO-1 |
| 7.2 | Entering, Editing and Saving Data | LO-2 |
| 7.3 | Rows and Columns: Width, Height, Insert and Delete | LO-3 |
| 7.4 | Formatting Cells: Font, Fill, Borders and Alignment | LO-4 |
| 7.5 | Number Formats: Money, Percentages and Dates | LO-5 |
| 7.6 | Your First Formulas | LO-6 |
| 7.7 | Copying Formulas with the Fill Handle | LO-7 |
| 7.8 | Functions: SUM and AVERAGE | LO-8 |
| 7.9 | Functions: MIN, MAX and COUNT | LO-9 |
| 7.10 | Sorting Data | LO-10 |
| 7.11 | Making a Simple Chart | LO-11 |
| 7.12 | Page Setup and Printing a Worksheet | LO-12 |
| 7.13 | Project: Student Result Sheet | LO-13 |

Why this order: students first learn to type and arrange data (7.1–7.5), then calculate
(7.6–7.9), then sort, show and print (7.10–7.12). The project uses everything.

## 4. Acceptance Criteria — All Lessons

The same common criteria as Module 1 (`specs/module-01-computer-basics/spec.md` §4, AC-C1 to
AC-C10), with these changes:
- **AC-C7**: Key Terms has 2 columns (Term, Simple meaning). No Urdu needed.
- **AC-E1**: Every Excel step and every function cites a Microsoft Support page that applies to
  Excel 2016 or Excel 2019, or is in an UNVERIFIED box.
- **AC-E2**: Every formula in a lesson shows the data it uses and the correct result, so the
  teacher and students can check their answer. Results are calculated and double-checked
  before writing.
- **AC-E3**: Practice data uses everyday examples from Pakistan (shop sales, monthly
  household expenses, class marks) with made-up names.

## 5. Lessons in Detail

### 7.1 Starting Excel: Workbooks, Worksheets and Cells
- **In scope**: opening Excel, blank workbook, worksheet tabs, rows (numbers), columns
  (letters), cell, cell address, active cell, Name Box, formula bar.
- **Out of scope**: templates, many sheets, settings.
- **Diagram idea**: workbook → worksheet → cell; how a cell address is made (column + row).

### 7.2 Entering, Editing and Saving Data
- **In scope**: typing text and numbers, Enter and Tab to move, editing a cell, clearing a
  cell, Undo; saving the workbook (links back to Word Lesson 4.3).
- **Practice**: a shop item list (item, quantity, price).

### 7.3 Rows and Columns: Width, Height, Insert and Delete
- **In scope**: changing column width and row height with the mouse, AutoFit, inserting and
  deleting a row and a column.
- **Common mistake to include**: "####" when a column is too narrow (verify this behaviour).

### 7.4 Formatting Cells: Font, Fill, Borders and Alignment
- **In scope**: bold heading row, fill colour, borders, alignment, Merge & Center for a title.
- **Out of scope**: cell styles, conditional formatting.

### 7.5 Number Formats: Money, Percentages and Dates
- **In scope**: the Number Format list, number with decimal places, currency or "Rs", percentage,
  short date.
- **Risk**: rupee currency steps may vary; UNVERIFIED box or the plain-number fallback (§1).

### 7.6 Your First Formulas
- **In scope**: a formula starts with "=", the operators + − * /, using cell addresses
  instead of numbers, the formula bar shows the formula.
- **Out of scope**: order of operations beyond one simple example, absolute references.

### 7.7 Copying Formulas with the Fill Handle
- **In scope**: the fill handle, copying a formula down a column, how cell addresses change
  as the formula is copied (explained in plain words), filling a series (1, 2, 3 or months).
- **Out of scope**: absolute references ($).

### 7.8 Functions: SUM and AVERAGE
- **In scope**: what a function is, SUM, AVERAGE, a range (A1:A5), AutoSum.

### 7.9 Functions: MIN, MAX and COUNT
- **In scope**: MIN, MAX, COUNT, and the difference between COUNT and counting text.
- **Out of scope**: COUNTA, COUNTIF (named only if needed, not taught).

### 7.10 Sorting Data
- **In scope**: sorting A to Z, Z to A, smallest to largest; keeping rows together when sorting.
- **Out of scope**: custom sort with many levels, filters.
- **Common mistake to include**: sorting one column only, which mixes up the rows (verify how
  Excel warns about this).

### 7.11 Making a Simple Chart
- **In scope**: selecting data, inserting a column chart, chart title, moving and resizing.
- **Out of scope**: chart types beyond column (pie mentioned only), chart formatting in depth.

### 7.12 Page Setup and Printing a Worksheet
- **In scope**: orientation, fitting a sheet on one page, print preview, printing gridlines
  (if verified), printing.
- **Note**: the task must still work if the lab has no printer (preview only).

### 7.13 Project: Student Result Sheet
- **In scope**: a result sheet for 5–8 made-up students: marks in 3–5 subjects, total (SUM),
  average (AVERAGE), percentage (formula), highest and lowest (MAX, MIN), sorting by total,
  a column chart, print preview.
- **Out of scope**: grades with IF (that is intermediate level).

## 6. Module-Level Acceptance Criteria

- **M7-01**: The overview page lists all lessons in order, each linking to its page.
- **M7-02**: Every learning outcome is covered by at least one lesson's Goal and Student Task.
- **M7-03**: Every lesson meets the criteria in §4.
- **M7-04**: The owner gets a full list of UNVERIFIED steps to test before teaching.

## 7. Open Questions

All answered by the owner on 2026-10-12:
1. Lesson list and order approved as is.
2. 13 lessons approved.
3. Project topic: student result sheet.
