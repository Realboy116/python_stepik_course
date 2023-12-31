'''Шахматная доска
На вход программе подаются два натуральных числа n и m. Напишите программу для создания матрицы размером n×m, 
заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную 
матрицу на экран, разделяя элементы пробелами.
Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи.'''

# n, m = input().split()
# mtx = [([i for i in ('.' * int(m))]) for i in range(int(n))]

# for i in range(int(n)):
#     for j in range(int(m)):
#         if j % 2 == 0 and i % 2 == 1:
#             mtx[i][j] = '*'
#         if j % 2 == 1 and i % 2 == 0:
#             mtx[i][j] = '*'
#         print(mtx[i][j], end=' ')
#     print()

# Побочная диагональ
# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и заполняет
# её по следующему правилу:
# числа на побочной диагонали равны 1;
# числа, стоящие выше этой диагонали, равны 0;
# числа, стоящие ниже этой диагонали, равны 2.
# Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.
# Формат входных данных
# На вход программе подается натуральное число n — количество строк и столбцов в матрице.
# Формат выходных данных
# Программа должна вывести матрицу в соответствии с условием задачи.
# Примечание. Побочная диагональ — это диагональ, идущая из правого верхнего в левый нижний угол матрицы.

# n = int(input())
# mtx = [[1] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i + j + 1 < n:
#             mtx[i][j] = 0
#         if i + j + 1 > n:
#             mtx[i][j] = 2
            
# for i in mtx:
#     print(*i)

# Заполнение 1
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m и 
# заполняет её числами от 1 до n⋅m в соответствии с образцом.
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
# Формат выходных данных
# Программа должна вывести матрицу в соответствии с образцом.
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого 
# используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

# n, m = [int(x) for x in input().split()]
# mtx = [[0] * m for _ in range(n)]


# for i in range(n):
#     for j in range(m):
#         mtx[i][j] = i * m + j + 1
#         print(str(mtx[i][j]).ljust(3), end=' ')
#     print()

#   Заполнение 2
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
# заполнив её в соответствии с образцом.
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого 
# используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇'''

# '''Образец: (тестовые данные) Sample Input:
#                                           3 7
#                             Sample Output:

#                                           1  4  7  10 13 16 19
#                                           2  5  8  11 14 17 20
#                                           3  6  9  12 15 18 21
                                          
# n, m = [int(x) for x in input().split()]
# mtx = [[0] * m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         mtx[i][j] = i + n * j + 1
#         print(str(mtx[i][j]).ljust(3), end= ' ')
#     print()

#  Заполнение 3
# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив 
# её в соответствии с образцом.
# Формат входных данных
# На вход программе подается натуральное число n — количество строк и столбцов в матрице.
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом: разместить единицы на главной и побочной 
# диагоналях, остальные позиции матрицы заполнить нулями.
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого 
# используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
# Sample Input 1:

# 5
# Sample Output 1:

# 1  0  0  0  1
# 0  1  0  1  0
# 0  0  1  0  0
# 0  1  0  1  0
# 1  0  0  0  1  '''

# n = int(input())
# mtx = [[0] * n for _ in range(n)]

# for i in range(n):
#     mtx[i][i] = 1
#     mtx[i][n - i - 1] = 1
    
# for i in range(n):                   вариант вывода 1
#     for j in range(n):
#         print(mtx[i][j], end=' ')
#     print()
    
# for i in mtx:                         вариант вывода 2
#     print(*i)

#     Заполнение 4
# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив её 
# в соответствии с образцом.
# Формат входных данных
# На вход программе подается натуральное число n — количество строк и столбцов в матрице.
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого 
# используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
# 5
# Sample Output 1:

# 1  1  1  1  1
# 0  1  1  1  0
# 0  0  1  0  0
# 0  1  1  1  0
# 1  1  1  1  1

# n = int(input())
# mtx = [[1] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if (i > j and i < n - 1 - j) or (i < j and i > n - 1 - j):
#             mtx[i][j] = 0
#         print(str(mtx[i][j]).ljust(3), end=' ')
#     print()


# Заполнение 5 🌶️
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером 
# n×m заполнив её в соответствии с образцом.
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого 
# используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
# Sample Input 1:

# 5 5
# Sample Output 1:

# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4     

# n, m = [int(x) for x in input().split()]
# mtx = [[0] * m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         mtx[i][j] = (j + i) % m + 1
#         print(str(mtx[i][j]).ljust(3), end=' ')
#     print()

# Заполнение змейкой
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
# заполнив её "змейкой" в соответствии с образцом.
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 
# 3
# 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система 
# примет и такое решение 😇

# Sample Input 1:

# 3 5
# Sample Output 1:

# 1  2  3  4  5
# 10 9  8  7  6
# 11 12 13 14 15  

# n, m = [int(x) for x in input().split()]
# mtx = [[0] * m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         mtx[i][j] = m * i + ((i + 1) % 2) * (j + 1) + (i % 2) * (m - j)
#         print(str(mtx[i][j]).ljust(3), end=' ')
#     print()