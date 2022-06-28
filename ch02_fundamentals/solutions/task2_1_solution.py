"""

    task2_1_solution.py

    To test this out, for now, simply use a browser.
    Start the server and browser to:
    http://localhost:8051/api/invoices/536365


"""
from pathlib import Path

from flask import Flask, jsonify, Response


app = Flask(__name__)
data_file = '../../data/customer_purchases.csv'
data = [line.strip().split(',') for line in Path(data_file).open(encoding='unicode_escape')][1:]
print('Customer purchase data read.')


@app.route('/api/invoices/<invoice_num>', methods=['GET'])
def retrieve_invoice(invoice_num):
    results = [row[1:] for row in data if invoice_num == row[0]]

    resp = jsonify(results=results, invoice=invoice_num)
    return Response(resp.data, status=200, mimetype='application/json')


app.run(host='localhost', port=8051)
