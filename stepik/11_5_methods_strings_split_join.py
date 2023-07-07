'''Построчный вывод
На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.
На вход программе подается строка текста.
Программа должна вывести текст в соответствии с условием задачи.'''
# s = input()
# s = s.split()
# print('\n'.join(s))
'''Инициалы
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая 
выводит инициалы человека.
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.'''
# s = input().split()
# for i in range(len(s)):
#     print(s[i][0], end='.')
'''Windows OS
В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и символ  
\",  затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл, в конце пишется имя 
файла (C:\Windows\System32\calc.exe).
На вход программе подается одна строка с корректным именем файла в операционной системе Windows. Напишите программу, 
которая разбирает строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.
На вход программе подается одна строка.'''
# s = input().split('\\')
# print('\n'.join(s))
'''Диаграмма
На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам 
строит столбчатую диаграмму.
На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.
Программа должна вывести столбчатую диаграмму.'''
# numbers = input().split()
# for i in numbers:
#     print('+' * int(i))
'''Корректный ip-адрес
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу, которая 
определяет является ли введенная строка текста корректным ip-адресом.
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.
Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.'''
# s = input().split('.')
# for n in s:
#     if 255 < int(n) or int(n) < 0:
#         print('НЕТ')
#         break
# else:
#     print('ДА')
'''Добавь разделитель
На вход программе подается строка текста и строка разделитель. Напишите программу, которая вставляет указанный 
разделитель между каждым символом введенной строки текста.
На вход программе подается строка текста и строка разделитель, каждая на отдельной строке
Программа должна вывести текст в соответствии с условием задачи.'''
# s1, s2 = input(), input()
# print(s2.join(s1))
'''Количество совпадающих пар
На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел. 
Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается, 
что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
На вход программе подается строка текста, содержащая натуральные числа, отделенные символом пробела.
Программа должна вывести одно число – количество пар элементов, равных друг другу.'''
# s = input().split()
# count = 0
# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if s[i] == s[j]:
#             count += 1
# print(count)