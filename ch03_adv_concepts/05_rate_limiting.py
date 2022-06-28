"""

    05_rate_limiting.py

"""


from flask import Flask, jsonify, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from pathlib import Path


app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

data = [line.strip().split(',') for line in Path('../data/celebrity_100.csv').open(encoding='utf-8')][1:]
print('Celebrity data read.')


@app.route('/api/celebrities/<name>', methods=['GET'])
@limiter.limit('3/minute')
def get_one_celebrity(name):
    try:
        results = [row for row in data if name.casefold() in row[0].casefold()]
    except Exception as err:
        results = err.args

    resp = jsonify(results=results, name=name)
    return Response(resp.data, status=200, mimetype='application/json')


app.run(host='localhost', port=8051)
