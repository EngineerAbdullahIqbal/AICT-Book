"""Lesson 7.18: Adding With Conditions: SUMIF, SUMIFS and AVERAGEIF."""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'sumif-sumifs-averageif.mdx'
FOLDER = 'sumif-sumifs-averageif'

# Step by Step: a general store's sales record for two months. Answers in E2:F7.
SHOP = [
    ('January', 'Sugar', 4500),
    ('January', 'Rice', 6200),
    ('January', 'Tea', 3000),
    ('January', 'Sugar', 3500),
    ('January', 'Rice', 5800),
    ('February', 'Sugar', 5200),
    ('February', 'Tea', 2700),
    ('February', 'Rice', 4800),
    ('February', 'Sugar', 4000),
    ('February', 'Tea', 3300),
]
SHOP_LABELS = ['Sugar total', 'Rice total', 'Tea total', 'Sugar in February',
               'Average Rice sale', 'All sales']


def build_shop_sales(wb, finished):
    ws = wb.active
    put_rows(ws, [('Month', 'Product', 'Sales (Rs)'), *SHOP])
    put_rows(ws, [('Question', 'Answer (Rs)'), *[(label,) for label in SHOP_LABELS]],
             start_col=5)
    if finished:
        formula(ws, 'F2', '=SUMIF(B2:B11,"Sugar",C2:C11)')
        formula(ws, 'F3', '=SUMIF(B2:B11,"Rice",C2:C11)')
        formula(ws, 'F4', '=SUMIF(B2:B11,"Tea",C2:C11)')
        formula(ws, 'F5', '=SUMIFS(C2:C11,B2:B11,"Sugar",A2:A11,"February")')
        formula(ws, 'F6', '=AVERAGEIF(B2:B11,"Rice",C2:C11)')
        formula(ws, 'F7', '=SUM(C2:C11)')


def total(rows, product=None, month=None):
    return sum(s for m, p, s in rows
               if (product is None or p == product) and (month is None or m == month))


def average(rows, product):
    values = [s for _, p, s in rows if p == product]
    return sum(values) / len(values)


sugar, rice, tea = total(SHOP, 'Sugar'), total(SHOP, 'Rice'), total(SHOP, 'Tea')
sugar_feb = total(SHOP, 'Sugar', 'February')
rice_avg = average(SHOP, 'Rice')
all_sales = total(SHOP)

# Practice: a mobile accessories shop with two salespeople. Answers in F2:G5.
ACCESSORIES = [
    ('Asif', 'Charger', 1200),
    ('Zara', 'Earphones', 800),
    ('Asif', 'Mobile cover', 600),
    ('Zara', 'Charger', 1500),
    ('Asif', 'Earphones', 950),
    ('Zara', 'Mobile cover', 450),
    ('Asif', 'Charger', 1300),
    ('Zara', 'Charger', 1100),
    ('Asif', 'Mobile cover', 500),
]
ACCESSORY_LABELS = ['Charger total', "Asif's total", "Zara's chargers", 'Average earphones sale']


def build_accessory_sales(wb, finished):
    ws = wb.active
    put_rows(ws, [('Salesperson', 'Item', 'Amount (Rs)'), *ACCESSORIES])
    put_rows(ws, [('Question', 'Answer (Rs)'), *[(label,) for label in ACCESSORY_LABELS]],
             start_col=6)
    if finished:
        formula(ws, 'G2', '=SUMIF(B2:B10,"Charger",C2:C10)')
        formula(ws, 'G3', '=SUMIF(A2:A10,"Asif",C2:C10)')
        formula(ws, 'G4', '=SUMIFS(C2:C10,A2:A10,"Zara",B2:B10,"Charger")')
        formula(ws, 'G5', '=AVERAGEIF(B2:B10,"Earphones",C2:C10)')


charger_total = sum(a for _, i, a in ACCESSORIES if i == 'Charger')
asif_total = sum(a for p, _, a in ACCESSORIES if p == 'Asif')
zara_chargers = sum(a for p, i, a in ACCESSORIES if p == 'Zara' and i == 'Charger')
earphones = [a for _, i, a in ACCESSORIES if i == 'Earphones']
earphones_avg = sum(earphones) / len(earphones)

FILES = [
    XlsxFile('shop-sales', build_shop_sales, {
        'F2': sugar, 'F3': rice, 'F4': tea, 'F5': sugar_feb, 'F6': rice_avg, 'F7': all_sales,
    }),
    XlsxFile('accessory-sales', build_accessory_sales, {
        'G2': charger_total, 'G3': asif_total, 'G4': zara_chargers, 'G5': earphones_avg,
    }),
]

# The lesson states these results; keep them in step with the page.
assert (sugar, rice, tea) == (17200, 16800, 9000)
assert sugar_feb == 9200 and rice_avg == 5600 and all_sales == 43000
assert sugar + rice + tea == all_sales
assert (charger_total, asif_total, zara_chargers, earphones_avg) == (5100, 4550, 2600, 875)
