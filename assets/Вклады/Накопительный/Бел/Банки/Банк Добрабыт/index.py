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

Num = [10, 6, 7, 14, 14, 0, 9, 18, 18, 11, 17, 10, 12, 6, 31, 9]

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# for i in range(len(Num)):

# 	for j in range(Num[i]):
# 		values = [[0 for i in range(Num[i])] for i in range(len(Num))]
# 		prices = [[0 for i in range(Num[i])] for i in range(len(Num))]
# 		terms  = [[0 for i in range(Num[i])] for i in range(len(Num))]
# 		response = requests.get(URL[i], headers = headers)
# 		soup = BeautifulSoup(response.content, 'html.parser')
# 		value = soup.findAll(class_='row expenses')
# 		time = soup.findAll(class_='col add-info-row')
# 		value = value[j].findAll('p')
# 		time = time[j].findAll('p')
# 		values[i][j] = value[1].text
# 		prices[i][j] = value[2].text
# 		terms[i][j] = time[6].text


values1 = [0 for i in range(Num[0])]
prices1 = [0 for i in range(Num[0])]
terms1  = [0 for i in range(Num[0])] 


values2 = [0 for i in range(Num[1])]
prices2 = [0 for i in range(Num[1])]
terms2  = [0 for i in range(Num[1])] 

values3 = [0 for i in range(Num[0])]
prices3 = [0 for i in range(Num[0])]
terms3  = [0 for i in range(Num[0])] 


values4 = [0 for i in range(Num[1])]
prices4 = [0 for i in range(Num[1])]
terms4  = [0 for i in range(Num[1])] 

values5 = [0 for i in range(Num[0])]
prices5 = [0 for i in range(Num[0])]
terms5  = [0 for i in range(Num[0])] 


values6 = [0 for i in range(Num[1])]
prices6 = [0 for i in range(Num[1])]
terms6  = [0 for i in range(Num[1])] 

values7 = [0 for i in range(Num[0])]
prices7 = [0 for i in range(Num[0])]
terms7  = [0 for i in range(Num[0])] 


values8 = [0 for i in range(Num[1])]
prices8 = [0 for i in range(Num[1])]
terms8  = [0 for i in range(Num[1])] 

values9 = [0 for i in range(Num[0])]
prices9 = [0 for i in range(Num[0])]
terms9  = [0 for i in range(Num[0])] 

values10 = [0 for i in range(Num[1])]
prices10 = [0 for i in range(Num[1])]
terms10  = [0 for i in range(Num[1])] 

values11 = [0 for i in range(Num[0])]
prices11 = [0 for i in range(Num[0])]
terms11  = [0 for i in range(Num[0])] 

values12 = [0 for i in range(Num[1])]
prices12 = [0 for i in range(Num[1])]
terms12  = [0 for i in range(Num[1])] 

values13 = [0 for i in range(Num[0])]
prices13 = [0 for i in range(Num[0])]
terms13  = [0 for i in range(Num[0])] 


values14 = [0 for i in range(Num[1])]
prices14 = [0 for i in range(Num[1])]
terms14  = [0 for i in range(Num[1])] 

values15 = [0 for i in range(Num[0])]
prices15 = [0 for i in range(Num[0])]
terms15  = [0 for i in range(Num[0])] 

values16 = [0 for i in range(Num[1])]
prices16 = [0 for i in range(Num[1])]
terms16  = [0 for i in range(Num[1])] 


