"""

    06_consuming_apis.py

"""
import json

import requests

base_url = 'http://localhost:8051'
path = '/api/celebrities/'
default = 'Kevin'

celeb_name = input('Enter celebrity to find info about (def. Kevin): ')
if not celeb_name:
    celeb_name = default

results = requests.get(f'{base_url}{path}{celeb_name}').json()
print(json.dumps(results, indent=4))
