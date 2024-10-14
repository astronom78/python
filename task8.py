# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".
attempt = 21
for i in range(attempt, 0, -1):
    number = input("введите четырехзначное число ")
    if len(number) != 4:
        print("введите ЧЕТЫРЕХЗНАЧНОЕ число ")
    else:
        reversed_number = number[::-1]
        if number==reversed_number:
            print (f"{number}={reversed_number}, Данное четырехзначное число читается одинаково слева направо и справа налево")
        else:
            print(f"{number}={reversed_number}, Данное четырехзначное число НЕ читается одинаково слева направо и справа налево")
