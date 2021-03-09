import requests
from bs4 import BeautifulSoup
IND = [40, 0, 11, 74, 0, 2, 21, 0, 0, 15, 0, 34, 52, 6, 68, 36]

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
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

for i in range(len(IND)):
	a = 'a' + str(i)
	m_accumulative_d.append(a)
	response = requests.get(URL[i], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	m_accumulative_d[i] = value[IND_a_d[i]].findAll('p')
	m_accumulative_d[i] = m_accumulative_d[i][2].text
	m_accumulative_d[i] = m_accumulative_d[i][4] + '.' + m_accumulative_d[i][6]
	# m_accumulative_d[i] = float(m_accumulative_d[i])
for i in range(len(IND)):
	m_accumulative_d[13] = 0
	m_accumulative_d[i] = float(m_accumulative_d[i])
print(m_accumulative_d.index(max(m_accumulative_d))+1)
# print(m_accumulative_d)

