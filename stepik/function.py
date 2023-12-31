'''Забыл как правильно вызывать и делать принт функции а именно проблемы с аргументами передаваемыми в функцию'''

'''Функции без параметров
В предыдущих уроках мы использовали встроенные в Python функции print(), input(), int(), str(), len() и многие другие. 
Пришло время начать писать свои собственные функции.
В самом начале курса вам было предложено решить задачу, в которой требовалось изобразить звездный прямоугольник размерами 
5×7 (5 строк и 7 столбцов).
Наш первый вариант кода выглядел примерно так: 
print('*******')
print('*******')
print('*******')
print('*******')
print('*******')
Далее мы изучили оператор умножения строки на число (оператор повторения) и написали бы код:
print('*' * 7)
print('*' * 7)
print('*' * 7)
print('*' * 7)
print('*' * 7)
Ну и наконец, мы изучили циклы, после чего код принял бы вид:
for _ in range(5):
    print('*' * 7)
    
А теперь представим, что таких прямоугольников нужно изобразить не один, а несколько, скажем 3 штуки.
Тогда код программы будет иметь вид:
for _ in range(5):
    print('*' * 7)

print()

for _ in range(5):
    print('*' * 7)

print()

for _ in range(5):
    print('*' * 7)
И хотя предыдущий код полностью решает поставленную задачу, он не лишен недостатков. Во-первых, он довольно громоздкий 
из-за повторения части кода, отвечающей за вывод прямоугольника. Во-вторых, если понадобится изменить размеры 
прямоугольника, придется менять их трижды, в каждой части кода, выводящей прямоугольник.
Вместо повторения кода для вывода прямоугольника, можно перенести  его в отдельную функцию  и вызвать ее 3 раза.
Для создания функции пишем такой код:'''

# def draw_box():
#     for _ in range(5):
#         print('*' * 7)
'''Когда функция создана, чтобы увидеть результат ее работы, надо вызвать ее по имени:'''
#draw_box() # так мы вызываем функцию

'''Теперь чтобы изобразить 3 прямоугольника можно написать код:'''
# draw_box()
# print()
# draw_box()
# print()
# draw_box()
# print()

'''Именование функций
Имена функциям назначаются точно так же, как переменным. Имя функции должно быть достаточно описательным, чтобы любой, 
читающий ваш код, мог догадаться, что именно функция делает.
Python и тут требует соблюдения тех же правил, что при именовании переменных:
-в имени функции используются только латинские буквы a-z, A-Z, цифры и символ нижнего подчеркивания (_);
-имя функции не может начинаться с цифры;
-имя функции по возможности должно отражать ее назначение;
-символы верхнего и нижнего регистра различаются.'''
'''Объявление функции
Итак, функция – отдельная, функционально независимая часть программы, выполняющая определенную задачу.
Функции объявляются с помощью ключевого слова def (от слова define – определять). За ключевым словом def следуют 
название функции, круглые скобки (), и двоеточие :.
def название_функции():
    блок кода
Первая строка объявления функции называется заголовком функции.
Со следующей строки идет блок кода – тело функции. Это набор инструкций, составляющих одно целое и выполняющихся 
каждый раз, когда вызывается функция.
Вызов функции
Для вызова функции пишут ее название и круглые скобки.
Важно: очень часто начинающие программисты забывают вызывать функцию. Помните, что объявление функции не вызывает ее.
# объявление функции
def print_message():
    print('Я - Артур,')
    print('король британцев. ')

# вызов функции
print_message()
Всегда сначала функцию объявляем (и пишем ей код) и только потом вызываем ее. !!! Мы не можем вызвать функцию которой не
существует!'''
'''Примечание 4. Иногда, при объявлении функции требуется сделать своего рода заглушку, чтобы функция ничего не выполняла. 
Тогда мы используем ключевое слово pass: 
def do_nothing():
    pass
Мы объявили функцию с именем do_nothing(). Тело такой функции содержит единственную строку кода, которая ничего не делает.
Функции с параметрами
В предыдущем уроке мы определили функцию draw_box(), которая выводит звездный прямоугольник с размерами 
5
×
7
5×7
Было бы намного удобнее, если бы функция draw_box() выводила прямоугольник с произвольными размерами. И действительно, 
функции могут принимать входные параметры, что делает их более гибкими.
Функции с параметрами объявляются так же как функции без параметров, только с указанием в скобках:
def название_функции(параметры):
    блок кода

Давайте перепишем предыдущую версию функции draw_box() так, чтобы она принимала параметры, задающие высоту(height) и 
ширину(width) прямоугольника:'''
# def draw_box(height, width):
#     for i in range(height):
#         print('*' * width)
'''Теперь наша функция draw_box() принимает два целочисленных параметра height – высота прямоугольника и width – ширина 
прямоугольника, и для ее вызова нам нужно обязательно их указать.
Чтобы вывести звездный прямоугольник размерами 5 на 7 мы пишем код:'''
#draw_box(5, 7)
'''Результатом такого вызова функции draw_box(5, 7) будет:
*******
*******
*******
*******
*******'''
'''Теперь с помощью нашей новой версии функции draw_box() можем в одной программе выводить прямоугольники разных 
размеров. Следующий программный код:'''
# draw_box(3, 5)
# print()
# draw_box(4, 8)
# print()
# draw_box(5, 10)
'''На место параметров мы можем подставлять не только целочисленные константы, но и значения переменных. Следующий 
программный код:'''
# v = 3
# sh = 6
# draw_box(v, sh)
'''Выведет:
******
******
******'''
'''Еще примеры
Напишем функцию print_hello(n), которая принимает одно натуральное число n и печатает слово Hello ровно n раз.'''
# def print_hello(n): параметр n
#     print('Hello' * n)
'''Следующий программный код:'''
#print_hello(5) аргумент 5
'''Выведет: HelloHelloHelloHelloHello'''
'''Функцию print_hello() можно сделать более гибкой, если передавать в нее еще один параметр – текст для вывода:'''
# def print_text(text, n): это пармаетры функции в скобках
#     print(text * n)
    
