"""

    task2_5_client.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/invoices/'
invoice_no = '581588'

payload = {
    'invoice_no': invoice_no,
    'stock_code': '20961',
    'quantity': 3,
    'description': 'STRAWBERRY BATH SPONGE',
    'invoice_date': '2/2/2022',
    'unit_price': 2.46,
    'customer_id': 17850,
    'country': 'United Kingdom'
}

print('posting:')
results = requests.post(f'{base_url}{path}', data=payload)
print(results.text)
