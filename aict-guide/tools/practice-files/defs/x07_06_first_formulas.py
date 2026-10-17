"""Lesson 7.6: Your First Formulas.

Starter = the words and numbers typed, answer cells empty. Finished = the end of each task, with
the formulas, after the number is changed (Step by Step step 11: B1 = 1500; Practice step 6:
B2 = 300), like the pilot lesson 7.8.
"""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'first-formulas.mdx'
FOLDER = 'first-formulas'

# Step by Step: Bilal's shop. None = answer cell (left empty in the starter).
SHOP = [('Morning sales (Rs)', 1200), ('Evening sales (Rs)', 800), ('Total sales (Rs)', None),
        ('Cost of goods (Rs)', 1450), ('Profit (Rs)', None), ('Pens sold', 12),
        ('Price of one pen (Rs)', 25), ('Money from pens (Rs)', None), ('Bill to share (Rs)', 1500),
        ('People', 3), ('Each person pays (Rs)', None)]
SHOP_FORMULAS = {'B3': '=B1+B2', 'B5': '=B3-B4', 'B8': '=B6*B7', 'B11': '=B9/B10'}
MORNING_AFTER_CHANGE = 1500


def build_shop_money(wb, finished):
    ws = wb.active
    put_rows(ws, SHOP, bold_first=False)
    if finished:
        ws['B1'] = MORNING_AFTER_CHANGE
        for ref, text in SHOP_FORMULAS.items():
            formula(ws, ref, text)


# Practice: Hina's school trip.
TRIP = [('Bus fare (Rs)', 350), ('Lunch (Rs)', 250), ('Cost for one student (Rs)', None),
        ('Money from home (Rs)', 1000), ('Money left (Rs)', None), ('Number of students', 25),
        ('Cost for all students (Rs)', None), ('Number of groups', 5),
        ('Students in each group', None)]
TRIP_FORMULAS = {'B3': '=B1+B2', 'B5': '=B4-B3', 'B7': '=B3*B6', 'B9': '=B6/B8'}
LUNCH_AFTER_CHANGE = 300


def build_school_trip(wb, finished):
    ws = wb.active
    put_rows(ws, TRIP, bold_first=False)
    if finished:
        ws['B2'] = LUNCH_AFTER_CHANGE
        for ref, text in TRIP_FORMULAS.items():
            formula(ws, ref, text)


def shop_results(morning):
    b = {1: morning, 2: 800, 4: 1450, 6: 12, 7: 25, 9: 1500, 10: 3}
    b[3] = b[1] + b[2]
    return {'B3': b[3], 'B5': b[3] - b[4], 'B8': b[6] * b[7], 'B11': b[9] / b[10]}


def trip_results(lunch):
    b = {1: 350, 2: lunch, 4: 1000, 6: 25, 8: 5}
    b[3] = b[1] + b[2]
    return {'B3': b[3], 'B5': b[4] - b[3], 'B7': b[3] * b[6], 'B9': b[6] / b[8]}


FILES = [
    XlsxFile('shop-money', build_shop_money, shop_results(MORNING_AFTER_CHANGE)),
    XlsxFile('school-trip', build_school_trip, trip_results(LUNCH_AFTER_CHANGE)),
]

# The lesson states these results; keep them in step with the page.
assert [dict(SHOP)[k] for k in ('Morning sales (Rs)', 'Evening sales (Rs)')] == [1200, 800]
assert shop_results(1200) == {'B3': 2000, 'B5': 550, 'B8': 300, 'B11': 500}
assert shop_results(1500) == {'B3': 2300, 'B5': 850, 'B8': 300, 'B11': 500}
assert trip_results(250) == {'B3': 600, 'B5': 400, 'B7': 15000, 'B9': 5}
assert trip_results(300) == {'B3': 650, 'B5': 350, 'B7': 16250, 'B9': 5}