'''Следующий программный код:'''
# print_text('Вот это да!', 3) это аргументы функции в скобках
# print_text('А круто', 5) это аргументы функции в скобках
'''Выведет:
Вот это да!Вот это да!Вот это да!
А крутоА крутоА крутоА крутоА круто'''

'''Параметры VS аргументы
Аргумент – это любая порция данных, которая передается в функцию, когда функция вызывается. Параметр – это переменная, 
которая получает аргумент, переданный в функцию.
Для функции draw_box(height, width):'''
# def draw_box(height, width): # здесь параметры для функции это height и width
#     for i in range(height):
#         print('*' * width)
'''А вот когда мы уже вызываем саму функцию:
height = 10 если мы параметр высота обозгачили как 10 (отдельно)
draw_box(height, 9) то здесь при вызове функции АРГУМЕНТАМИ будут heght и 9
ЕЩЕ РАЗ!!!! Аргумент – это любая порция данных, которая передается в функцию, ПРИ ВЫЗОВЕ ФУНКЦИИ!!!
А Параметр – это переменная, которая получает аргумент, переданный в функцию'''
'''Внесение изменений в параметры
Когда аргумент передается в функцию, параметрическая переменная функции будет ссылаться на значение этого аргумента. 
Однако любые изменения, которые вносятся в параметрическую переменную, не будут влиять на аргумент.
Cледующий программный код:'''
# def new_f(v, sh):
#     v = 3 # В теле функции вносятся изменения в значения параметрических переменных height и width, однако это никак не
#     sh = 6 #повлияло на значение переменных n и m из основной программы, которые передавались в качестве аргументов
#     for i in range(v): # в функцию new_f().
#         print('$' * sh)
# n = 10
# m = 20
# new_f(n, m)

'''!!! ЗАПОМНИТЬ !!! имена, указанные в объявлении функции, называются параметрами, тогда как значения, которые вы 
передаёте в функцию при её вызове, – аргументами."'''

'''Локальные переменные
Локальными называются переменные, объявленные внутри функции и доступные только ей самой. Программный код за пределами 
функции к ним доступа не имеет.
Рассмотрим функцию print_texas(), которая выводит информацию о количестве птиц, обитающих в Техасе.'''
# def print_texas():
#     birds = 5000  #В теле функции мы создаем переменную birds, которой присваивается значение, равное 5000
#     print('В Техасе обитает', birds, 'птиц.')
'''Такая переменная (birds) является локальной для функции print_texas(). Всякий раз, когда переменной внутри функции 
присваивается значение, в результате создается локальная переменная. Она принадлежит функции, в которой создается,  и 
к ней получает доступ только программный код этой функции.'''
'''ВАЖНО!!! Если программный код одной функции попытается обратиться к локальной переменной, принадлежащей другой 
функции, произойдет ошибка'''
#Вот пример такой ситуации и ошибки:
# def print_texas():
#     birds = 5000   внутри этой функции есть переменная birds
#     print('В Техасе обитает', birds, 'птиц.')

