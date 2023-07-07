'''Угадайка чисел
Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это 
число. Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, 
попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, 
попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы 
угадали, поздравляем!'.
Составляющие проекта:
Целые числа (тип int);
Переменные;
Ввод / вывод данных (функции input() и print());
Условный оператор (if/elif/else);
Цикл while;
Бесконечный цикл;
Операторы break, continue;
Работа с модулем random для генерации случайных чисел.'''
# from random import *
# n = randrange(1, 100)


# def is_valid(s):
#     return s.isdigit() and 1 <= int(s) <= 100

# def game():
#     print('Добро пожаловать в числовую угадайку!\nВведите число от 1 до 100:')
#     total = 0
#     while True:
#         s = input()
#         if is_valid(s) == False:
#             print('А может все-таки введем целое число от 1 до 100?')
#         if is_valid(s) == True:
#             s = int(s)
#             if s > n:
#                 print('Ваше число больше загаданного, попробуйте еще разок')
#                 total += 1
#             if s < n:
#                 print('Ваше число меньше загаданного, попробуйте еще разок')
#                 total += 1
#             if s == n:
#                 print('Вы угадали с', total, 'попытки, поздравляем!')
#                 break
            
# game()
# while True:
#     print('Хотите сыграть еще раз? (Да/Нет)')
#     answer = input()
#     if answer.lower() == 'да' or answer.lower() == 'д' or answer.lower() == 'lf':
#         game()
#     elif answer.lower() == 'нет' or answer.lower() == 'н' or answer.lower() == 'ytn':
#         print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
#         break


'''Магический шар 8
Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее. Программа должна просить 
пользователя задать некий вопрос, чтобы случайным образом на него ответить.'''

# from random import choice

# def is_valid_s(s):
#     return not s.isdigit()   

# print('Тебя приветствует "Магический шар судьбы"!') 
# name = input('Как тебя зовут: ')
     
# answer = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 
#           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 
#           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 
#           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 
#           'Перспективы не очень хорошие', 'Весьма сомнительно']

# def game():
#     while True:
#         print('Задай мне вопрос', name, ':')
#         s = input()
#         if is_valid_s(s):
#             print(choice(answer))
#             print('Хочешь спросить что-нибудь еще', name, '? (да/нет)')
#             s2 = input()
#             if s2 == 'да':
#                 continue
#             if s2 == 'нет':
#                 break
#         if is_valid_s(s) == False:
#             print("Неверно введен вопрос! Попробуй еще раз")
#             continue
# game()

'''Генератор безопасных паролей
Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину 
пароля, а также на то, какие символы требуется в него включить, а какие исключить.'''

# import random
# print('Добро пожаловать в генератор безопасных(но это не точно) паролей!')

# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_'
# chars = ''

# pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
# pwd_len = int(input('Какой длины должен быть пароль? '))
# pwd_digits = input('Включать ли в пароль цифры от 0 до 9? (Да/Yes или Нет/No) ')
# pwd_uppercase = input('Включать ли в пароль прописные буквы? (Да/Yes или Нет/No) ')
# pwd_lowercase = input('Включать ли в пароль строчные буквы? (Да/Yes или Нет/No) ')
# pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (Да/Yes или Нет/No) ')
# pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? (Да/Yes или Нет/No) ')

# if pwd_digits == 'Да' or pwd_digits == 'да' or pwd_digits == 'Yes' or pwd_digits == 'yes' or pwd_digits == 'lf':
#     chars += digits
# if pwd_lowercase == 'Да' or pwd_lowercase == 'да' or pwd_lowercase == 'Yes' or pwd_lowercase == 'yes' or pwd_lowercase == 'lf':
#     chars += lowercase_letters
# if pwd_uppercase == 'Да' or pwd_uppercase == 'да' or pwd_uppercase == 'Yes' or pwd_uppercase == 'yes' or pwd_uppercase == 'lf':
#     chars += uppercase_letters
# if pwd_punctuation == 'Да' or pwd_punctuation == 'да' or pwd_punctuation == 'Yes' or pwd_punctuation == 'yes' or pwd_punctuation == 'lf':
#     chars += pwd_punctuation
# if pwd_exceptions == 'Да' or pwd_exceptions == 'да' or pwd_exceptions == 'Yes' or pwd_exceptions == 'yes' or pwd_exceptions == 'lf':
#     for c in 'il1Lo0O':
#         chars = chars.replace(c, '')

# def generate_pwd(pwd_len, chars):
#     password = ''
#     for j in range(pwd_len):
#         password += random.choice(chars)
#     return password 

# for _ in range(pwd_quantity):
#     generate_pwd(pwd_len, chars)
#     print(generate_pwd(pwd_len, chars))

'''Зашифруйте текст "Блажен, кто верует, тепло ему на свете!" алгоритмом Цезаря с сдвигом вправо на 10 символов.
Примечание. Считайте, что русский алфавит состоит из 32 букв (буква ё отсутствует).'''
# s = input()
# a = ''
# for c in s:
#     if c.isalpha():
#         a += (chr(ord(c) - 25))
#     else:
#         a += c
# print(a)

