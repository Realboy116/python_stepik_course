#Области видимости 1 локальные переменные
# def s(): # это фунция
#     # local это локальные переменные (после того как функция отработает эти переменные удаляются)
#     a, b, c = 1, 2, 3 # переменные существуют только в момент вызова функции
#     print(a, b, c)
    
# def q(): # из функци (любой) мы не можем обращаться к переменной из другой функции
#     r, t = 7, 5
#     print(r, t) # например мы не можем обратится к переменной "а" из функции s будет ошибка

# s() # так мы вызываем нашу функцию
# q()
# 2 Глобальные переменные
# def s(): # это фунция
#     # local это локальные переменные (после того как функция отработает эти переменные удаляются)
#     a, b, c = 1, 2, 3 # переменные существуют только в момент вызова функции
#     w = 'HELLO' # изменим перем 'w' внутри функции при принте из функции она измениться
#     print(a, b, c, w) # здесь обращаемся к глоб перем 'w' и она выводится в принте без ошибок
# # global
# w = 'hello' # к глобальной переменная будет доступна в любом месте нашего модуля (модуль может быть весь этот файл)
# y = 100 # вызывать переменную до того как она была объявлена (создана) нельзя будет ошибка
# print(w) # НО! при принте не из функции она остается такой же
# s()
# ПРимер 2
# def s():
#     print(w) #если мы будем принтовать переменную которой нет в этой функции то питон будет искать эту переменную
#     z, x, c = 5, 7, 9 # вне этой функции и если найдет то выведет ее
#     # w = 'njt' но если перем объявлена в функции и мы попытаемся ее вызвать выше (до объявления) будет ошибка!
#     print(z, x, c)
# w = 'this global variable' #то есть питон найдет это перем и обратиться к ней из функции, то из функции мы видим 
#                            # глобальные переменные
# s()
# ПРимер 3 
# def q(a, b, c):
#     a[1] = 222 # из функции мы можем изменить элемент списка глобальной переменной!
#     b = 22
#     #c = 33 если уберем одну локальную переменную то на принт перем "с" будет браться из глобал
#     print(a, b, c, 'local')
# a = [1, 2, 3, 4, 5]
# b = 200
# c = 300 
# q(a, b, c)
# print(a, b, c, 'global')
# ПРимер 4 (изменени глобальной переменной из функции)
# def s():
#     #local
#     global a # вот так можем менять значения глобальных переменных из функции
#     a = 999
# #global
# a = [4, 5, 6, 7, 8]
# s() # если не будет вызова функции то глобальная перменная не изменится
# print(a, 'global')
