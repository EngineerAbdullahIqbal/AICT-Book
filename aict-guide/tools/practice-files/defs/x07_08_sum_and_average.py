"""Lesson 7.8: Functions: SUM and AVERAGE."""

from xlsxkit import XlsxFile, put_rows, formula, bold

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'sum-and-average.mdx'
FOLDER = 'sum-and-average'

# Step by Step: the mark sheet.
MARKS = [('Ali', 78, 70), ('Sana', 85, 88), ('Hamza', 62, 55), ('Fatima', 91, 95), ('Usman', 74, 67)]


def build_marks(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Maths', 'English'), *MARKS])
    put_rows(ws, [('Total',), ('Average',)], start_row=7, bold_first=False)
    bold(ws, 'A7', 'A8')
    if finished:
        formula(ws, 'B7', '=SUM(B2:B6)')
        formula(ws, 'C7', '=SUM(C2:C6)')
        formula(ws, 'B8', '=AVERAGE(B2:B6)')
        formula(ws, 'C8', '=AVERAGE(C2:C6)')


maths = [m for _, m, _ in MARKS]
english = [e for _, _, e in MARKS]

# Practice: Saima's weekly sales. The finished file shows the end of the task, after Saturday
# is changed to 5600 (Practice step 6).
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
SALES = [2500, 3200, 2800, 4100, 3400, 5000]
SALES_AFTER_CHANGE = SALES[:5] + [5600]


def build_weekly_sales(wb, finished):
    ws = wb.active
    sales = SALES_AFTER_CHANGE if finished else SALES
    put_rows(ws, [('Day', 'Sales (Rs)'), *zip(DAYS, sales)])
    put_rows(ws, [('Total',), ('Average',)], start_row=8, bold_first=False)
    bold(ws, 'A8', 'A9')
    if finished:
        formula(ws, 'B8', '=SUM(B2:B7)')
        formula(ws, 'B9', '=AVERAGE(B2:B7)')


FILES = [
    XlsxFile('marks', build_marks, {
        'B7': sum(maths), 'C7': sum(english),
        'B8': sum(maths) / len(maths), 'C8': sum(english) / len(english),
    }),
    XlsxFile('weekly-sales', build_weekly_sales, {
        'B8': sum(SALES_AFTER_CHANGE),
        'B9': sum(SALES_AFTER_CHANGE) / len(SALES_AFTER_CHANGE),
    }),
]

# The lesson states these results; keep them in step with the page.
assert sum(maths) == 390 and sum(english) == 375
assert sum(maths) / 5 == 78 and sum(english) / 5 == 75
assert sum(SALES) == 21000 and sum(SALES) / 6 == 3500
assert sum(SALES_AFTER_CHANGE) == 21600 and sum(SALES_AFTER_CHANGE) / 6 == 3600
