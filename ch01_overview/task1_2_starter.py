"""

    task1_2_starter.py

    As part of Task 1-2, run this file to verify your interpreter
    is set up and ready to be used.  If it runs, then prettytable (and thus the other
    items) will be set up.  We don't use prettytable in this course it's just
    used as a test here.

"""
from prettytable import from_csv


with open('../data/celebrity_100.csv') as f:
    table = from_csv(f)

table.align['Name'] = 'l'
table.align['Pay (USD millions)'] = 'r'
table.align['Category'] = 'l'
print(table)


