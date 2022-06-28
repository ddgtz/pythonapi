"""

    task2_3_starter.py

    This version of the exercise will add in additional methods using the
    Flask-RESTX plugin.  You will build the classes needed to

"""
from pathlib import Path

from flask import Flask, jsonify, Response
# Step 1: import Resource and Api from flask_restx

app = Flask(__name__)
# Step 2: Create the Api() object passing the Flask app object into it as the first argument.  Set a prefix parameter of '/api' as observed in the Celebrity Flask-RESTX example.

data_file = '../data/customer_purchases.csv'
data = [line.strip().split(',') for line in Path(data_file).open(encoding='unicode_escape')][1:]
print('Customer purchase data read.')

# Step 3: Create an Invoices and Invoice class.  Have each inherit from Resource.

# Step 4: At the bottom (just above the app.run() statement), define the two Resources and endpoints
#         as follows:
#                api.add_resource(Invoice, '/invoices/<string:invoice_num>')
#                api.add_resource(Invoices, '/invoices/')

# Step 5: Move the retrieve_invoice() method into the Invoice class.  Drop the decorator.  Rename the method to get().

# Step 6: Create a get() and post() method within Invoices.

# Step 7: Create a put() and delete() method within Invoice.  Each should accept
#         an invoice_num parameter after the self parameter.

# Step 8 For now, have the put(), delete() and post() methods return a simple object (for example,
#        {'action': 'delete'}).  Have the get method within Invoices() return the first 100 invoices.


@app.route('/api/invoices/<invoice_num>', methods=['GET'])
def retrieve_invoice(invoice_num):
    results = [row[1:] for row in data if invoice_num == row[0]]

    resp = jsonify(results=results, invoice=invoice_num)
    return Response(resp.data, status=200, mimetype='application/json')


app.run(host='localhost', port=8051)
