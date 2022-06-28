"""

    task1_3_solution.py

"""
import requests


urls = [
    'https://api.coinlore.net/api/tickers/?start1&limit=5',
    'https://apimeme.com/meme?top=Tell%20Me%20More&bottom=About%20Chocolate',
    'https://cat-fact.herokuapp.com/facts'
]

for url in urls:
    r = requests.get(url)

    print(r.url)
    print('-'*len(r.url))
    print(r.text)            # or r.json()



# For fun, here's how to capture the apimeme.com image into a file...
file = open('meme_image.jpg', 'wb')
file.write(requests.get(urls[1]).content)



# (Optional) Advanced version (read the URLs from task1_1_starter.json file)
import json
from pathlib import Path
data = json.loads(Path('../task1_1_starter.json').read_text(encoding='utf-8'))
for url in data.values():
    r = requests.get(url)
    print(r.url)
    print('-' * len(r.url))
    print(r.text)
