# Стройные функции
# zip(iterables) - она соединят каждый элемент итерируемых обьектов между собой в тип данных tuple и возвращает итератор

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300, 123]
# ls3 = ['hello', 'world', 'John']


# result = zip(ls1, ls2, ls3)
# print(list(result))
# for x in result:
#     print(x)

# -----------------
# all(), any()
# all(iterable) - Возвращает True, если все элементы интереруемого обьекта истина, иначе False
    
# ls = [[1,2], -5, 'stroka', 1]
# print(all(ls))

# # For example:
# ip1 = '14.543.45.234'
# ip2 = '12.343.5y.464'

# result = all(x.isdigit() for x in ip1.split('.'))
# print(result)

# result2 = all(x.isdigit() for x in ip2.split('.'))
# print(result2)


# any - Возвращает True, если хотябы один из эленментов истина

# ls = [0, 0, '', None, [], 1]
# print(any(ls))


# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']

# command = input('Vvedite commands: ')
# if any(x in command for x in ignore):
#     raise Exception('You dont\'t have perissions')

# print('Ok!')


# ----------------

# Анонимные функции - Lambda(Обычные функции только без названия)

# lambda фунция могуть принимать сколько угодно аргументов, но всегда возвращает одно вырожение

# def sum_of_args(a, b):
#     return a + b 
# print(sum_of_args(5, 6))

# func = lambda a, b: a + b
# print(func(25, 5))


# когда исп lambda

# def myFunc(n):
#     return lambda num: num * n
#     # def result(num):
    #     return num * n
    
    # return result

# myDoubler = myFunc(2)
# myTripler = myFunc(3)

# print(myDoubler(50))
# print(myDoubler(34))
# print(myDoubler(10000000000))

# print(myTripler(2134))
# print(myTripler(36))
# print(myTripler(353))


# dict_ = {'John': 1_000_000, 'Jamie': 100, 'Din': 10_000, 
#          'Anvar': 500, 'San': 100_000}

# res = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
# print(res)

# enumerate - она пронумерозывает каждый элемент внутри iterable, уу собственным индексом


# ls = ['hello', 'world', 'Don', 'Leanardo', 'Sam', 'Winchesters']
# print(ls)
# for i, x in enumerate(ls):
#     print(f'Index: {1}, Element: {x}')
# res =  list(enumerate(ls))
# print(res)

# map(function, itrable) -> применяет, функцию которую мы передаем ко всем элементам iterable

# ls = ['One', 'Two', 'three', 'Anvar' ,'King']
# res = list(map(str.upper,ls))
# print(res)
# names = ['John', 'Sultan', 'Anvar', 'Din', 'Sam']
# res = list(map(
#     lambda name: f'Hello mr/mrs {name}!', names
# ))
# print(res)

# dict_ = {1: 2, 3: 4, 5: 6}
# #----> {1: '2', 3: '4', 5: '6'}
# print(dict_)
# res = dict(map(
#     lambda x: (x[0], str(x[1])), dict_.items()
# ))
# print(res)

# filter -(function, iterable) -> применяет ко всем элементам iterable функции которую мы передали и возвращает итератор с теми элементами для которых функции вернула True
# ls = ['one', 'two', '', 'list', '100', '12', 'din']
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)
# print(res)
# res = list(filter(str.isdigit, ls))
# print(res)

# ls = ['john', 'codify', 'aibek ', 'ono ', 'bootcam', 'Kyrgyzstan', 'mountains'] # > 5
# res = list(filter(lambda x: len(x) > 5, ls))
# print(res)


# ls = [
#     {'name': 'Python', 'point': 10},
#     {'name': 'C++', 'point': 6},
#     {'name': 'JS', 'point': 8},
#     {'name': 'JAVA', 'point': 3},
#     {'name': 'C#', 'point': 9},

# ]

# res = list(filter(
#     lambda dict_:dict_['point'] > 8, ls
# ))
# print(res)

# users = [
#     {'username': 'Din', 'comments': ['I love u!', 'so gorgeous!']},
#     {'username': 'Raychel', 'comments': []},
#     {'username': 'Steven', 'comments': ['Bishkek, Python']},
#     {'username': 'Sam', 'comments': []},
#     {'username': 'Kira', 'comments': ['The best post']},

# ]

# actiev_users = list(filter(
#     lambda obj: obj['comments'], users


# ))

# inactiev_users = list(filter(
#     lambda obj: not obj['comments'], users
# ))
# print(actiev_users)
# print()
# print(inactiev_users)

# -------------------------

# names = ['Rychal', 'Sultan', 'Aigerim', 'John', 'Kira', 'Bob']

# res = list(map(
#     lambda x: f'Hello Mr/Mrs {x}', filter(lambda x: len(x) > 5, names)
# ))
# print(res)

# Функция Reduce () принимает функцию и последовательность и возвращает одно значение, рассчитанное следующим образом:
# 1. Первоначально функция вызывается с первыми двумя элементами из последовательности, и результат возвращается.
# 2. Затем функция вызывается снова с результатом, полученным на шаге 1, и следующим значением в последовательности. Этот процесс повторяется до тех пор, пока в последовательности не закончатся элементы.


# from functools import reduce 

# ls = [1, 2, 3, 4, 5]
# sum_ = reduce(lambda x, y: x + y, ls)
# res = reduce(lambda a, b: b * a, ls)
# print(sum_, res)

# ------------------------------


# from itertools import repeat
# from random import choices
# from string import ascii_letters, digits
# from statistics import mean

# symbols = '_()$!%-@#'
# q_pass = int(input('Введите колличество паролей: '))

# result = { 
#     f(choices(ascii_letters, k=10),
#       choices(digits, k=5),
#       choices(symbols, k=2))
#     for f in repeat(
#         lambda a, d, s: ''.join(set(a+d+s)), q_pass)

# }
# print(result)
# print(f'Quantity of passwords: {len(result)}')
# dlina = [len(x) for x in result]
# print(f'Average len: {mean(dlina)}')