#Комменты
# print("Результат:",6, 47, sep="", end="!\n")
# print('Second \\ \t l\ni\nn\ne')
#print("Результат:",5//3) результат целое число
#print("Результат:", min(2, 4, 5, 10, -15, -10)) находит мин число из написанных с кобках
#print("Результат:", max(2, 4, 5, 10, -15, -10)) находит макс число из написанных с кобках
#print("Результат:", pow(5, 3)) возводит в степень
# print("Результат:", round(5 / 3)) округляет к ближайшему
# input("Enter your age please: ")

#number = 5 тип int (integer) создали переменную присвоили ей значение
#del number удалили переменную
# digit = 4.57894 можем хранить разные числа в переменных тип float
# word = 'Результат:' можем хранить строки тип str(string)
# print(word, digit)
# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# print("Result: ", num_1 + num_2)
# print("Result: ", num_1 - num_2)
# print("Result: ", num_1 / num_2)
# print("Result: ", num_1 * num_2)
# word = "Hi"
# print(word * 2)
#user_data = int(input("Введите число: "))
# if user_data != 7:
#     print("Мы на месте")
#     if user_data > 8:
#         print("Это больше 8")
# isHappy = False
# if isHappy or user_data == 6:
#     print("User is Happy")
# elif user_data == 5:
#     print("Number is 5")
# elif user_data == 8:
#     print("Number is 5")
# else:
#     print("User is unhappy")
#data = input()
#number = 5 if data == "Five" else 0 тернарный оператор это сокращенный вариант if else
# if data == "Five":
#     number = 5
# else:
#     number = 0
#print(number)
# for i in range(1, 6, 2):
#     print(i)
# count = 0
# word = "Hello world!"
# for i in word:
#    if i == "l":
#        count += 1
# print("Count:", count)
# i = 5
# while i < 18:
#     print(i)
#     i += 3
# isHasCar = True
# while isHasCar:
#     if input("Enter magic word: ") == "stop":
#         isHasCar = False
# for i in range(1, 10):
#     if i >= 6:
#         break остановка цикла
#     if i % 2 == 0: если при делении на 2 остаток будет равен 0
#         continue пропуск определенной итерации
#     print(i)
# found = None
# for i in "hello":
#     if i == "w":
#         found = True
#         break
# else:
#     found = False
# print(found)
# nums = [4, 5, 6, 2, 5, 6, True, "Hi", 5.66, [78, 65]]
# nums[0] = 50
# nums[6] = 1.23
# print(nums[-1][])
# numbers = [4, 5, 6]
# numbers.append(100)
# numbers.insert(1, True)
# b = [5, 6, 8]
# numbers.extend(b)
#numbers.sort() сортировка
#numbers.reverse() реверс все наоборот
#numbers.sort()
#numbers.pop() удаляет последний элемент если скобки пустые
#numbers.pop(2) удаляет элемент по индексу
#numbers.pop(-2) удаляет элемент второй с конца
#numbers.remove(5) удаляет конкретное значение, если в списке несколько одинаковых то удаляет только одно значение
#numbers.clear() удаляет весь список
#print(numbers.count(6)) считает кол-во совпадений
#print(len(numbers)) длина списка
# n = int(input("Enter length: "))
# user_list = []
# i = 0
# while i < n:
#     string = "Enter element №" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1
# print(user_list)
#word ='ceNter'
#print(word.count('e'))
#print(word.upper()) приводит всю строку к верхнему регистру
#print(word.isupper()) проверяет в верхнем ли регистре строка
#print(word.islower()) проверяет в нижнем ли регистре строка
#print(word.lower()) приводит всю строку к нижнему регистру
#print(word.capitalize()) приводит каждый первый символ слова (кроме остальных) к верхнему регистру в строке
#print(word.find('t')) находит по символу в строке выводит по индексу
#word = "Music, films, sport"
#print(word.split(', ')) разбивает строку на элементы (по указанным символам) и выводит список
#hobby = word.split(', ')
#print(hobby[1]) выводит элементы списка по индексу
# word = "Music, films, sport"               эта конструкция
# hobby = word.split(', ')                  позволяет сделать
# for i in range(len(hobby)):               каждое слово в списке
#     hobby[i] = hobby[i].capitalize()      с заглавной
# print(hobby)                              буквы
#result = ", ".join(hobby)                здесь выведет
#print(result)                            список без квадратных скобок+все приводит в правильный вид (регистры)
#Срезы и индексы
# word = 'Football'                       здесь выводит диапазон
# print(word[0:4])                        символы по индексам например с 0 по 4 индекс
# lis = [4, 5, 6, "Stroka", True, 5.67]   здесь добавляя : выводит
# print(lis[2:])                          продолжение списка от указанного индекса
# lis = [4, 5, 6, "Stroka", True, 5.67]   здесь добавляя -1 после : выводит
# print(lis[2:-1])                        выводит продолжение списка от указанного индекса без последнего элмента
# lis = [4, 5, 6, "Stroka", True, 5.67]   здесь выведет элементы
# print(lis[::2])                         через один (указываем шаг)
# lis = [4, 5, 6, "Stroka", True, 5.67]   здесь выведет элементы
# print(lis[::-2])                        через один но справа налево
#Кортежи (гугли инфу определение в инете)
# data = (4, 5, 6, 7, True, 5.67, 'Hello') это кортеж(tuple), вывод элементов   функций меньше чем в списке
# print(data[1])                           по индексу                           нельзя удалять, изменять, добавлять
# data = (4, 5, 6, 7, True, 5.67, 'Hello') срез (вывод) элементов
 # print(data[1:5])                         по диапазону
