"""

    02_acquiring_data.py

"""
from flask import Flask
from pathlib import Path


app = Flask(__name__)

data = [line.strip().split(',') for line in Path('../data/celebrity_100.csv').open(encoding='utf-8')][1:]
print('Celebrity data read.')


app.run(host='localhost', port=8051)
