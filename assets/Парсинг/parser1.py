# Парсинг для Альфа банка
import requests
from bs4 import BeautifulSoup

URL = 'https://www.alfabank.by/offices/d41647/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

response = requests.get(URL, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
tr= soup.findAll('span', class_='informer-currencies_value-txt')

print(tr)

# print("Доллары: ")
# print("Покупка: " + tr[1].text)
# print("Продажа: " + tr[2].text)
# print("Евро: ")
# print("Покупка: " + tr[4].text)
# print("Продажа: " + tr[5].text)
# print("Российский Рубль: ")
# print("Покупка: " + tr[7].text)
# print("Продажа: " + tr[8].text)
