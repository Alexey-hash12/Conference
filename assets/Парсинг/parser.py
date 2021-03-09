# Парсинг для Банка Добробыт
import requests
from bs4 import BeautifulSoup

URL = 'https://bankdabrabyt.by/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

response = requests.get(URL, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find('table')
tr = items.findAll('td')
print(tr)
print("Доллары: ")
print("Покупка: " + tr[1].text)
print("Продажа: " + tr[2].text)
print("Евро: ")
print("Покупка: " + tr[4].text)
print("Продажа: " + tr[5].text)
print("Российский Рубль: ")
print("Покупка: " + tr[7].text)
print("Продажа: " + tr[8].text)
