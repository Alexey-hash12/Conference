import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

URL = ['https://myfin.by/bank/mmbank/department/2604-vitebsk-pr-t-frunze-35-1/courses','https://myfin.by/bank/alfabank/department/5028-vitebsk-ul-kosmonavtov-11/courses',
'https://myfin.by/bank/mtbank/currency/vitebsk', 'https://myfin.by/bank/belarusbank/department/3056-vitebsk-pr-moskovskiyi-7/courses',
'https://myfin.by/bank/belarusbank/department/3056-vitebsk-pr-moskovskiyi-7/courses', 'https://myfin.by/bank/technobank/department/4525-vitebsk-ul-chapaeva-16/courses',
'https://myfin.by/bank/belgazprombank/department/3786-vitebsk-pr-stroiteleyi-1g/courses', 'https://myfin.by/bank/belinvestbank/department/3847-vitebsk-ul-lenina-22-16/courses',
'https://myfin.by/bank/belinvestbank/department/3861-vitebsk-ul-kirova-7-13/courses', 'https://myfin.by/bank/priorbank/department/4733-vitebsk-ul-tolstogo-3/courses',
'https://myfin.by/bank/bps-sberbank/department/4180-vitebsk-ul-lenina-26-2/courses','https://myfin.by/bank/btabank/department/13054-vitebsk-ul-sovetskaya-19/courses',
'https://myfin.by/bank/bnbank/department/5912-vitebsk-ul-tolstogo-4-ploschadj-svobody-ratusha/courses',
'https://myfin.by/bank/paritetbank/department/18411-vitebsk-moskovskiyi-prospekt-12/courses',
'https://myfin.by/bank/bank-vtb/department/2586-vitebsk-pr-frunze-15/courses',
'https://myfin.by/bank/belagroprombank/department/2692-vitebsk-ul-tolstogo-2/courses'
]

currency_usa_buy = []
currency_usa_out = []
currnecy_rub_buy = []
currnecy_rub_out = []
currency_eur_buy = []
currency_eur_out = []

# Покупка Usa

for i in range(len(URL)):
	if i == 2 or i == 3 or i == 13:
		response = requests.get(URL[0], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currency_usa_buy.append(float(value[0].text))
	else:	
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currency_usa_buy.append(float(value[0].text))

print(currency_usa_buy.index(min(currency_usa_buy)) + 1)	

# Продажа Usa

# for i in range(len(URL)):
# 	if i == 2 or i == 3:
# 		response = requests.get(URL[0], headers = headers)
# 		soup = BeautifulSoup(response.content, 'html.parser')
# 		value = soup.findAll(class_='curr_block')
# 		currency_usa_out.append(float(value[1].text))
# 	else:	
# 		response = requests.get(URL[i], headers = headers)
# 		soup = BeautifulSoup(response.content, 'html.parser')
# 		value = soup.findAll(class_='curr_block')
# 		currency_usa_out.append(float(value[1].text))

# print(currency_usa_out.index(max(currency_usa_out)) + 1)	

# Покупка Eur
'''
for i in range(len(URL)):
	if i == 2 or i == 3:
		response = requests.get(URL[0], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currency_eur_buy.append(float(value[2].text))
	else:	
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currency_eur_buy.append(float(value[2].text))
'''
# print(currency_eur_buy.index(min(currency_eur_buy)) + 1)	

#Продажа Eur
'''
for i in range(len(URL)):
	if i == 2 or i == 3:
		response = requests.get(URL[0], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currency_eur_out.append(float(value[2].text))
	else:	
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currency_eur_out.append(float(value[3].text))
'''
# print(currency_eur_out.index(max(currency_eur_out)) + 1)

# Покупка Rub
'''
for i in range(len(URL)):
	if i == 2 or i == 3:
		response = requests.get(URL[0], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currnecy_rub_buy.append(float(value[2].text))
	else:	
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currnecy_rub_buy.append(float(value[4].text))
'''
# print(currnecy_rub_buy.index(min(currnecy_rub_buy)) + 1)

# Продажа Rub
'''
for i in range(len(URL)):
	if i == 2 or i == 3:
		response = requests.get(URL[0], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currnecy_rub_out.append(float(value[2].text))
	else:	
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		currnecy_rub_out.append(float(value[4].text))
'''
# print(currnecy_rub_out.index(max(currnecy_rub_out)) + 1)