"""Lesson 7.12: Page Setup and Printing a Worksheet.

Finished files: the SUM totals, and the page set up as the lesson ends: Landscape, fit to
1 page wide by 1 page tall, gridlines printed.
"""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'page-setup-and-printing.mdx'
FOLDER = 'page-setup-and-printing'


def set_up_page(ws):
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.print_options.gridLines = True


# Step by Step: a family's weekly home expenses in rupees.
WEEKLY = [('Groceries', 4500, 3800, 5200, 4100), ('Milk', 1400, 1400, 1400, 1400),
          ('Vegetables', 1200, 950, 1300, 1100), ('Fruit', 800, 600, 900, 700),
          ('Transport', 1500, 1500, 1800, 1500), ('Mobile balance', 500, 300, 400, 300)]


def build_weekly_expenses(wb, finished):
    ws = wb.active
    put_rows(ws, [('Item', 'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Total'), *WEEKLY])
    if finished:
        for r in range(2, 8):
            formula(ws, f'F{r}', f'=SUM(B{r}:E{r})')
        set_up_page(ws)


# Practice: Mrs Rabia's tuition fee record (0 = no fee paid that month).
FEES = [('Ahmed', 2000, 2000, 2000, 2000, 2000, 2000), ('Hira', 2500, 2500, 0, 2500, 2500, 2500),
        ('Zeeshan', 1500, 1500, 1500, 1500, 1500, 1500), ('Nimra', 3000, 3000, 3000, 3000, 0, 3000),
        ('Faraz', 2000, 2000, 2000, 2500, 2500, 2500)]


def build_tuition_fees(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Total'), *FEES])
    if finished:
        for r in range(2, 7):
            formula(ws, f'H{r}', f'=SUM(B{r}:G{r})')
        set_up_page(ws)


weekly_totals = [sum(row[1:]) for row in WEEKLY]
fee_totals = [sum(row[1:]) for row in FEES]

FILES = [
    XlsxFile('weekly-expenses', build_weekly_expenses,
             {f'F{r}': t for r, t in zip(range(2, 8), weekly_totals)}),
    XlsxFile('tuition-fees', build_tuition_fees,
             {f'H{r}': t for r, t in zip(range(2, 7), fee_totals)}),
]

# The lesson states these results; keep them in step with the page.
assert weekly_totals == [17600, 5600, 4550, 3000, 6300, 1500]
assert fee_totals == [12000, 12500, 9000, 15000, 13500]
