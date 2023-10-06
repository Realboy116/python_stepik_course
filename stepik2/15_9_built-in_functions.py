'''Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,
и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False
Перепишите функцию ignore_command(), чтобы она использовала встроенные функции all()/any() сохранив при этом ее 
функционал.'''

# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    # return any(map(lambda x: x in command, ignore)) Вариант через any с помощью map
    # return any(word in command for word in ignore)  Вариант через any без map
# print(ignore_command('trancate'))

'''Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о стране 
в формате:
<capital> is the capital of <country>, population equal <population> people.
Moscow is the capital of Russia, population equal 145934462 people.
Washington is the capital of USA, population equal 331002651 people.'''

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

# for x, y, z in zip(capitals, countries, population):
#       print(x, 'is the capital of', y+',', 'population equal', z, 'people.')  вариант вывода 1
#       print(f'{x} is the capital of {y}, population equal {z} people.')      вывод через f строку

'''Корректный IP-адрес
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающей по протоколу TCP/IP. В 4-й 
версии IP-адрес представляет собой 32-битное число. Адрес записывается в виде четырёх десятичных чисел (октетов) со 
значением от 0 до 255 (включительно), разделённых точками, например,192.168.1.2
Напишите программу с использованием встроенной функции all() для проверки корректности IP-адреса: все ли октеты в 
IP-адресе – числа со значением от 0 до 255.
Формат входных данных
На вход программе подается строка в формате x.x.x.x, где x – непустой набор символов 0-9, a-z.
Формат выходных данных
Программа должна вывести True если введенная строка – корректный IP-адрес и False в противном случае.'''

# ls = input().split('.')
# res = all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, ls))
# print(res)

'''Хороший пароль
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и 
строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.
Формат входных данных
На вход программе подаётся одна строка текста.
Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.'''

# s = input()
# print(('NO', 'YES')[len(s) >= 7 and s.upper() != s and s.lower() != s and any(map(lambda x: True if x in '0123456789' else False, s))])
#Вариант 2 
# def good_password(password):        создаем функцию и передаем в нее аргумент при вызове функции
#     if len(password) < 7:           проверяем длину входной строки
#         return 'NO'
#     flag = [False, False, False]    создаем флаг-список для проверки пароля на три  условия (кол-во эл-ов в списке)
#     for i in password:
#         if all(flag):               если все значения станут True до прохода по ВСЕМУ паролю то прерываем функцию 
#             return 'YES'
#         elif i.isdigit():           если символ из строки цифра то меняем нулевой элемент списка на True
#             flag[0] = True
#         elif i.isupper():           если символ из строки заглавная буква то меняем первый элемент списка на True
#             flag[1] = True
#         elif i.islower():           если символ из строки строчная буква то меняем пвторой элемент списка на True
#             flag[2] = True
#     if all(flag):                   если все элементы списка flag будут True то возвращаем YES
#         return 'YES'
#     return 'NO'
# s = input()
# print(good_password(s))

'''Отличники
Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться, 
что в каждом классе есть хотя бы один отличник – ученик с оценкой 5 по контрольной работе. Напишите программу с 
использованием встроенных функций all(), any() для помощи Тимуру в проверке.
Формат входных данных
На вход программе подается натуральное число n – количество классов. Затем для каждого класса вводится блок информации 
вида:
натуральное число k – количество учеников в классе;
далее вводится k строк вида: фамилия оценка.
Формат выходных данных
Программа должна вывести YES, если в каждом классе есть хотя бы один отличник, и NO в противном случае.'''

# n = int(input())
# students = []
# for _ in range(n):
#     m = int(input())
#     temp = []
#     for _ in range(m):
#         surname, mark = input().split()
#         temp.append((surname, int(mark)))
#     students.append(temp)

# result = all(map(lambda x: any(map(lambda y: y[1] == 5, x)), students))
# print('YES' if result else 'NO')

'''Письмо для экзамена
Напишите функцию generate_letter(), которая будет собирать электронное письмо в соответствии с шаблоном:
To: <mail>
Приветствую, <name>!
Вам назначен экзамен, который пройдет <date>, в <time>.
По адресу: <place>. 
Экзамен будет проводить <teacher> в кабинете <number>. 
Желаем удачи на экзамене!
Функция должна получать на вход пять обязательных аргументов mail, name, date, time, place и два необязательных teacher,
number и возвращать текст готового письма. При отсутствии аргумента teacher учителем будет Тимур Гуев, а если нет 
аргумента number, то кабинет будет 17.
Примечание 1. Следующий программный код:
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))
должен выводить:
To: lara@yandex.ru
Приветствую, Лариса!
Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
По адресу: Часова 23, корпус 2. 
Экзамен будет проводить Тимур Гуев в кабинете 17. 
Желаем удачи на экзамене!
To: lara@yandex.ru
Приветствую, Лариса!
Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
По адресу: Часова 23, корпус 2. 
Экзамен будет проводить Василь Ярошевич в кабинете 23. 
Желаем удачи на экзамене!
Примечание 2. Вызывать функцию generate_letter() не нужно, требуется только реализовать.'''
    
# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return (f'''To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!''')

# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
    
# def concat(*args, sep=' '):
#     return sep.join([str(i) for i in args])

# print(concat('hello', 'python', 'and', 'stepik', sep='*'))