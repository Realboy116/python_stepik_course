'''Итак повторим цикл for а именно я забыл как проходить циклом по элементам списка и как проходить по индексам. '''
# ls = ['a', 'b', 'c', 'd', 'e', 'f', 'j'] # создали список из символов
# for i in ls: # если написать просто ls то i принимает значения символов из списка
#     print(i)
'''здесь принт выведет вот так:
b
c
d
e
f
j'''

# ls = ['a', 'b', 'c', 'd', 'e', 'f', 'j'] # создали список из символов
# for i in range(len(ls)): # если написать range(len(ls)) то i принимает значения индекса из списка
#     print(i)
'''здесь принт выведет вот так:
0
1
2
3
4
5
6'''

# ls = ['a', 'b', 'c', 'd', 'e', 'f', 'j'] # создали список из символов
# for i in len(ls): # если написать len(ls) то будет ошибка TypeError: 'int' object is not iterable
#     print(i)

# ls = ['a', 'b', 'c', 'd', 'e', 'f', 'j'] # создали список из символов
# for i in range(ls): # если написать range(ls) то будет ошибка TypeError: 'list' object cannot be interpreted as an integer
#     print(i)

'''Вывод если нужны сами символы из списка или из строки то пишем: for i in ls если нужны индексы списка то пишем 
for i in range(len(ls))
!!! НЕЛЬЗЯ ПИСАТЬ: for i in len(список или строка); for i in range(список или строка)'''

'''Проверим на строках'''
# s = 'a', 's', 'd', 'f', 'g', 'h', 'j', 'q', 'w', 'e' #создали строку из символов
# for i in s: # если написать просто ls то i принимает значения символов из списка
#     print(i)

# s = 'a', 's', 'd', 'f', 'g', 'h', 'j', 'q', 'w', 'e' #создали строку из символов
# for i in range(len(s)): # если написать range(len(s)) то i принимает значения индекса из строки
#     print(i)

# s = 'a', 's', 'd', 'f', 'g', 'h', 'j', 'q', 'w', 'e' #создали строку из символов
# for i in range(s): # если написать range(s) то будет ошибка TypeError: 'tuple' object cannot be interpreted as an integer
#     print(i)

# s = 'a', 's', 'd', 'f', 'g', 'h', 'j', 'q', 'w', 'e' #создали строку из символов
# for i in len(s): # если написать len(s) то будет ошибка TypeError: 'int' object is not iterable
#     print(i)
