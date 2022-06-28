import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


page = 'https://jigsaw.w3.org/HTTP/Basic/'
auth = HTTPBasicAuth('guest', 'guest')
page_text = requests.get(page, auth=auth).text
soup = BeautifulSoup(page_text, 'html.parser')
print(soup.select('p')[2].text)
