"""Lesson 7.26: Filtering Data.

Filtering has no formulas, so there are no answer cells to recalculate (`expected` is empty).
The finished files show the filter the lesson ends with: the filter arrows are on, the filter
condition is saved, and the rows that do not match are hidden (openpyxl stores the condition but
does not hide rows itself, so build() hides them, as Excel does). The asserts below check every
row list the lesson states and the saved filter settings.
"""

from openpyxl.worksheet.filters import CustomFilter, CustomFilters, FilterColumn

from xlsxkit import XlsxFile, new_workbook, put_rows

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'filtering-data.mdx'
FOLDER = 'filtering-data'

# Step by Step: a tuition centre's fee record (Student, Grade, Fee (Rs), Status).
FEES = [
    ('Ayesha', 9, 2500, 'Paid'), ('Bilal', 10, 3000, 'Unpaid'), ('Hira', 9, 2500, 'Paid'),
    ('Kamran', 8, 2000, 'Unpaid'), ('Maryam', 10, 3000, 'Paid'), ('Noman', 9, 2500, 'Unpaid'),
    ('Rabia', 8, 2000, 'Paid'), ('Saad', 10, 3000, 'Paid'), ('Sana', 9, 2500, 'Paid'),
    ('Usman', 8, 2000, 'Unpaid'), ('Zainab', 10, 3000, 'Paid'), ('Hamza', 9, 2500, 'Paid'),
]
FEE_HEADINGS = ('Student', 'Grade', 'Fee (Rs)', 'Status')
FEE_RANGE = f'A1:D{len(FEES) + 1}'


def build_fee_record(wb, finished):
    """Finished: the last step of Step by Step, Status filtered to Unpaid."""
    ws = wb.active
    put_rows(ws, [FEE_HEADINGS, *FEES])
    if finished:
        ws.auto_filter.ref = FEE_RANGE
        ws.auto_filter.add_filter_column(3, ['Unpaid'])        # column D (Status)
        for r, row in enumerate(FEES, start=2):
            if row[3] != 'Unpaid':
                ws.row_dimensions[r].hidden = True


# Practice: a grocery shop's sales log (Bill No, Product, Quantity, Amount (Rs)).
PRICE = {'Tea': 450, 'Sugar': 160, 'Oil': 560, 'Rice': 320, 'Daal': 300}
BILLS = [(101, 'Tea', 2), (102, 'Sugar', 5), (103, 'Oil', 4), (104, 'Rice', 10), (105, 'Tea', 1),
         (106, 'Daal', 3), (107, 'Sugar', 2), (108, 'Oil', 1), (109, 'Tea', 6), (110, 'Rice', 3),
         (111, 'Daal', 5), (112, 'Sugar', 10), (113, 'Oil', 5), (114, 'Tea', 3), (115, 'Rice', 2)]
SALES = [(b, p, q, q * PRICE[p]) for b, p, q in BILLS]
SALES_HEADINGS = ('Bill No', 'Product', 'Quantity', 'Amount (Rs)')
SALES_RANGE = f'A1:D{len(SALES) + 1}'
LIMIT = 2000


def build_shop_sales(wb, finished):
    """Finished: the last filter of Practice, Amount Greater Than 2000."""
    ws = wb.active
    put_rows(ws, [SALES_HEADINGS, *SALES])
    if finished:
        ws.auto_filter.ref = SALES_RANGE
        ws.auto_filter.filterColumn.append(FilterColumn(
            colId=3, customFilters=CustomFilters(
                customFilter=[CustomFilter(operator='greaterThan', val=str(LIMIT))])))
        for r, row in enumerate(SALES, start=2):
            if not row[3] > LIMIT:
                ws.row_dimensions[r].hidden = True


FILES = [
    XlsxFile('fee-record', build_fee_record),
    XlsxFile('shop-sales', build_shop_sales),
]

# The lesson states these results; keep them in step with the page.
grade9 = [r[0] for r in FEES if r[1] == 9]
assert grade9 == ['Ayesha', 'Hira', 'Noman', 'Sana', 'Hamza']                    # step 6
assert [i + 2 for i, r in enumerate(FEES) if r[1] == 9] == [2, 4, 7, 10, 13]      # step 7
unpaid = [r for r in FEES if r[3] == 'Unpaid']
assert [r[0] for r in unpaid] == ['Bilal', 'Kamran', 'Noman', 'Usman']          # step 10
assert [i + 2 for i, r in enumerate(FEES) if r[3] == 'Unpaid'] == [3, 5, 7, 11]  # row numbers
assert [r[2] for r in unpaid] == [3000, 2000, 2500, 2000]                         # step 11
assert sum(r[2] for r in unpaid) == 9500
assert len(FEES) == 12 and sorted({r[1] for r in FEES}) == [8, 9, 10]            # step 4

tea = [r for r in SALES if r[1] == 'Tea']
assert [r[0] for r in tea] == [101, 105, 109, 114]                               # Practice 3
assert [r[2] for r in tea] == [2, 1, 6, 3] and sum(r[2] for r in tea) == 12     # Practice 4
big = [r for r in SALES if r[3] > LIMIT]
assert [(r[0], r[1], r[3]) for r in big] == [                                    # Check your work
    (103, 'Oil', 2240), (104, 'Rice', 3200), (109, 'Tea', 2700), (113, 'Oil', 2800)]
assert [r[0] for r in SALES if r[1] == 'Sugar'] == [102, 107, 112]               # question 3
assert len(SALES) == 15

# The finished files hold the filter the lesson ends with; the starters have no filter.
for build, ref, shown in ((build_fee_record, FEE_RANGE, [3, 5, 7, 11]),
                          (build_shop_sales, SALES_RANGE, [4, 5, 10, 14])):
    _wb = new_workbook()
    build(_wb, True)
    _ws = _wb.active
    assert _ws.auto_filter.ref == ref
    assert len(_ws.auto_filter.filterColumn) == 1 and _ws.auto_filter.filterColumn[0].colId == 3
    visible = [r for r in range(2, _ws.max_row + 1) if not _ws.row_dimensions[r].hidden]
    assert visible == shown, visible
    _wb = new_workbook()
    build(_wb, False)
    assert _wb.active.auto_filter.ref is None
    assert not any(_wb.active.row_dimensions[r].hidden for r in range(1, _wb.active.max_row + 1))
