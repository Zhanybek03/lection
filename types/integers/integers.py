# -
# num1 = int(input('enter first num1: '))
# num2 = int(input('enter second num2: '))
# print(num2, '-', num1, '=', num2 - num1)

# *
# num1 = int(input('enter first num1: '))
# num2 = int(input('enter second num2: '))
# print(num2, '*', num1, '=', num2 * num1)

# / and // and %
# - / обычное деление
# - // деление без остатка 
# - % модульное деление

# num1 = 17
# num2 = 5
# print('/', num1 / num2,)
# print('//', num1 // num2,)
# print('%', num1 % num2,)


# ** -> возведение в степень
# print(77 ** 100)

# print(36 ** 0.5)   квадратный  корень числа 


# pow -> возведение в степень
# pow(num1, num2,<mod>)
# print(pow(5,2))
# a = 6 
# c = 3
# res = pow(a, c, 50)
# print(res)

# abs() - абсолютное значение числа -> abs(-5) -> 5
# ------------------------------------- |-5| -> 5

# a = abs(-14)
# b = abs(15)
# c = abs(-2.5)
# print(a, b, c)


# round() - округление число с плавающей точкой
# a = 6.6
# print(round(a))

# b = 7.368232
# print(round(b,))

# divmod(a, b) - она выводить два числа первое число это результат целого деления(//) а второе это модульное деление чисел  a and b
# print(divmod(22, 5))
# import math
# a = 5
# print(round(math.sqrt(5),1))

# Множественное присваивание
# a = 'Milk'
# b = 'Water'
# c = None
# c = b
# b = a
# a = c
# print(a, b)


# a = 'Milk'
# b = 'Water'
# a, b = b, a
# print(a, b)

# num1, num2, num3 = input('num1: '), input('num2: '), input('num3: ')
# print(num1)
# print(num2)
# print(num3)

# import math
# katet1 = 5
# katet2 = 6
# res = math.sqrt(katet1 ** 2 + katet2 ** 2)
# print(round(res, 2))

"""
16) Дана переменная с радиусом окружности, найдите периметр и площадь окружности, результат выведите в терминал
"""

# from math import pi
# r = int(input('Vedite radius: '))
# resP = 2 * r * pi
# resS = r ** 2 * pi
# print('S okruzhnosti: ', round(resP, 2))
# print('P okruzhnosti: ', round(resS, 2))

# from random import randint
# num = randint(1, 10)
# print(num)
# i = 0
# while i < 3:
#     guess = int(input('Guess the number: '))
#     if guess == num:
#         print(
#             'You won!'
#         )
#         i = 3
#     i += 1