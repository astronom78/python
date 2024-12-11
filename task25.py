#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.
import string
znaki = string.punctuation
s = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
print(s)
alfavit =  'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
itog = ''
n = 0
for i in range(0,26):
    for j in s:
        if j in znaki or j == " ":
            itog += j
            continue
        mesto = alfavit.find(j)
        new_mesto = mesto - i
        itog += alfavit[new_mesto]
    if len(itog)//len(s):
        itog += "\n"
    else:
        continue
print(itog)
