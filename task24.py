#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alfavit =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T','U', 'V','W','X','Y','Z']

numbers = input("Введите числа: ")
lst = numbers.split()
numbers_list = [int(item) for item in lst]

itog = ''
for i in numbers_list: #условие для первой строки
    letter = alfavit[i]
    itog += letter
print(itog)