# data = 4, 5, 6, 7, True, 5.67, 'Hello'   это еще один способоб
# print(data)                              создать кортеж
# data = (4,)                              создаем кортеж
# print(data)                              с одним символом обязательно запятая, без запято НЕ кортеж
# data = (4, 5, 6, 7, True, 5.67, 'Hello')
# for el in data:
#     print(el)
#Словари (dict)  и работа с ними
# country = {'code': 'RU', 'name': 'Russian', 'population': 144} создаем словарь (в качестве ключа можно и числа и строки
# print(country['name'])                                         выводим значение по ключу
#country = dict(code='RU', name='Russian', population=144)      еще один способ
# print(country['code'])                                        создать словарь только СТРОКИ в качестве ключа
#print(country)                                                 вывод всего словаря
# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# print(country['code'])
# country = {'code': 'RU', 'name': 'Russian', 'population': 144} циклом
# for key in country:                                            выводим
#     print(key)                                                 только ключи из словаря
# country = {'code': 'RU', 'name': 'Russian', 'population': 144} циклом
# for key, value in country.items():                             выводим
#     print(key, '-', value)                                     ключи через дефис значения
# country = {'code': 'RU', 'name': 'Russian', 'population': 144} метод get позволяет нам
# print(country.get('name'))                                     получить значение по ключу
# country = {'code': 'RU', 'name': 'Russian', 'population': 144} очищаем
# country.clear()                                                словарь
# print(country)                                                 методом clear
# country = {'code': 'RU', 'name': 'Russian', 'population': 144} удаляем определенное значение
# country.pop('name')                                            по ключу
# country.popitem('name')                                        удяляем последние ключ и значение
#print(country.keys())                                           выводим только ключи из словаря
#print(country.values())                                         выводим только значения из словаря
#country['code'] = 'None'                                        заменили(обновили) значения для ключа 'code'
# person = {
#     'User_1': {
#         'first_name': 'Jony',
#         'last_name': 'Smirnof',
#         'age': 45,
#         'address': ['г. Казань', 'ул. Гагарина', 45],
#         'grades': {'math': 5, 'physics': 4}
#     },
#     'User_2': {
# 'first_name': 'Tomy',
#         'last_name': 'Lee',
#         'age': 28,
#         'address': ['г. Москва', 'ул. Пятницкая', 178],
#         'grades': {'math': 5, 'physics': 4}
#     }
# }
# print(person['User_1']['address'][1]) вытаскиваем то что нужно, здесь вытащили улицу у User_1
#Множества (set и frozenset)
#Функции (def, lambda) здесь про функцию "def" стандартные
# def test_func():            объявляем функцию
#     print("Hello", end="")  вводим параметры для функции
#     print("!")              вводим параметры для функции
# test_func()                 пишем название функции и тем самым выводим ее
# def summa(a, b):            функция принимает какие то значения
#     res = a + b             далее мы указываем что делать с этими значениями
#     print("Result: ", res)  указываем что выводить
# summa(4, 6)                 вызываем функцию
# summa("H", "i")             вызываем функцию
# nums1 = [5, 3, 8, 7, 9, 2]  вариант
# min = nums1[0]              нахождения
# for el in nums1:            минимального числа
#     if el < min:            много строчек кода
#         min = el            потому что не
# print(min)                  используем функции
# def minimal(l):             прописываем функцию называем ее "minimal" она будет принимать один параметр некий список
#     min_number = l[0]       создал некую переменную установил в нее нулевой по индексу из списка
#     for el in l:            создал переменную "el" в цикле перебираю список "l"
#         if el < min_number:
#             min_number = el
#     print(min_number)        выводим минимальный элемент
# nums1 = [5, 3, 8, 7, 9, 2]
# minimal(nums1)             обращаюсь к функции передаю туда "nums1"
# nums2 = [5.2, 6.7, 5.4, 8.9, 7.5]
# minimal(nums2)             обращаюсь к функции передаю туда "nums2"
# def minimal(l):            можем вообще
#     min_number = l[0]      можем вообще
#     for el in l:           можем вообще
#         if el < min_number:можем вообще
#             min_number = elможем вообще
#     return min_number      можем вообще не выводить мин элемент а возвращать его ретЕрном
# nums1 = [5, 3, 8, 7, 9, 2]
# min1 = minimal(nums1)      создал переменную min1
# nums2 = [5.2, 6.7, 5.4, 8.9, 7.5, 1.9]
# min2 = minimal(nums2)      создал переменную min2
# if min1 < min2:            пишем условие для
#     print(min1)            вывода минимального
# else:                      значения из
#     print(min2)            двух списков
#Lambda функции (анонимные)
# func = lambda x, y: x * y    пишем ключевое слово "lambda" указываем параметры которые передаются в эту функцию
# res = func(5, 2)             обращаемся по названию к самой переменной (в переменную пишем определенные параметры)
# print(res)                   выводим переменную "res"
#Работа с файлами создание и запись данных в файл
#file = open('data/text.txt', 'w') создал файл в указанной папке, "w" write значит что данные в файле всегда стираются
#                                  и записываются новые данные старые удаляются
#file = open('data/text.txt', 'a') "a" append данные добавляются к старым данным ничего не удаляется
# data = input("Введите текст: ")  забираем текст от юзера (вбивает текст в консоль) через инпут
# file = open('data/text.txt', 'w') создаем текстовый файл (папка/название файла, запись данных)
# file.write(data)                  внутрь функции wrtie помещаем инфу от юзера
# file.close()                      закрываем файл, команда обязательная!
# file.write(data + "\n")           тоже самое только! ПЕРЕВОД на новую строку
#Чтение файлов
# file = open('data/text.txt', 'r', encoding='utf-8') открыл файл+ команда для чтения кирилицы encoding='utf-8'
# print(file.read())                функция read возвращает полностью весь текст если не прописаны иные параметры
# file.close()                      закрыл файл
# print(file.read(1))               1 выведет только один символ из текста
# file = open('data/text.txt', 'r') построчный
# for line in file:                 вывод текста
#     print(line)                   из файла благодаря циклу for
# file.close()
#Обработчик исключений try - expect
# x = int(input("Введите число: ")) здесь если ввести в
# x +=5                             терминале строку то
# print(x)                          будет ошибка
# try:                                  обработчик ошибок
#     x = int(input("Введите число: ")) если здесь
#     x +=5                             юзер введет число то
#     print(x)                          то код норм отработает
# except ValueError:                    если введут НЕ число то выведет
#     print("Вы ввели не число!")       подсказку которую мы написали
# x = 0                                 создал переменную со значением ноль
# while x == 0: условия цикла: до тех пор пока Х равен значению ноль цикл будет постоянно работать
#     try:
#         x = int(input("Введите число: ")) если мы получим число от пользователя то
#         x +=5                             х будет уже явно больше чем ноль
#         print(x)                          и мы выйдем из цикла
#     except ValueError: если введут не число будем получать ошибку х будет оставться как ноль и цикл будет повторяться
#         print("Вы ввели не число!")
# try:                              здесь обрабатываем сразу несколько ошибок
#     x = 5 / 0  деление на ноль    если будет эта ошибка то код не обработает вторую ошибку
#     x = int(input())              в общем мы можем
# except ZeroDivisionError:         обрабатывать
#     print("Деление на ноль!")     множество
# except ValueError:                  разных
#     print("Вы ввели что то не то!") ошибок
# try:                                 все
#     x = 5 / 0                        тоже
#     x = int(input("Число: "))        самое
# except ZeroDivisionError:             только
#     print("Деление на ноль!")         здесь
# except ValueError:                    вместе с
#     print("Вы ввели что то не то!")   ошибкой
# finally:                              выведет надпись
#     print("Finally")                  которую мы напишем
#Менеджер "with ... as" для работы с файлами
# try:
#    with open('data/text2.txt', 'r', encoding='utf-8') as file: здесь with...as сам закрывает файл который открыл
#         print(file.read())                                     поэтому мы не пишем команду file.close
# except FileNotFoundError:
#     print("Файл не найден!")
#Модули в Python. Создание и работа с модулями.
#Модуль времени
# import time                       пример time это встроенный модуль сначала мы его импортируем
# time.sleep(5)                     команда sleep "замораживает" запуск кода на поределенное время здесь 5 сек
# print("Ты отсчитал 5 секунд?")    вывод текста через 5 сек
#Модуль datetime
#import datetime as d               импортнули модуль, сделали короткое название модуля, обращаемся к модулю буквой d
# print(d.datetime.now())           выводим полную текущую дату и время
# print(d.datetime.now(). date())   выводим полную текущую только дату
# print(d.datetime.now(). time())   выводим полное текущее только время
#Модули sys и os для получения какой либо инфы
#import sys, os, platform
#print(sys.path)                    полный путь к текущему файлу
#print(os.name)
#print(platform.system())           инфо об ос
#from math import sqrt мы можем импортировать не весь модуль целиком а только нужную нам функцию
# import cowsay                     проверили забавный модуль
# cowsay.cow('I am funny cow!')     модуль = библиотека
# ООП
# class Cat:                        создал класс Cat
#     name = None                   создал
#     age = None                    разные
#     isHappy = None                параметры для класса Cat
#     def set_data(self, name, age, isHappy): функция set_data будет принимать параметры и будет устанавливать их в
#         self.name = name                   поля name,age,isHappy которые выше SELF вначале обязательно! название этих
#         self.age = age                     параметров которые выше в скобках обычно совпадает с названиями полей класса
#         self.isHappy = isHappy здесь и 2 строки выше забираем значения для параметров из полей выше
#     def get_data(self): этот метод ничего не принимает но он возвращает полную характеристику нашего объекта
#         print(self.name, "age:", self.age, ". Happy", self.isHappy)
# cat1 = Cat()
# cat1.set_data("Барсик", 3, True) обращаемся к функции set_data и указываем параметры
# cat2 = Cat()
# cat2.set_data("Жопен", 2, False)
# cat1.get_data() обращаемся к объекту cat к функции get_data и выводим полную инфу по нашим объектам
# cat2.get_data()
#Конструкторы, переопределение методов
# class Cat:
#     name = None
#     age = None
#     isHappy = None
#     def __init__(self, name, age, isHappy): #создаем конструктор командой __init__
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#         #self.set_data(name, age, isHappy) эта строка сделает тоже самое что 3 строки выше только одной строкой
#         #self.get_data() это вместо принта выводит все
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#     def get_data(self):
#         print(self.name, "age:", self.age, ". Happy", self.isHappy)
# cat1 = Cat("Барсик", 3, True) # установка данных теперь происходит в момент создания объекта
# cat2 = Cat("Жопен", 2, False)
# cat1.get_data()
# cat2.get_data()
#Переопределение методов
# class Cat:
#     name = None
#     age = None
#     isHappy = None
#     def __init__(self, name, age, isHappy):
#         self.set_data(name, age, isHappy)
#         self.get_data()
#     def set_data(self, name = None, age = None, isHappy = None):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#     def get_data(self):
#         print(self.name, "age:", self.age, ". Happy", self.isHappy)
# cat1 = Cat("Барсик", 3, True)
# cat1.set_data("Tom", 2)
# cat2 = Cat("Жопен", 2, False)
#Наследование, инкапсуляция, полиморфизм
# class Building:
#     year = None
#     city = None
#
#     def __init__(self, year, city):
#         self.year = year
#         self.city = city
#
#     def get_info(self):
#         print("Year:", self.year, ". City:", self.city)
#
# class School(Building): #создаем класс School в скобках пишем Building и теперь класс School наследует все от Building
#     pupils = 0
#     def __init__(self, pupils,year, city): #в конструкторе указываем те харатеристики которые хотим получать
#         super(School, self).__init__(year, city) #вызвал класс родитель командой "super" указываем откуда что
#         self.pupils = pupils  #для pupils указывваем значение pupils из самого конструктора
#     def get_info(self):
#         super().get_info()
#         print("Pupils:", self.pupils)
# class House(Building): #класс "родитель" можем указывать только один, то есть наследовать только от одного класса
#     pass
# class Shop(School): #клас наследник "School" может быть классом родителем для других классов объеденяя все параметры
#     pass
# school = School(100, 2000, "Moscow") #создал объект на основе класса School и передал туда параметры от класса Building
# school.get_info() #через этот объект можно обратится ко всем параметрам класса Building или например к get_info
# house = House(2000, "Moscow")
# shop = Shop(100, 2000, "Moscow")
#Деораторы функций
# import webbrowser
# def validator(func): #вложенные функции здесь валидируем данные проверяем url адрес принимаем параметр func
#     def wrapper(url): #та самая "вложенная" функция+ принимаем параметр url
#         if "." in url: #условие "есть ли точка в url адресе"
#             func(url) #принимаем параметр url
#         else:          # если точки нет в URL то выводим соотвествующую надпись
#             print("Неверный URL")
#     return wrapper #необходимо возвращать из основной функц "validator" функц "wrapper" без скобок в конце
# @validator #непосредственно сам "декоратор", если убрать эту строку то никаких проверок не будет
# def open_url(url): #создал функцию назвал "open_url" она принимает один параметр это url адрес
#     webbrowser.open(url) #обращаемся к модулю "webbrowser" функция open в нее передаем определенный адрес url
# open_url("https://ya.ru") #здесь можно вбить сайт он откроется в браузере по умолчанию