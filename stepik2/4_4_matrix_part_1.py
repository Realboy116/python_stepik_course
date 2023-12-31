'''Матрицы
В прошлых уроках мы изучили вложенные списки, то есть списки, входящие в качестве элементов в другие списки. Частный 
случай вложенных списков — матрицы — прямоугольные таблицы, заполненные какими-то значениями, обычно числами.
Для работы с матрицами нужно уметь получать элемент i-й строки j-го столбца. Для этого обычно заводят список строк 
матрицы, где каждая строка — список элементов. Получается вложенный список или список списков. Теперь, чтобы получить 
определенный элемент, достаточно из списка строк матрицы выбрать i-ю и взять j-й элемент этой строки.
Давайте заведем матрицу размера 3×4 (3 строки и  столбца), содержащую числа, и получим элемент на позиции (2, 3), то 
есть элемент второй строки в третьем столбце.'''
# matrix  = [[2, -5, -11, 0],
#            [-9, 4, 6, 13],
#            [4, 7, 12, -2]]

# print(matrix[1][2])  # вывод элемента на позиции (2, 3) это будет 6
'''В переменной matrix — хранится вся матрица, при этом matrix[1] — список значений во второй строке, matrix[1][2] — 
элемент в третьем столбце этой строки.
В математике нумерация строк и столбцов начинается с единицы, а не с нуля. По договоренности сначала всегда указывается 
строка, а затем — столбец. Элемент на i-ой строке, j-м столбце матрицы a обозначается так aij.'''

'''Перебор элементов матрицы
Чтобы перебрать элементы матрицы, необходимо использовать вложенные циклы. Например, выведем на экран все элементы 
матрицы, перебирая их по строкам:'''
# stroki, stolb = 3, 4    # stroki - количество строк, stolb - количество столбцов

# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]

# for s1 in range(stroki):
#     for s2 in range(stolb):
#         print(matrix[s1][s2], end=' ') 
#     print()
    
'''Выведет: 
2 3 1 0
9 4 6 8
4 7 2 7'''

'''Для перебора элементов матрицы по столбцам можно использовать следующий код:'''

# stroki, stolb = 3, 4

# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]

# for s2 in range(stolb):        #здесь меняем местами строки со столбцами в циклах и переменные циклов соответственно
#     for s1 in range(stroki):    #тоже меняются
#         print(matrix[s1][s2], end=' ')
#     print()
    
'''Выведет:
2 9 4
3 4 7
1 6 2
0 8 7'''

'''Функции ljust() и rjust()
Рассмотрим программный код:'''

# rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов

# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]

# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()
    
'''Выведет:
277 -930 11 0
9 43 6 87
4456 8 290 7'''

'''Выведенная матрица не сильно похожа на упорядоченный прямоугольник. Элементы матрицы имеют разное количество разрядов
и результат вывода получается смазанным. Для решения проблемы удобно использовать строковые методы ljust() и rjust().'''

'''Метод ljust()
"Метод ljust(width[, fillchar]) возвращает строку, выровненную по левому краю, с требуемой длиной width. Заполнение 
строки выполняется указанным символом fillchar (необязательный параметр, по умолчанию пробел). Если параметр width 
меньше или равен длине строки, возвращается исходная строка. Аналогично, метод rjust(width[, fillchar]) возвращает 
строку, выровненную по правому краю." Ну и далее из примеров будет очевидно, как это работает.

Строковый метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста.
Результатом выполнения следующего кода:'''
# print('a'.ljust(3))
# print('ab'.ljust(3))
# print('abc'.ljust(3))
'''будет:
a⎵⎵
ab⎵
abc    '''
'''Исходная строка не обрезается, даже если в ней больше символов, чем нужно.

Результатом выполнения следующего кода:'''
# print('abcdefg'.ljust(3))
'''будет:
abcdefg '''

'''Строковый метод rjust() использует вместо пробела другой символ, если передать ему второй аргумент, необязательный.

Результатом выполнения следующего кода:

print('a'.rjust(5, '*'))
print('ab'.rjust(5, '$'))
print('abc'.rjust(5, '#'))
будет:

****a
$$$ab
##abc'''

'''Применив метод ljust() для выравнивания столбцов при выводе таблицы мы получим следующий код:'''
# stroki, stolb = 3, 4


# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]

# for s1 in range(stroki):
#     for s2 in range(stolb):
#         print(str(matrix[s1][s2]).ljust(6), end=' ')
#     print()
    
