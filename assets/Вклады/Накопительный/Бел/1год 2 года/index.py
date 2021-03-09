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
m_accumulative_3 = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
m_accumulative_term_2 = []
for i in range(len(IND)):
	a = 'a' + str(i)
	m_accumulative_3.append(a)
	response = requests.get(URL[i], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	m_accumulative_3[i] = value[1].findAll('p')
	m_accumulative_3[i] = m_accumulative_3[i][2].text
	m_accumulative_3[i] = m_accumulative_3[i][4] + m_accumulative_3[i][5]

for i in range(len(IND)):
	m_accumulative_3[5] = 0
	m_accumulative_3[i] = int(m_accumulative_3[i])
print(m_accumulative_3)

for i in range(len(IND)):
	a = 'a' + str(i)
	m_accumulative_term_2.append(a)
	response = requests.get(URL[i], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='add-info-item')
	m_accumulative_term_2[i] = value[7].findAll('p')
	m_accumulative_term_2[i] = m_accumulative_term_2[i][0].text
	if m_accumulative_term_2[i][2] == 'г' and m_accumulative_term_2[i][0] == '1':
		m_accumulative_term_2[i] = 10
	elif m_accumulative_term_2[i][2] == 'г' and m_accumulative_term_2[i][0] == '2':	
		m_accumulative_term_2[i] = 20
	else:
		m_accumulative_term_2[i] = m_accumulative_term_2[i][0]	

print(m_accumulative_term_2)
for i in range(len(IND)):
	m_accumulative_term_2[5] = 0
	m_accumulative_term_2[i] = int(m_accumulative_term_2[i])
print(m_accumulative_term_2)

m_accumulative_4 = [0 for i in range(len(IND))]
m_accumulative_5 = [0 for i in range(len(IND))]


for i in range(len(IND)):
	if m_accumulative_term_2[i] == 10:
		m_accumulative_4[i] = m_accumulative_3[i]
	elif m_accumulative_term_2[i] == 20:
		m_accumulative_5[i] = m_accumulative_3[i]
print("1год")	
print(m_accumulative_4)
print("2 год")	
print(m_accumulative_5)		
