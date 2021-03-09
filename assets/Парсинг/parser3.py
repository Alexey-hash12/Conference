# Парсинг для Беларусбанка
import requests
from bs4 import BeautifulSoup

URL = 'https://myfin.by/currency/minsk'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

response = requests.get(URL, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
item = soup.find('tr', class_='tr-tb acc-link_11 not_h')
items = item.findAll("td");
print(items[1].text)
