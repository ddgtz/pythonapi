"""

    10_adding_other_operations.py

"""
from pathlib import Path

from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app, prefix='/api')

data = [line.strip().split(',') for line in Path('../data/celebrity_100.csv').open(encoding='utf-8')][1:]
print('Celebrity data read.')


class Celebrities(Resource):
    def get(self):
        return {'celebrities': data}

    def post(self):
        print('post:', request.form)
        return {'action': 'post'}


class Celebrity(Resource):
    def get(self, name):
        try:
            results = [row for row in data if name.casefold() in row[0].casefold()]
        except Exception as err:
            results = err.args

        return {'results': results, 'name': name}

    def delete(self, name):
        return {'action': 'delete'}

    def put(self, name):
        return {'action': 'put'}


api.add_resource(Celebrity, '/celebrities/<string:name>')
api.add_resource(Celebrities, '/celebrities/')


app.run(host='localhost', port=8051)
