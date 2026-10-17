"""Lesson 7.14: Fixed Cells: Absolute References."""

from xlsxkit import XlsxFile, put_rows, formula, bold

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'absolute-references.mdx'
FOLDER = 'absolute-references'

# Step by Step: a school shop gives one discount rate (B1) on every item.
RATE = 0.10
ITEMS = [('School bag', 1500), ('Shoes', 2400), ('Water bottle', 450), ('Lunch box', 650),
         ('Raincoat', 1200)]
FIRST = 4  # first data row


def build_shop_discount(wb, finished):
    ws = wb.active
    ws['A1'] = 'Discount rate'
    ws['B1'] = RATE
    ws['B1'].number_format = '0%'
    bold(ws, 'A1')
    put_rows(ws, [('Item', 'Price (Rs)', 'Discount (Rs)', 'Price after discount (Rs)'), *ITEMS],
             start_row=FIRST - 1)
    if finished:
        for r in range(FIRST, FIRST + len(ITEMS)):
            formula(ws, f'C{r}', f'=B{r}*$B$1')
            formula(ws, f'D{r}', f'=B{r}-C{r}')


discounts = [round(p * RATE, 9) for _, p in ITEMS]
after = [p - d for (_, p), d in zip(ITEMS, discounts)]
shop_expected = {}
for i, r in enumerate(range(FIRST, FIRST + len(ITEMS))):
    shop_expected[f'C{r}'] = discounts[i]
    shop_expected[f'D{r}'] = after[i]

# Step by Step also tries a 20% rate before going back to 10%.
discounts_20 = [p * 2 / 10 for _, p in ITEMS]

# Practice: a cloth shop with one price per metre (B1). The finished file shows the end of the
# task, after the price is changed from 350 to 400 (Practice step 6).
PRICE = 350
PRICE_AFTER_CHANGE = 400
CUSTOMERS = [('Ayesha', 3), ('Kamran', 2.5), ('Nadia', 4), ('Tariq', 1.5), ('Rubina', 5)]


def build_cloth_shop(wb, finished):
    ws = wb.active
    ws['A1'] = 'Price per metre (Rs)'
    ws['B1'] = PRICE_AFTER_CHANGE if finished else PRICE
    bold(ws, 'A1')
    put_rows(ws, [('Customer', 'Metres', 'Bill (Rs)'), *CUSTOMERS], start_row=FIRST - 1)
    put_rows(ws, [('Total',)], start_row=FIRST + len(CUSTOMERS), bold_first=True)
    if finished:
        for r in range(FIRST, FIRST + len(CUSTOMERS)):
            formula(ws, f'C{r}', f'=B{r}*$B$1')
        formula(ws, 'C9', '=SUM(C4:C8)')


bills_350 = [m * PRICE for _, m in CUSTOMERS]
bills_400 = [m * PRICE_AFTER_CHANGE for _, m in CUSTOMERS]
cloth_expected = {f'C{r}': b for r, b in zip(range(FIRST, FIRST + len(CUSTOMERS)), bills_400)}
cloth_expected['C9'] = sum(bills_400)

FILES = [
    XlsxFile('shop-discount', build_shop_discount, shop_expected),
    XlsxFile('cloth-shop', build_cloth_shop, cloth_expected),
]

# The lesson states these results; keep them in step with the page.
assert discounts == [150, 240, 45, 65, 120]
assert after == [1350, 2160, 405, 585, 1080]
assert discounts_20 == [300, 480, 90, 130, 240]
assert bills_350 == [1050, 875, 1400, 525, 1750] and sum(bills_350) == 5600
assert bills_400 == [1200, 1000, 1600, 600, 2000] and sum(bills_400) == 6400
assert FIRST + len(CUSTOMERS) == 9
