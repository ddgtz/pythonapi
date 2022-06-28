"""

    05b_testing_rate_limit
    This client should be used with the 05_rate_limiting.py server.

"""
import json

import requests

base_url = 'http://localhost:8051'
path = '/api/celebrities/'
celeb_id = default = 'Kevin'

while True:
    celeb_id = input('Enter celebrity name to find (def. Kevin, 0 to exit): ')
    if not celeb_id:
        celeb_id = default
    elif celeb_id == '0':
        break

    r = requests.get(f'{base_url}{path}{celeb_id}')
    try:
        results = r.json()
        print(json.dumps(results, indent=4))
    except requests.exceptions.RequestException as err:
        print(err)
