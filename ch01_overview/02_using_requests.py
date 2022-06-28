"""

    02_using_requests.py

"""
import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/1', params={'age': 37})
print(r.url)
print(r.text)
print(r.json())
print(r.headers)
print(r.status_code)
