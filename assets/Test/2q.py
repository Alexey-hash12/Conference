import pyautogui
pyautogui.hotkey('win','down')
async function openTabs(dep_add) {
				let dep_res = await eel.get_deposits_value(dep_add)();
				document.getElementById('suc').classList.toggle("success_action");
				setTimeout(() => {
					showTabsContent(dep_res)		
				}, 1000);
				setTimeout(() => {
					document.getElementById('suc').classList.toggle("success_action");
					let load = document.getElementById('load');
					load.classList.toggle('load-animate');
					load.style.opacity = '0';
				}, 1500);
			}
if (document.getElementById('btn_checked')) {
				if (document.getElementById('dep_check_1').checked) {
					if (document.getElementById('dep_check_5').checked && document.getElementById('dep_check_12').checked) {
						openTabs(5)
					}
					else if (document.getElementById('dep_check_6').checked && document.getElementById('dep_check_12').checked) {
						openTabs(6)
					}
					else if (document.getElementById('dep_check_8').checked && document.getElementById('dep_check_12').checked) {
						openTabs(7)
					}
					else if (document.getElementById('dep_check_10').checked && document.getElementById('dep_check_12').checked) {
						openTabs(8)
					}

					if (document.getElementById('dep_check_5').checked) {
						openTabs(1)
					}
					else if (document.getElementById('dep_check_6').checked) {
						openTabs(2)
					}
					else if (document.getElementById('dep_check_8').checked) {
						openTabs(3)
					}
					else if (document.getElementById('dep_check_10').checked) {
						openTabs(4)
					}
				}
				else if (document.getElementById('dep_check_2').checked) {
					if (document.getElementById('dep_check_5').checked) {
						openTabs(9)
					}
					else if (document.getElementById('dep_check_6').checked) {
						openTabs(10)
					}
				}	
				else {
					setTimeout(() => {
						document.getElementById('err').classList.toggle("error_action");
					}, 500);
					setTimeout(() => {
						document.getElementById('err').classList.toggle("error_action");
						let load = document.getElementById('load');
						load.classList.toggle('load-animate');
						load.style.opacity = '0';
					}, 1500);
				}
			}				
import eel
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random

for i in range(len(IND)):
		dep_term_1[13] = ''
		dep_value_1[13] = 0
		dep_name_1[13] = ''
		dep_value_1[i] = float(dep_value_1[i])
	''''''	

	if dep_add == 1:
		for i in range(len(IND)):
			if dep_term[i] != '1м':
				dep_value[i] = 0
				dep_name[i] = ''
		return dep_value.index(max(dep_value)) + 1		
	elif dep_add == 2:
		for i in range(len(IND)):
			if dep_term[i] != '3м':
				dep_value[i] = 0
				dep_name[i] = ''
		return dep_value.index(max(dep_value)) + 1	
	elif dep_add == 3:
		for i in range(len(IND)):
			if dep_term[i] != '1г':
				dep_value[i] = 0
				dep_name[i] = ''
		return dep_value.index(max(dep_value)) + 1		
	elif dep_add == 4:
		for i in range(len(IND)):
			if dep_term[i] != '2г':
				dep_value[i] = 0
				dep_name[i] = ''
		return dep_value.index(max(dep_value)) + 1	
	elif dep_add == 5:
		for i in range(len(IND)):
			if dep_term[i] != '1м':
				dep_value[i] = 0
				dep_name[i] = ''
				for j in range(len(IND)):
					if "Безотзывный" not in dep_name[j] and 'безотзывный' not in dep_name[j]:
						dep_name[j] = ''
						dep_value[j] = 0
		return dep_value.index(max(dep_value)) + 1	
	elif dep_add == 6:
		for i in range(len(IND)):
			if dep_term[i] != '3м':
				dep_value[i] = 0
				dep_name[i] = ''
				for j in range(len(IND)):
					if "Безотзывный" not in dep_name[j] and 'безотзывный' not in dep_name[j]:
						dep_name[j] = ''
						dep_value[j] = 0
		return dep_value.index(max(dep_value)) + 1	
	elif dep_add == 7:
		for i in range(len(IND)):
			if dep_term[i] != '1г':
				dep_value[i] = 0
				dep_name[i] = ''
				for j in range(len(IND)):
					if "Безотзывный" not in dep_name[j] and 'безотзывный' not in dep_name[j]:
						dep_name[j] = ''
						dep_value[j] = 0
		return dep_value.index(max(dep_value)) + 1				
	elif dep_add == 8:
		for i in range(len(IND)):
			if dep_term[i] != '2г':
				dep_value[i] = 0
				dep_name[i] = ''
				for j in range(len(IND)):
					if "Безотзывный" not in dep_name[j] and 'безотзывный' not in dep_name[j]:
						dep_name[j] = ''
						dep_value[j] = 0
		return dep_value.index(max(dep_value)) + 1		
	elif dep_add == 9:
		for i in range(len(IND)):
			if dep_term_1[i] != '1м':
				dep_value_1[i] = 0
				dep_name_1[i] = ''
		return dep_value_1.index(max(dep_value_1)) + 1			
	elif dep_add == 10:
		for i in range(len(IND)):
			if dep_term_1[i] != '3м':
				dep_value_1[i] = 0
				dep_name_1[i] = ''
		return dep_value_1.index(max(dep_value_1)) + 1		
	elif dep_add == 11:
		for i in range(len(IND)):
			if dep_term_1[i] != '1г':
				dep_value_1[i] = 0
				dep_name_1[i] = ''
		return dep_value_1.index(max(dep_value_1)) + 1			
					

