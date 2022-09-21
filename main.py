import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'lxml')

title = doc.find_all('ul', {'class':'Pos(r) article-cluster-boundary'})
parent = title[0].parent
print(parent.prettify())
#strong = parent.find("strong")
#print(strong.string)

