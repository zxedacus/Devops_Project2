import requests
from bs4 import BeautifulSoup

url = 'https://www.newegg.com/gigabyte-geforce-rtx-3090-gv-n3090gaming-oc-24gd/p/N82E16814932327?Item=N82E16814932327'
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)

