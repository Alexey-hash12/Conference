import requests
from bs4 import BeautifulSoup
import re


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
IND_a_e = [20, 10, 9, 36, 36, 0, 15, 58, 58, 12, 34, 20, 26, 0, 44, 18]
IND_a_r = [30, 10, 0, 55, 55, 0, 0, 98, 98, 13, 38, 30, 40, 0, 56, 27]
IND_s_d = [0, 0, 15, 0, 0, 8, 23, 0, 0, 0, 0, 0, 54, 14, 71, 38]
IND_s_e = [0, 0, 17, 0, 0, 16, 24, 0, 0, 0, 0, 0, 56, 23, 73, 40]
IND_s_r = [0, 0, 0, 0, 0, 22, 25, 0, 0, 0, 0, 0, 58, 32, 74, 41]

dep_value = []
dep_term = []
dep_name = []
m_accumulative_term = []
m_accumulative_name = []
m_accumulative = []

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
# 1м 3м 1г 2г безотзывн отзывн
# for i in range(len(IND)):
# 	a = 'a' + str(i)
# 	dep_value.append(a)
# 	dep_name.append(a)
# 	dep_term.append(a)
# 	response = requests.get(URL[i], headers = headers)
# 	soup = BeautifulSoup(response.content, 'html.parser')
# 	value = soup.findAll(class_='row expenses')
# 	dep_value[i] = value[IND_a_d[i]+1].findAll('p')
# 	dep_value[i] = dep_value[i][2].text
# 	dep_value[i] = dep_value[i][4] + '.' + dep_value[i][6]
# 	dep_name[i] = value[IND_a_d[i]+1].findAll('p')
# 	dep_name[i] = dep_name[i][1].text
# 	dep_name[i] = dep_name[i][2::]
# 	time = soup.findAll(class_='col add-info-row')
# 	dep_term[i] = time[IND_a_d[i]+1].findAll('p')
# 	dep_term[i] = dep_term[i][6].text
# 	dep_term[i] = dep_term[i][0] + dep_term[i][2]

# dep_term[13] = ''
# dep_value[13] = 0
# dep_name[13] = ''
# for i in range(len(IND)):
# 	dep_value[13] = 0
# 	dep_value[i] = float(dep_value[i])
# for i in range(len(IND)):
# 	if dep_term[i] != '1г':
# 		dep_value[i] = 0
# 		dep_name[i] = ''	
# 		for j in range(len(IND)):
# 			if "отзывный" not in dep_name[j]:
# 				dep_name[j] = ''
# 				dep_value[j] = 0

