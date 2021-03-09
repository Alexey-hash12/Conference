# Парсинг для БелгазпромБанка
import requests
from bs4 import BeautifulSoup

URL = 'https://belgazprombank.by/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

response = requests.get(URL, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.findAll(class_='curr-table__cell')
print(items)
