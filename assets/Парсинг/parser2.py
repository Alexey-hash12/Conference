# Парсинг для МтБанка
import requests
from bs4 import BeautifulSoup

URL = 'https://myfin.by/bank/mtbank/currency'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

response = requests.get(URL, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.findAll('td')
print(items[1].text + " " + items[2].text + " " + items[6].text + " " + items[7].text \
	+ " " + items[11].text + " " + items[12].text
	)