# print(dep_value)
# print(dep_term)
# print(dep_name)
# print(dep_value.index(max(dep_value)) + 1)		
# print(dep_term)
# print(dep_value)			
# print(dep_name)
'''
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
for i in range(len(IND)):
	if dep_term[i] != '1г':
		dep_value[i] = 0
		dep_name[i] = ''	
		for j in range(len(IND)):
			if "отзывный" not in dep_name[j]:
				dep_name[j] = ''
				dep_value[j] = 0

print(dep_value)
print(dep_term)
print(dep_name)'''
#Сберегательный Доллар 1м 3м 1г 2г 3г 
'''
for i in range(len(IND)):
	a = 'a' + str(i)
	dep_value.append(a)
	dep_term.append(a)
	dep_name.append(a)
	if IND_s_e[i] == 0:
		dep_value[i] = 0
		dep_term[i] = ''
		dep_name[i]	= ''
	else:
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='row expenses')
		dep_value[i] = value[IND_s_d[i]+1].findAll('p')
		dep_value[i] = dep_value[i][2].text
		dep_value[i] = dep_value[i][4] + "." + dep_value[i][6]
		dep_name[i] = value[IND_s_d[i]+1].findAll('p')
		dep_name[i] = dep_name[i][1].text
		dep_name[i] = dep_name[i][2::]
		time = soup.findAll(class_='col add-info-row')
		dep_term[i] = time[IND_s_d[i]+1].findAll('p')
		dep_term[i] = dep_term[i][6].text
		dep_term[i] = dep_term[i][0] + dep_term[i][2]

for i in range(len(IND)):
	dep_value[i] = float(dep_value[i])
print(dep_value)
print(dep_name)
print(dep_term)
'''
#Сберегательный Евро 1м 3м 1г 2г 3г безотзывн
'''
for i in range(len(IND)):
	a = 'a' + str(i)
	dep_value.append(a)
	dep_term.append(a)
	dep_name.append(a)
	if IND_s_e[i] == 0:
		dep_value[i] = 0
		dep_term[i] = ''
		dep_name[i]	= ''
	else:
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='row expenses')
		dep_value[i] = value[IND_s_e[i]].findAll('p')
		dep_value[i] = dep_value[i][2].text
		dep_value[i] = dep_value[i][4] + "." + dep_value[i][6]
		dep_name[i] = value[IND_s_e[i]].findAll('p')
		dep_name[i] = dep_name[i][1].text
		dep_name[i] = dep_name[i][2::]
		time = soup.findAll(class_='col add-info-row')
		dep_term[i] = time[IND_s_e[i]].findAll('p')
		dep_term[i] = dep_term[i][6].text
		dep_term[i] = dep_term[i][0] + dep_term[i][2]

for i in range(len(IND)):
	dep_value[i] = float(dep_value[i])
# print(m_saving_e.index(max(m_saving_e)))
print(dep_value)
print(dep_term)
print(dep_name)
'''
#Сберегательный Российский рубль 1м 3м 1г 3г безотзывн
'''
for i in range(len(IND)):
	a = 'a' + str(i)
	dep_value.append(a)
	dep_term.append(a)
	dep_name.append(a)
	if IND_s_r[i] == 0:
		dep_value[i] = 0
		dep_term[i] = ''
		dep_name[i]	= ''
	else:
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='row expenses')
		dep_value[i] = value[IND_s_e[i]].findAll('p')
		dep_value[i] = dep_value[i][2].text
		dep_value[i] = dep_value[i][4] + "." + dep_value[i][6]
		dep_name[i] = value[IND_s_e[i]].findAll('p')
		dep_name[i] = dep_name[i][1].text
		dep_name[i] = dep_name[i][2::]
		time = soup.findAll(class_='col add-info-row')
		dep_term[i] = time[IND_s_e[i]].findAll('p')
		dep_term[i] = dep_term[i][6].text
		dep_term[i] = dep_term[i][0] + dep_term[i][2]

for i in range(len(IND)):
	dep_value[i] = float(dep_value[i])
print(dep_value)
print(dep_term)
print(dep_name)
'''
#Накопительный 1м 3м 1г 2г безотзывн отзывн

# for i in range(len(IND)):
# 	a = 'a' + str(i)
# 	m_accumulative.append(a)
# 	m_accumulative_term.append(a)
# 	m_accumulative_name.append(a)
# 	response = requests.get(URL[i], headers = headers)
# 	soup = BeautifulSoup(response.content, 'html.parser')
# 	value = soup.findAll(class_='row expenses')
# 	m_accumulative[i] = value[1].findAll('p')
# 	m_accumulative[i] = m_accumulative[i][2].text
# 	m_accumulative[i] = m_accumulative[i][4] + m_accumulative[i][5]
# 	m_accumulative_name[i] = value[1].findAll('p')
# 	m_accumulative_name[i] = m_accumulative_name[i][1].text
# 	m_accumulative_name[i] = m_accumulative_name[i][2::]
# 	time = soup.findAll(class_='col add-info-row')
# 	m_accumulative_term[i] = time[1].findAll('p')
# 	m_accumulative_term[i] = m_accumulative_term[i][6].text
# 	m_accumulative_term[i] = m_accumulative_term[i][0] + m_accumulative_term[i][2]
# for i in range(len(IND)):
# 	m_accumulative[5] = 0
# 	m_accumulative[i] = int(m_accumulative[i])
# 	m_accumulative_term[5] = 0
# 	m_accumulative_name[5] = ''
# 	for i in range(len(IND)):
# 		if m_accumulative_term[i] != '1м':
# 			m_accumulative[i] = 0
# 			m_accumulative_name[i] = ''
# print(m_accumulative.index(max(m_accumulative)) + 1)		
# print(m_accumulative_term)
# print(m_accumulative)			
# print(m_accumulative_name)
# Накопительный Доллар  3м 6м 1г 1.5г 2г 3г отзывн безотзыв фиксиров
dep_value = []
dep_name = []
dep_term = []
for i in range(len(URL)):
	response = requests.get(URL[i], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='table-new')
	roud = value[0].find(class_='col add-info-row')
	name = value[0].find(class_='row expenses')
	name = name.find(class_='col col-name')
	print(name.text.split('«')[1])
	outdil = roud.findAll('p')
	res = re.findall(r'[0-9]+', outdil[0].text)
	res = '.'.join(res)
	dep_value.append(res)
	dep_term.append(outdil[-2].text)
	name = value[0].find(class_='row expenses')
	name = name.find(class_='col col-name')
	dep_name.append(name.text.split('«')[1])

