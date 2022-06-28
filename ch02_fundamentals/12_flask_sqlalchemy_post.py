"""

    12_flask_sqlalchemy_post.py

"""
from pathlib import Path
import sys

from flask import Flask, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

student_files_dir = Path(__file__).parents[1]     # our student_files directory
db_file = student_files_dir / 'data/course_data.db'

if not db_file.exists():
    print(f'Database file does not exist at: {db_file}--exiting.', file=sys.stderr)
    sys.exit()

app = Flask(__name__)
api = Api(app, prefix='/api')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(db_file)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(f'Using db engine: {db.engine}')


class CelebrityModel(db.Model):
    __tablename__ = 'celebrity'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    pay = db.Column(db.Float)
    year = db.Column(db.String(15))
    category = db.Column(db.String(50))

    def __init__(self, name, pay, year, category):
        self.name = name
        self.pay = pay
        self.year = year
        self.category = category

    def __str__(self):
        return f'{self.year} {self.name} {self.pay} {self.category}'


class Celebrities(Resource):
    def get(self):
        return {'celebrities': []}

    def post(self):
        name = request.form.get('name')
        year = request.form.get('year')
        category = request.form.get('category')
        pay = float(request.form.get('pay'))

        new_celeb = CelebrityModel(name, pay, year, category)
        db.session.add(new_celeb)
        db.session.commit()

        return {'id': new_celeb.id, 'name': name, 'year': year, 'pay': pay, 'category': category}


class Celebrity(Resource):
    def get(self, id):
        return {'action': 'get'}

    def delete(self, id):
        return {'action': 'delete'}

    def put(self, id):
        return {'action': 'put'}


api.add_resource(Celebrity, '/celebrities/<string:id>')
api.add_resource(Celebrities, '/celebrities/')


app.run(host='localhost', port=8051)