URL_1 = 'https://bankdabrabyt.by/'
URL_1_1 = 'https://www.alfabank.by/offices/d41647/'
URL_2_1 = 'https://myfin.by/bank/mtbank/currency'
URL_3_1 = 'https://myfin.by/currency/minsk'
URL_4_1 = 'https://belgazprombank.by/'

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
m_saving_d = []
m_saving_e = []
m_saving_r = []
m_universal = []
m_universal_d = []
m_universal_e = []
m_universal_r = []
m_accumulative_term = []
m_accumulative_name = []
dep_value = []
dep_term = []
dep_name = []
dep_value_1 = []
dep_term_1 = []
dep_name_1 = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

@eel.expose
def get_input_value(value):
	addres = ['Проспект фрунзе', 'Улица космонавтов',
	'Проспект Строителей', 'Смоленская улица', 
	'Московский проспект', 'улица Чапаева', 
	'Проспект Строителей', 'улица Ленина', 'Улица Кирова', 
	'Улица Толстого 3', "Улица Ленина", "Советская улица", 'улица Толстого 4',
	'Московский проспект 12', 'проспект Фрунзе', 
	]

	for i in range(0, len(addres)):
		if fuzz.WRatio(value, addres[i])>80:
			return i+1
@eel.expose
def get_deposits_value(dep_add):
	''''''
	for i in range(len(IND)):
		a = 'a' + str(i)
		m_accumulative.append(a)
		m_accumulative_term.append(a)
		m_accumulative_name.append(a)
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='row expenses')
		m_accumulative[i] = value[1].findAll('p')
		m_accumulative[i] = m_accumulative[i][2].text
		m_accumulative[i] = m_accumulative[i][4] + m_accumulative[i][5]
		m_accumulative_name[i] = value[1].findAll('p')
		m_accumulative_name[i] = m_accumulative_name[i][1].text
		m_accumulative_name[i] = m_accumulative_name[i][2::]
		time = soup.findAll(class_='col add-info-row')
		m_accumulative_term[i] = time[1].findAll('p')
		m_accumulative_term[i] = m_accumulative_term[i][6].text
		m_accumulative_term[i] = m_accumulative_term[i][0] + m_accumulative_term[i][2]
	for i in range(len(IND)):
		m_accumulative[5] = 0
		m_accumulative[i] = int(m_accumulative[i])
		m_accumulative_term[5] = 0
		m_accumulative_name[5] = ''
	''''''	
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
		a = 'a' + str(i)
		dep_value_1.append(a)
		dep_term_1.append(a)
		dep_name_1.append(a)
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='row expenses')
		dep_value_1[i] = value[IND_a_e[i]+1].findAll('p')
		dep_value_1[i] = dep_value_1[i][2].text
		dep_value_1[i] = dep_value_1[i][4] + '.' + dep_value_1[i][6]
		dep_name_1[i] = value[IND_a_e[i]+1].findAll('p')
		dep_name_1[i] = dep_name_1[i][1].text
		dep_name_1[i] = dep_name_1[i][2::]
		time = soup.findAll(class_='col add-info-row')
		dep_term_1[i] = time[IND_a_e[i]+1].findAll('p')
		dep_term_1[i] = dep_term_1[i][6].text
		dep_term_1[i] = dep_term_1[i][0] + dep_term_1[i][2]
	for i in range(len(IND)):
		dep_value_1[13] = 0
		dep_value_1[4] = 0
		dep_value_1[i] = float(dep_value_1[i])	
		dep_name_1[13] = ''
		dep_name_1[4] = ''
		dep_term_1[13] = ''
		dep_term_1[4] = ''
		
	dep_term[13] = ''
	dep_value[13] = 0
	dep_name[13] = ''

	for i in range(len(IND)):
		dep_value[13] = 0
		dep_value[i] = float(dep_value[i])	
	
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
	if dep_add == 1:	
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '1м', "Отзывный")
	
	elif dep_add == 0:
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '1м', "")

	elif dep_add == 2:
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '1м', "безотзывный")	

	elif dep_add == 3:
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '3м', "")	
	
	elif dep_add == 4:
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '3м', "отзывной")	
	
	elif dep_add == 5:
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '3м', "безотзывный")	
	
	elif dep_add == 6:
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '1г', "")	
	
	elif dep_add == 7:
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '1г', "безотзывный")
	
	elif dep_add == 8:
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '2г', "")
	
	elif dep_add == 9:
		return dep_function(m_accumulative, m_accumulative_name, m_accumulative_term, '2г', "безотзывный")
	
	elif dep_add == 10:
		print(dep_function(dep_value, dep_name, dep_term, '3м', ""))
					
	# elif dep_add == 10:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '3м':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 	return dep_value.index(max(dep_value)) + 1				
	# elif dep_add == 11:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '6м':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 	return dep_value.index(max(dep_value)) + 1	
	# elif dep_add == 12:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '1г':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 	return dep_value.index(max(dep_value)) + 1	
	# elif dep_add == 13:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '15':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 	return dep_value.index(max(dep_value)) + 1	
	# elif dep_add == 14:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '2г':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 	return dep_value.index(max(dep_value)) + 1	
	# elif dep_add == 15:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '3г':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 	return dep_value.index(max(dep_value)) + 1		
	# elif dep_add == 16:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '1г':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 			for j in range(len(IND)):
	# 				if 'безотзывной' not in dep_name[j]:
	# 					dep_name[j] = ''
	# 					dep_value[j] = 0
	# 	return dep_value.index(max(dep_value)) + 1	
	# elif dep_add == 17:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '1г':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 			for j in range(len(IND)):
	# 				if "фиксированной" not in dep_name[j]:
	# 					dep_name[j] = ''
	# 					dep_value[j] = 0
	# 	return dep_value.index(max(dep_value)) + 1
	# elif dep_add == 18:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '1г':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 			for j in range(len(IND)):
	# 				if "фиксированной" not in dep_name[j] and 'безотзывной' not in dep_name[j]:
	# 					dep_name[j] = ''
	# 					dep_value[j] = 0
	# 	return dep_value.index(max(dep_value)) + 1
	# elif dep_add == 19:	
	# 	for i in range(len(IND)):
	# 		if dep_term[i] != '1г':
	# 			dep_value[i] = 0
	# 			dep_name[i] = ''
	# 			for j in range(len(IND)):
	# 				if 'отзывный' not in dep_name[j]:
	# 					dep_name[j] = ''
	# 					dep_value[j] = 0
	# 	return dep_value.index(max(dep_value)) + 1	
	# if dep_add == 20:
	# 	for i in range(len(IND)):
	# 		if dep_term_1[i] != '3м':
	# 			dep_value_1[i] = 0
	# 			dep_name_1[i] = ''
	# 	return dep_value_1.index(max(dep_value_1)) + 1	

