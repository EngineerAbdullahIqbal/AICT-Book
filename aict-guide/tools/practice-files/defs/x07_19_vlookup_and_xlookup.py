"""Lesson 7.19: Finding Data: VLOOKUP and XLOOKUP.

VLOOKUP and XLOOKUP are kept in separate files. verify.py cannot recalculate a file that uses
XLOOKUP until LibreOffice 24.8+ is installed (it skips the whole file), so the VLOOKUP-only files
(price-list, staff-salaries) are fully checked now. The -xlookup files hold the whole finished
sheet (VLOOKUP and XLOOKUP) in the same cells as the lesson.
"""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'vlookup-and-xlookup.mdx'
FOLDER = 'vlookup-and-xlookup'

NOT_FOUND = 'Not found'

# Step by Step: a general store's price list (made-up prices).
PRICES = [
    ('P101', 'Basmati rice 1 kg', 380),
    ('P102', 'Sugar 1 kg', 160),
    ('P103', 'Cooking oil 1 litre', 560),
    ('P104', 'Tea pack', 450),
    ('P105', 'Flour 10 kg', 1300),
    ('P106', 'Daal chana 1 kg', 320),
]
# Part 1 (VLOOKUP): code in E2, item in F2, price in G2.
# Part 2 (XLOOKUP): codes in E5 and E6 → price in F5, F6; item name in E9 → code in F9.
PART1_CODE = 'P104'
PART2_CODES = ['P106', 'P999']
PART2_ITEM = 'Sugar 1 kg'


def put_price_list(ws, part2):
    put_rows(ws, [('Code', 'Item', 'Price (Rs)'), *PRICES])
    put_rows(ws, [('Code', 'Item', 'Price (Rs)'), (PART1_CODE,)], start_col=5)
    if part2:
        put_rows(ws, [('Code', 'Price (Rs)'), *[(c,) for c in PART2_CODES]], start_row=4,
                 start_col=5)
        put_rows(ws, [('Item', 'Code'), (PART2_ITEM,)], start_row=8, start_col=5)


def put_vlookups(ws):
    formula(ws, 'F2', '=VLOOKUP(E2,A2:C7,2,FALSE)')
    formula(ws, 'G2', '=VLOOKUP(E2,A2:C7,3,FALSE)')


def build_price_list(wb, finished):
    ws = wb.active
    put_price_list(ws, part2=False)
    if finished:
        put_vlookups(ws)


def build_price_list_xlookup(wb, finished):
    ws = wb.active
    put_price_list(ws, part2=True)
    if finished:
        put_vlookups(ws)
        formula(ws, 'F5', f'=XLOOKUP(E5,A2:A7,C2:C7,"{NOT_FOUND}")')
        formula(ws, 'F6', f'=XLOOKUP(E6,A2:A7,C2:C7,"{NOT_FOUND}")')
        formula(ws, 'F9', f'=XLOOKUP(E9,B2:B7,A2:A7,"{NOT_FOUND}")')


def find(rows, key_col, value, return_col):
    """Exact-match lookup: the first row whose key_col equals value, else NOT_FOUND."""
    for row in rows:
        if row[key_col] == value:
            return row[return_col]
    return NOT_FOUND


p1_item = find(PRICES, 0, PART1_CODE, 1)
p1_price = find(PRICES, 0, PART1_CODE, 2)
p2_prices = [find(PRICES, 0, c, 2) for c in PART2_CODES]
p2_code = find(PRICES, 1, PART2_ITEM, 0)

# Practice: an office staff list (made-up names and salaries).
STAFF = [
    (201, 'Ahmed Raza', 'Accounts', 65000),
    (202, 'Sadia Noor', 'Sales', 52000),
    (203, 'Waqas Ali', 'Store', 38000),
    (204, 'Nadia Khan', 'Accounts', 71000),
    (205, 'Tariq Mehmood', 'Sales', 47000),
    (206, 'Sobia Akhtar', 'Reception', 41000),
]
# Part 1 (VLOOKUP): ID in F2 → name in G2, salary in H2.
# Part 2 (XLOOKUP): names in F5, F6 → staff ID in G5, G6 and department in H5, H6.
STAFF_ID = 204
STAFF_NAMES = ['Waqas Ali', 'Hamid Shah']


def put_staff(ws, part2):
    put_rows(ws, [('Staff ID', 'Name', 'Department', 'Salary (Rs)'), *STAFF])
    put_rows(ws, [('Staff ID', 'Name', 'Salary (Rs)'), (STAFF_ID,)], start_col=6)
    if part2:
        put_rows(ws, [('Name', 'Staff ID', 'Department'), *[(n,) for n in STAFF_NAMES]],
                 start_row=4, start_col=6)


def put_staff_vlookups(ws):
    formula(ws, 'G2', '=VLOOKUP(F2,A2:D7,2,FALSE)')
    formula(ws, 'H2', '=VLOOKUP(F2,A2:D7,4,FALSE)')


def build_staff(wb, finished):
    ws = wb.active
    put_staff(ws, part2=False)
    if finished:
        put_staff_vlookups(ws)


def build_staff_xlookup(wb, finished):
    ws = wb.active
    put_staff(ws, part2=True)
    if finished:
        put_staff_vlookups(ws)
        for r in (5, 6):
            formula(ws, f'G{r}', f'=XLOOKUP(F{r},B2:B7,A2:A7,"{NOT_FOUND}")')
            formula(ws, f'H{r}', f'=XLOOKUP(F{r},B2:B7,C2:C7,"{NOT_FOUND}")')


s1_name = find(STAFF, 0, STAFF_ID, 1)
s1_salary = find(STAFF, 0, STAFF_ID, 3)
s2_ids = [find(STAFF, 1, n, 0) for n in STAFF_NAMES]
s2_depts = [find(STAFF, 1, n, 2) for n in STAFF_NAMES]

VLOOKUP_PRICES = {'F2': p1_item, 'G2': p1_price}
VLOOKUP_STAFF = {'G2': s1_name, 'H2': s1_salary}

FILES = [
    XlsxFile('price-list', build_price_list, dict(VLOOKUP_PRICES)),
    XlsxFile('price-list-xlookup', build_price_list_xlookup, {
        **VLOOKUP_PRICES, 'F5': p2_prices[0], 'F6': p2_prices[1], 'F9': p2_code,
    }),
    XlsxFile('staff-salaries', build_staff, dict(VLOOKUP_STAFF)),
    XlsxFile('staff-salaries-xlookup', build_staff_xlookup, {
        **VLOOKUP_STAFF,
        'G5': s2_ids[0], 'H5': s2_depts[0], 'G6': s2_ids[1], 'H6': s2_depts[1],
    }),
]

# The lesson states these results; keep them in step with the page.
assert (p1_item, p1_price) == ('Tea pack', 450)
assert p2_prices == [320, 'Not found'] and p2_code == 'P102'
assert (s1_name, s1_salary) == ('Nadia Khan', 71000)
assert s2_ids == [203, 'Not found'] and s2_depts == ['Store', 'Not found']
