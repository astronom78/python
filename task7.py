#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

a = int(input("введите a " ))
b = int(input("введите b " ))
c = int(input("введите c " ))
print("длина отрезка AC =", c-a)
print("длина отрезка BC =", c-b)
print("сумма отрезков AC + BC =", (c-a)+(c-b) )