for i in range(Num[0]):
	response = requests.get(URL[0], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values1[i] = value[1].text
	prices1[i] = value[2].text
	terms1[i] = time[6].text

for i in range(Num[0]):
	print(str(values1[i]) + " "+ str(prices1[i]) + " " + str(terms1[i]))

print("\n")
for i in range(Num[1]):
	response = requests.get(URL[1], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values2[i] = value[1].text
	prices2[i] = value[2].text
	terms2[i] = time[6].text

for i in range(Num[1]):
	print(str(values2[i]) + str(prices2[i]) + str(terms2[i]))
print("\n")

for i in range(Num[2]):
	response = requests.get(URL[2], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values3[i] = value[1].text
	prices3[i] = value[2].text
	terms3[i] = time[6].text

for i in range(Num[2]):
	print(str(values3[i]) + str(prices3[i]) + str(terms3[i]))
print("\n")

# for i in range(Num[3]):
# 	response = requests.get(URL[3], headers = headers)
# 	soup = BeautifulSoup(response.content, 'html.parser')
# 	value = soup.findAll(class_='row expenses')
# 	time = soup.findAll(class_='col add-info-row')
# 	value = value[i].findAll('p')
# 	time = time[i].findAll('p')
# 	values4[i] = value[1].text
# 	prices4[i] = value[2].text
# 	terms4[i] = time[6].text

# for i in range(Num[3]):
# 	print(str(values4[i]) + str(prices4[i]) + str(terms4[i]))
# print("\n")

# for i in range(Num[4]):
# 	response = requests.get(URL[4], headers = headers)
# 	soup = BeautifulSoup(response.content, 'html.parser')
# 	value = soup.findAll(class_='row expenses')
# 	time = soup.findAll(class_='col add-info-row')
# 	value = value[i].findAll('p')
# 	time = time[i].findAll('p')
# 	values5[i] = value[1].text
# 	prices5[i] = value[2].text
# 	terms5[i] = time[6].text

# for i in range(Num[4]):
# 	print(str(values5[i]) + str(prices5[i]) + str(terms5[i]))
# print("\n")

for i in range(Num[5]):
	response = requests.get(URL[5], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values6[i] = value[1].text
	prices6[i] = value[2].text
	terms6[i] = time[6].text

for i in range(Num[5]):
	print(str(values6[i]) + str(prices6[i]) + str(terms6[i]))
print("\n")

for i in range(Num[6]):
	response = requests.get(URL[6], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values7[i] = value[1].text
	prices7[i] = value[2].text
	terms7[i] = time[6].text

for i in range(Num[6]):
	print(str(values7[i]) + str(prices7[i]) + str(terms7[i]))
print("\n")

for i in range(Num[7]):
	response = requests.get(URL[7], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values8[i] = value[1].text
	prices8[i] = value[2].text
	terms8[i] = time[6].text

for i in range(Num[7]):
	print(str(values8[i]) + str(prices8[i]) + str(terms8[i]))
print("\n")

for i in range(Num[8]):
	response = requests.get(URL[8], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values9[i] = value[1].text
	prices9[i] = value[2].text
	terms9[i] = time[6].text

for i in range(Num[8]):
	print(str(values9[i]) + str(prices9[i]) + str(terms9[i]))
print("\n")

for i in range(Num[9]):
	response = requests.get(URL[9], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values10[i] = value[1].text
	prices10[i] = value[2].text
	terms10[i] = time[6].text

for i in range(Num[9]):
	print(str(values10[i]) + str(prices10[i]) + str(terms10[i]))
print("\n")

for i in range(Num[10]):
	response = requests.get(URL[10], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values11[i] = value[1].text
	prices11[i] = value[2].text
	terms11[i] = time[6].text

for i in range(Num[10]):
	print(str(values11[i]) + str(prices11[i]) + str(terms11[i]))
print("\n")

for i in range(Num[11]):
	response = requests.get(URL[11], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values12[i] = value[1].text
	prices12[i] = value[2].text
	terms12[i] = time[6].text

for i in range(Num[11]):
	print(str(values12[i]) + str(prices12[i]) + str(terms12[i]))
print("\n")

for i in range(Num[12]):
	response = requests.get(URL[12], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values13[i] = value[1].text
	prices13[i] = value[2].text
	terms13[i] = time[6].text

for i in range(Num[12]):
	print(str(values13[i]) + str(prices13[i]) + str(terms13[i]))
print("\n")

for i in range(Num[13]):
	response = requests.get(URL[13], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values14[i] = value[1].text
	prices14[i] = value[2].text
	terms14[i] = time[6].text

for i in range(Num[13]):
	print(str(values14[i]) + str(prices14[i]) + str(terms14[i]))
print("\n")

for i in range(Num[14]):
	response = requests.get(URL[14], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values15[i] = value[1].text
	prices15[i] = value[2].text
	terms15[i] = time[6].text

for i in range(Num[14]):
	print(str(values15[i]) + str(prices15[i]) + str(terms15[i]))
print("\n")

for i in range(Num[15]):
	response = requests.get(URL[15], headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	value = soup.findAll(class_='row expenses')
	time = soup.findAll(class_='col add-info-row')
	value = value[i].findAll('p')
	time = time[i].findAll('p')
	values16[i] = value[1].text
	prices16[i] = value[2].text
	terms16[i] = time[6].text

for i in range(Num[15]):
	print(str(values16[i]) + str(prices16[i]) + str(terms16[i]))
print("\n")