"""

    02_testing_pagination.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/celebrities/'


print('getting:')
new_celeb_id = '2000'
results = requests.get(f'{base_url}{path}{new_celeb_id}')
print(f'Status: {results.status_code}')
print(results.text)

