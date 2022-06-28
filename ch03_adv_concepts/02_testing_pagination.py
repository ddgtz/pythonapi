"""

    02_testing_pagination.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/celebrities'

for n in range(1, 4):
    print(f'\ngetting page ({n}):')
    results = requests.get(f'{base_url}{path}', params={'page': n})
    print(f'Status: {results.status_code}')
    print(results.text)
