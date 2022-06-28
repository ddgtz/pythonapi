"""

    task2_2_solution.py

"""
import json

import requests

base_url = 'http://localhost:8051'
path = '/api/invoices/'

default = '536365'
invoice_num = input('Enter invoice number to retrieve (def. 536365): ')
if not invoice_num:
    invoice_num = default

results = requests.get(f'{base_url}{path}{invoice_num}').json()
print(json.dumps(results, indent=4))
