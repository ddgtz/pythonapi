"""

    04_working_with_json.py

"""
from flask import Flask, jsonify, Response
from pathlib import Path


app = Flask(__name__)

data = [line.strip().split(',') for line in Path('../data/celebrity_100.csv').open(encoding='utf-8')][1:]
print('Celebrity data read.')


@app.route('/api/celebrities/<name>', methods=['GET'])
def do_stuff(name):
    results = ['value1', 'value2', 'value3']

    resp = jsonify(results=results, name=name, sample='message')
    return Response(resp.data, status=200, mimetype='application/json')


app.run(host='localhost', port=8051)
