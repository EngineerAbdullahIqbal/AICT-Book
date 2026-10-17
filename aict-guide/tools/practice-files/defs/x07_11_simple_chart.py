"""Lesson 7.11: Making a Simple Chart.

The tables have no formulas, so `expected` is empty. The finished files add the titled column
chart (a clustered column chart, Excel's plain column chart) to the right of the table.
"""

from openpyxl.chart import BarChart, Reference
from openpyxl.chart.data_source import AxDataSource, StrRef

from xlsxkit import XlsxFile, put_rows

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'simple-chart.mdx'
FOLDER = 'simple-chart'


def add_column_chart(ws, title, last_row, anchor):
    """A column chart of A1:B<last_row> (names in A, numbers in B, headings in row 1)."""
    chart = BarChart()
    chart.type = 'col'
    chart.grouping = 'clustered'
    chart.title = title
    chart.add_data(Reference(ws, min_col=2, min_row=1, max_row=last_row), titles_from_data=True)
    # The names are text, so the categories are a text reference (strRef).
    chart.series[0].cat = AxDataSource(strRef=StrRef(f=f"'{ws.title}'!$A$2:$A${last_row}"))
    chart.legend = None              # one series: the title says what it is
    chart.x_axis.delete = False      # show both axes in Excel
    chart.y_axis.delete = False
    ws.add_chart(chart, anchor)


# Step by Step: one week's sales at a small shop.
SALES = [('Monday', 4500), ('Tuesday', 3800), ('Wednesday', 5200), ('Thursday', 4100),
         ('Friday', 6000), ('Saturday', 7300)]


def build_weekly_sales(wb, finished):
    ws = wb.active
    put_rows(ws, [('Day', 'Sales (Rs)'), *SALES])
    if finished:
        add_column_chart(ws, 'Weekly Sales', 7, 'D2')


# Practice: Nadia's family's monthly expenses.
EXPENSES = [('Groceries', 18000), ('Electricity', 6500), ('Gas', 2500), ('Milk', 4200),
            ('Transport', 5000), ('School fees', 7000)]


def build_monthly_expenses(wb, finished):
    ws = wb.active
    put_rows(ws, [('Item', 'Amount (Rs)'), *EXPENSES])
    if finished:
        add_column_chart(ws, 'Monthly Expenses', 7, 'D2')


FILES = [
    XlsxFile('weekly-sales', build_weekly_sales),
    XlsxFile('monthly-expenses', build_monthly_expenses),
]

# The lesson states these results; keep them in step with the page.
assert max(SALES, key=lambda r: r[1]) == ('Saturday', 7300)
assert min(SALES, key=lambda r: r[1]) == ('Tuesday', 3800)
assert max(EXPENSES, key=lambda r: r[1]) == ('Groceries', 18000)
assert min(EXPENSES, key=lambda r: r[1]) == ('Gas', 2500)
