"""

    08_classes.py

"""
from pathlib import Path


class Celebrity:
    def __init__(self, name, pay, year, category):
        self.name = name
        self.pay = pay
        self.year = year
        self.category = category

    def __str__(self):
        return f'{self.year:<6}{self.name} ({self.category}) ${self.pay:>} million'


f = Path('../data/celebrity_100.csv').open(encoding='utf-8')
f.readline()  # reads the header
data = f.readline().strip().split(',')

celeb = Celebrity(*data)
print(celeb)
