# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

count = int(input('Введите количество паролей, которое необходимо сгенерировать: '))
len_psw = int(input('Введите длину одного пароля: '))
is_numb_in = (input('Включать ли в пароль цифры "0123456789"? (да/нет) '))
is_upplett_in = (input('Включать ли в пароль прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? (да/нет) '))
is_lowlett_in = (input('Включать ли в пароль строчные буквы "abcdefghijklmnopqrstuvwxyz"? (да/нет) '))
is_symb_in = (input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (да/нет) '))
is_contrvrs_in = (input('Исключить из пароля неоднозначные символы "il1Lo0O"? (да/нет) '))

if is_numb_in == 'да':
    chars += digits
if is_lowlett_in == 'да':
    chars += lowercase_letters
if is_upplett_in == 'да':
    chars += uppercase_letters
if is_symb_in == 'да':
    chars += punctuation
if is_contrvrs_in == 'да':
    for i in  "il1Lo0O":
        chars = chars.replace(i, '')
    
def generate_password(length, chars):
    password = random.sample(chars, length)
    return password

for i in range(1, count+1):
    print(str(i)+'. ', *generate_password(len_psw, chars), sep='')