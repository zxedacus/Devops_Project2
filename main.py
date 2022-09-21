import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'lxml')

title = doc.find_all('h3', {'class':'Fz(14px)--md1100'})
#title1 = title[0].getText()

for t in title:
    print(t.getText())

#strong = parent.find("strong")


