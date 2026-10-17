"""Lesson 7.3: Rows and Columns: Width, Height, Insert and Delete.

Starter = Shop List / Mobile Stock as they are at the END of Lesson 7.2.
Finished = the end of Lesson 7.3: the new row inserted (Salt / Power bank), the inserted and
deleted rows and columns undone, row 1 taller. Column widths: build.py fits every column to its
longest value (like AutoFit), which is how the lesson leaves columns A and C.

`expected` checks the row that ends up below the inserted row (Eggs / Memory card): that cell
range is empty in the starter and shows the insert put the new item in the right place.
"""

from xlsxkit import XlsxFile, new_workbook
from defs.x07_02_entering_editing_saving_data import SHOP_END, MOBILE_END, put_list

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'rows-and-columns.mdx'
FOLDER = 'rows-and-columns'

TALL_ROW = 24  # points; row 1 "made taller" (default is 15)

# Step 7-8: Salt goes after Rice (new row 4). Steps 11-12: Eggs deleted, then brought back.
SHOP_END_73 = SHOP_END[:2] + [('Salt', 1, 60)] + SHOP_END[2:]
# Practice 5: Power bank above Memory card. Practice 7: Charger deleted, then brought back.
MOBILE_END_73 = MOBILE_END[:4] + [('Power bank', 4, 2500)] + MOBILE_END[4:]


def build_shop_list(wb, finished):
    ws = wb.active
    if finished:
        put_list(ws, SHOP_END_73)
        ws.row_dimensions[1].height = TALL_ROW
    else:
        put_list(ws, SHOP_END)


def build_mobile_stock(wb, finished):
    ws = wb.active
    if finished:
        put_list(ws, MOBILE_END_73)
        ws.row_dimensions[1].height = TALL_ROW
    else:
        put_list(ws, MOBILE_END)


FILES = [
    XlsxFile('shop-list', build_shop_list, {'A8': 'Eggs', 'B8': 12, 'C8': 30}, fit='finished'),
    XlsxFile('mobile-stock', build_mobile_stock, {'A7': 'Memory card', 'B7': 3, 'C7': 1200}, fit='finished'),
]


def _finished(build):
    wb = new_workbook()
    build(wb, True)
    return wb.active


# The lesson states these results; keep them in step with the page.
_ws = _finished(build_shop_list)
assert [_ws[f'A{r}'].value for r in (4, 5)] == ['Salt', 'Cooking oil']   # step 7
assert (_ws['B4'].value, _ws['C4'].value) == (1, 60)                     # step 8
assert _ws['B1'].value == 'Quantity'                                      # step 10
_ws = _finished(build_mobile_stock)
assert (_ws['A6'].value, _ws['B6'].value, _ws['C6'].value) == ('Power bank', 4, 2500)
assert _ws['A7'].value == 'Memory card' and _ws['A3'].value == 'Charger'  # Practice 9
assert _ws['B1'].value == 'Quantity'
