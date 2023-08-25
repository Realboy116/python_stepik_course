'''Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи – числа от 
1 до 15 (включительно), а значения представляют собой квадраты ключей.
Примечание. Выводить содержимое словаря result не нужно.'''

# result = {}
# for i in range(1, 16):
#     result.setdefault(i, i ** 2)
# print(result)

'''Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, складывая значения 
по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. Результирующий словарь необходимо присвоить 
переменной result.
Примечание. Выводить содержимое словаря result не нужно.'''

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = {}
# result = dict1.copy()
# for i, j in dict2.items():
#     result[i] = result.get(i, 0) + j
# print(result)

'''Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text 
будет подсчитано количество его вхождений.
Примечание. Выводить содержимое словаря result не нужно.'''

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

# result = {}
# for num in text:
#     result[num] = result.get(num, 0) + 1 

'''Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, 
должно быть выведено то, что меньше в лексикографическом порядке.'''

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# result = {}
# result2 = {}
# numbers = [c for c in s.split()]
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# mx = (max(result.values()))
# for key, value in result.items():
#     if value == mx:
#         result2[key] = result2.get(key, value)
# mx2 = (min(result2))
# print(mx2)

''''Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж вида 
(кличка собаки, имя владельца, фамилия владельца, возраст владельца).
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут 
перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список кличек 
собак (сохранив исходный порядок следования).
Примечание 1. Не забывайте: кортежи являются неизменяемыми, поэтому могут быть ключами словаря.
Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.'''

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
# result = {}
# for dog in pets:
#     result.setdefault((dog[1], dog[2], dog[3]), []).append(dog[0])
# print(result)


'''Самое редкое слово 🌶️
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без 
учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.
Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.
Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:
;-, которые нужно игнорировать. Других символов в тексте нет.'''

# s = [word.strip('.,!?:;-') for word in input().lower().split()]
# result = {}
# result2 = {}
# numbers = [c for c in s]
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# mx = (min(result.values()))
# for key, value in result.items():
#     if value == mx:
#         result2[key] = result2.get(key, value)
# mx2 = (min(result2))
# print(mx2)

'''Исправление дубликатов 🌶️
На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так, 
чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам 
постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.
Формат входных данных
На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.
Формат выходных данных
Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.'''

# s = input().split()
# d = {}
# for w in s:
#     if w in d:                            #проверка элемента исходной строки на наличие в словаре
#         print(f'{w}_{d[w]}', end=' ')    #есть - печать ф-строки {элемент}_{значение от элемента в словаре}
#     else:
#         print(w, end=' ')                 #нет - печать элемента без значения
#     d[w] = d.get(w, 0) + 1                #заполнение словаря через get