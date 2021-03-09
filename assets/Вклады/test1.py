import requests
from bs4 import BeautifulSoup

URL_1 = 'https://bankchart.by/vklady/tarify/org/1070'
URL_2 = 'https://bankchart.by/vklady/tarify/org/1069'
URL_3 = 'https://bankchart.by/vklady/tarify/org/1064'
URL_4 = 'https://bankchart.by/vklady/tarify/org/1053'
URL_5 = 'https://bankchart.by/vklady/tarify/org/1065'
URL_6 = 'https://bankchart.by/vklady/tarify/org/1061'
URL_7 = 'https://bankchart.by/vklady/tarify/org/1055'
URL_8 = 'https://bankchart.by/vklady/tarify/org/1058'
URL_9 = 'https://bankchart.by/vklady/tarify/org/1057'
URL_10 = 'https://bankchart.by/vklady/tarify/org/1073'
URL_11 = 'https://bankchart.by/vklady/tarify/org/1060'
URL_12 = 'https://bankchart.by/vklady/tarify/org/1056'
URL_13 = 'https://bankchart.by/vklady/tarify/org/1068'
URL_14 = 'https://bankchart.by/vklady/tarify/org/1054'
# Накопительный Вклад
# Белорусские рубли
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


#БелгазпромБанк
response = requests.get(URL_9, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
value = soup.findAll(class_='row expenses')
a20= value[21].findAll('p')
a20 = a20[2].text
a20 = a20[4] + a20[5]#поэтому сдесь мы получаем конкретно 5 и 6 элемент строки т.е 1 и 5 
print(a20)