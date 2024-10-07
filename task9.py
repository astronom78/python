# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

a = int(input("введите a " ))
#b = int(input("введите b " ))
'''x = -b/a # A·x + B = 0
print ("x =", x)'''

def _x(_a, _b): #функция def - define определить def y(x)
    # тело функции
    x = -_b / _a # A·x + B = 0
    return x #без return функия вернет none
result = _x(a,b)
print(result)

'''def y(x):
    _y = x**2
    return _y
result = y(a)
print(result)''''''