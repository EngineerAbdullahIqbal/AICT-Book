"""Lesson 7.20: Errors and Rounding: IFERROR and ROUND."""

from fractions import Fraction

from xlsxkit import XlsxFile, put_rows, formula, bold

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'iferror-and-round.mdx'
FOLDER = 'iferror-and-round'


def excel_round(value: Fraction, digits: int):
    """ROUND as Excel does it: halves go away from zero (worked out exactly, with fractions)."""
    scale = Fraction(10) ** digits
    scaled = abs(value) * scale
    whole = int(scaled)
    if scaled - whole >= Fraction(1, 2):
        whole += 1
    result = Fraction(whole) / scale * (1 if value >= 0 else -1)
    return int(result) if digits == 0 or result.denominator == 1 else float(result)


# Step by Step: a general store works out the cost of one piece from the carton price.
# Soap bars: the pieces are not counted yet, so C4 is empty (this gives #DIV/0!).
CARTONS = [('Biscuit packs', 1150, 24), ('Juice boxes', 1380, 27), ('Soap bars', 2000, None),
           ('Pencils', 1000, 12), ('Notebooks', 1800, 12)]
FIND = ['Notebooks', 'Sugar']  # A10, A11: items a customer asks about
COUNT_MSG = 'Count pieces'
NOT_FOUND = 'Not in list'


def build_shop_prices(wb, finished):
    ws = wb.active
    put_rows(ws, [('Item', 'Carton price (Rs)', 'Pieces', 'Price per piece (Rs)'), *CARTONS])
    put_rows(ws, [('Item to find', 'Price per piece (Rs)'), *[(f,) for f in FIND]], start_row=9)
    if finished:
        for r in range(2, 2 + len(CARTONS)):
            formula(ws, f'D{r}', f'=IFERROR(ROUND(B{r}/C{r},0),"{COUNT_MSG}")')
        for r in (10, 11):
            formula(ws, f'B{r}', f'=IFERROR(VLOOKUP(A{r},$A$2:$D$6,4,FALSE),"{NOT_FOUND}")')


raw_per_piece = [Fraction(p, n) if n else None for _, p, n in CARTONS]
per_piece = [excel_round(x, 0) if x is not None else COUNT_MSG for x in raw_per_piece]
price_of = {name: v for (name, _, _), v in zip(CARTONS, per_piece)}
found = [price_of.get(f, NOT_FOUND) for f in FIND]

shop_expected = {f'D{r}': v for r, v in zip(range(2, 7), per_piece)}
shop_expected.update({'B10': found[0], 'B11': found[1]})

# Practice: an office checks each salesperson's sales against the monthly target.
# Nida is new and has no target yet (B5 empty). The finished file shows the end of the task,
# after her target 50000 is typed in B5 (Practice step 6).
SALES = [('Bilal', 150000, 127500), ('Saba', 120000, 131000), ('Imran', 90000, 61250),
         ('Nida', None, 15000), ('Faisal', 200000, 172345)]
NIDA_TARGET = 50000
SALES_AFTER_CHANGE = [(n, NIDA_TARGET if n == 'Nida' else t, s) for n, t, s in SALES]
NO_TARGET = 'No target'


def build_sales_target(wb, finished):
    ws = wb.active
    rows = SALES_AFTER_CHANGE if finished else SALES
    put_rows(ws, [('Salesperson', 'Target (Rs)', 'Sales (Rs)', '% of target'), *rows])
    if finished:
        for r in range(2, 2 + len(rows)):
            formula(ws, f'D{r}', f'=IFERROR(ROUND(C{r}/B{r}*100,2),"{NO_TARGET}")')


def percent_of_target(rows):
    return [excel_round(Fraction(s, t) * 100, 2) if t else NO_TARGET for _, t, s in rows]


pct_before = percent_of_target(SALES)
pct_after = percent_of_target(SALES_AFTER_CHANGE)

FILES = [
    XlsxFile('shop-prices', build_shop_prices, shop_expected),
    XlsxFile('sales-target', build_sales_target,
             {f'D{r}': v for r, v in zip(range(2, 7), pct_after)}),
]

# The lesson states these results; keep them in step with the page.
assert [float(x) for x in raw_per_piece if x is not None][:2] == [1150 / 24, 1380 / 27]
assert round(1150 / 24, 4) == 47.9167 and round(1380 / 27, 4) == 51.1111
assert per_piece == [48, 51, 'Count pieces', 83, 150]
assert found == [150, 'Not in list']
assert pct_before == [85, 109.17, 68.06, 'No target', 86.17]
assert pct_after == [85, 109.17, 68.06, 30, 86.17]
# Format versus ROUND (Why ROUND changes the value): 24 biscuit packs at the shown price.
assert float(Fraction(1150, 24) * 24) == 1150 and per_piece[0] * 24 == 1152
