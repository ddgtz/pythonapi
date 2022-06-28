"""

    03_creating_a_mapping.py

"""
from flask import Flask
from pathlib import Path


app = Flask(__name__)

data = [line.strip().split(',') for line in Path('../data/celebrity_100.csv').open(encoding='utf-8')][1:]
print('Celebrity data read.')


@app.route('/api/celebrities/<name>', methods=['GET'])
def do_stuff(name):
    return f'Hi there {name}!'


app.run(host='localhost', port=8051)
