"""

    task2_2_starter.py

"""
import json

import requests
base_url = 'http://localhost:8051'
path = '/api/invoices/'

# Step 1. You may optionally prompt the user for the invoice number
#         To do this, use:
#


# Step 2. Construct the URL to access the API resource.  Include the server, path, and invoice number

default_inv = '536365'
invoice_num = input('Enter invoice number: ')
if not invoice_num:
    invoice_num = default_inv

# Step 3. Use requests to make a request to the server using the URL from step 2.  Perform a .json()
#         on the returned results to obtain a dictionary.
url= f'{base_url}{path}{invoice_num}'
results = requests.get(url).json()

# Step 4. Display the dictionary.  One nice way to do this is to use the Python json module (already
#         imported).  You can pass the dictionary into json.dumps() and print this out.
print(results)
print(json.dumps(results, indent=4))


results_str = requests.get(url).text
print(results_str)
results_dict = json.loads(results_str)
print(results_dict)