# def print_california():
#     print('В Калифорнии обитает', birds, 'птиц.') здесь мы пытаемся обратится к переменной birds которой нет в этой 
#  функция не видит локальную переменную из другой функции  поэтому будет ошибка: NameError: name 'birds' is not defined
'''Локальные переменные скрыты от других функций, поэтому другие функции могут иметь собственные локальные переменные с 
тем же именем. Например,'''
# def print_texas():
#     birds = 5000  переменная birds
#     print('В Техасе обитает', birds, 'птиц.')

# def print_california():
#     birds = 9000  и здесь переменная birds но с другим значением эти переменные скрыты (невидимы) друг от друга
#     print('В Калифорнии обитает', birds, 'птиц.')
'''В каждой из этих двух функций есть локальная переменная с именем birds. Но они никогда не видны одновременно, так 
как находятся в разных функциях.'''
'''Для функции print_texas(), видима переменная birds, значение которой равно 5000. Для функции print_california(),
видима переменная birds, значение которой равно 9000.'''

'''Область действия переменной
К локальной переменной не может обращаться программный код, который появляется внутри функции до того, как переменная 
была создана. Например, если в функции print_texas() поменять местами строки кода:'''
# def print_texas():
#     print('В Техасе обитает', birds, 'птиц.')
#     birds = 5000
'''то при вызове этой функции получим ошибку: UnboundLocalError: local variable 'birds' referenced before assignment'''

'''Область действия параметрической переменной
Область действия параметрической переменной — функция, в которой этот параметр используется. К параметрической 
переменной имеет доступ весь программный код этой функции. Рассмотрим уже известную нам функцию:

def draw_box(height, width):
    for i in range(height):
        print('*' * width)
Параметрические переменные тут height, width. Внутри функции объявляется одна локальная переменная i.'''

'''Функция с возвратом значения
Когда функция с возвратом значения завершается, она возвращает значение в ту часть программы, которая ее вызвала. 
Возвращаемое из функции значение используется как любое другое: оно может быть присвоено переменной, выведено на экран, 
использовано в математическом выражении (если это число) и т. д.'''

'''При изучении вещественных чисел мы решали задачу о переводе градусов по шкале Фаренгейта в градусы по шкале Цельсия
Напишем функцию, которая осуществляет перевод:'''
# def convert_to_celcius(tmp):
#     result = (5 / 9) * (tmp - 32)
#     return result
'''Задача этой функции — принять одно число temp в качестве аргумента – количество градусов по шкале Фаренгейта, и 
вернуть другое — количество градусов по шкале Цельсия.
Рассмотрим ее работу. Первая инструкция в блоке функции присваивает значение (5 / 9) * (temp - 32) переменной result. 
Затем исполняется инструкция return, которая приводит к завершению исполнения функции и отправляет значение из переменной
result, назад в ту часть программы, которая вызвала эту функцию.'''
# функция перевода градусов Фаренгейта в градусы Цельсия
# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result

# основная программа
#temp = float(input('Bвeдитe количество градусов по Фаренгейту: ')) здесь сами вводим любое число
# celsius = convert_to_celsius(temp) можно функция приравнять к переменной
# print(celsius)  # градусы Цельсия  и принатнуть эту переменную
#print(convert_to_celsius(temp)) а можно сразу вызвать функцию в принте
'''Основная программа получает от пользователя одно число – значение в градусах Фаренгейта, и вызывает функцию, передавая
значение переменной temp в качестве аргумента. Значение, которое возвращается из функции convert_to_celsius, 
присваивается переменной celsius. '''

'''Использование инструкции return по максимуму
Взглянем еще раз на функцию convert_to_celsius():

def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result
Обратите внимание, что внутри этой функции происходят две вещи: во-первых, переменной result присваивается значение 
выражения (5 / 9) * (temp - 32), и во-вторых, значение переменной result возвращается из функции. Эта функция хорошо 
справляется с поставленной перед ней задачей, но ее можно упростить. Поскольку инструкция return возвращает значение 
выражения, переменную result устраняем и переписываем функцию так:

def convert_to_celsius(temp):
    return (5 / 9) * (temp - 32)
Эта версия функции не сохраняет значение (5 / 9) * (temp - 32) в отдельной переменной, а сразу возвращает значение 
выражения с помощью инструкции return. Делает то же, что и предыдущая версия, но за один шаг.'''

