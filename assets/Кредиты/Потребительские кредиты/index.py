import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

URL = ['https://bankchart.by/potrebitelskie_kredity/tarify/org/1070',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1069',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1064',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1070',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1070',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1065',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1070',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1055',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1055',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1058',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1057',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1073',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1060',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1056',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1068',
'https://bankchart.by/potrebitelskie_kredity/tarify/org/1070',
]
credit_mas = []
for i in range(len(URL)):
	if i == 4 or i == 3 or i == 6 or i == 15 or i == 5:
		credit_mas.append(40)	
	else:	
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='col col-rate')
		value = value[1].text
		value = value[5] +value[6]
		credit_mas.append(value)
print(credit_mas.index())
		