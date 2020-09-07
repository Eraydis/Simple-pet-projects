#Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.

from random import randint
from time import sleep
question_answer = True

# Проверка валидности введенного номера
def valid_number(number, n2):
    flag = False
    if number.isdigit():
        if 0 <= int(number) <= int(n2):
            flag = True
    return flag

# Проверка валидности верхней границы диапазона игры
def valid_n2(n):
    return n.isdigit() and int(n) > 1

# Ответ на вопрос
def question():
    print('Сыграем еще разок? (Да / Нет)')
    while 1:
        global question_answer
        n = input().lower()
        if n not in 'данет':
            n = input('Напишите, пожалуйста, "ДА" или "НЕТ") ').lower()
            continue
        if n in ' нет ':
            print('С Вами было интересно поиграть!')
            question_answer = False
        return question_answer


# Основная программа
def game():
    print('Добро пожаловать в числовую угадайку!')
    n2 = (input('Введите верхнюю границу диапазона игры!'))
    while not valid_n2(n2):
        print('Введите корректную верхнюю границу диапазона игры!')
        n2 = input()
    n2, count = int(n2), 0
    num = randint(1, n2)
    sleep(0.5)
    print(f'Введите число от 1 до {n2}!')
    while 1:
        number = input()
        sleep(0.5)
        if not valid_number(number, n2):
            print(f'Введите, пожалуйста, корректное число в интервале от 1 до {n2}!')
            continue
        number = int(number)
        if number > num:
            print('Ваше число больше загаданного, попробуйте еще раз!')
            count += 1
        if int(number) < num:
            print('Ваше число меньше загаданного, попробуйте еще раз!')
            count += 1
        if number == num:
            count += 1
            print(f'Ура, Вы угадали загаданное число {num}!')
            print(f'Число попыток: {count}'
            sleep(0.5)            
            break

while question_answer:
    game()