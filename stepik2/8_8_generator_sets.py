'''Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные значения 
списка items. Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.
Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки, при этом строки необходимо 
трактовать как числа.
Примечание 2. Чтобы вывести элементы множества в упорядоченном виде используйте следующий код:

print(*sorted(myset))'''

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# my_set = {int(c) for c in items}
# print(*sorted(my_set))

'''Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее первую букву каждого 
слова (в нижнем регистре) списка words. Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним 
символом пробела.'''

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# my_set = {i[0].lower() for i in words}
# print(*sorted(my_set))

'''Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные слова (в 
нижнем регистре) строки sentence. Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним 
символом пробела.
Примечание. Учтите, что знаки пунктуации не относятся к словам.'''

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a 
# pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you 
# can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those 
# redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the 
# rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

# my_set = {c.lower().strip(',.():;') for c in sentence.split()}
# print(*sorted(my_set))

'''Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные слова  
строки sentence длиною меньше 4 символов. Результат вывести на одной строке (в нижнем регистре) в алфавитном порядке, 
разделяя элементы одним символом пробела.
Примечание. Учтите, что знаки пунктуации не относятся к словам.'''

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a 
pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you 
can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those 
redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the 
rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

# my_set = {c.lower().strip(',.();:') for c in sentence.split() if len(c.strip(':')) < 4}
# print(*sorted(my_set))

'''Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files уникальные имена файлов c 
расширением .png, независимо от регистра имен и расширений. Имена файлов вывести вместе с расширением, все на одной 
строке, в нижнем регистре, в алфавитном порядке через пробел.'''

# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

# my_set = {c.lower() for c in files if c.lower().endswith('.png')}  #вариант 1
# my_set = {c.lower() for c in files if c[-4::1].lower() == '.png'}  #вариант 2
# print(*sorted(my_set))


