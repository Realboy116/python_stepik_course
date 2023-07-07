#print(11111*1111111)
#print(42/(4+2*(-2)))
#print(2014**14)
#print(1.2345e-3)
#print(2014.0**14)
#print(7//3)
#print(9**19 - int(float(9**19)))
#print(type(True))
# a = 2 #создал переменную "а" и присвоил ей значение 2
#b = 3 здесь: "b" имя переменной "=" оператор присваивания "3" значение
# print(a + b)  вывод суммы переменных
# a = 6 можем присвоить новое значение перемнной "а"
# print(c) ошибка! любая переменная должна быть объявленна перед использованием
#b = 3    имя переменной не может быть ключевым словом! например "True"
#b = b + 2 переменные это НЕОБЯЗАТЕЛЬНО только одно число! регистр букв имеет значение! A и a разные переменные
#print(b)
# 2 = a ОШИБКА! НЕПРАВИЛЬНО! слева имя переменной, справа значение
# a += 3 увеличиваем предыдущее значение переменной на 3 также есть -=, *=, /=, //=, %=, **=
#input() читает строку с клавиатуры
#input('Веедите данные: ')  просто пример
#s = input() записать в переменную пользовательский ввод
#print(s) выведет то что мы ввели
# s = input("Enter your name: ") записать в переменную пользовательский ввод+ то что напишем в кавычках
# print("Your name is " + s) выведет то что мы ввели+ то что написано в кавычках
#a = int(input()) прочитать строку с клавиатуры и преобразовать в число
#print(a, s) выведет значение переменных a и s через пробел
# a = int(input()) "input" читает строку, преобразовываем строку в число с помошью "int"
# print(a * 2) переменная преобразованная в число умножается на 2
# a = int(input()) вводим первое число
# b = int(input()) вводим второе число
# print(a * b)     выводим результат умножения этих переменных
# x = int(input())
# print(x // 60)
# print(x % 60)
# x = int(input())
# h = int(input())
# m = int(input())
# z = (h * 60) + m + x
# print(z // 60)
# print(z % 60)
# a = 1
# b = 2
# a and b or not a and not b
# A = int(input())
# B = int(input())
# H = int(input())
# if H < A:
#     print("Недосып")
# elif H > B:
#     print("Пересып")
# elif H >= A <= B:
#     print("Это нормально")
'''вот пример
мультистрочного коммента'''
# a = 'abcdfj'
# print(len(a))
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c) / 2
# S = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
# print(S)
# a = int(input())
# if -15 < a <= 12:
#     print("True")
# elif 14 < a < 17:
#     print("True")
# elif 19 <= a:
#     print("True")
# else:
#     print("False")
#Простенький калькулятор
# a = float(input())
# b = float(input())
# c = (input())
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/' and b == 0:
#     print("Деление на ноль!")
# elif c == '/' and b != 0:
#         print(a / b)
# elif c == 'mod' and b == 0:
#     print("Деление на ноль!")
# elif c == 'mod' and b != 0:
#     print(a % b)
# elif c == 'pow':
#     print(a ** b)
# elif c == 'div' and b == 0:
#     print("Деление на ноль!")
# elif c == 'div' and b != 0:
#     print(a // b)
# Вычисление треугольника, прямоугольника и круга по формулам
# form = str(input())
# if form == "треугольник":
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     S = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
#     print(S)
# elif form == "прямоугольник":
#     a = int(input())
#     b = int(input())
#     print(a * b)
# elif form == "круг":
#     r = int(input())
#     S = float(3.14 * (r ** 2))
#     print(S)
# else:
#     print("Вы ввели не то!")
'''Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит 
на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.'''
# a, b, c = int(input()), int(input()), int(input())
# if a > b and a > c:
#     max = a
#     if b > c:
#         mid = b
#         min = c
#     else:
#         mid = c
#         min = b
#     print(max, mid, min, sep='\n')
# elif b > a and b > c:
#     max = b
#     if a > c:
#         mid = a
#         min = c
#     else:
#         mid = c
#         min = a
#     print(max, min, mid, sep='\n')
# elif c > a and c > b:
#     max = c
#     if a > b:
#         mid = a
#         min = b
#     else:
#         mid = b
#         min = a
#     print(max, min, mid, sep='\n')
# elif c == a and b == c:
#     max = a
#     min = b
#     mid = c
#     print(max, min, mid, sep='\n')
# elif c == a and (b > a or b > c):
#     max = b
#     min = c
#     mid = a
#     print(max, min, mid, sep='\n')
# elif c == a and (b < a or b < c):
#     max = a
#     min = b
#     mid = c
#     print(max, min, mid, sep='\n')
# elif a == b and (c < b or c < a):
#     max = a
#     min = c
#     mid = b
#     print(max, min, mid, sep='\n')
# elif a == b and (c > b or c > a):
#     max = a
#     min = b
#     mid = c
#     print(max, min, mid, sep='\n')
# elif c == b and (a > c or a > b ):
#     max = a
#     min = c
#     mid = b
#     print(max, min, mid, sep='\n')
# elif c == b and (a < c or a < b):
#     max = c
#     min = a
#     mid = b
#     print(max, min, mid, sep='\n')
# Задачка "про программистов" на степике хе-хе
# a, b, c, d, e, f,  = str(input())
# n1 = "Счастливый"
# n2 = "Обычный"
# if (int(a) + int(b) + int(c)) == (int(d) + int(e) + int(f)):
#     print(n1)
# else:
#     print(n2)
#print(5 % 2) деление по модулю
#Пример как работает цикл while
# Допустим есть перем. n и мы хотим вывести числа от 1 до 9 на экран
# n = 1 объявляем перем. и присваиваем ей значение 1
# while n < 10: цикл будет повторяться пока перем. n (а она меняется) будет меньше < 10 это будет True
                # как только n станет = или больше > 10 это будет False и цикл остановится
#     print(n) выводим текущее значение n
#     n = n +1 в будущем это n += 1 что бы цикл не "зациклился" будем увеличивать n на еденицу 1 и
               # присваивать опять n
# Добавляем ввод числа от юзера в цикл while
# summa = 0
# n = 0
# while n < 3:
#     summa += int(input())
#     n += 1
# print(summa)
# Юзер будет вводить любы числа до определленых условий пример (кол-во повторов неизвестно)
# summa = 0 к этой перем будем добавлять то что ввел юзер
# a = None присвоили None - это объект ничто
# while a != 0: цикл повторяется пока юзер не введет 0
#     a = int(input()) в эту перем будем записывать число которое вводит юзер
#     summa += a к перем summa добавляем то что ввел юзер
# print(summa) когда цикл завершится выводим сумму
# Добавляем условие if в цикл while!!!
# summa = 0
# while True: АККУРАТНО С ЭТИМ! Это бесконечный цикл и без "break" лучше не использовать!
#     a = int(input())
#     if a == 0: условие в цикле если перем "a" будет равна == 0
#         break  то цикл остановится и перейдет к команде print
#     summa += a
# print(summa)
# a = int(input())
# b = int(input())
# d = 1
# while d % a != 0 or d % b != 0:
#     d % a
#     d % b
#     d += 1
# print(d)