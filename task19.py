# #todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm
#
# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
# "EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#
# Каждое значение из списка должно находится на отдельной строке.
# Выход:
# 1 % "C4.5"
# 2 % "k - means"
# и т.д.

# print("Привет", "мир!", sep="\n")
import csv
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
             "EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" ,
             "CART" ]
id = []
for i in range(10):
    n = i + 1
    id.append(n)
new_id = str(id)
print(new_id, sep='\n')
f = open("algoritm.csv", 'w+t')
writer = csv.writer(f)
writer.writerow(id)
writer.writerow(algoritm)
# id = []
# for i in range(10):
#     n = i + 1
#     id.append(n)
#
# f.writelines(str(id))
# f.writelines()
f.seek(0)
print(f.read())
f.close()