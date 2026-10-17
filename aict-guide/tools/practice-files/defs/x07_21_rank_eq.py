"""Lesson 7.21: Positions: RANK.EQ."""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'rank-eq.mdx'
FOLDER = 'rank-eq'


def rank_eq(number, numbers, order=0):
    """RANK.EQ as Microsoft describes it: equal numbers share the top rank of their set."""
    if order == 0:
        return 1 + sum(1 for n in numbers if n > number)
    return 1 + sum(1 for n in numbers if n < number)


# Step by Step: a result sheet, total marks out of 500. Bilal and Usman have equal totals.
RESULTS = [('Ayesha', 412), ('Bilal', 389), ('Hira', 455), ('Usman', 389), ('Zainab', 430),
           ('Kashif', 367), ('Mariam', 398)]


def build_result_positions(wb, finished):
    ws = wb.active
    put_rows(ws, [('Name', 'Total (out of 500)', 'Position'), *RESULTS])
    if finished:
        for r in range(2, 2 + len(RESULTS)):
            formula(ws, f'C{r}', f'=RANK.EQ(B{r},$B$2:$B$8)')


totals = [t for _, t in RESULTS]
positions = [rank_eq(t, totals) for t in totals]

# Practice: a 100-metre race on sports day. The lowest time comes 1st, so order is 1.
# The finished file shows the end of the task, after Rizwan's time is corrected from 15.1 to
# 14.0 (Practice step 6).
RACE = [('Ahmed', 14.2), ('Danish', 13.8), ('Rizwan', 15.1), ('Saad', 13.8), ('Owais', 14.9),
        ('Junaid', 13.5)]
RACE_AFTER_CHANGE = [(n, 14.0 if n == 'Rizwan' else t) for n, t in RACE]


def build_race_times(wb, finished):
    ws = wb.active
    race = RACE_AFTER_CHANGE if finished else RACE
    put_rows(ws, [('Runner', 'Time (seconds)', 'Position'), *race])
    if finished:
        for r in range(2, 2 + len(race)):
            formula(ws, f'C{r}', f'=RANK.EQ(B{r},$B$2:$B$7,1)')


def race_positions(race):
    times = [t for _, t in race]
    return [rank_eq(t, times, 1) for t in times]


race_before = race_positions(RACE)
race_after = race_positions(RACE_AFTER_CHANGE)

FILES = [
    XlsxFile('result-positions', build_result_positions,
             {f'C{r}': v for r, v in zip(range(2, 9), positions)}),
    XlsxFile('race-times', build_race_times,
             {f'C{r}': v for r, v in zip(range(2, 8), race_after)}),
]

# The lesson states these results; keep them in step with the page.
assert positions == [3, 5, 1, 5, 2, 7, 4]
assert 6 not in positions                      # the tie at 5th skips 6th
assert race_before == [4, 2, 6, 2, 5, 1]
assert race_after == [5, 2, 4, 2, 6, 1]
# Check Question 2: Kashif's total changed to 455 (only on the page, not in the files).
q2_totals = [455 if n == 'Kashif' else t for n, t in RESULTS]
assert [rank_eq(t, q2_totals) for t in q2_totals] == [4, 6, 1, 6, 3, 1, 5]
