'''Обратный порядок 1
Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.
На вход программе подается одно натуральное число.
Программа должна вывести цифры введенного числа в столбик в обратном порядке.'''
# n = int(input())       1 ввод числа
# while n != 0:          цикл выполняется пока n не равно 0
#     l = n % 10         находим последнюю цифру
#     print(l)           выводим последнюю цифру
#     n = n // 10        удаляем последнюю цифру
'''max и min
Дано натуральное число (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.
На вход программе подается одно натуральное число.
Программа должна вывести максимальную и минимальную цифры введенного числа (с поясняющей надписью).'''
# n = int(input())
# s = str(n)
# print('Максимальная цифра равна', max(s))
# print('Минимальная цифра равна', min(s))
'''Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:
сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
На вход программе подается одно натуральное число.
Программа должна вывести значения указанных величин в указанном порядке.'''
# n = int(input()) изменяемая переменная в цикле
# n2 = n         неизменяемая переменная (цикл ее не трогает)
# counter = 0      счетчик
# counter2 = 0     счетчик
# counter3 = 1     счетчик
# while n != 0:    пока в числе есть цифры
#     s = n % 10      определяем последнюю цифру на каждой итерации
#     counter += s     "сумму его цифр"
#     counter2 += 1     "количество цифр в нем"
#     counter3 *= s      "произведение его цифр"
#     counter4 = counter / counter2  "среднее арифметическое его цифр"
#     n = n // 10        убираем последнюю цифру числа на каждой итерации
#     counter5 = n2 // 10 ** (counter2 - 1)   "его первую цифру"
#     counter6 = n2 % 10 + counter5            "сумму его первой и последней цифры"
# print(counter, counter2, counter3, counter4, counter5, counter6, sep='\n')
'''Вторая цифра
Дано натуральное число (n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.
Программа должна вывести его вторую (с начала) цифру.'''
# n = int(input())   здесь понятно ввод
# while n > 9:       здесь цикл считает нам пока число двузначное то есть больше 9 (от 10 и до бесконечности)
#     n1 = n % 10    здесь щипаем вторую цифру от 2-х значного числа оно остается двузначным из за строчки ниже
#     n = n // 10    здесь "убирается последняя цифра" что бы число всегда было двузначным
# print(n1)
'''Одинаковые цифры
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
На вход программе подается одно натуральное число.
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.'''
# n = int(input())                вводим любое число
# last_digit1 = n % 10                   тут последняя цифра (вне цикла!) она постоянная и не меняется это важно!
# same_n = True                   сигнальный флаг!
# while n != 0:                   условие цикла
#     last_digit2 = n % 10               тут последняя цифра (в цикле!) она меняется с каждой итерацией!
#     if last_digit1 != last_digit2:     сравниваем меняющююся и неменяющююся последние цифры на каждой итерации
#         same_n = False                 если различаются то флаг изменится
#     n = n // 10                        убираем последнюю цифру на каждой итерации
# if same_n == True:                     если цифры одинаковые то флаг не изменится соответственно YES
#     print('YES')
# elif same_n == False:                  если цифры не одинаковые то флаг изменится соответственно NO
#     print('NO')
'''Упорядоченные цифры 🌶️
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре 
справа налево упорядоченной по неубыванию.
На вход программе подается одно натуральное число.
Программа должна вывести «YES» если последовательность его цифр при просмотре справа налево является упорядоченной по 
неубыванию и «NO» в противном случае.'''
# n = int(input())              Проверяем рядом стоящие цифры: если порядок нарушен, меняем сигнальную метку.
# flag = 'YES'                  Если дошли до конца, то есть рассмотрели все цифры числа и сигнальная метка
# l_d1 = n % 10                 не поменялась, то цифры числа упорядочены:
# while n != 0:
#     l_d2 = n % 10
#     if l_d1 > l_d2:
#         flag = 'NO'
#     else:
#         l_d1 = l_d2
#     n = n // 10
# print(flag)