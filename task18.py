#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()

# f = open("text.txt", "w+t")
# f.write("Hello\n")

f = open("text.txt", 'w+t') #октрытие файла
print(f.read())
f.write("Hello\n") #запись в файл слова hello
print(f.readlines())#чтение файла
f.close()#закрытие файла
#почему оно не выводит ничего????