'''Результат выровненные цифры:
277    -930   11     0
9      43     6      87
4456   8      290    7    '''

'''Квадратные матрицы
Матрица с одинаковым количеством строк и столбцов называется квадратной. У квадратной матрицы есть две диагонали:
главная: проходит из верхнего левого в правый нижний угол матрицы;
побочная: проходит из нижнего левого в правый верхний угол матрицы.

Элементы с равными индексами i == j находятся на главной диагонали. Такие элементы обозначаются matrix[i][i].
Элементы с индексами i и j, связанными соотношением i + j + 1 = n (или j = n - i - 1), где n — размерность матрицы, 
находятся на побочной диагонали.
Таким образом, чтобы установить элементы главной или побочной диагонали, достаточно одного цикла.
Результатом выполнения следующего кода:'''
# n = 8
# matrix = [[0] * n for _ in range(n)] # создаем квадратную матрицу размером 8×8
# for i in range(n):
#     matrix[i][i] = 1               # создаем квадратную матрицу размером 8×8
#     matrix[i][n-i-1] = 2

# for r in range(n):                  ## выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()

'''Выведет:
1 0 0 0 0 0 0 2 
0 1 0 0 0 0 2 0
0 0 1 0 0 2 0 0
0 0 0 1 2 0 0 0
0 0 0 2 1 0 0 0
0 0 2 0 0 1 0 0
0 2 0 0 0 0 1 0
2 0 0 0 0 0 0 1    '''

'''Индексыi и jэлементов на главной диагонали связаны соотношением i = j. Индексы i и jэлементов на побочной диагонали 
связанны соотношением i + j + 1 = n (или  j = n - i - 1), где n — размерность матрицы
Заметим также, что:
если элемент находится выше главной диагонали, то i < j, если ниже, i > j.
если элемент находится выше побочной диагонали, то i + j + 1 < n, если ниже, i + j + 1 > n.'''

'''Примечание 2. Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:'''
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
        
# matrix = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]

# print_matrix(matrix, 5)

'''По поводу выравнивания (в уроке это не было пояснено), при выравнивании не просто добавляются пробелы(символы), иначе 
получается не понятно, задали столько-то символов, а на выходе по-разному почему-то. Число указанное в методе задает 
размер строки, которая будет в результате форматирования, а уже в зависимости от длины той строки, к которой метод 
применяется и будет добавлятся нужное число пробелов (или символов, если заданы), если их не хватает: 
 

"abc".ljust(6)   # строка 'abc' - три символа, 
                 # а на печать задан вывод 6 символов,
                 # вырвнивание по левому краю
# сначала (т.е. от левого края) будет напечатана строка 'abc', а остальные 3 символа из 6 требемых
# будут заполнены пробелами


"abc".rjust(6)  # условия как и выше, но с выравниванием по правому краю.
# Будет напечатана строка из 6 символов, которая завершится строкой 'abc'
#(т.е. она будет "прижата" к правому краю), а недостающие три символа вначале будут забиты пробелами.
Т.е. символов будет добавлятся = заданная в методе длина строки - длина обрабатываемой методом строки.
В примере это  6 - len("abc")
Соответсвенно, если длина строки больше, чем задано символов выравнивания в методе, то ничего добавлятся не будет, при 
этом длина строки заданная в методе игнорируется и строка не обрезается под это число.

Но зачем заморачиваться с конвертацией типов и строковым методом, когда все можно в тех же f-строках отформатировать?
print(str(matrix[r][c]).ljust(6), end='')
можно просто задать как:
print(f"{matrix[r][c]:<6}", end='') знак < задает сторону выравнивания - здесь по левому краю, знак > - по правому краю
 

причем числа (раз уж за матрицы речь) лучше по правому краю выравнивать:
print(f"{matrix[r][c]:>6}", end='') 

и для чисел такое выравнивание по-умолчанию и можно просто записать, не указывая явно выравнивание:
print(f"{matrix[r][c]:6}", end='')
для большинства других типов по-умолчанию будет выравнивание по левому краю. 
Но проще явно задавать и не париться.

Если нужен знак заполнитель, его без кавычек задают перед угловой скобкой, пусть будет, например, звездочка:
print(f"{matrix[r][c]:*<6}", end='')'''

'''Что покажет приведенный ниже фрагмент кода?'''
# n = 3
# a = [[1, 2, 3,],
#      [4, 5, 6],
#      [7, 8, 9]]

