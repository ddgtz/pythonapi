"""

    task2_6_starter.py

"""
from pathlib import Path
import sys

from flask import Flask, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
# Step 1. import Marshmallow from flask_marshmallow


app = Flask(__name__)
api = Api(app, prefix='/api')
# Step 2. instantiate the Marshmallow object as discussed in the notes     ma = Marshmallow(app)

student_files_dir = Path(__file__).parents[1]     # our student_files directory (1 levels up)
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
        # Step 4. Complete this method by using SQLAlchemy to retrieve all invoices
        #         Remove the return below.
        #         Hint: use InvoiceModel.query.all()
        #         Return a JSON object that contains the searched results.
        #         Hint: use the invoices_schema object and dump the results.
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
        # Step 5. Complete this method by using SQLAlchemy to retrieve one invoice.
        #         Hint: use InvoiceModel.query.get(id)
        #         Return a JSON object that contains the desired invoice
        #         Hint: use the invoice_schema object and jsonify the query results.
        return {'action': 'get'}

    def put(self, id):
        # Step 6. Complete this method by using SQLAlchemy to first retrieve the desired invoice
        #         Hint: use InvoiceModel.query.get(id) again
        #         Then obtain each submitted form field.
        #         Hint: It's the same 8 lines from the post() method above.
        #         (And, yes, this could be turned into a function)
        #         Assign the newly submitted values to the invoice instance
        #         Hint: invoice.invoice_no = invoice_no  (repeat for 7 other fields)
        #         Commit the changes (no hint, it's just db.session.commit() )
        #         Return a JSON object that contains the desired invoice
        #         Hint: It's the same as the return from the get() method
        return {'action': 'put'}

    def delete(self, id):
        # Step 7. By now this should be a little familiar.  So, no hints this time.
        #         Retrieve the object with the provided id.
        #         Delete it using the SQLAlchemy db.session.
        #         Commit the data.
        #         Return a JSON object, as done in the above two methods.
        return {'action': 'delete'}

# Step 3. A Marshmallow class has been created for us (simply uncomment it).
# class InvoiceSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'invoice_no', 'stock_code', 'quantity', 'description', 'invoice_date', 'unit_price', 'customer_id', 'country')

# Next, instantiate an InvoiceSchema() object and a plural-based version (many=True).
# invoice_schema = InvoiceSchema()
# invoice_schemas = InvoiceSchema(many=True)


api.add_resource(Invoice, '/invoices/<string:id>')
api.add_resource(Invoices, '/invoices/')

app.run(host='localhost', port=8051)
