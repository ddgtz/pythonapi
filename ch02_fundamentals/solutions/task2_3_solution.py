"""

    task2_3_solution.py

    This version of the exercise will add in additional methods using the
    Flask-RESTX plugin.  You will build the classes needed to

"""
from pathlib import Path

from flask import Flask
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app, prefix='/api')

data_file = '../../data/customer_purchases.csv'
data = [line.strip().split(',') for line in Path(data_file).open(encoding='unicode_escape')][1:]
print('Customer purchase data read.')


class Invoices(Resource):
    def get(self):
        return {'results100': data[1:100]}

    def post(self):
        return {'action': 'post'}


class Invoice(Resource):
    def get(self, invoice_num):
        results = [row[1:] for row in data if invoice_num == row[0]]
        return {'results': results}

    def put(self, invoice_num):
        return {'action': 'put'}

    def delete(self, invoice_num):
        return {'action': 'delete'}


api.add_resource(Invoice, '/invoices/<string:invoice_num>')
api.add_resource(Invoices, '/invoices/')

app.run(host='localhost', port=8051)
