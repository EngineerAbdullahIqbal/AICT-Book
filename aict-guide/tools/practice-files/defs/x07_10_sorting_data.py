"""Lesson 7.10: Sorting Data.

Sorting has no formulas, so there are no answer cells to recalculate (`expected` is empty).
The finished files hold the list in the order the lesson ends with; the asserts below check
every order the lesson states.
"""

from xlsxkit import XlsxFile, put_rows

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'sorting-data.mdx'
FOLDER = 'sorting-data'

# Step by Step: grocery price list (Item, Price (Rs), Quantity).
SHOP = [('Sugar', 150, 10), ('Tea', 420, 4), ('Atta', 120, 25), ('Rice', 300, 12),
        ('Oil', 550, 8), ('Daal', 280, 15)]
# The last sort in Step by Step (step 14): Price, Largest to Smallest, whole rows together.
SHOP_SORTED = sorted(SHOP, key=lambda r: r[1], reverse=True)


def build_shop_prices(wb, finished):
    ws = wb.active
    put_rows(ws, [('Item', 'Price (Rs)', 'Quantity'), *(SHOP_SORTED if finished else SHOP)])


# Practice: tuition centre test (Name, City, Marks).
TEST = [('Zainab', 'Karachi', 35), ('Hina', 'Multan', 47), ('Bilal', 'Peshawar', 29),
        ('Ayesha', 'Lahore', 42), ('Kamran', 'Quetta', 38), ('Mariam', 'Faisalabad', 44)]
# The last sort in Practice (step 7): Marks, Largest to Smallest.
TEST_SORTED = sorted(TEST, key=lambda r: r[2], reverse=True)


def build_test_list(wb, finished):
    ws = wb.active
    put_rows(ws, [('Name', 'City', 'Marks'), *(TEST_SORTED if finished else TEST)])


FILES = [
    XlsxFile('shop-prices', build_shop_prices),
    XlsxFile('test-list', build_test_list),
]

# The lesson states these orders; keep them in step with the page.
names = lambda rows: [r[0] for r in rows]  # noqa: E731
assert names(sorted(SHOP)) == ['Atta', 'Daal', 'Oil', 'Rice', 'Sugar', 'Tea']          # step 4
assert names(sorted(SHOP, reverse=True))[0] == 'Tea'                                   # step 6
assert names(sorted(SHOP, reverse=True))[-1] == 'Atta'
assert [(r[0], r[1]) for r in sorted(SHOP, key=lambda r: r[1])] == [                   # step 8
    ('Atta', 120), ('Sugar', 150), ('Daal', 280), ('Rice', 300), ('Tea', 420), ('Oil', 550)]
assert [(r[0], r[1]) for r in SHOP_SORTED] == [                                        # step 14
    ('Oil', 550), ('Tea', 420), ('Rice', 300), ('Daal', 280), ('Sugar', 150), ('Atta', 120)]
assert ('Tea', 420, 4) in SHOP_SORTED
assert names(sorted(TEST))[0] == 'Ayesha' and names(sorted(TEST))[-1] == 'Zainab'      # step 3
by_marks = sorted(TEST, key=lambda r: r[2])
assert by_marks[0] == ('Bilal', 'Peshawar', 29) and by_marks[-1] == ('Hina', 'Multan', 47)  # step 6
assert [(r[0], r[2]) for r in TEST_SORTED] == [                                        # step 10
    ('Hina', 47), ('Mariam', 44), ('Ayesha', 42), ('Kamran', 38), ('Zainab', 35), ('Bilal', 29)]
assert TEST_SORTED[0] == ('Hina', 'Multan', 47)
assert ('Ayesha', 'Lahore', 42) in TEST_SORTED
