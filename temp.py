from flask import Flask, jsonify, Response
from pathlib import Path
app =Flask(__name__)

data = [line.strip().split(',') for line in Path('data/celebrity_100.csv').open()]

#data = []
#with Path('data/celebrity_100.csv').open() as f:
#    f.readline()
#    for line in f:
#        data.append(line.strip().split(','))

@app.route('/api/celebrities/<name>')

def get_celebrity(name):
    results=[]
    try:
        results = [item for item in data if name.lower() == item[0].lower()]
    except Exception as err:
        results = err.args
    obj = jsonify(results=results, search_name=name)
    return Response (obj.data, status=200, mimetype='application/json')
app.run(host='localhost',port=8051)
