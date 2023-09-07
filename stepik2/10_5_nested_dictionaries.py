# d = {i: i**2 for i in range(6)}  генератор словарей
# print(d)

# d = {i: {j: j**2 for j in range(i)} for i in range(5)}
# print(d)

'''Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
colors, кроме тех, у которых значением является None.'''

# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}

# result = {i: colors[i] for i in colors if colors[i] is not None}
# print(result)

'''Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
favorite_numbers , значения которых являются двузначными числами.'''

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}

# result = {i: favorite_numbers[i] for i in favorite_numbers if 9 < favorite_numbers[i] < 100 }
# print(result)

'''Дополните приведенный код, используя генератор, так, чтобы получить словарь result, состоящий из всех элементов 
словаря months , в которых ключ и значение поменялись местами.'''

# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

# result = {months[i]: i for i in months}
# print(result)

'''В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор, чтобы получить словарь 
result , в котором числа будут ключами, а слова – значениями.
Примечание 1. Ключи словаря должны быть целыми числами (иметь тип int), значения – строками (иметь тип str).'''

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

# result = {int(i[: i.find(":")]): i[i.find(":")+1:] for i in s.split() }
# print(result)

'''Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка 
numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 1
Примечание 1. Если бы список numbers имел вид: numbers = [1, 6, 18], то результатом был бы словарь
result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}'''

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

# result = {i: [v for v in range(1, i+1) if i % v == 0] for i in numbers }
# print(result)

'''Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет строка – 
элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.
Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'], то результатом был бы словарь
result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}
Примечание 2. Для получения ASCII кода символа используйте функцию ord().'''

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

# result = {i: [ord(s) for s in i] for i in words}
# print(result)

'''Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
letters , за исключением тех, ключи которых есть в списке remove_keys.'''

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}

# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]

# result = {k: i for k, i in letters.items() if k not in remove_keys}
# print(result)

'''В переменной students хранится словарь, содержащий информацию о росте (в см) и весе (в кг) студентов.

Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
students , где указан рост больше 167 см, а вес меньше 75 кг.'''

# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}

# result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}
# print(result)

'''Список tuples содержит кортежи, состоящие из трех чисел.
Дополните приведенный код, используя генератор, чтобы получить словарь result, в котором ключом является первый элемент 
каждого кортежа, а значением – кортеж из оставшихся двух элементов.'''

#tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]

#result = {k: (*v,) for k, *v in tuples}       вариант 1
#result = {i[0]: (i[1], i[2]) for i in tuples} вариант 2
#print(result)

'''Даны три списка student_ids, student_names, student_grades, содержащие информацию о студентах.
Дополните приведенный код, используя генератор, так чтобы получить список result, содержащий вложенные словари в 
соответствии с образцом: [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].
Примечание 1. Для параллельной итерации по всем трем спискам одновременно можно использовать встроенную функцию zip().'''

# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013'] 
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy'] 
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

# result = [{a:{c: b}} for a, b, c in zip(student_ids, student_grades, student_names)]
# print(result)

# s = input().split()
# res ={k: }
# for num in s:
#     res[num] = res.get(num, 0) +1
#     print(res[keys])