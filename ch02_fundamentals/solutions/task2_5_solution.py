"""

    task2_5_solution.py

    This version of the exercise will add in Flask-SQLAlchemy plugin to integrate
    our database.

"""
from pathlib import Path
import sys

from flask import Flask, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app, prefix='/api')

student_files_dir = Path(__file__).parents[2]     # our student_files directory (2 levels up)
db_file = student_files_dir / 'data/course_data.db'

if not db_file.exists():
    print(f'Database file does not exist at: {db_file}--exiting.', file=sys.stderr)
    sys.exit()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(db_file)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
print(f'Using db engine: {db.engine}')


class InvoiceModel(db.Model):
    __tablename__ = 'purchases'
    id = db.Column(db.Integer, primary_key=True)
    invoice_no = db.Column('InvoiceNo', db.String(30))
    stock_code = db.Column('StockCode', db.String(30))
    quantity = db.Column(db.Integer)
    description = db.Column(db.String(150))
    invoice_date = db.Column('InvoiceDate', db.String(50))
    unit_price = db.Column('UnitPrice', db.Float)
    customer_id = db.Column('CustomerID', db.String(50))
    country = db.Column(db.String(50))

    def __init__(self, invoice_no, stock_code, quantity, description, invoice_date,
                 unit_price, customer_id, country):
        self.invoice_no = invoice_no
        self.stock_code = stock_code
        self.quantity = quantity
        self.description = description
        self.invoice_date = invoice_date
        self.unit_price = unit_price
        self.customer_id = customer_id
        self.country = country

    def __str__(self):
        return f'{self.year} {self.name} {self.pay} {self.category}'


class Invoices(Resource):
    def get(self):
        return {'action': 'get all'}

    def post(self):
        invoice_no = request.form.get('invoice_no')
        stock_code = request.form.get('stock_code')
        quantity = int(request.form.get('quantity'))
        description = request.form.get('description')
        invoice_date = request.form.get('invoice_date')
        unit_price = float(request.form.get('unit_price'))
        customer_id = request.form.get('customer_id')
        country = request.form.get('country')

        new_purchase = InvoiceModel(invoice_no, stock_code, quantity, description, invoice_date,
                                 unit_price, customer_id, country)
        db.session.add(new_purchase)
        db.session.commit()

        return {'id': new_purchase.id, 'invoice_no': invoice_no, 'stock_code': stock_code, 'quantity': quantity, 'description': description,
                'invoice_date': invoice_date, 'unit_price': unit_price, 'customer_id': customer_id, 'country': country}


class Invoice(Resource):
    def get(self, id):
        return {'action': 'get'}

    def put(self, id):
        return {'action': 'put'}

    def delete(self, id):
        return {'action': 'delete'}


api.add_resource(Invoice, '/invoices/<string:id>')
api.add_resource(Invoices, '/invoices/')

app.run(host='localhost', port=8051)
