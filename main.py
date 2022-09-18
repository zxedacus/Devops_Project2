import requests
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

url = 'https://finance.yahoo.com/cryptocurrencies/'
r = requests.get(url)

print(doc)