# for i in range(n):
#     for j in range(n):
#         print(a[i][j], end=' ')
#     print()
'''Покажет
1 2 3
4 5 6
7 8 9    '''

'''Что покажет приведенный ниже фрагмент кода?'''
# n = 3
# a = [[1, 2, 3,],
#      [4, 5, 6],
#      [7, 8, 9]]

# for i in range(n):
#     for j in range(n):
#         print(a[j][i], end=' ')
#     print()
'''Покажет
 1 4 7
2 5 8
3 6 9   '''

'''Что покажет приведенный ниже фрагмент кода?'''
# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# for i in range(n):
#     for j in range(n):
#         print(a[n - i - 1][n - j - 1], end=' ')
#     print()
'''Покажет:
9 8 7
6 5 4
3 2 1   '''

'''ЭТО ДОП МАТЕРИАЛ ПО ТЕМЕ МАТРИЦЫ, МАТЕРИАЛ НА ОСНОВЕ ВИДЕО ЕГОРОФФ ПРО ВЛОЖЕННЫЕ СПИСКИ:
Пример 1; просто переберем список как циклом фор: примечание дальще в коде везде используем список 'a' '''
# a = [[0, 2, 4, 6], 
#      [1, 5, 9, 13], 
#      [3, 10,17, 19]]
# for i in a:
#     print(i)
    
'''вывод: 
[0, 2, 4, 6]
[1, 5, 9, 13]
[3, 10, 17, 19]  '''

'''ПРимер 2. Переберем каждый элемент вложенного списка: '''

# for i in a: # здесь i это вложенный список в а
#     for j in i: #заведем перем j что бы перебрать список i
#        print(j) # при таком принте список выведется в столбик 
'''вывод:
0
2
4
6
1
5
9
13
3
10
17
19    '''
'''сделаем другой принт с таким же кодом '''
# for i in a: # здесь i это вложенный список в а
#     for j in i: #заведем перем j что бы перебрать список i
#        print(j, end= ' ') # при таком принте список выведется в одну строку 
'''вывод:   0 2 4 6 1 5 9 13 3 10 17 19    '''

'''сделаем другой принт с таким же кодом но добавим пустой принт в конце:'''
# for i in a: # здесь i это вложенный список в а
#     for j in i: #заведем перем j что бы перебрать список i
#        print(j, end= ' ') # при этом принте 
#     print() # и + пустой принт выведет уже как надо
'''вывод:
0 2 4 6 
1 5 9 13 
3 10 17 19     '''

'''Если изменить код допустим прибавть 10 к каждому элементу в цикле:'''
# for i in a: # здесь i это вложенный список в а
#     for j in i: #заведем перем j что бы перебрать список i
#         j += 10
#         print(j, end= ' ')  
#     print() 
# print(a) # еще выведем список а что бы посмотреть изменился ли сам список
'''вывод цикла: то есть принты в цикле
10 12 14 16           здесь видим что к каждому элементу прибавилось чилос 10
11 15 19 23
13 20 27 29   '''
'''вывод списка а:
[[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]  здесь видим что сам список не изменился'''

'''Выше были примеры перебора по символам теперь разберем перебор по индексам, здесь нужно внимательно смотреть
на вывод и запоминать какой код как выводит этот список, при обращение к каждому элементу используем если вложенность 
двумерная то две пары квадратных скобок [строка][столбец]. При таком переборе юзаем вложенный цикл фор'''
# for i in range(3):      диапазон от 0 до 2 (индексы строк) поэтому range(3)
#     for j in range(4):  диапазон от 0 до 3 (индексы столб) поэтому range(4)
#         print(a[i][j], end=' ')
#     print()
'''вывод: здесь стандартный вывод слева направо сверху вниз
0 2 4 6
1 5 9 13
3 10 17 19   '''

'''сделаем вывод сверху вниз по столбцам и слева направо по столбцам'''
# for j in range(4):
#     for i in range(3):
#         print(a[i][j], end=' ')
#     print()
'''вывод здесь строки выведет в столбик внимательно на вывод:
0 1 3
2 5 10
4 9 17
6 13 19   '''

'''как еще можно сделать вывод? например справа налево снизу вверх '''
# for i in range(2, -1, -1): #в убывающем порядке начинаем с 2-ки до 0 (это до -1), с шагом -1
#     for j in range(3, -1, -1): # здесь все так же
#         print(a[i][j], end=' ')
#     print()
'''внимательно анализируем вывод:
19 17 10 3
13 9 5 1
6 4 2 0     '''

