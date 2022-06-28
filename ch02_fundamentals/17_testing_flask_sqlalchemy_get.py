"""

    17_testing_flask_sqlalchemy_get.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/celebrities/'

print('get:')
id = 235
results = requests.get(f'{base_url}{path}{id}')
print(results.text)

print('get all:')
results = requests.get(f'{base_url}{path}')
print(results.text)
