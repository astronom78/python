#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# Содержимое файла import_this.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# выходные данные:
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

f = open("import_this.txt", 'w+t')
f.write('''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
''')
f.seek(0) #чтение с нулевого символа
s = f.readlines() #читаем построчно
s.reverse() #читаем строки в обратном порядке (не 1-2-3, а 3-2-1)
#print(s) #выводит список строк
b = ''.join(s) #''.join(s) - join(s) делит список на строки, а в кавычках разделитель
print(b)
f.close()
