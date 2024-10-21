
#todo: Дан массив размера N.
# Найти минимальное растояние между одинаковыми значениями
# в массиве и вывести их индексы.

# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

mass = []
n = int(input("какого размера вы хотите массив? "
              ""))
for i in range(n):
    mass_value = int(input("введите значение для списка: "))
    mass.append(mass_value)
print("mass:", mass)

length = len(mass)
print("длина массива = ", length)

duplicate_values = [] #объявляю новый список
for i in range(length): #итерируем по длине массива
    for j in range(i + 1, length): #итерируем еще раз по длине, но на символ правее
        if mass[i] == mass[j]: #если значения, находящиеся под первым индексом и вторым индексом, совпадают
            #print("повторяющееся значение:", mass[i])
            duplicate_values.append(mass[i]) #то добавляем в новый список, какое именно значение повторилось

if len(duplicate_values) > 0:
    print(f"Одинаковые значения в массиве: {duplicate_values}")
else:
    print("В массиве нет одинаковых значений.")

# res = [x for x in duplicate_values if x in mass]
# print (res)
# if set(mass) == set (duplicate_values):
#     print("Массивы содержат одни и те же элементы")
# else:
#     print("Массивы содержат разные элементы")
for c in range(len(duplicate_values)): #итерируем по длине списка дупликатов
    duplicate_value = duplicate_values[c] #объявляю новую переменную в виде значения, которое находится под первым индексом
    duplicate_value_index = mass.index(duplicate_value)#ищу, какой индекс имеет это значение в изначальном массиве
    print(f"индекс значения {duplicate_values[c]} в массиве: {duplicate_value_index}" )
    print(f"Для числа {duplicate_values[c]} "
          f"минимальное расcтояние в массиве по индексам: {duplicate_value_index} и {mass[j]}") #под конец я поплыла, все неправильно