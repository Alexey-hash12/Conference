import requests
from bs4 import BeautifulSoup

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
# Накопительный Вклад
# Белорусские рубли
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# Добрабыт
response = requests.get(URL_1, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text) # вывод названия депозита(самого первого)
# у всех названих один и тот же класс
value = soup.findAll('p') # находим первый депозит
a1 = value[6].text # мы получаем 15,00 - это не тип данных float, а str
a_1 = a1[4] + a1[5]#поэтому сдесь мы получаем конкретно 5 и 6 элемент строки т.е 1 и 5 
# print(a_1)
# мы это делаем для того, чтобы можно было перевести в тип данных int и потом сравнивать

# Альфа Банк
response = requests.get(URL_2, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a2 = value[5].text
a_2 = a2[4] + a2[5]
# print(a_2)
# Проверка на работу сравнения
# if int(a_1_1) > int(a__1):
# 	print('yes')

#МТБАНК
response = requests.get(URL_3, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a3 = value[6].text
a_3 = a3[4] + a3[5]
# print(a_3)

#БеларусБанк
response = requests.get(URL_4, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a4 = value[6].text
a_4 = a4[4] + a4[5]
# print(a_4)

#Технобанк
#отсутствует накопительные вклады в белорусских рублях 
# response = requests.get(URL_5, headers = headers)
# soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
# value = soup.findAll('p')
# a_2 = value[6].text
# a_2_1 = a_2[4] + a_2[5]
# print(a_2_1)


#БелгазпромБанк
response = requests.get(URL_6, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a6 = value[6].text
a_6 = a6[4] + a6[5]
# print(a_6)

#БелИнвестБанк
response = requests.get(URL_7, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a7 = value[6].text
a_7 = a7[4] + a7[5]
# print(a_7)

#ПриорБанк
response = requests.get(URL_8, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a8 = value[6].text
a8 = a8[4] + a8[5]
# print(a8)

#БПС Банк
response = requests.get(URL_9, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a9 = value[6].text
a9 = a9[4] + a9[5]
# print(a9)

#БТА БАнк
response = requests.get(URL_10, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a10 = value[6].text
a10 = a10[4] + a10[5]
# print(a10)

#БНБ БАнк
response = requests.get(URL_11, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a11 = value[6].text
a11 = a11[4] + a11[5]
# print(a11)

#ПритетБанк
response = requests.get(URL_12, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a12 = value[6].text
a12 = a12[4] + a12[5]
# print(a12)

#ВТВ Банк
response = requests.get(URL_13, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a13 = value[7].text
a13 = a13[4] + a13[5]
# print(a13)

#Белаграпром Банк
response = requests.get(URL_14, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a14 = value[7].text
a14 = a14[4] + a14[5]

mas_value = [a_1, a_2, a_3, a_4, 0, a_6, a_7, a_8, a_9, a_10, a_11, a_12, a_13, a_14]
for i in range (0, len(mas_value)):
	mas_value[i] = int(mas_value[i])#делаем все значения массива типа int 
print(mas_value.index(max(mas_value)))	

#Сберегательный

#Добрабыт
response = requests.get(URL_1, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
value = soup.findAll(class_='row expenses')
a15 = value[40].findAll('p')
a15 = a15[2].text
a15 = a15[4] + a15[5]
# print(a15)

# # Альфа Банк
# response = requests.get(URL_2, headers = headers)
# soup = BeautifulSoup(response.content, 'html.parser')
# # deposits = soup.findAll(class_='col col-name')
# # print(deposits[1].text)
# value = soup.findAll('p')
# a2 = value[5].text
# a_2 = a2[4] + a2[5]
# # print(a_2)
# # Проверка на работу сравнения
# # if int(a_1_1) > int(a__1):
# # 	print('yes')

#Мтбанк
response = requests.get(URL_3, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
value = soup.findAll(class_='row expenses')
a17 = value[11].findAll('p')
a17 = a17[2].text
a17 = a17[4] + a17[5]#поэтому сдесь мы получаем конкретно 5 и 6 элемент строки т.е 1 и 5 
print(a17)

#БеларусБанк
response = requests.get(URL_4, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
value = soup.findAll(class_='row expenses')
a18 = value[74].findAll('p')
a18 = a18[2].text
a18 = a18[4] + a18[5]
# print(a17)

#Технобанк
response = requests.get(URL_5, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
value = soup.findAll(class_='row expenses')
a19 = value[2].findAll('p')
a19 = a19[2].text
a19 = a19[4] + a19[5]#поэтому сдесь мы получаем конкретно 5 и 6 элемент строки т.е 1 и 5 
# print(a18)

#БелгазпромБанк
response = requests.get(URL_6, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
value = soup.findAll(class_='row expenses')
a20= value[21].findAll('p')
a20 = a20[2].text
a20 = a20[4] + a20[5]#поэтому сдесь мы получаем конкретно 5 и 6 элемент строки т.е 1 и 5 
print(a20)


# #БелИнвестБанк
# response = requests.get(URL_7, headers = headers)
# soup = BeautifulSoup(response.content, 'html.parser')
# # deposits = soup.findAll(class_='col col-name')
# # print(deposits[1].text)
# value = soup.findAll('p')
# a7 = value[6].text
# a_7 = a7[4] + a7[5]
# # print(a_7)

#ПриорБанк
response = requests.get(URL_8, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
value = soup.findAll(class_='row expenses')
a22 = value[15].findAll('p')
a22 = a22[2].text
a22 = a22[4] + a22[5]#поэтому сдесь мы получаем конкретно 5 и 6 элемент строки т.е 1 и 5 
print(a22)

# #БПС Банк
# response = requests.get(URL_9, headers = headers)
# soup = BeautifulSoup(response.content, 'html.parser')
# value = soup.findAll(class_='row expenses')
# a23 = value[44].findAll('p')
# a23 = a23[2].text
# a23 = a23[4] + a23[5]#поэтому сдесь мы получаем конкретно 5 и 6 элемент строки т.е 1 и 5 
# print(a23)

#БТА БАнк
response = requests.get(URL_10, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a10 = value[6].text
a_10 = a10[4] + a10[5]
# print(a_10)

#БНБ БАнк
response = requests.get(URL_11, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a11 = value[6].text
a_11 = a11[4] + a11[5]
# print(a_11)

#ПритетБанк
response = requests.get(URL_12, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a12 = value[6].text
a_12 = a12[4] + a12[5]
# print(a_12)

#ВТВ Банк
response = requests.get(URL_13, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a13 = value[7].text
a_13 = a13[4] + a13[5]
# print(a_13)

#Белаграпром Банк
response = requests.get(URL_14, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
# deposits = soup.findAll(class_='col col-name')
# print(deposits[1].text)
value = soup.findAll('p')
a14 = value[7].text
a_14 = a14[4] + a14[5]

mas_value = [a_15, 0, a_17, a_18, a_19, a_20, 0, a_22, a_23, a_24, a_25, a_26, a_27, a_28, a_29, a_30]
for i in range (0, len(mas_value)):
	mas_value[i] = int(mas_value[i])#делаем все значения массива типа int 
print(mas_value.index(max(mas_value)))	