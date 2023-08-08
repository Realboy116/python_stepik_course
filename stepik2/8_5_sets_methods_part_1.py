'''Уникальные символы 1
Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
Формат входных данных
На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк с словами.
Формат выходных данных
Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.'''

# for i in range(int(input())):
#     print(len(set(input().lower())))

'''Уникальные символы 2
Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
Формат входных данных
На вход программе в первой строке подается число n – общее количество слов. Далее идут 
n строк со словами.
Формат выходных данных
Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.'''
# my_set = set()
# for _ in range(int(input())):
#     my_set.update(input().lower())
# print(len(set(my_set)))

# n = int(input())  Вариант от препода 
# symbols = set()

# for _ in range(n):
#     for c in input().lower():
#         symbols.add(c)
        
# print(len(symbols))

'''Количество слов в тексте
Напишите программу для определения общего количества различных слов в строке текста.
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести одно число – общее количество различных слов в строке без учета регистра.
Примечание 1. Словом считается последовательность непробельных символов, идущих подряд, слова разделены одним или 
большим числом пробелов.
Примечание 2. Знаками препинания .,;:-?! пренебрегаем.'''

# n = input().lower().replace('.', '').replace(',', '').replace(';', '').replace(':', '').replace('-', '').replace('?', '').replace('!', '').split()
# print(len(set(n)))

# text = input().lower() ввод строки и преобразование всех символов к нижнему регистру
# for sign in '.,;:-?!':   цикл для удаления указанных символов в строке
#     text = text.replace(sign, '')  операция по удалению необходимых символов
# print(len(set(text.split()))) вывод длины строки преобразованный в список, преобразованный во множество

# words = [word.lower().strip('.,;:-?!') for word in input().split()] решение от преподов внимание на метод strip!!!
# print(len(set(words)))

'''Встречалось ли число раньше?
На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке), 
если это число ранее встречалось в последовательности или NO, если не встречалось.
Формат входных данных
На вход программе подается строка текста, содержащая числа, разделенные символом пробела.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Ведущие нули в числах должны игнорироваться.'''

# s = set()
# n1 = [int(i) for i in input().split()]
# for n in n1:
#     if n not in s:
#         print('NO')
#         s.add(n)
#     else:
#         print('YES')