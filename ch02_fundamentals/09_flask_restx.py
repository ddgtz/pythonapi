"""

    09_flask_restx.py

"""
from pathlib import Path

from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

data = [line.strip().split(',') for line in Path('../data/celebrity_100.csv').open(encoding='utf-8')][1:]
print('Celebrity data read.')


@api.route('/api/celebrities/<string:name>')
class Celebrity(Resource):

    def get(self, name):
        try:
            results = [row for row in data if name.casefold() in row[0].casefold()]
        except Exception as err:
            results = err.args

        return {'results': results, 'name': name}


app.run(host='localhost', port=8051)
