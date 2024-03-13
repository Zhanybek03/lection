# найти квадрат, куб, результат деления на 100 любых 3 чисел


# num = 5
# {'num': 5, '2':  25, '3': 125, '100': 0.05}

# num1 = 5
# num2 = 75
# num3 = 1154
# res  = {'num': num1, '2':  num1 ** 2, '3':  num1 ** 3, '100': num1 / 100}
# res2 = {'num': num2, '2':  num2 ** 2, '3':  num2 ** 3, '100': num2 / 100}
# res3  = {'num': num3, '2':  num3 ** 2, '3':  num3 ** 3, '100': num3 / 100}

# print(res, res2, res3, sep='\n\n')

# DRY - Don't Repeat Yourself

# def do_operations(num: int) -> None:
#     res = {'num': num, '2':  num ** 2, '3':  num ** 3, '100': num / 100}
#     print(res)

# do_operations(5)
# do_operations(75)
# do_operations(1154)


# ---------------------------
# Функция - это именнованная часть кода, которая содержит в себе определенный блок кода, и может вызываться в других частяях программы столько раз сколько угодно.

# def name_of_func(<a, b> параматеры функции):
#     <body> код, какая то логика которая будет давать конечный результат

#     # <return> опереатор который помогает сохранить результат 

# name_of_func(4, 6 #аргумент)

# параметры функции - данные которые мы передаем при вызове функции, они попадают в параметры по очередно

# аргумент функции - данные которые мы передаем при вызове функции, они попадают в параметры по очередно

# def isEven(num):
#     # print(True if num % 2 == 0 else False)
#     return True if num % 2 == 0 else False


# res = isEven(16)
# res1 = isEven(17)
# print(res, res1)

# def isEven(num: int) -> bool:
#     """Return True or False after cheking for even!""" # анатация
#     return True if num % 2 == 0 else False

# -----------------------------

# default параметры

# def sum_of_args(a: int, b: int, c: int=0) -> int: #c- необезательные параметры он всегда в конце
#     """Return sum of given arguments"""
#     try:
#         return a + b + c
#     except TypeError:
#         raise Exception('Invalid values for arguments!')
# print(sum_of_args(1, 2, 3))
# print(sum_of_args(5, 6, 4))
# # print(sum_of_args(5, 6, None))


#------------------------------------

# print(len('string'))
# from typing import Iterable

# def our_len(obj: Iterable) -> str:
#     """Возвращает длину интерируемого обьекта"""
#     i = 0
#     print(obj)
#     for _ in obj:
#         i += 1
#     print(f'result: {i}')


# our_len([1, 2, 3, 4, 5])
# our_len('string Hello world My name is John Snow')

# --------------------------------------

# 'Hello world! My name is John, Last name is Snow. Nice to meet you!'
# 


# def reverse_text(text: str) -> str:
#     """Reversing text"""
#     spisok = text.split()

#     return ' '.join(spisok[::-1])

# print(reverse_text('Hello world! My name is John, Last name is Snow. Nice to meet you!'))





