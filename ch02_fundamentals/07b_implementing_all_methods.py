"""

    07b_implementing_all_methods.py

    This version is an extension of the 05_get_single_celebrity.py version.
    It implements stubs for the GET (one), POST, PUT, and DELETE

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


# Now we can implement the other methods on our resource...
@app.route('/api/celebrities', methods=['GET'])
def get_all_celebrities():
    resp = jsonify(action='GET (all) response')
    return Response(resp.data, status=200, mimetype='application/json')


@app.route('/api/celebrities', methods=['POST'])
def create_celebrity():
    resp = jsonify(action='POST response')
    return Response(resp.data, status=200, mimetype='application/json')


@app.route('/api/celebrities/<name>', methods=['PUT'])
def update_celebrity(name):
    resp = jsonify(action='PUT response')
    return Response(resp.data, status=200, mimetype='application/json')


@app.route('/api/celebrities/<name>', methods=['DELETE'])
def delete_celebrity(name):
    resp = jsonify(action='DELETE response')
    return Response(resp.data, status=200, mimetype='application/json')


app.run(host='localhost', port=8051)
