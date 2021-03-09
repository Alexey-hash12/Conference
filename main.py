import pyautogui
pyautogui.hotkey('win','down')

import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import eel
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random
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

URL_C = ['https://myfin.by/bank/mmbank/department/2604-vitebsk-pr-t-frunze-35-1/courses','https://myfin.by/bank/alfabank/department/5028-vitebsk-ul-kosmonavtov-11/courses',
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

URL_CR_DEF = [
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1070', 
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1070',
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1064', 
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1053',
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1053', 
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1070',
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1070',
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1055', 
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1055', 
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1058', 
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1070', 
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1070',
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1060', 
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1070',
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1070',
'https://bankchart.by/biznes/kredity_biznesu/tarify/org/1054', 
]

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


@eel.expose
def get_deposits_value(dep_add_value, dep_add_term, dep_add_ret, dep_add_typ):
	ind = 0
	dep_values = []
	inds = ['Белорусский рубль', 'Американский доллар', 'Евро', 'Российский рубль']
	for i in range(len(URL)):
		response = requests.get(URL[i], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='table-new')[inds.index(dep_add_value)]
		roud = value.find(class_='col add-info-row')
		dep_term = roud.findAll('p')[-2].text
		dep_value = re.findall(r'[0-9]+', dep_term[0])
		dep_value = float('.'.join(dep_value))
		dep_name = value.find(class_='row expenses')
		dep_name = dep_name.find(class_='col col-name').text.split('«')[1]
		if dep_term == dep_add_term and dep_add_ret in dep_name:
			dep_values.append(dep_value)
		else:
			dep_values.append(0)	

	if all(map(lambda x: x == 0, dep_values)):
		return 100	
	else:	
		return dep_values.index(max(dep_values)) + 1


@eel.expose 
def get_currency_value(cur_value, cur_def):
	currency_usa_buy = []
	currency_usa_out = []
	currency_rub_buy = []
	currency_rub_out = []
	currency_eur_buy = []
	currency_eur_out = []
	def get_mas_value(currency_mas, a):
		for i in range(len(URL)):
			if i == 2 or i == 3:
				response = requests.get(URL_C[0], headers = headers)
				soup = BeautifulSoup(response.content, 'html.parser')
				value = soup.findAll(class_='curr_block')
				currency_mas.append(float(value[a].text))
			else:	
				response = requests.get(URL_C[i], headers = headers)
				soup = BeautifulSoup(response.content, 'html.parser')
				value = soup.findAll(class_='curr_block')
				currency_mas.append(float(value[a].text))

	if cur_value == "Американский доллар" and cur_def == "Покупка":
		get_mas_value(currency_usa_buy, 1)
		return currency_usa_buy.index(min(currency_usa_buy)) + 1
	if cur_value == "Американский доллар" and cur_def == "Продажа":
		get_mas_value(currency_usa_out, 0)	
		return currency_usa_out.index(max(currency_usa_out)) + 1
	if cur_value == "Евро" and cur_def == "Покупка":
		get_mas_value(currency_eur_buy, 3)	
		return currency_eur_buy.index(min(currency_eur_buy)) + 1
	if cur_value == "Евро" and cur_def == "Продажа":
		get_mas_value(currency_eur_out, 2)	
		return currency_eur_out.index(min(currency_eur_out)) + 1
	if cur_value == "Российский рубль" and cur_def == "Покупка":
		get_mas_value(currency_rub_buy, 5)	
		return currency_rub_buy.index(min(currency_rub_buy)) + 1
	if cur_value == "Российский рубль" and cur_def == "Продажа":
		get_mas_value(currency_rub_out, 4)	
		return currency_rub_out.index(min(currency_rub_out)) + 1		
	else:
		currency_usa_buy = []
		currency_usa_out = []
		currency_rub_buy = []
		currency_rub_out = []
		currency_eur_buy = []
		currency_eur_out = []
		return 100	

@eel.expose
def get_credit_value(inp_cre_potr ,inp_cre_def):
	def cretit_potr():
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
				credit_mas.append(float(value))
		return credit_mas.index(min(credit_mas)) + 1
	def credit_dev():
		index_of_devel_mas = [0, 100, 100, 6, 6, 100, 100, 0, 0, 0, 100, 100, 0, 100, 100, 5]
		credit_devel_mas = []	
		for i in range(len(URL_CR_DEF)):
			if index_of_devel_mas[i] == 100:
				credit_devel_mas.append(40)	
			else:	
				response = requests.get(URL_CR_DEF[i], headers = headers)
				soup = BeautifulSoup(response.content, 'html.parser')
				value = soup.findAll(class_='row expenses')
				value = value[index_of_devel_mas[i]].findAll('p')
				value = value[2].text
				try:
					value = value[4] + value[5]
					credit_devel_mas.append(float(value))
				except:
					value = value[0]
					credit_devel_mas.append(float(value))	


		return credit_devel_mas.index(min(credit_devel_mas)) + 1
	def credit_accom():
		index_of_accom_mas = [100, 100, 3, 13, 13, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 3]
		credit_accom_mas = []
		for i in range(len(URL_CR_DEF)):
			if index_of_accom_mas[i] == 100:
				credit_accom_mas.append(40)	
			else:	
				response = requests.get(URL_CR_DEF[i], headers = headers)
				soup = BeautifulSoup(response.content, 'html.parser')
				value = soup.findAll(class_='row expenses')
				value = value[index_of_accom_mas[i]].findAll('p')
				value = value[2].text
				try:
					value = value[4] + value[5] + '.' + value[7] + value[8]
					credit_accom_mas.append(float(value))
				except:
					value = value[0]
					credit_accom_mas.append(float(value))
		return credit_accom_mas.index(min(credit_accom_mas)) + 1
	def credit_auto():
		credit_auto_mas = []
		for i in range(len(URL_CR_DEF)):
			if i == 3 or i == 4 or i == 5 or i == 15:
				response = requests.get(URL_CR_DEF[i], headers = headers)
				soup = BeautifulSoup(response.content, 'html.parser')
				value = soup.findAll(class_='row expenses')
				value = value[0].findAll('p')
				value = value[2].text
				try:
					value = value[4] + value[5] + '.' + value[7] + value[8]
					credit_auto_mas.append(float(value))
				except:
					value = value[0]
					credit_auto_mas.append(float(value))
			else:
				credit_auto_mas.append(40)			
		return credit_auto_mas.index(min(credit_auto_mas)) + 1
		
	if 	inp_cre_potr == 'Потребительский':
		return cretit_potr()
	if 	inp_cre_def == 'На развитие':
		return credit_dev()
	if 	inp_cre_def == 'На жилье':
		return credit_accom()
	if 	inp_cre_def == 'На автомобиль':
		return credit_auto()	

@eel.expose 
def get_currency_value_in_template(cur_value):
	
	currency = []
	def get_in_template(n, mas):
		response = requests.get(URL_C[n], headers = headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		value = soup.findAll(class_='curr_block')
		for i in range(6):	
			a = float(value[i].text)
			a = float('{:.2f}'.format(a))
			if float(a)*10 == int(a)*10:
				a = str(a) + '0'
			if float(a)*100 == int(float(a)*100):
				a = float(a)
			mas.append(a)
	if 	cur_value == 'first':
		get_in_template(0, currency)
		return currency
	if 	cur_value == 'second':
		get_in_template(1, currency)
		return currency
	if cur_value == 'third':
		currency = ['---', '---', '---', '---', '---', '---']
		return currency
	if cur_value == 'fourth':
		currency = ['---', '---', '---', '---', '---', '---']
		return currency	
	if cur_value == 'fifth':
		get_in_template(4, currency)
		return currency	
	if cur_value == 'sixth':
		get_in_template(5, currency)
		return currency		
	if cur_value == 'seventh':
		get_in_template(6, currency)
		return currency		
	if cur_value == 'eighth':
		get_in_template(7, currency)
		return currency	
	if cur_value == 'ninth':
		get_in_template(8, currency)
		return currency	
	if cur_value == 'tenth':
		get_in_template(9, currency)
		return currency		
	if cur_value == 'eleventh':
		get_in_template(10, currency)
		return currency
	if cur_value == 'twentieth':
		get_in_template(11, currency)
		return currency	
	if cur_value == 'thirteenth':
		get_in_template(12, currency)
		return currency	
	if cur_value == 'fourteenth':
		get_in_template(13, currency)
		return currency	
	if cur_value == 'fifteenth':
		get_in_template(14, currency)
		return currency		
	if cur_value == 'sixteenth':
		get_in_template(15, currency)
		return currency		

@eel.expose()
def send_mail(login, password, topic, message):
    URL = "smtp.mail.ru"
    toaddr = "alex-ryzh@mail.ru"
    msg = MIMEMultipart()
    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = root.SMTP_SSL( URL, 465 )#smtp.mail.ru
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())

eel.init("Web")

eel.start("main.html", size=(900, 700))