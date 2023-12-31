'''Что будет выведено на экран в результате выполнения следующей программы?'''
# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1) 
# print(res)

'''Функции, возвращающие булево значение
Мы можем создавать функции, возвращающие булевы значения (True или False). Такая практика очень полезна. 
Напишем функцию is_even(), принимающую одно число и возвращающую значение True если переданное число четное и False 
в противном случае:'''

# def is_even(num):
#     return num % 2 == 0
# '''Следующий программный код:'''
# print(is_even(8))
# print(is_even(7))
# '''Выведет нам True(первый принт) и False(второй принт)'''

'''Предикат делимости
Напишите функцию func(num1, num2), принимающую в качестве аргументов два натуральных числа num1 и num2 и возвращающую 
значение True если число num1 делится без остатка на число num2 и False в противном случае.
Результатом вывода программы должно быть "делится" (если функция func() вернула True) и "не делится" (если функция 
func() вернула False).'''

# def func(num1, num2):
#     return num1 % num2 == 0
# num1 = int(input())
# num2 = int(input())
# print('делится' if func(num1, num2) else 'не делится')