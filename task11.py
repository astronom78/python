# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

'''if 2000<a:
    print(f"это {c} век!")
elif 1899<a<2000:
    print(f"это {c - 1} век!")
elif 1799 < a < 1900:
    print(f"это {c - 2} век!")
elif 1699 < a < 1800:
    print(f"это {c - 3} век!")
elif 1599 < a < 1700:
    print(f"это {c - 4} век!")
elif 1499 < a < 1600:
    print(f"это {c - 5} век!")
elif 1399 < a < 1500:
    print(f"это {c - 6} век!")
elif 1299 < a < 1400:
    print(f"это {c - 7} век!")'''
'''attempt = 21
c = 21
for i in range(attempt, 0, -1): #range - диапозон
    a = int(input("введите год "))
    if a>2100:
        print("введите год нормально")
    else:
        #for i in range (i, 1):
        #    a = a-1000
        #    c = c - 1
        if 2000 < a:
            print(f"это {c} век!")
        elif 1899 < a < 2000:
            c = c - 1
            print(f"это {c} век!")
        elif 1799 < a < 1900:
            c = c - 1
            print(f"это {c} век!")
        elif 1699 < a < 1800:
            c = c - 1
            print(f"это {c} век!")
        elif 1599 < a < 1700:
            print(f"это {c - 4} век!")
        elif 1499 < a < 1600:
            print(f"это {c - 5} век!")
        elif 1399 < a < 1500:
            print(f"это {c - 6} век!")
        elif 1299 < a < 1400:
            print(f"это {c - 7} век!")
        elif 1199 < a < 1400:
            print(f"это {c - 7} век!")
        elif 1099 < a < 1400:
            print(f"это {c - 7} век!")
        elif 999 < a < 1400:
            print(f"это {c - 7} век!")
        elif 899 < a < 1400:
            print(f"это {c - 7} век!")'''

attempt = 21
for i in range(attempt, 0, -1):
    year = int(input("введите год "))
    if year > 2100:
        print("введите год нормально")
    else:
        print(f"это {int(year/100)+1} век!") #при делении года на 100 получаем две первые цифры, а если прибавить 1, то получим век.


