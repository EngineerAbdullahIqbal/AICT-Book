"""Lesson 7.15: Making Decisions With IF."""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'if-function.mdx'
FOLDER = 'if-function'

# Step by Step: Pass or Fail. The pass mark is 40%.
PASS_MARK = 40
STUDENTS = [('Ali', 72), ('Sana', 38), ('Hamza', 40), ('Fatima', 85), ('Usman', 29),
            ('Zainab', 56)]


def build_pass_fail(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Percentage', 'Result'), *STUDENTS])
    if finished:
        for r in range(2, 2 + len(STUDENTS)):
            formula(ws, f'C{r}', f'=IF(B{r}>=40,"Pass","Fail")')


results = ['Pass' if p >= PASS_MARK else 'Fail' for _, p in STUDENTS]

# Practice: a small general store. Fewer than 10 in stock means "Order more".
# The finished file shows the end of the task, after Tea changes from 12 to 9 (Practice step 6).
LIMIT = 10
STOCK = [('Sugar (kg)', 25), ('Cooking oil (bottles)', 6), ('Tea (packs)', 12), ('Rice (kg)', 8),
         ('Soap (bars)', 30), ('Matchboxes', 10)]
STOCK_AFTER_CHANGE = [(n, 9 if n == 'Tea (packs)' else q) for n, q in STOCK]


def build_shop_stock(wb, finished):
    ws = wb.active
    stock = STOCK_AFTER_CHANGE if finished else STOCK
    put_rows(ws, [('Item', 'In stock', 'Status'), *stock])
    if finished:
        for r in range(2, 2 + len(stock)):
            formula(ws, f'C{r}', f'=IF(B{r}<10,"Order more","OK")')


def status(q):
    return 'Order more' if q < LIMIT else 'OK'


status_before = [status(q) for _, q in STOCK]
status_after = [status(q) for _, q in STOCK_AFTER_CHANGE]

FILES = [
    XlsxFile('pass-fail', build_pass_fail, {f'C{r}': v for r, v in zip(range(2, 8), results)}),
    XlsxFile('shop-stock', build_shop_stock,
             {f'C{r}': v for r, v in zip(range(2, 8), status_after)}),
]

# The lesson states these results; keep them in step with the page.
assert results == ['Pass', 'Fail', 'Pass', 'Pass', 'Fail', 'Pass']
assert status_before == ['OK', 'Order more', 'OK', 'Order more', 'OK', 'OK']
assert status_after == ['OK', 'Order more', 'Order more', 'Order more', 'OK', 'OK']
assert status_after.count('Order more') == 3
