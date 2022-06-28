"""

    05_get_single_celebrity.py

"""
from flask import Flask, jsonify, Response
from pathlib import Path


app = Flask(__name__)

data = [line.strip().split(',') for line in Path('../data/celebrity_100.csv').open(encoding='utf-8')][1:]
print('Celebrity data read.')


@app.route('/api/celebrities/<name>', methods=['GET'])
def get_one_celebrity(name):
    try:
        results = [row for row in data if name.casefold() in row[0].casefold()]
    except Exception as err:
        results = err.args

    resp = jsonify(results=results, name=name)
    return Response(resp.data, status=200, mimetype='application/json')


app.run(host='localhost', port=8051)