@eel.expose
def get_value(value):
	response = requests.get(URL_1, headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.find('table')
	tr = items.findAll('td')
	a_1 = tr[1].text
	b_1 = tr[2].text
	a_2 = tr[4].text
	b_2 = tr[5].text
	a_3 = tr[7].text
	b_3 = tr[8].text
	return a_1 +  b_1 + '\n'  +  a_2 + b_2 + '\n'  + a_3 +  b_3 

@eel.expose
def get_value_1(value):
	response = requests.get(URL_1_1, headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	tr= soup.findAll('span', class_='informer-currencies_value-txt')
	return tr[0].text + " " +  tr[1].text + '\n' + tr[2].text + " " +tr[3].text + '\n' + tr[4].text + ' ' + tr[5].text

@eel.expose
def get_value_2(value):
	response = requests.get(URL_2_1, headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.findAll('td')
	return items[1].text + " " + items[2].text + "\n" + items[6].text + " " + items[7].text	+ "\n" + items[11].text + " " + items[12].text

@eel.expose
def get_value_3(value):
	response = requests.get(URL_3_1, headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	item = soup.find('tr', class_='tr-tb acc-link_11 not_h')
	items = item.findAll("td");
	return items[1].text + " " + items[2].text + "\n" + items[3].text + " " + items[4].text	+ "\n" + items[5].text + " " + items[6].text

@eel.expose
def get_value_4(value):
	response = requests.get(URL_4_1, headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.findAll(class_='curr-table__cell')
	return items[16].text + items[17].text + items[19].text + items[20].text + items[22].text + items[23].text


eel.init("Web")

eel.start("main.html", size=(900, 700))