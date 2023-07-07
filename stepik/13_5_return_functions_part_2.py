'''Is Valid Triangle?
Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных 
числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и 
False в противном случае.'''
# объявление функции
# def is_valid_triangle(side1, side2, side3): это я так решил мне не очень нравится мой код
#     if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#         return True
#     else:
#         return False

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))
#вот как можно было решить еще:
'''чтобы вернуть булево значение достаточно просто сравнить что-то
return a > b
такой код вернет True если а будет больше b, и вернёт False, если это не так
пишем просто return и условие, и всё'''
# def is_valid_triangle(side1, side2, side3):
#     return (side1 < side2 + side3) and (side2 < side3 + side1) and (side3 < side1 + side2)

# print(is_valid_triangle(int(input()), int(input()), int(input())))

'''Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True 
если число является простым и False в противном случае.'''
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# n = int(input())

# print(is_prime(n))
'''Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает 
первое простое число большее числа num.
Примечание 1. Используйте функцию is_prime() из предыдущей задачи.'''
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def get_next_prime(num):
#     x = num + 1
#     while is_prime(x) == False:
#         x += 1
#     return x
# n = int(input())
# print(get_next_prime(n))

'''Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля 
password и возвращает значение True если пароль является надежным и False в противном случае.
Пароль является надежным если:
его длина не менее 8 символов; 
он содержит как минимум одну заглавную букву (верхний регистр); 
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.'''
# def is_password_good(password):
#    if len(password) < 8:
#        return False
#    Flag1 = False
#    Flag2 = False
#    Flag3 = False 
#    for c in password:
#        if c.isupper():
#            Flag1 = True
#        elif c.islower():
#            Flag2 = True
#        elif c.isdigit():
#            Flag3 = True
#    return Flag1 and Flag2 and Flag3  
# txt = input()
# print(is_password_good(txt))

'''Ровно в одном
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и 
возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном 
случае.'''
# def is_one_away(word1, word2):
#     count = 0
#     if len(word1) != len(word2):
#         return False
#     for c in range(len(word1)):
#         if word1[c] != word2[c]:
#             count += 1
#     #if count == 0 or count >= 2: вот эти строки можно было запихнуть в одну
#     #   return False   и вот как это
#     #return True       делается(смысл отсается таким же!):
#     return len(word1) == len(word2) and count == 1 #круто подсмотрено в решениях!
        
# txt1 = input()
# txt2 = input()
# print(is_one_away(txt1, txt2))

'''Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True 
если указанный текст является палиндромом и False в противном случае.
Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также 
символы , . ! ? -.'''
# def is_palindrome(text):
#     text = text.lower()
#     text = text.replace(' ', '').replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('-', '')
#     if text[::] == text[::-1]:
#         return True
#     return False
    
# txt = input()
# print(is_palindrome(txt))

'''BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK 
фанатеет от математики, то он решил:
число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля 
password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном 
случае.'''
# объявление функции
# def is_valid_password(password):
#     password = password.split(':')
#     if len(password) != 3:
#         return False
#     a = password[0]
#     b = password[1]
#     c = password[2]
#     if a[::] != a[::-1] or int(c) % 2 != 0:
#         return False
#     b = int(b)
#     if b < 2:
#         return False
#     for i in range(2, b):
#         if b % i == 0:
#             return False
#     return True
    
# # считываем данные
# psw = input()

# # вызываем функцию
# print(is_valid_password(psw))

'''Правильная скобочная последовательность 🌶️
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из 
символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной 
последовательностью и False в противном случае.
Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), где 
каждой открывающей скобке найдется парная закрывающая скобка (при этом каждая открывающая скобка должна быть левее 
соответствующей ей закрывающей скобки).'''
#объявление функции
# def is_correct_bracket(text):
#     count = 0
#     for i in text:
#         if i == '(':
#             count += 1
#         if i == ')':
#             count -= 1
#         if count < 0:
#             return False
#     if count != 0 or text[0] == ')' or text[-1] == '(':
#         return False
#     return True
# # считываем данные
# txt = input()
# # вызываем функцию
# print(is_correct_bracket(txt))

'''Змеиный регистр
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» 
и преобразует его в «змеиный регистр».'''
# объявление функции
# def convert_to_python_case(text): 
#     s = ''
#     for c in text:
#         if c.isupper():
#             s += '_'
#         s += c.lower()
#     return s[1:]

# # считываем данные
# txt = input()

# # вызываем функцию
# print(convert_to_python_case(txt))