'''Зашифруйте текст "To be, or not to be, that is the question!" алгоритмом Цезаря с сдвигом вправо на 17 символов.'''
# orig = 'To be, or not to be, that is the question!'
# orig = input()
# k = -25
# abc = ('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z').split()
# #print(abc)
# st_an = ''
# for i in range(len(orig)):
#     if orig[i].upper() not in abc:
#         st_an += (orig[i])
#     if orig[i].upper() in abc:
#         c = abc[(abc.index(orig[i].upper()) + k ) % len(abc)]
#         if orig[i].isupper():
#             st_an += c.upper()
#         else:
#             st_an += c.lower()
# print(st_an)

'''Текст "Hawnj pk swhg xabkna ukq nqj." был получен в результате шифрования алгоритмом Цезаря с сдвигом вправо на 
n символов. Расшифруйте данный текст.
Примечание. Считайте, что n∈[0;25].'''

'''BOH
На вход программе подается натуральное число в десятичной системе счисления. Напишите программу, которая переводит 
его в двоичную, восьмеричную и шестнадцатеричную системы счисления.
Формат входных данных 
На вход программе подается натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание 1. Используйте встроенные функции bin(), oct(), hex().
Примечание 2. Для шестнадцатеричной системы счисления используйте заглавные буквы A, B, C, D, E, F.
Примечание 3. BOH = Binary, Octal, Hex.'''
# n = int(input())
# bin_num = bin(n)
# oct_num = oct(n)
# hex_num = hex(n)
# print(bin_num[2:])
# print(oct_num[2:])
# print(hex_num[2:].upper())

'''Проект (мини игра) "Угадайка слов"'''
# from time import sleep
# from random import choice
# import requests
# from bs4 import BeautifulSoup
# word_list = []
# r = requests.get('http://klavogonki.ru/vocs/559/')
# soup = BeautifulSoup(r.text, features="html.parser")
# text = soup.findAll('td', {'class':'text'})

# for i in range(len(text)):
#     for j in text[i]:
#         word_list.append(j)

# def get_word():
#     word = choice(word_list)
#     return word.upper()


# def display_hangman(tries):
#     stages = ['''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     / \\
#                    -
#                 ''', '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     / 
#                    -
#                 ''', '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |      
#                    -
#                 ''',   '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|
#                    |      |
#                    |     
#                    -
#                 ''',  '''
#                    --------
#                    |      |
#                    |      O
#                    |      |
#                    |      |
#                    |     
#                    -
#                 ''', '''
#                    --------
#                    |      |
#                    |      O
#                    |    
#                    |      
#                    |     
#                    -
#                 ''', '''
#                    --------
#                    |      |
#                    |      
#                    |    
#                    |      
#                    |     
#                    -
#                 ''']
#     return stages[tries]


# def play(word):
#     word_completion = '_' * len(word)
#     guessed = False
#     guessed_letters = []
#     guessed_words = []
#     tries = 6
    
#     print('\033[1;30;42mНачинаем игру "Угадайка слов"!\033[0;0m')
#     sleep(3)
#     print(display_hangman(tries))
#     sleep(2)
#     print(word_completion)
#     print() 
    
#     while not guessed and tries > 0:
#         guess = input('Введите букву или слово целиком: ').upper()
#         if len(guess) == 1 and guess.isalpha():
#             if guess in guessed_letters:
#                 print('Вы уже называли букву', guess)
#             elif guess not in word:
#                 print('Буквы', guess, 'нет в слове.')
#                 tries -= 1
#                 guessed_letters.append(guess)
#             else:
#                 print('Отличная работа, буква', guess, 'присутствует в слове!')
#                 guessed_letters.append(guess)
#                 word_as_list = list(word_completion)
#                 indices = [i for i in range(len(word)) if word[i] == guess]
#                 for index in indices:
#                     word_as_list[index] = guess
#                 word_completion = ''.join(word_as_list)
#                 if '_' not in word_completion:
#                     guessed = True
#         elif len(guess) == len(word) and guess.isalpha():
#             if guess in guessed_words:
#                 print('Вы уже называли слово', guess)
#             elif guess != word:
#                 print('Слово', guess, 'не является верным.')
#                 tries -= 1
#                 guessed_words.append(guess)
#             else:
#                 guessed = True
#                 word_completion = word
#         else:
#             print('Введите букву или слово.')
#         print(display_hangman(tries))
#         print(word_completion)
#         print()
#     if guessed:
#         print('Поздравляем, вы уагадали слово!')
#     else:
#         print('Вы не угадали слово. Загаданным словом было', word + '. Может быть в следующий раз!')
        
# again = 'д'
# while again.lower() == 'д':
#     word = get_word()
#     play(word)
#     again = input('Играем еще раз? (д = да, н = нет):')
    
