'''Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных функций min() и max() 
выводит те кортежи (каждый на отдельной строке), которые имеют минимальное и максимальное среднее арифметическое 
значение элементов.
Примечание. Используйте необязательный аргумент key.'''

# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# def average(num):
#     return sum(num) / len(num)
# print(min(numbers, key=average))
# print(max(numbers, key=average))

'''Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от начала 
координат (точки (0;0)). Программа должна вывести отсортированный список.'''

# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# def compare(x):
#     return (x[0]**2 + x[1]**2) ** 0.5
# print(sorted(points, key=compare))

'''Дан список numbers, содержащий кортежи чисел. Напишите программу, которая сортирует и выводит список numbers в 
соответствии с суммой минимального и максимального элемента кортежа.'''

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# def compare(x):
#     return min(x) + max(x)

# print(sorted(numbers, key=compare))

'''Сортируй как хочешь
Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
Напишите программу сортировки списка спортсменов по указанному полю:
1: по имени;
2: по возрасту;
3: по росту;
4: по весу.
Формат входных данных
На вход программе подается натуральное число от 1 до 4 – номер поля по которому требуется отсортировать список.
Формат выходных данных
Программа должна вывести отсортированный по заданному полю список в соответствии с примерами.
Примечание. Решите задачу без использования условного оператора.'''

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# def compare(el):
#     return el[n-1]
# n = int(input())
# for i in sorted(athletes, key=compare):
#     print(*i, end='\n')

# s = input().split()  разные варианты создания списков   вариант 1
# d = list(input())                                       вариант 2
# print(s)
# print(d)