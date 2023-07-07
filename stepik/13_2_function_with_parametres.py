'''Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.
Примечание. Гарантируется, что основание треугольника – нечетное число.'''
# def draw_triangle(fill, base):      
#     for i in range(base // 2 + 1):   
#         for j in range(i + 1):
#             print(fill, end='')
#         print()
#     for x in range(base // 2, 0, -1):
#         for z in range(x, 0, -1):
#             print(fill, end='')
#         print()


# fill = input()
# base = int(input())
        
# draw_triangle(fill, base) ниже решение более умных людей:)
# def draw_triangle(fill, base):          это решение без вложенных циклов!
#     for i in range(1, base // 2 + 2):
#         print(fill * i)
#     for i in range(base // 2, 0, -1):
#         print(fill * i)   ниже самое круто и краткое решение!
# def draw_triangle(fill, base):
#     for i in range(1, base + 1):
#         print(fill * min(i, base - i + 1))
'''def draw_triangle(fill, base):
for i in range(1, base + 1): # i принимает значения от 1 до base. base + 1 тут потому, что последнее значение не 
включается. А начинаем отсчёт с 1, т.к. по умолчанию отсчёт с 0, а 0 нам не нужен, т.к. с ним следующая команда 
выведет просто пустую строку
print(fill * min(i, base - i + 1)) # а тут начинается магия. min возьмёт минимальное из двух предложеных значений.
В итоге в динамике получим, что i начинается от 1 и идёт до base (1, 2, 3,..., base), а второй параметр 
"base - i + 1" начинается с base (ведь на первом шаге i = 1, так что - i + 1 = 0) и на каждом шаге уменьшается на 1,
пока не дойдёт до 1 (base - base + 1).
Первую половину цикла минимальное значение будет возрастать каждый шаг на 1, пока i не сравняется с base - i + 1 
(это произойдёт на середине отрезка от 1 до base), вторую половину цикла значение будет уменьшаться, пока не дойдёт 
до 1. В общем вся магия вертится вокруг встроенной функции min, которая берёт минимальное из двух чисел. И из двух 
параметров, один из которых возрастает, а другое убывает.'''

'''ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.
Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.'''
# def print_fio(name, surname, patronymic):
#     print(surname[0], name[0], patronymic[0], sep='')

# name = input().capitalize()
# surname = input().capitalize()
# patronymic = input().capitalize()

# print_fio(name, surname, patronymic)
'''Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.'''
# def print_digit_sum(n):
#     total = 0
#     while n > 0:           #ВНИМАНИЕ!!! БУДЬ ОЧЕНЬ АККУРАТЕН С ТАКИМ ЦИКЛОМ!!!
#         total += n % 10
#         n = n // 10
#     print(total)
   
# n = int(input())

# print_digit_sum(n)