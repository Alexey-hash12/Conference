import requests
from bs4 import BeautifulSoup
import random

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
IND_u = [0, 0, 0, 0, 0, 0, 0, 138, 138, 0, 44, 0, 0, 0, 75, 42]
IND_u_d = [0, 0, 0, 0, 0, 0, 0, 143, 143, 0, 0, 0, 0, 0, 0, 46]
IND_u_e = [0, 0, 0, 0, 0, 0, 0, 146, 146, 0, 0, 0, 0, 0, 0, 50]
IND_u_r = [0, 0, 0, 0, 0, 0, 0, 149, 149, 0, 0, 0, 0, 0, 0, 54]
IND_a_d = [10, 6, 7, 14, 14, 0, 9, 18, 18, 11, 17, 10, 12, 0, 31, 9]
IND_a_e = [20, 9, 9, 36, 36, 0, 15, 58, 58, 12, 34, 20, 26, 0, 44, 18]
IND_a_r = [30, 10, 0, 55, 55, 0, 0, 98, 98, 13, 38, 30, 40, 0, 56, 27]
IND_s_d = [0, 0, 15, 0, 0, 8, 23, 0, 0, 0, 0, 0, 54, 14, 71, 38]
IND_s_e = [0, 0, 17, 0, 0, 16, 24, 0, 0, 0, 0, 0, 56, 23, 73, 40]
IND_s_r = [0, 0, 0, 0, 0, 22, 25, 0, 0, 0, 0, 0, 58, 32, 74, 41]
m_saving = []
m_accumulative = []
m_accumulative_d = []
m_accumulative_e = []
m_accumulative_r = []
m_accumulative_term = []
m_accumulative_name = []
dep_value = []
dep_term = []
dep_name = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

for i in range(len(IND)):
	a = 'a' + str(i)
	dep_value.append(a)
	dep_name.append(a)
	dep_term.append(a)
	response = requests.get(URL[i], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	dep_value[i] = value[IND_a_d[i]+1].findAll('p')
	dep_value[i] = dep_value[i][2].text
	dep_value[i] = dep_value[i][4] + '.' + dep_value[i][6]
	dep_name[i] = value[IND_a_d[i]+1].findAll('p')
	dep_name[i] = dep_name[i][1].text
	dep_name[i] = dep_name[i][2::]
	time = soup.findAll(class_='col add-info-row')
	dep_term[i] = time[IND_a_d[i]+1].findAll('p')
	dep_term[i] = dep_term[i][6].text
	dep_term[i] = dep_term[i][0] + dep_term[i][2]
dep_term[13] = ''
dep_value[13] = 0
dep_name[13] = ''
for i in range(len(IND)):
	dep_value[13] = 0
	dep_value[i] = float(dep_value[i])
print(dep_value)
print(dep_name)
print(dep_term)
def dep_function(mas, mas_name, mas_term, term, item):
	for i in range(len(IND)):
		if mas_term[i] != term:
			mas[i] = 0
			mas_name[i] = ''
			for j in range(len(IND)):
				if item not in mas_name[j]:
					mas_name[j] = ''
					mas[j] = 0

	return mas.index(max(mas)) + 1
print(dep_function(dep_value, dep_name, dep_term, '3м', ""))
		