import re

import csv
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ

book= []
list_name = []
for element in contacts_list:
  list = []
  for i in element:
    list.append(i)
  #проверяем фамилию
  lastname = re.findall(r'\w+', element[0])
  if len(lastname) == 3:
    list[0] = lastname[0]
    list[1] = lastname[1]
    list[2] = lastname[2]
  elif len(lastname) == 2:
    list[0] = lastname[0]
    list[1] = lastname[1]


  #проверяем отчество
  name = re.findall(r'\w+', element[1])
  if len(name) > 1:
    list[1] = name[0]
    list[2] = name[0]




  if len(list) >= 8 and list[7] == '':
    del list[7]



  if list[-2] != '':
    property = re.findall(r'\d+', list[-2])
    myString = ''.join(property)
    #print(myString)
    true_number = 'Номер не указан'
    #print(len(myString))
    if 0 < len(myString) < 12:
      true_number = f'+7({myString[1:4]}){myString[4:7]}-{myString[7:9]}-{myString[9:11]}'
    elif len(myString) > 11:
      true_number = f'+7({myString[1:4]}){myString[4:7]}-{myString[7:9]}-{myString[9:11]}' \
                    f' доб.{myString[11:]}'
    list[-2] = true_number
    print(true_number)



  if list[0] not in list_name:
    list_name.append(list[0])
    book.append(list)
  else:
    try:
      number1 = 0
      while number1 < 7:
        number = number1
        number1 += 1

        if book[number][0] == list[0] or book[number][1] == list[1] or book[number][2] == list[2]:
          if list[3] != '' and book[number][3] == '':
            book[number][3] = list[3]

          if list[4] != '' and book[number][4] == '':
            book[number][4] = list[4]

          if list[5] != '' and book[number][5] == '':
            book[number][5] = list[5]

          if list[6] != '' and book[number][6] == '':
            book[number][6] = list[6]
    except IndexError:
      continue



#pprint(book)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(book)


