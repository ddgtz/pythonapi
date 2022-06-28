"""

    task2_6_client.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/invoices/'

payload = {
    'invoice_no': '581588',
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

print('getting:')
new_invoice_id = results.json().get('id')
results = requests.get(f'{base_url}{path}{new_invoice_id}')
print(results.text)

print('putting:')    # note put is appropriate because we are sending all object fields
payload['quantity'] = 6
results = requests.put(f'{base_url}{path}{new_invoice_id}', data=payload)
print(results.text)

print('deleting:')
results = requests.delete(f'{base_url}{path}{new_invoice_id}')
print(results.text)