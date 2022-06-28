"""

    task2_1_starter.py

    To test this out, for now, simply use a browser.
    Start the server and browser to:
    http://localhost:8051/api/invoices/536365

"""
from pathlib import Path

from flask import Flask, jsonify, Response

app = Flask(__name__)

# Step 1. create the main Flask() object, call it app

data_file = '../data/customer_purchases.csv'
data = [line.strip().split(',') for line in Path(data_file).open(encoding='unicode_escape')][1:]
print('Customer purchase data read.')

# Step 2. Create a decorator below that defines the URL mapping for this function.
#         The mapping URL path is up to you.
#         Use a path parameter (/<_____>) to allow an invoice number to be specified

@app.route('/api/invoices/<invoice_num>', methods=['GET'])

def retrieve_invoice(invoice_num):
    # Step 3. Complete the line so that it searches data to find the matching invoice nums
    results = [ line for line in data if invoice_num == line[0]]

    # Step 4. Complete the jsonify() statement to return our newly found data results
    resp = jsonify(results=results, invoice_num=invoice_num)
    return Response(resp.data, status=200, mimetype='application/json')


app.run(host='localhost', port=8051)
