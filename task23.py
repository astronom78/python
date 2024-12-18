# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.
#
# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

f = open("message.txt", encoding = "utf-8")
fr = f.readlines()
count = []
for i in open("message.txt", encoding = "utf-8"): #разобьем текст на список
    count.append(i)
print(count)
for value in count: #выведем элементы списка
    print(value)
# alfavit =  'АaБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
#че с заглавными буквами?
alfavit =  'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
itog = ''
for j in count[0]: #условие для первой строки
    mesto = alfavit.find(j)
    new_mesto = mesto - 1
    if j in alfavit:
        itog += alfavit[new_mesto]  # Задаем значения в итог
    else:
        itog += j

for j in count[1]: #условие для первой строки
    mesto = alfavit.find(j)
    new_mesto = mesto - 2
    if j in alfavit:
        itog += alfavit[new_mesto]  # Задаем значения в итог
    else:
        itog += j

for j in count[2]: #условие для первой строки
    mesto = alfavit.find(j)
    new_mesto = mesto - 3
    if j in alfavit:
        itog += alfavit[new_mesto]  # Задаем значения в итог
    else:
        itog += j
print(itog)