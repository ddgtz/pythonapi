"""

    18_flask_sqlalchemy_put.py

"""
from pathlib import Path
import sys

from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

student_files_dir = Path(__file__).parents[1]     # our student_files directory
db_file = student_files_dir / 'data/course_data.db'

if not db_file.exists():
    print(f'Database file does not exist at: {db_file}--exiting.', file=sys.stderr)
    sys.exit()

app = Flask(__name__)
api = Api(app, prefix='/api')
ma = Marshmallow(app)

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
        all_celebs = CelebrityModel.query.all()
        return {'results': celebrities_schema.dump(all_celebs)}

    def post(self):
        name = request.form.get('name')
        year = request.form.get('year')
        category = request.form.get('category')
        pay = float(request.form.get('pay'))

        new_celeb = CelebrityModel(name, pay, year, category)
        db.session.add(new_celeb)
        db.session.commit()

        return celebrity_schema.jsonify(new_celeb)


class Celebrity(Resource):
    def get(self, id):
        celeb = CelebrityModel.query.get(id)
        return celebrity_schema.jsonify(celeb)

    def delete(self, id):
        celeb = CelebrityModel.query.get(id)
        db.session.delete(celeb)
        db.session.commit()
        return celebrity_schema.jsonify(celeb)

    def put(self, id):
        year = request.form.get('year')
        category = request.form.get('category')
        pay = float(request.form.get('pay'))

        celeb = CelebrityModel.query.get(id)
        celeb.year = year
        celeb.category = category
        celeb.pay = pay

        db.session.commit()

        return celebrity_schema.jsonify(celeb)

class CelebritySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'year', 'pay', 'category')   # Fields to expose


celebrity_schema = CelebritySchema()
celebrities_schema = CelebritySchema(many=True)

api.add_resource(Celebrity, '/celebrities/<string:id>')
api.add_resource(Celebrities, '/celebrities/')


app.run(host='localhost', port=8051)