print(dep_value, dep_term, dep_name)
dep_res = []
for i in range(len(IND)):
	if dep_term[i] != '3 месяца':
		dep_value[i] = 0
		dep_name[i] = ''
for j in range(len(IND)):
	if 'отзывной' not in dep_name[j]:
		dep_name[j] = ''
		dep_value[j] = 0

print(dep_value)
print(dep_name)
print(dep_value.index(max(dep_value)) + 1)
# res = roud.find(class_='col col-rate')
# res = res.find('p').text
# res = re.findall(r'[0-9]+', res)
# res = '.'.join(res)
# 
# name = name.find('p').text
# name.split('«')[1].split(' ')[0]
# temp = roud.findAll(class_='add-info-item')
# print(temp)


# Накопительный Евро 3м 6м 1г 2г 3г отзывн безотзывн
'''
for i in range(len(IND)):
	a = 'a' + str(i)
	dep_value.append(a)
	dep_term.append(a)
	dep_name.append(a)
	response = requests.get(URL[i], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	dep_value[i] = value[IND_a_e[i]+1].findAll('p')
	dep_value[i] = dep_value[i][2].text
	dep_value[i] = dep_value[i][4] + '.' + dep_value[i][6]
	dep_name[i] = value[IND_a_e[i]+1].findAll('p')
	dep_name[i] = dep_name[i][1].text
	dep_name[i] = dep_name[i][2::]
	time = soup.findAll(class_='col add-info-row')
	dep_term[i] = time[IND_a_e[i]+1].findAll('p')
	dep_term[i] = dep_term[i][6].text
	dep_term[i] = dep_term[i][0] + dep_term[i][2]
dep_name[13] = ''
dep_name[4] = ''
dep_term[13] = ''
dep_term[4] = ''

for i in range(len(IND)):
	dep_value[13] = 0
	dep_value[4] = 0
	dep_value[i] = float(dep_value[i])	
	for j in range(len(IND)):
		if "Безотзывный" not in dep_name[j] and 'безотзывный' not in dep_name[j] and 'безотзывной' not in dep_name[j]:
			dep_name[j] = ''
			dep_value[j] = 0
print(dep_value)
print(dep_name)
print(dep_term)
'''
# Накопительный Русский Рубль 1г 2г 3г отзывной, безотзывн

# for i in range(len(IND)):
# 	a = 'a' + str(i)
# 	dep_value.append(a)
# 	dep_term.append(a)
# 	dep_name.append(a)
# 	response = requests.get(URL[i], headers = headers)
# 	soup = BeautifulSoup(response.content, 'html.parser')
# 	value = soup.findAll(class_='row expenses')
# 	dep_value[i] = value[IND_a_r[i]+1].findAll('p')
# 	dep_value[i] = dep_value[i][2].text
# 	dep_value[i] = dep_value[i][4] + '.' + dep_value[i][6]
# 	dep_name[i] = value[IND_a_r[i]+1].findAll('p')
# 	dep_name[i] = dep_name[i][1].text
# 	dep_name[i] = dep_name[i][2::]
# 	time = soup.findAll(class_='col add-info-row')
# 	dep_term[i] = time[IND_a_r[i]+1].findAll('p')
# 	dep_term[i] = dep_term[i][6].text
# 	dep_term[i] = dep_term[i][0] + dep_term[i][2]

