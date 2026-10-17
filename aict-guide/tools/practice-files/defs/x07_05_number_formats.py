"""Lesson 7.5: Number Formats: Money, Percentages and Dates.

Starter = the table as typed: prices and shares in the General format, dates as real dates in
the Short Date format (what Excel shows after you type a date).
Finished = the end of each task:
  Step by Step: prices Number with 0 decimal places (2 places, then Decrease Decimal twice),
  discounts Percent Style, dates Short Date (step 15).
  Practice: amounts Number with 2 decimal places, shares Percent Style, dates Short Date.

No formulas and no typed answers, so `expected` is empty. The formats are checked by the asserts
below. Short Date is Excel's built-in format 14, which shows the date in the computer's own
short date order.
"""

from datetime import datetime

from xlsxkit import XlsxFile, put_rows, new_workbook

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'number-formats.mdx'
FOLDER = 'number-formats'

SHORT_DATE = 'mm-dd-yy'   # openpyxl's name for Excel's built-in format 14 (Short Date)
NUMBER_0 = '0'            # Number, 0 decimal places (built-in 1)
NUMBER_2 = '0.00'         # Number, 2 decimal places (built-in 2)
PERCENT = '0%'            # Percent Style (built-in 9)

SALES = [('Sugar 1 kg', 160, 0.05, datetime(2025, 3, 15)),
         ('Rice 1 kg', 350, 0.1, datetime(2025, 3, 18)),
         ('Cooking oil 1 litre', 560, 0.02, datetime(2025, 3, 20)),
         ('Tea 250 g', 420, 0.15, datetime(2025, 3, 22)),
         ('Flour 5 kg', 650, 0.2, datetime(2025, 3, 25))]

BUDGET = [('House rent', 20000, 0.4, datetime(2025, 4, 15)),
          ('Groceries', 15000, 0.3, datetime(2025, 4, 18)),
          ('Electricity', 6000, 0.12, datetime(2025, 4, 20)),
          ('Gas', 2500, 0.05, datetime(2025, 4, 22)),
          ('School fees', 6500, 0.13, datetime(2025, 4, 25))]


def build_table(ws, headings, rows, finished, money_format):
    put_rows(ws, [headings, *rows])
    for r in range(2, 2 + len(rows)):
        ws[f'D{r}'].number_format = SHORT_DATE
        if finished:
            ws[f'B{r}'].number_format = money_format
            ws[f'C{r}'].number_format = PERCENT


def build_shop_sales(wb, finished):
    build_table(wb.active, ('Item', 'Price (Rs)', 'Discount', 'Date sold'), SALES, finished, NUMBER_0)


def build_household_budget(wb, finished):
    build_table(wb.active, ('Expense', 'Amount (Rs)', 'Share of budget', 'Date paid'), BUDGET,
                finished, NUMBER_2)


FILES = [
    XlsxFile('shop-sales', build_shop_sales),
    XlsxFile('household-budget', build_household_budget),
]


def _sheet(build, finished):
    wb = new_workbook()
    build(wb, finished)
    return wb.active


# The lesson states these results; keep them in step with the page.
assert [f'{p:.2f}' for _, p, _, _ in SALES] == ['160.00', '350.00', '560.00', '420.00', '650.00']
assert [f'{p:.0f}' for _, p, _, _ in SALES] == ['160', '350', '560', '420', '650']
assert [f'{d:.0%}' for _, _, d, _ in SALES] == ['5%', '10%', '2%', '15%', '20%']
assert [f'{a:.2f}' for _, a, _, _ in BUDGET] == ['20000.00', '15000.00', '6000.00', '2500.00', '6500.00']
assert [f'{s:.0%}' for _, _, s, _ in BUDGET] == ['40%', '30%', '12%', '5%', '13%']
for _build, _money in ((build_shop_sales, NUMBER_0), (build_household_budget, NUMBER_2)):
    _ws = _sheet(_build, False)
    assert all(_ws[f'{c}{r}'].number_format == 'General' for c in 'BC' for r in range(2, 7))
    _ws = _sheet(_build, True)
    for _r in range(2, 7):
        assert _ws[f'B{_r}'].number_format == _money and _ws[f'C{_r}'].number_format == PERCENT
        assert _ws[f'D{_r}'].number_format == SHORT_DATE
