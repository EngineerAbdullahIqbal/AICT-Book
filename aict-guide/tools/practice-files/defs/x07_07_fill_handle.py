"""Lesson 7.7: Copying Formulas with the Fill Handle.

Starter = only what the student types before using the fill handle: headings and the data
columns. The cells the fill handle fills (numbers 1, 2, 3 …, months, the repeated price and the
copied formulas) are empty. Finished = every filled cell, with the real formulas in column E.
`expected` checks the formula results and the filled series.
"""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'fill-handle.mdx'
FOLDER = 'fill-handle'

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Step by Step: the school shop bill. Columns A and E (and the months in G) start empty.
SHOP = [('Notebook', 4, 80), ('Pencil', 10, 15), ('Eraser', 6, 10), ('Ruler', 3, 40),
        ('Glue stick', 2, 90)]


def build_school_shop_bill(wb, finished):
    ws = wb.active
    put_rows(ws, [('No.', 'Item', 'Quantity', 'Price (Rs)', 'Total (Rs)')])
    put_rows(ws, SHOP, start_row=2, start_col=2, bold_first=False)
    if finished:
        for i in range(len(SHOP)):
            ws[f'A{i + 2}'] = i + 1
            formula(ws, f'E{i + 2}', f'=C{i + 2}*D{i + 2}')
        for r, month in enumerate(MONTHS, start=2):
            ws[f'G{r}'] = month


# Practice: the milk bill. The student types the headings and the litres.
LITRES = [60, 56, 62, 60, 62, 60]
PRICE = 200


def build_milk_bill(wb, finished):
    ws = wb.active
    put_rows(ws, [('No.', 'Month', 'Milk (litres)', 'Price per litre (Rs)', 'Bill (Rs)')])
    for r, litres in enumerate(LITRES, start=2):
        ws[f'C{r}'] = litres
        if finished:
            ws[f'A{r}'] = r - 1
            ws[f'B{r}'] = MONTHS[r - 2]
            ws[f'D{r}'] = PRICE
            formula(ws, f'E{r}', f'=C{r}*D{r}')


shop_totals = [q * p for _, q, p in SHOP]
milk_bills = [litres * PRICE for litres in LITRES]

FILES = [
    XlsxFile('school-shop-bill', build_school_shop_bill, {
        **{f'E{r}': t for r, t in enumerate(shop_totals, start=2)},
        **{f'A{r}': r - 1 for r in range(2, 7)},
        **{f'G{r}': m for r, m in enumerate(MONTHS, start=2)},
    }),
    XlsxFile('milk-bill', build_milk_bill, {
        **{f'E{r}': b for r, b in enumerate(milk_bills, start=2)},
        **{f'A{r}': r - 1 for r in range(2, 8)},
        **{f'B{r}': m for r, m in enumerate(MONTHS, start=2)},
        **{f'D{r}': PRICE for r in range(2, 8)},
    }),
]

# The lesson states these results; keep them in step with the page.
assert shop_totals == [320, 150, 60, 120, 180]
assert milk_bills == [12000, 11200, 12400, 12000, 12400, 12000]
