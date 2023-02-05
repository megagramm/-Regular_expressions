import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("file.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  contacts_list.sort()
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
previous_index = None
delete_indexes = []
for index, contact in enumerate(contacts_list):
  if index == 0:
    continue

  # приветси почту к ловеркейс
  contact[6] = contact[6].lower()

  # привести имена к title
  contact[0] = contact[0].title()
  contact[1] = contact[1].title()
  contact[2] = contact[2].title()

  # привести телефон в норму
  pat_phone = r'(\+7|8)\s*\(*([\d]{3})\)*[-\s]*([\d]{3})[-]*([\d]{2})[-]*([\d]{2})'
  sub_phone = r'+7(\2)\3-\4-\5'
  if "доб." in contact[5]:
    pat_phone = pat_phone + r'(\s\(?доб\.\s)?([\d]{4})?\)?'
    sub_phone = sub_phone + r' доб.\7'
  contact[5] = re.sub(pat_phone, sub_phone, contact[5])

  #имена в норму
  io = contact[1].split(' ', 2)
  if len(io) > 1:
    for i, f in enumerate(io):
      contact[i + 1] = io[i]

  fio = contact[0].split(' ', 3)
  if len(fio) > 1:
    for i, f in enumerate(fio):
      contact[i] = fio[i]

# актуализируем данные
  if previous_index != None:
    if contact[0] == contacts_list[previous_index][0] and contact[1] == contacts_list[previous_index][1]:
      for i, x in enumerate(contact):
        if i not in range(0, 1):
          if x != '':
            contacts_list[previous_index][i] = x
      delete_indexes.append(index)
  previous_index = index


# удаляем дубли
delete_indexes.reverse()
for i in delete_indexes:
  contacts_list.pop(i)


  #def привести телефон к формату





# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("file2.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)