'''допустим нам нужно посчитать сумму каждой строки i и сумму каждого столбца j
сначала пример сумма по строкам'''
# for i in range(3):
#     s = 0 # ну счетчики мы уже знаем как использовать
#     for j in range(4):
#         s += a[i][j]
#     print(s)
'''вывод: 
12  сумма первой строки
28  сумма второй строки
49  сумма третьейй строки   '''

'''что бы вычислить сумму по столбцам нужно просто поменять местами циклы:'''
# for j in range(4):
#     s = 0 
#     for i in range(3):
#         s += a[i][j]
#     print(s)
'''вывод сумма по столбцам уже 4 значения т.к у нас 4 столбца
4    сумма первого столбца и так далее
17
30
38'''

'''Как сделать вложенный список с помощью цикла (что бы самому не заполнять вручную)'''
# a = []
# n = int(input()) #stroka
# m = int(input()) #stolb
'''вариант 1 если надо заполнить список конкретными значениями например 0 (нулями)'''
# for i in range(n):  #здесь n количество строк
#     a.append([0] * m)  #  здесь о уже как список идет он в квадратных скобках сколько столбцов столько и m
# print(a)
'''Вывод:    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]    '''
'''можно вывести по другому:'''
# for i in a:
#     print(i)
'''здесь вывод уже :
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]     '''

'''Пример: заполнить таблицу значениями которые вводит юзер:'''
# a = []
# n = int(input()) #stroka
# m = int(input()) #stolb

# for i in range(n):
#     tmp_ls = [] # временный список
#     for i in range(m): #цикл для столбцов m
#         tmp_ls.append(int(input())) # во временный список добавляем то что вводим с клавы
#     a.append(tmp_ls) # после того как временный список накопится добавляем его в список а
'''делаем вывод с помошью цикла фор:'''
# for i in a:
#     print(i)
'''здесь вывод если мы ввели (2 кол-во строк) (3 кол-во столбцов) (1 2 3 4 5 6) 
[1, 2, 3]
[4, 5, 6]     '''

'''Квадратные таблицы(матрицы), главная диагональ номер строки i == номеру столбца j(i == j). Главная диагональ делит 
матрицу на два треугольника 1-й треугольник то что лежит выше главной диагонали тут номер строки i меньш < номера 
столбца j (i < j) 2-й треугольник то что ниже главной диагонали тут номер строки i больше > номера столбца j (i > j)
теперь заполним нашу квадратную матрицу так: главная диагональ будут лежать 10-ки, ниже гл.диаг. будут 3-ки а выше 
будут лежать 5-ки, для начала заполним матрицу нулями и проверим вывод'''
# a = []                     этот код
# n = int(input())           заполняем 

# for i in range(n):          нашу таблицу 
#     a.append([0] * n)       нулями
    
# for i in a:                на выводе смотрим
#     print(i)               что полуичлось:
'''
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]'''
    
    
# a = []
# n = int(input())

# for i in range(n): 
#     a.append([0] * n)
    
# for i in range(n): # перебираем все строки
#     for j in range(n): # перебираем все столбцы
#          if i == j:    #если наш элемент лежит на главной диагонали (номер строки равен номеру столбца)
#              a[i][j] = 10  # в этот элемент записываем знач 10 (это будет главная диагональ) 
# for i in a:  это 
#     print(i) вывод
# '''код выше заполняет главную диагональ 10-ми вывод будет
# [10, 0, 0, 0]
# [0, 10, 0, 0]
# [0, 0, 10, 0]
# [0, 0, 0, 10]   '''
        #  elif i > j: #здесь заполняем 3-ми то что ниже гл.диаг
        #      a[i][j] = 3 #присваиваем 3 всем элементам которые ниже главной диагонали
# for i in a:  это
#     print(i)  вывод
# '''код выше заполняет то что ниже глав. диаг. 3-ми вывод будет
# [10, 0, 0, 0]
# [3, 10, 0, 0]
# [3, 3, 10, 0]
# [3, 3, 3, 10]   '''
        #  elif i < j:  #здесь заполняем 5-ми то что выше гл.диаг
        #      a[i][j] = 5 #присваиваем 5 всем элементам которые выше главной диагонали
# for i in a:  Это 
#     print(i)  вывод
# '''код выше заполняет то что выше глав. диаг. 5-ми вывод будет
# [10, 5, 5, 5]
# [3, 10, 5, 5]
# [3, 3, 10, 5]
# [3, 3, 3, 10]

