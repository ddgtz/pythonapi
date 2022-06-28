"""
    example02.py
    Sequences and Iterating
"""
my_list = [1, 2, 3]
my_list.append(10)
my_list.insert(1, 'hello')
print(my_list)


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for season in seasons:
    if season.lower().startswith('s'):
        print(f'{season} has {len(season)} characters.')

records = [
    ('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    ('Ellen', 'James',   32, 'jamestel@google.com'),
    ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    ('Keith', 'Cramer',  29, 'kcramer@sintech.com')
]

for record in records:
    print(f'{record[0]} {record[1]}, {record[2]} {record[3]}')

for record in records:
    print('{0} {1}, {2} {3}'.format(*record))

for (first, last, age, email) in records:
    print(f'{first} {last}, {age} {email}')

for first, last, age, email in records:
    print('{first} {last}, {age} {email}'.format(first=first, last=last, age=age, email=email))
