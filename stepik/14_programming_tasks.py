'''Искомый месяц
Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en и 
number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.'''
# объявление функции
# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     if lan == 'ru':
#         return lng_ru[number - 1]
#     if lan == 'en':
#         return lng_en[number - 1]
# # считываем данные
# lan = input()
# num = int(input())

# # вызываем функцию
# print(get_month(lan, num))

# объявление функции
# def is_pangram(text):
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     for i in abc:
#         if i not in text.lower():
#             return False
#     return True

# считываем данные
# text = input()

# # вызываем функцию
# print(is_pangram(text))