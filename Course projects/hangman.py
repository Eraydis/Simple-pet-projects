import random

words = '''аист акула бабуин баран барсук бобр бык верблюд
волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра
коза козел койот корова кошка кролик крыса курица лама ласка лебедь
лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь
норка носорог обезьяна овца окунь олень орел осел панда паук питон
попугай пума семга скунс собака сова тигр тритон тюлень утка форель
хорек черепаха ястреб ящерица'''.split()


def choose_word():
    word = choice(words_list)
    print(word)
    return word


def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',

        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',

        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',

        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]




def play(word):
    word_completion = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Давайте сыграем в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print('Введите букву.')
    while True:
        let = input().upper()
        if let in guessed_letters:
            print('Вы уже вводили эту букву!')
        elif 'A' <= let <= 'Z':
            print('Введите буву!')
        elif let in word:
            print('Вы угадали букву!')
            guessed_letters.append(let)
            print('Желаете ввести слово целиком? Если нет - напишите Н, если не угадаете - проиграете.')
            all_word = input().upper()
            if all_word == 'Н':
                print('Тогда продолжаем.')
            elif all_word == word:
                return True
            elif all_word != word:
                return False
        elif let is not word:
            print('Этой буквы нет в слове.')
            tries = tries - 1
            print(display_hangman(tries))
        word_completion = ''.join([x if x in guessed_letters else '_' for x in word])
        print(word_completion)
        if '_' not in word_completion:
            return True
        if tries == 0:
            return False

f = True
while f:
    word = choose_word()
    if play(word):
        print('Вы выиграли!')
    else:
        print('Вы проиграли. Загаданное слово -', word)
    print('Если желаете сыграть ещё раз нажмите Д. Если нет - нажмите Н')
    x = input().upper()
    if x == 'Н':