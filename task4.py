# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

# Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130

x=int(input("введите x "))
y=int(input("введите y "))
z=int(input("введите z "))
if x>y and x>z:
    print(f"наибольшее из этих чисел {x}")
elif y>x and y>z:
    print(f"наибольшее из этих чисел {y}")
else:
    print(f"наибольшее из этих чисел {z}")