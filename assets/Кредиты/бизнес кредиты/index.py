import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

URL = [
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
index_of_devel_mas = [0, 100, 100, 6, 6, 100, 100, 0, 0, 0, 100, 100, 0, 100, 100, 5]
index_of_accom_mas = [100, 100, 3, 13, 13, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 3]
credit_devel_mas = []
credit_auto_mas = []
credit_accom_mas = []

# for i in range(len(URL)):
# 	if index_of_accom_mas[i] == 100:
# 		credit_accom_mas.append(40)	
# 	else:	
# 		response = requests.get(URL[i], headers = headers)
# 		soup = BeautifulSoup(response.content, 'html.parser')
# 		value = soup.findAll(class_='row expenses')
# 		value = value[index_of_accom_mas[i]].findAll('p')
# 		value = value[2].text
# 		try:
# 			value = value[4] + value[5] + '.' + value[7] + value[8]
# 			credit_accom_mas.append(float(value))
# 		except:
# 			value = value[4] + '.' + value[6] + value[7] 
# 			credit_accom_mas.append(float(value))

# print(credit_accom_mas)
# print(credit_accom_mas.index(min(credit_accom_mas)) + 1)		

index_of_devel_mas = [0, 100, 100, 6, 6, 100, 100, 0, 0, 0, 100, 100, 0, 100, 100, 5]
credit_devel_mas = []	
for i in range(len(URL)):
	if index_of_devel_mas[i] == 100:
		credit_devel_mas.append(40)	
	else:	
		response = requests.get(URL[i], headers = headers)
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

print(credit_devel_mas)		

# for i in range(len(URL)):
# 	if i == 3 or i == 4 or i == 5 or i == 15:
# 		response = requests.get(URL[i], headers = headers)
# 		soup = BeautifulSoup(response.content, 'html.parser')
# 		value = soup.findAll(class_='row expenses')
# 		value = value[0].findAll('p')
# 		value = value[2].text
# 		try:
# 			value = value[4] + value[5] + '.' + value[7] + value[8]
# 			credit_auto_mas.append(float(value))
# 		except:
# 			value = value[4] + '.' + value[6] + value[7] 
# 			credit_auto_mas.append(float(value))
# 	else:
# 		credit_auto_mas.append(40)			
# print(credit_auto_mas)
# print(credit_auto_mas.index(min(credit_auto_mas)) + 1)