# for i in range(len(IND)):
# 	dep_value[13] = 0
# 	dep_value[2] = 0
# 	dep_value[5] = 0
# 	dep_value[6] = 0
# 	dep_value[i] = float(dep_value[i])	

# dep_name[13] = ''
# dep_name[2] = ''
# dep_name[5] = ''
# dep_name[6] = ''
# dep_term[13] = ''
# dep_term[2] = ''
# dep_term[5] = ''
# dep_term[6] = ''
# print(dep_value)
# print(dep_name)
# print(dep_term)



# Универсальный Доллар 6м 1г 2г
'''
for i in range(len(IND)):
	a = 'a' + str(i)
	dep_value.append(a)
	dep_term.append(a)
	dep_name.append(a)
	if IND_u_d[i] == 0:
		dep_value[i] = 0
		dep_term[i] = ''
		dep_name[i] = ''	
	else:
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='row expenses')
		dep_value[i] = value[IND_u_d[i]].findAll('p')
		dep_value[i] = dep_value[i][2].text
		dep_value[i] = dep_value[i][4] + '.' +dep_value[i][6]
		dep_name[i] = value[IND_u_d[i]].findAll('p')
		dep_name[i] = dep_name[i][1].text
		dep_name[i] = dep_name[i][2::]
		time = soup.findAll(class_='col add-info-row')
		dep_term[i] = time[IND_u_d[i]].findAll('p')
		dep_term[i] = dep_term[i][6].text
		dep_term[i] = dep_term[i][0] + dep_term[i][2]
	dep_value[i] = float(dep_value[i])

print(dep_value)	
print(dep_term)
print(dep_name)
'''

# Универсальный Евро 6м 1г 2г отзывн
'''
for i in range(len(IND)):
	a = 'a' + str(i)
	dep_value.append(a)
	dep_term.append(a)
	dep_name.append(a)
	if IND_u_e[i] == 0:
		dep_value[i] = 0
		dep_term[i] = ''
		dep_name[i] = ''
	else:
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='row expenses')
		dep_value[i] = value[IND_u_e[i]].findAll('p')
		dep_value[i] = dep_value[i][2].text
		dep_value[i] = dep_value[i][4] + "." +dep_value[i][6]
		dep_name[i] = value[IND_u_e[i]].findAll('p')
		dep_name[i] = dep_name[i][1].text
		dep_name[i] = dep_name[i][2::]
		time = soup.findAll(class_='col add-info-row')
		dep_term[i] = time[IND_u_e[i]].findAll('p')
		dep_term[i] = dep_term[i][6].text
		dep_term[i] = dep_term[i][0] + dep_term[i][2]
	dep_value[i] = float(dep_value[i])

# # print(m_universal_e.index(max(m_universal_e)))
print(dep_value)	
print(dep_term)
print(dep_name)
'''
#  Универсальный Российский Рубль 3м 1г 2г отзывный 
'''
for i in range(len(IND)):
	a = 'a' + str(i)
	dep_value.append(a)
	dep_term.append(a)
	dep_name.append(a)
	if IND_u_e[i] == 0:
		dep_value[i] = 0
		dep_term[i] = ''
		dep_name[i] = ''
	else:
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='row expenses')
		dep_value[i] = value[IND_u_r[i]].findAll('p')
		dep_value[i] = dep_value[i][2].text
		dep_value[i] = dep_value[i][4] + "." +dep_value[i][6]
		dep_name[i] = value[IND_u_r[i]].findAll('p')
		dep_name[i] = dep_name[i][1].text
		dep_name[i] = dep_name[i][2::]
		time = soup.findAll(class_='col add-info-row')
		dep_term[i] = time[IND_u_r[i]].findAll('p')
		dep_term[i] = dep_term[i][6].text
		dep_term[i] = dep_term[i][0] + dep_term[i][2]
	dep_value[i] = float(dep_value[i])

# # print(m_universal_e.index(max(m_universal_e)))
print(dep_value)	
print(dep_term)
print(dep_name)
'''	