# EXTRA


# 1) '''Магическими называются даты, в которых произведение дня и месяца
# составляет последние две цифры года. Например, 10 июня 1960 года –
# магическая дата, поскольку 10 ´ 6 = 60. Напишите функцию, определя-
# ющую, является ли введенная дата магической. Используйте написан-
# ную функцию в главной программе для отображения всех магических
# дат в XX ве­ке.'''





# #

# 2) '''Напишите функцию для определения количества дней в конкретном ме-
# сяце. Ваша функция должна принимать два параметра: номер месяца
# в виде целого числа в диапазоне от 1 до 12 и год, состоящий из четырех
# цифр. Убедитесь, что функция корректно обрабатывает февраль високос-
# ного года. В основной программе запросите у пользователя номер месяца
# и год и отобразите на экране количество дней в указанном месяце.'''
# def decor(func):
#     def wrapper(*args, **kwargs):
#         while True:
#             months = int(input('Ввыберите то 1 до 12 месяц года: '))
#             years = int(input('Введите год: '))
#             print(f'Year: {years}')
#             if months == 1:
#                 print("January 31 days")
#             elif months == 2:
#                 print("Febuary 28 or 29 days")
#             elif months == 3:
#                 print("March 31 days")
#             elif months == 4:
#                 print("April 30 days")
#             elif months == 5:
#                 print("May 31 days")
#             elif months == 6:
#                 print("June 30 days")
#             elif months == 7:
#                 print("July 31 days")
#             elif months == 8:
#                 print("August 31 days")
#             elif months == 9:
#                 print("September 30 days")
#             elif months == 10:
#                 print("October 31 days")
#             elif months == 11:
#                 print("November 30 days")
#             elif months == 12:
#                 print("December 31 days")
#             else:
#                 print("Нужно выбирать от 1 до 12")
#                 continue
#     return wrapper
# @decor
# def func(month, year):
#     return month, year
# func(2, 2024)
# #

# 3) '''Напишите две функции с именами hex2int и int2hex для конвертации
# значений из шестнадцатеричной системы счисления (0, 1, 2, 3, 4, 5, 6, 7,
# 8, 9, A, B, C, D, E и F) в десятичную (по основанию 10) и обратно. Функ-
# ция hex2int должна принимать на вход строку с единственным символом
# в шестнадцатеричной системе и преобразовывать его в число от нуля
# до 15 в десятичной системе, тогда как функция int2hex будет выполнять
# обратное действие – принимать десятичное число из диапазона от 0 до
# 15 и возвращать шестнадцатеричный эквивалент. Обе функции должны
# принимать единственный параметр со входным значением и возвращать
# преобразованное число. Удостоверьтесь, что функция hex2int корректно
# обрабатывает буквы в верхнем и нижнем регистрах. Если введенное поль-
# зователем значение выходит за допустимые границы, вы должны вывести
# сообщение об ошибке.'''




# #

# 4) '''Представьте, что в вашем регионе устаревшим является формат номер-
# ных автомобильных знаков из трех букв, следом за которыми идут три
# цифры. Когда все номера такого шаблона закончились, было решено об-
# новить формат, поставив в начало четыре цифры, а за ними три буквы.
# Напишите функцию, которая будет генерировать случайный номерной
# знак. При этом номера в старом и новом форматах должны создаваться
# примерно с одинаковой вероятностью. В основной программе нужно сге-
# нерировать и вывести на экран случайный номерной знак.'''

# #dailyreport
# from string import ascii_letters, digits
# from random import choices


# def decor(func):
#     def wrapper(*args, **kwargs):
#         old_number = ''.join(choices(ascii_letters, k=3)).upper()+ ''.join(choices(digits, k=3))
#         new_number = ''.join(choices(digits, k=4))+ old_number[:3]
#         print(f'old number: {old_number}')
#         print(f'new number: {new_number}')
#     return wrapper

# @decor
# def func(old, new):
#     return 'old_number, new_number'
# func(34, 56)


# ---------------------------------------------

# 1)Дано: переменная digits = '123456789'



# Функция для получения суммы цифр числа
# digits = '123456789'
# def getSum(n):
    
#     sum = 0
#     for digit in digits: 
#       sum += int(digit)      
#     return sum
   
# print(getSum(sum))
# Результат
# Необходимо вывести сумму цифр, представленных в виде одного строкового значения '123456789'. Сумма этих цифр составляет 45. Напишите код, который выдаст эту её.
# Подсказка: используйте генератор списка, функцию int(), функцию sum() для суммирования списка, состоящего из чисел.

# 2) напишите лямбда функцию
# которая принимает одно число, и возводит его в квадрат

# def func(n):
#     return n ** 2
# user = int(input('Enter your namber: '))  
# print(func(user))
 
# print(list(map(lambda x: x** 2, [int(input('enter you number: '))])))


# 3) напишите лямбда функцию которая принимает 2 числа, первое число возводите в степень второго числа
# user1 = int(input('Enter your first number: '))
# user2 = int(input('Enter your second number: '))

# def func(num1, num2):
  
   
#   return lambda: num1 ** num2




# print(func(user1, user2))

# power_function = lambda x, y: x ** y

# result = power_function(2, 3)
# print(result) 



# print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


# 4) напишите лямбда функцию 

# которая принимает список имён, и функция должна приветствовать все имена (используйте функцию map)
# names = ['Zhanybek', 'Kanybek', 'Adinai', 'Omon']

# res = list(map(
#     lambda name: f'Hello mr/mrs {name}!', names
# ))
# print(res)


# 5) напишите лямбда функцию 
# которая принимает список чисел, и она будет фильтровать этот список,
#  то есть будет принимать только те числа которые делятся на 5, использовать встроенные функции filter, list


# ls = [5, 36, 25, 125, 225, 200, 34, 45, 69, 101020]
# res = list(filter(lambda x: x % 5 == 0, ls))
# print(res)