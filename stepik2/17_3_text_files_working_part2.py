'''Переворот строки
Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку в 
обратном порядке.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести строку указанного файла в обратном порядке.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Используйте менеджер контекста 🙂.'''

# with open('D:/pythonProject/rever.txt', 'r', encoding='utf-8') as text:
#     print(text.read()[::-1])

# Обратный порядок
# Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу, выводящую все строки 
# данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должна вывести строки указанного файла в обратном порядке.
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
# Примечание 2. Используйте менеджер контекста 🙂.
# Примечание 3. Получить список всех строк файла можно при помощи метода readlines().
# Примечание 4. Не забывайте про символ конца строки '\n'.

# with open('D:/pythonProject/pyt.txt', 'r', encoding='utf-8') as text:
#     ls = text.read().split('\n')
#     print(*ls[::-1], sep='\n')

'''Длинные строки
Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все строки 
наибольшей длины из файла, не меняя их порядок.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Используйте менеджер контекста 🙂.'''

# with open('D:/pythonProject/pyt.txt', 'r', encoding='utf-8') as text:
#     ls = list(map(lambda x: x.strip(), text.readlines()))
#     maks = len(max(ls, key=len))
#     print(*filter(lambda x: len(x) == maks, ls), sep='\n')

'''Сумма чисел в строках
Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел, 
разделенных одним или несколькими пробелами.
Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран (для каждой строки 
выводится сумма чисел в этой строке).
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести сумму чисел в каждой строке.'''

# with open('D:/pythonProject/nums.txt', 'r', encoding='utf-8') as nums:  вариант 1
#     for row in nums:
#         print(sum(map(int, row.split())))
    
# with open('D:/pythonProject/nums.txt', 'r', encoding='utf-8') as nums:       вариант 2
#     print(*[sum(map(int, i.split())) for i in nums.readlines()], sep='\n')


'''Сумма чисел в файле
Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые неотрицательные числа и все, что угодно. 
Числом назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).
Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести сумму всех чисел, записанных в файле.'''

# with open('D:/pythonProject/nums.txt', 'r', encoding='utf-8') as nums:
#     text = nums.read()
#     s = ''
#     for i in text:
#         if i.isdigit():
#             s+= i
#         else:
#             s+= ' '
#     print(sum(map(int, s.split())))

'''Статистика по файлу
Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв 
латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести три найденных числа в формате, приведенном в примере.'''

# with open('D:/pythonProject/rever.txt') as f:          Вариант 1
#     slova = len(f.read().split())
#     f.seek(0)
#     ls = list(map(str.strip, f.readlines()))
#     bukvi = 0
#     for i in ls:
#         for j in i:
#             if j.isalpha():
#                 bukvi += 1
#     print(f"Input file contains:\n{bukvi} letters\n{slova} words\n{len(ls)} lines")


# with open('D:/pythonProject/rever.txt') as f:        Вариант 2
#     ls = f.read()
#     lines = ls.count('\n') +1                        считаем кол-во строк по количеству вхождений '\n'
#     slova = len(ls.split())
#     bukvi = len([c for c in ls if c.isalpha()])
#     print(f"Input file contains:\n{bukvi} letters\n{slova} words\n{lines} lines")

'''Random name and surname
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их, каждую 
на отдельной строке.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.'''

# from random import choice
# with open('D:/pythonProject/first_names.txt') as f, open('D:/pythonProject/last_names.txt') as l:
#     fls = f.read().split()
#     lls = l.read().split()
#     for i in range(3):
#         res = choice(fls), choice(lls)
#         print(*res)

# Необычные страны
# Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом 
# табуляции '\t'.
# Напишите программу выводящую все страны, название которых начинается с буквы 'G', численность населения которых больше 
# чем 500000 человек, не меняя их порядок.
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должна вывести названия стран, удовлетворяющие условиям задачи, каждое на отдельное строке.

# with open('population.txt') as text:
#     for line in text:
#         ls = [i.strip() for i in line.split()]
#         if ls[0][0] == 'G' and int(ls[-1]) > 500000:
#             print(*ls[:-1])

'''CSV-файл
Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из 
этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна содержать реализованную функцию read_csv.
Примечание 1. Вызывать функцию read_csv не нужно.
Примечание 2. Функция read_csv не должна принимать аргументов. 
Примечание 3. Подробнее прочитать про CSV-файлы можно тут.
Примечание 4. Считайте, что все ключи и значения по этим ключам в результирующем словаре имеют строковый тип (str).'''

# def read_csv():
#     ls = []
#     with open('D:/pythonProject/data.csv', 'r', encoding='utf-8') as file:
#         keys = file.readline().strip().split(',')
#         for i in file:
#             row = i.strip().split(',')
#             ls.append(dict(zip(keys, row)))
#     return ls

# read_csv()
     
       