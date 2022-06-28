"""

    task3_1_client.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/invoices/'

for n in range(1, 4):
    print(f'\ngetting page ({n}):')
    results = requests.get(f'{base_url}{path}', params={'page': n})
    print(results.text)