'''ВЫВОД КВАДРАТНОЙ МАТРИЦЫ КОД:'''
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=' ')
#     print()

'''Вывести матрицу 1
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в 
матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой 
строки, затем второй, и т.д.
Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.
Формат входных данных
На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут n×m слов, каждое на 
отдельной строке.
Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.'''

# n = int(input())        
# m = int(input())          
# a = []
# for i in range(n * m):
#     a.append(input())
#     if len(a) == m:
#         print(*a)
#         a.clear()

# код от преподов степика
# n = int(input())            красивый правильный код от преподов!
# m = int(input())
# matrix = []

# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(input())
#     matrix.append(row)
    
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()

'''Вывести матрицу 2
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в 
матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой 
строки, затем второй, и т.д.
Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку, 
и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так 
далее.              Формат входных данных
На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут n×m слов, каждое на 
отдельной строке.   Формат выходных данных
Программа должна вывести считанную матрицу, за ней пустую строку, и ту же матрицу, но поменяв местами строки со столбцами.
Элементы матрицы разделять одним пробелом.'''

# stroka, stolb = int(input()), int(input())
# matrix = []
# for i in range(stroka):
#     tmp_ls = []
#     for j in range(stolb):
#         tmp_ls.append(input())
#     matrix.append(tmp_ls)
    
# for i in range(stroka):
#     for j in range(stolb):
#         print(matrix[i][j], end=' ')
#     print()
# print()
# for j in range(stolb):
#     for i in range(stroka):
#         print(matrix[i][j], end=' ')
#     print()

'''След матрицы
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной 
квадратной матрицы.           Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые 
числа) построчно через пробел.       Формат выходных данных
Программа должна вывести одно число — след заданной матрицы.'''
# n = int(input())
# matrix = []
# s = 0
# for i in range(n):
#     temp =[int(num) for num in input().split()]
#     matrix.append(temp)
#     s += matrix[i][i]
# print(s)

'''Больше среднего
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего 
элементов данной строки.               Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы
(целые числа) построчно через пробел.  Формат выходных данных
Программа должна вывести n чисел — для каждой строки количество элементов матрицы, больших среднего арифметического 
элементов данной строки.'''
# n = int(input())
# matrix = [[int(num) for num in input().split() ] for _ in range(n)]

# for i in range(n):
#     count = 0
#     average_of_row = sum(matrix[i]) / n
#     for j in range(n):
#         if matrix[i][j] > average_of_row:
#             count += 1
#         print(count)

'''Максимальный в области 1
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы. 
В задании нарисован квадрат где заштрихована часть ниже главной диагонали  '''  

# n = int(input())
# matrix = []
# max_matr = []

# for i in range(n):
#     matrix.append([int(num) for num in input().split()])
# for i in range(n):
#     for j in range(i+1):
#         max_matr.append(matrix[i][j])
# print(max(max_matr)) 

'''Максимальный в области 2 🌶️
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
в задании нарисован квадрат где заштриованы левый и правый треугольники'''

# n = int(input())
# matrix = [[int(num) for num in input().split()] for _ in range(n)]
# tmp = [] 

# for i in range(n):
#     for j in range(n):
#         if i > j and i < n - 1 - j:              здесь два ифа
#             tmp.append(matrix[i][j])
#         elif i < j and i > n - 1 - j:
#             tmp.append(matrix[i][j])
# print(max(tmp))

# n = int(input())
# matrix = [[int(num) for num in input().split()] for _ in range(n)]
# tmp = [] 

# for i in range(n):
#     for j in range(n):
#         if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j): здесь один иф вместо двух
#             tmp.append(matrix[i][j])
# print(max(tmp))

'''Суммы четвертей
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и 
правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.
Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы 
(целые числа) построчно через пробел.       Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.'''

# n = int(input())
# matrix = [[int(num) for num in input().split()] for _ in range(n)]
# u_ch = 0
# r_ch = 0
# d_ch = 0
# l_ch = 0

# for i in range(n):
#     for j in range(n):
#       if i < j and i < n - 1- j:
#           u_ch += matrix[i][j]
#       elif i < j and i > n - 1- j:
#           r_ch += matrix[i][j]
#       elif i > j and i > n - 1- j:
#           d_ch += matrix[i][j]
#       elif i > j and i < n - 1- j:
#           l_ch += matrix[i][j]
# print('Верхняя четверть:', u_ch)
# print('Правая четверть:', r_ch)
# print('Нижняя четверть:', d_ch)
# print('Левая четверть:', l_ch)