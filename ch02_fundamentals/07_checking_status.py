"""

    07_checking_status.py

"""
import requests

r = requests.get('http://httpbin.org/status/200')

if r.ok:
    print('Request was successful.')

if r.status_code == 200:
    print('Request was successful.')

if r:
    print('Requests returned a non-400 or 500 error code.')

r = requests.get('http://httpbin.org/status/400')
try:
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
