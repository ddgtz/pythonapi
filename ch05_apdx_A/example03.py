"""
    example03.py
    Dictionaries
"""
print('\nCreating and accessing dicts:')
my_dict = {}
my_dict = dict()
my_dict = {'pet1': 'dog', 'pet2': 'fish' }
my_dict = dict(pet1='dog', pet2='fish')

my_dict['pet3'] = 'cat'
print(my_dict['pet2'])


print('\nIterating dicts:')
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
for item in d1:                     # iterating a dictionary returns the keys
    print(item, end=' ')


print('\n\nIterating dict values:')
for val in d1.values():             # iterating the values
    print(val, end=' ')


print('\nIterating keys and values:')
for key, val in d1.items():         # iterating both keys and values
    print(f'Key: {key}, Value: {val}')


print('\nAccessing dicts:')
print(d1.get('Green'))              # returns None
print(d1.get('Green', 'N/A'))       # returns N/A
# print(d1['Green'])                 # generates a KeyError


print('\nSorting with dicts:')
list1 = sorted(d1.keys())
list2 = sorted(d1.values())
print(list1, list2)

list3 = [value for (key, value) in sorted(d1.items())]
print(list3)


# ------------------------------------------------------------------------
# using an OrderedDict is the appropriate way for handling order in dicts
from collections import OrderedDict

d4 = OrderedDict([('Smith', 43), ('James', 32), ('Edwards', 36), ('Cramer', 29)])
for val in d4.values():
    print(val, end=' ')


# --------------------------------------------------------------
# using a defaultdict
from collections import defaultdict
d5 = defaultdict(str)
d5['greet1'] = 'hello'
print(d5['greet1'], d5['greet2'])
