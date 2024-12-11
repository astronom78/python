#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
#
#
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
#
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!


def load_matrix_from_file("Users/elizaveta/project/python/matrix.txt"):
    matrix = []
    with open("Users/elizaveta/project/python/matrix.txt", 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            matrix.append(row)
    return matrix


"Users/elizaveta/project/python/matrix.txt" = 'matrix.txt'  # Путь к файлу с матрицей
matrix = load_matrix_from_file(matrix.txt)
print(matrix)
