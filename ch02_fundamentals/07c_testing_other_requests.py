"""

    07c_testing_other_requests.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/celebrities/'
celeb_name = 'Kevin'

results = requests.get(f'{base_url}{path}{celeb_name}')
print(results.text)

print('posting:')
results = requests.post(f'{base_url}{path}'.strip('/'),
                        data={'name': celeb_name,
                              'category': 'Actors',
                              'pay': 3.0,
                              'year': 2022})
print(results.text)

print('putting:')
results = requests.put(f'{base_url}{path}{celeb_name}')
print(results.text)

print('deleting:')
results = requests.delete(f'{base_url}{path}{celeb_name}')
print(results.text)

print('get all:')
results = requests.get(f'{base_url}{path}'.strip('/'))
print(results.text)
