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

import csv #мне точно надо импортировать csv?
algoritm = [ "C4.5", "k - means", "Метод опорных векторов", "Apriori",
             "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор",
             "CART" ]
sl = []
for i in range(len(algoritm)):
    s = f"{i+1} % {algoritm[i]}\n"
    sl.append(s)
#print(sl)
#new_id = str(id)
#print(new_id, sep='\n')
f = open("algoritm.csv", 'w+t')
writer = csv.writer(f) #взяла эту функцию из интернета, не знаю, точно ли она нужна
writer.writerow(sl)
f.seek(0)
print(f.read())
f.close()