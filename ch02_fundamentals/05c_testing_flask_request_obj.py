"""

    05c_testing_flask_request_obj.py

"""
from datetime import date

import requests

birthdate = date.today().strftime('%Y-%m-%d')
payload = {'first': 'Fred', 'middle': 'Aaron', 'pay': 3.0}
url = f'http://localhost:8051/celebrity/Savage?category=Actors&birthdate={birthdate}'

print(f'Results: {requests.post(url, data=payload).json()}')
