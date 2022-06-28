"""

    15_testing_flask_sqlalchemy_marshmallow.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/celebrities/'

print('posting:')
celeb_name = 'Fred Savage'
results = requests.post(f'{base_url}{path}',
                        data={'name': celeb_name, 'pay': 3.0,
                              'category': 'Actors', 'year': 2022})
print(results.text)
