import requests
from bs4 import BeautifulSoup

URL = [
'https://bankchart.by/vklady/tarify/org/1070','https://bankchart.by/vklady/tarify/org/1069',
'https://bankchart.by/vklady/tarify/org/1064','https://bankchart.by/vklady/tarify/org/1053',
'https://bankchart.by/vklady/tarify/org/1053','https://bankchart.by/vklady/tarify/org/1065',
'https://bankchart.by/vklady/tarify/org/1061','https://bankchart.by/vklady/tarify/org/1055',
'https://bankchart.by/vklady/tarify/org/1055','https://bankchart.by/vklady/tarify/org/1058',
'https://bankchart.by/vklady/tarify/org/1057','https://bankchart.by/vklady/tarify/org/1073',
'https://bankchart.by/vklady/tarify/org/1060','https://bankchart.by/vklady/tarify/org/1056',
'https://bankchart.by/vklady/tarify/org/1068','https://bankchart.by/vklady/tarify/org/1054'
]

IND = [40, 0, 11, 74, 0, 2, 21, 0, 0, 15, 0, 34, 52, 6, 68, 36]

m_accumulative = []
m_accumulative_term = []
m_accumulative_1 = []
m_accumulative_2 = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

for i in range(len(IND)):
	a = 'a' + str(i)
	m_accumulative.append(a)
	response = requests.get(URL[i], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	m_accumulative[i] = value[0].findAll('p')
	m_accumulative[i] = m_accumulative[i][2].text
	m_accumulative[i] = m_accumulative[i][4] + m_accumulative[i][5]

for i in range(len(IND)):
	m_accumulative[5] = 0
	m_accumulative[i] = int(m_accumulative[i])
print(m_accumulative)

for i in range(len(IND)):
	a = 'a' + str(i)
	m_accumulative_term.append(a)
	response = requests.get(URL[i], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='add-info-item')
	m_accumulative_term[i] = value[3].findAll('p')
	m_accumulative_term[i] = m_accumulative_term[i][0].text
	m_accumulative_term[i] = m_accumulative_term[i][0]

for i in range(len(IND)):
	m_accumulative_term[5] = 0
	m_accumulative_term[i] = int(m_accumulative_term[i])
print(m_accumulative_term)

m_accumulative_1 = [0 for i in range(len(IND))]
m_accumulative_2 = [0 for i in range(len(IND))]

for i in range(len(IND)):
	if m_accumulative_term[i] == 3:
		m_accumulative_1[i] = m_accumulative[i]
	elif m_accumulative_term[i] == 1:
		m_accumulative_2[i] = m_accumulative[i]	
print('3 месяц')
print(m_accumulative_1)
print('1 месяц')
print(m_accumulative_2)		