# # todo: База данных пользователя.
# # Задан массив объектов пользователя
#
#
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Введите критерии поиска: 16
#
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"


# у меня есть список словарей. мне надо написать функции,
# использующие ключи этих словарей. чтобы добраться до ключей
# надо добраться словарей, в списке.
users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# for i in users:
#     print(users(i)['age'])
age_ = input("введите возраст: ")
for i in users: #  в переменной i словарь
    if i['age'] == age_:
        print('Ivan')
    else:
        print('неверный возраст')

# for i in users:
#     for key in i:
#         print(key)

# def age():
#     age_ = input("введите возраст: ")
#     # for i in users: #итерируем по массиву
#     #     print(users[i]['age'])
#     for i in users:
#         for key in i:
#             print(key)




# sort_type=int(input('''введите тип сортировки:
#                         1. По возрасту
#                         2. По первой букве
#                         3. По группе
#
#                         '''))
# match sort_type:
#     case 1:
#         age()
#     case 2:
#         first_letter(0)
#     case 3:
#         group(0)

