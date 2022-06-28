"""

    task2_3_client.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/invoices/'
invoice_num = '536365'

results = requests.get(f'{base_url}{path}{invoice_num}')
print(results.text)

print('posting:')
results = requests.post(f'{base_url}{path}')
print(results.text)

print('putting:')
results = requests.put(f'{base_url}{path}{invoice_num}')
print(results.text)

print('deleting:')
results = requests.delete(f'{base_url}{path}{invoice_num}')
print(results.text)

print('get all (100 invoices):')
results = requests.get(f'{base_url}{path}')
print(results.text)
