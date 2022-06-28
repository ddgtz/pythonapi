"""

    task2_5_starter.py

"""
from pathlib import Path
import sys

from flask import Flask, request
from flask_restx import Resource, Api
# Step 1. Add the import for SQLAlchemy from the flask_sqlalchemy module

app = Flask(__name__)
api = Api(app, prefix='/api')

# Step 2. Note: the path to the database has been provided for us below and it
#         will error out if it is incorrect (nothing to do here)
student_files_dir = Path(__file__).parents[1]     # our student_files directory (1 level up)
print(student_files_dir)
db_file = student_files_dir / 'data/course_data.db'

if not db_file.exists():
    print(f'Database file does not exist at: {db_file}--exiting.', file=sys.stderr)
    sys.exit()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(db_file)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Step 3. Instantiate the SQLAlchemy() main object passing the app object into it

# Step 4. Create the InvoiceModel class.  Inherit from db.model
#         To save a little time, here are the field mappings for this object/table:
#             __tablename__ = 'purchases'
#             id = db.Column(db.Integer, primary_key=True)
#             invoice_no = db.Column('InvoiceNo', db.String(30))
#             stock_code = db.Column('StockCode', db.String(30))
#             quantity = db.Column(db.Integer)
#             description = db.Column(db.String(150))
#             invoice_date = db.Column('InvoiceDate', db.String(50))
#             unit_price = db.Column('UnitPrice', db.Float)
#             customer_id = db.Column('CustomerID', db.String(50))
#             country = db.Column(db.String(50))
#
#         You should still build the __init__().


# Step 5. Refactor the post() method below.  It should obtain the fields from the
#         request object.  Instantiate an InvoiceModel.  Populate the model instance
#         with the request data.  Insert it into the database.
class Invoices(Resource):
    def get(self):
        return {'action': 'get all'}

    def post(self):
        return {'action': 'post'}


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
