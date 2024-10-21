# #todo: Дописать игру "Поле чудес"
# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:

from random import randint as ri
#words = None
words: None #тип None можно задать еще вот так
desc_ = None #в коде ничего не хранится, все берется из базы, сначала в none, потом в инициализицию
attempt = 0

def get_attempt():
    global attempt
    return attempt

def set_attempt():
    global attempt
    attempt += 1

def init(): #init - начальная(дефолтная) инициализация
    global words, desc_
    words = ["оператор", "конструкция", "объект"]
    desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования.",
               "Это синтаксическая структура, которая определяет способ организации кода.",
               "Это сущность, представляющая собой экземпляр класса." ] #массив строк
init()

def get_word():
    global words
    word_index = ri(0, len(words) - 1) #так как индексация с нуля, то вычитаем единичку
    print_(word_index) #создаем функцию с названием print_
    return words[word_index]
def print_(word_index):
    global desc_
    print("Угадайте слово по подсказке: " + desc_[word_index] + "\n")
def get_field(word_for_play):
    return [" ▒"] * len(word_for_play)

def get_letter():
    letter = input(f"\nУ вас осталось {10 - get_attempt()} попыток! \nВведите букву: ")
    return letter

def engine(word_for_play, player_word):
    while 0 <= get_attempt() < 10 and " ▒" in player_word:
        letter = get_letter()
        if letter in word_for_play:
            start = 0
            for j in range(word_for_play.count(letter)):
                 indx = word_for_play.index(letter, start)
                 player_word[indx] = " " + letter
                 start = indx + 1
            print("".join(player_word))
        else:
            print("Такой буквы в слове нет!")
        set_attempt()
    else:
        if " ▒" in player_word:
            print("Увы, слово отгадать Вам не удалось!")
        else:
            print("Поздравляем, Вы угадали слово!")
def game():
    init()
    word_for_play = get_word()
    player_word = get_field(word_for_play)
    print("".join(player_word))
    engine(word_for_play, player_word)

print("""
1. начать игру !
2. ВЫйти
""")
key=int(input("привет, игрок: "))
match key:
    case 1:
        game()
    case 2:
        exit(0)