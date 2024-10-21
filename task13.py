#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.
#n = int(input("введите числа:"))
'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
k = int(input())
l = int(input())
list = [a, b, c, d, e, f, g, k, l]'''

# n=input()
# n_list=list(n)
# print(n_list)
#if len(n_list)>10:
#    print("слишком много символов")
#else:

#print(list)
#for i in list:
#    print(i)

list = []
for i in range(10):
    n = int(input("введите значение для списка: "))
    list.append(n)
print("старый список:", list)

list_new = []
for index in range(len(list)):
    list_new.append(list[index]+1)

print("новый список:", list_new)