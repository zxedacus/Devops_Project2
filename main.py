import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/world-indices'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'lxml')

title = doc.find_all('tr', {'class':'simpTblRow'})
title1 = title[0].getText()
#print(title1)

for t in title:
    print(t.getText())