# def true_false(l, r): #допустим объявили функцию она принимает параметр n
#     return l < r  функц будет возвращать True или False по условию

# l = int(input()) перем для слева
# r = int(input()) перем для справа
# if true_false(l, r): вызываем результать функции прямо в условии
#     print('правда')
# else:
#     print('ложь')

'''Использование нескольких return
В одной функции может быть сколько угодно инструкций return. Рассмотрим функцию convert_grade(), которая переводит 
стобалльную оценку в пятибалльную:

def convert_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70: 
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1

# основная программа
grade = int(input('Введите вашу отметку по 100-балльной системе: '))
print(convert_grade(grade))
В функции convert_grade() используется 5 инструкций return. Каждая из них возвращает соответствующее значение и 
завершает работу функции.'''

'''В функции convert_grade() используется 5 инструкций return. Каждая из них возвращает соответствующее значение и 
завершает работу функции.
Функцию convert_grade() можно переписать с помощью одной инструкции return:

def convert_grade(grade):
    if grade >= 90:
        result = 5
    elif grade >= 80:
        result = 4
    elif grade >= 70: 
        result = 3
    elif grade >= 60:
        result = 2
    else:
        result = 1
    
    return result'''

'''Использование булевых функций для валидации входных данных
Булевы функции можно также использовать для упрощения сложного кода валидации входных данных. Например в программе, 
предлагающей пользователю ввести номер модели изделия, где возможны только значения 100, 200 и 300, можем написать 
такой код:'''
# model = int(input())
# while model != 100 and model != 200 and model != 300:
#     print('Номера моделей есть только 100, 200 и 300.')
#     model = int(input())
'''Цикл валидации использует длинное составное булево выражение, и повторяется до тех пор, покаmodel не будет равняться 
100 и 200 или 300. 
Можно упростить, написав булеву функцию проверки переменной model, и вызывая ее в цикле. Напишем функцию is_invalid(), 
которая принимает один параметр model и возвращает значение True, если модель недопустима и False в противном случае. 
Тогда цикл валидации можно переписать следующим образом:'''
# def true_model(model): объявили функц и передаем ей параметр model (глобальная переменная ввод данных)
#     return model != 100 and model != 200 and model != 300 возвращаем True пока ввод не равен 100, 200 или 300

# model = int(input())   глобальная переменная а при вызове функции это аргумент для функции
# while true_model(model): пока функция True а она True пока не введут допустимую модель
#     print('Номера моделей есть только 100, 200 и 300.') принтуем подсказку 
#     model = int(input()) даем еще раз ввести номер модели и это будет повторяться пока не введут допустимую модель

'''Функции с возвратом нескольких значений
В Python функции не ограничены возвратом всего одного значения. После инструкции return можно определить много выражений,
разделенных запятыми:

return выражение 1, выражение 2, выражение 3 ...
Следующий программный код определяет функцию get_powers(num), которая принимает в качестве аргумента число num и 
возвращает его квадрат, куб и четвертую степень.'''

# def get_powers(num):
#     return num ** 2, num ** 3, num ** 4 #прописываем разные действия с num через запятую важно количество действий
                                          #важно количество возвращаемых значений здесь их 3 запомни!
# a, b, c = get_powers(2) # при объявлени перемнной мы можем вызывать функцию и сразу запихивать в них возвращаемые               
# print(a, b, c, sep='\n') # значений НО! количество переменных и количество возвращаемых данных должны быть равны!

'''Рассмотрим еще один пример. Пусть требуется написать функцию, которая находит точку пересечения двух непараллельных 
прямых ax+by=e и cx+dy=f.
Программный код, решающий задачу, имеет вид:'''

# def solve(a, b, c, d, e, f):
#     x = (d * e - b * f) / (a * d - b * c)
#     y = (a * f - c * e) / (a * d - b * c)
#     return x, y

# xsol, ysol = solve(2, 3, 4, 1, 2, 5)
# print('Решением системы являются точки', 'x =', xsol, 'y =', ysol)
