import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://www.investing.com/indices/us-spx-500-historical-data'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'lxml')

x = []
y = []

def allin(keywords, string):
    for keyword in keywords:
        if keyword not in string:
            return False
    return True

for table in doc.find_all("table"):
    text = table.text.lower()
    keywords = "date price open high low vol change".split()
    
    if allin(keywords, text):
        break

tbody = table.find("tbody")

for tr in tbody.find_all("tr"):
    tds = tr.find_all("td")
    date = tds[0].text
    price = tds[1].text

print(date, price)
    

    
# print(x)
# print(y)

# plt.plot(x,y)

# plt.xlabel('Dates')
# plt.ylabel('Returns')
# plt.title('S&P 500')
# plt.show()

