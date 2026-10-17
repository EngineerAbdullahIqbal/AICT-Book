"""Lesson 7.2: Entering, Editing and Saving Data.

Two workbooks start here and carry on into Lessons 7.3 and 7.4: Shop List (Step by Step) and
Mobile Stock (Practice). Lesson 7.2 starts from a blank workbook, so the starter files hold the
list as it looks once it is typed (before the edits); the finished files show the end of the
lesson, after the edits.

The headings are NOT bold here on purpose: bold is taught in Lesson 7.4 with Ctrl+B, which
switches bold on and off, so bold headings in these files would break Lesson 7.4 step 6.

No formulas, and every edited cell already holds a value in the starter, so `expected` is empty
(verify.py requires answer cells to be empty in the starter). The edits are checked by the
assert lines at the bottom instead.
"""

from xlsxkit import XlsxFile, put_rows, new_workbook

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'entering-editing-saving-data.mdx'
FOLDER = 'entering-editing-saving-data'

HEADINGS = ('Item', 'Quantity', 'Price Rs')

# Step by Step: the grocery shop list. Step 9 changes milk from 220 to 240 (C6).
SHOP_TYPED = [('Sugar', 2, 150), ('Rice', 3, 320), ('Cooking oil', 1, 560), ('Tea', 2, 450),
              ('Milk', 4, 220), ('Eggs', 12, 30)]
SHOP_END = [row if row[0] != 'Milk' else ('Milk', 4, 240) for row in SHOP_TYPED]

# Practice: Imran's mobile shop. Step 4: charger 800 -> 850 (C3). Step 7: memory cards 5 -> 3 (B6).
MOBILE_TYPED = [('Phone cover', 10, 350), ('Charger', 6, 800), ('Earphones', 8, 450),
                ('Screen protector', 15, 200), ('Memory card', 5, 1200)]
MOBILE_END = [('Phone cover', 10, 350), ('Charger', 6, 850), ('Earphones', 8, 450),
              ('Screen protector', 15, 200), ('Memory card', 3, 1200)]


def put_list(ws, items):
    """The plain list from A1: headings in row 1 (not bold), one item per row."""
    put_rows(ws, [HEADINGS, *items], bold_first=False)


def build_shop_list(wb, finished):
    put_list(wb.active, SHOP_END if finished else SHOP_TYPED)


def build_mobile_stock(wb, finished):
    put_list(wb.active, MOBILE_END if finished else MOBILE_TYPED)


FILES = [
    XlsxFile('shop-list', build_shop_list),
    XlsxFile('mobile-stock', build_mobile_stock),
]


def _finished(build):
    wb = new_workbook()
    build(wb, True)
    return wb.active


# The lesson states these results; keep them in step with the page.
_ws = _finished(build_shop_list)
assert _ws['C6'].value == 240 and _ws['A7'].value == 'Eggs'          # steps 9 and 11
assert _ws.max_row == 7 and _ws.max_column == 3
_ws = _finished(build_mobile_stock)
assert (_ws['C3'].value, _ws['A4'].value, _ws['B6'].value) == (850, 'Earphones', 3)  # Practice 8
assert _ws.max_row == 6 and _ws.max_column == 3                      # "your list fills A1 to C6"
