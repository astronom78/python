#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

# #Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................

f = open("dumb.txt", encoding = "utf-8")#encoding = "utf-8" - чтобы текст понимался на русском
# f.seek(0)

count = 0
for i in open("dumb.txt", encoding = "utf-8"):
    count += 1
print(count)
# str_1 = ''
# str_23 = ''
str_ = ''
for j in range(count): #создаем из текста одну большую строку
    str_ += f.readline()
    # str_23 += f.readlines()
    # str_ = str_1 + str_23
print(str_)
print(len(str_))
print(f"кол-во букв а: {str_.count("а")}")
print(f"кол-во букв у: {str_.count("у")}")
print(f"кол-во букв е: {str_.count("е")}")
print(f"кол-во букв ы: {str_.count("ы")}")
print(f"кол-во букв ё: {str_.count("ё")}")
print(f"кол-во букв о: {str_.count("о")}")
print(f"кол-во букв э: {str_.count("э")}")
print(f"кол-во букв я: {str_.count("я")}")
print(f"кол-во букв и: {str_.count("и")}")
print(f"кол-во букв ю: {str_.count("ю")}")


# f=open('dump.txt', encoding='utf-8')
# kolvo_strok=0
# for line in open('dump.txt', encoding='utf-8'): #проходися по каждой строке и считаем их количество
#     kolvo_strok+=1
# str_1=''
# for i in range(kolvo_strok):
#     str_1+=f.readline()

# print("Количесто букв а: ",str_1.count('а'))
# print("Количесто букв е: ",str_1.count('е'))
# print("Количесто букв ё: ",str_1.count('ё'))
# print("Количесто букв и: ",str_1.count('и'))
# print("Количесто букв о: ",str_1.count('о'))
# print("Количесто букв у: ",str_1.count('у'))
# print("Количесто букв ы: ",str_1.count('ы'))
# print("Количесто букв э: ",str_1.count('э'))
# print("Количесто букв ю: ",str_1.count('ю'))
# print("Количесто букв я: ",str_1.count('я'))