import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://www.investing.com/indices/us-spx-500-historical-data'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'lxml')

x = []
y = []
#y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

tradingDate = doc.find_all('time') 
#tradingDate1 = tradingDate[0].getText()
#print(tradingDate1)

for d in tradingDate:
    x.append(d.getText())
    #print(d.getText())

price = doc.find_all('td', {'class':'datatable_cell__3gwri datatable_cell--align-end__Wua8C'}) 
#price1 = price[0].getText()
#print(price1)

for p in price:
#     y.append(p.getText())
    print(p.getText())
    
# print(x)
# print(y)

# plt.plot(x,y)

# plt.xlabel('Dates')
# plt.ylabel('Returns')
# plt.title('S&P 500')
# plt.show()

