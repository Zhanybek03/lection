# """
# 1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
# """
# def chislo(a, b):
#     return a + b

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(chislo(a, b))



# """
# 2) Создайте функцию, которая будет принимать строку. Функция должна выводить длину этой строки(не использовать функцию len).
# """
# def stroka(j):
#     count = 0
#     for _ in j:
#         count += 1
#     return count
    
# print(stroka("Hello"))




# """
# 3) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
# """




# def func(x, y):
#     print("func:", type(x)) 
#     print("func:", type(y))
# print_func = func(10, "Loop")


# """
# 4) Создайте функцию, которая должна принимать 2 числа и возвращать результат их деления.
# """
# def sum(num1, num2):
#     return num1 // num2 
    
# num1 = int(input("Ввeдите первое число:" ))
# num2 = int(input("Ввeдите второе число:" ))
# print(sum(num1, num2))



# """
# 5) Создайте функцию, которая принимает словарь. Пройдитесь по словарю циклом и распечатайте все его ключи
# """
# def dict(dictionary):
#     for key in dictionary:
#         print(key)

# dict({'Men':'49', 'Women': '51'})



# """
# 6) Создайте функцию, которая принимает и выводит "It's odd number" если это число не кратно двум и "It's even number" в противном случае.
# """

# def number(num):
#     if  num % 2 == 0:
#         print("It's even number")
#     else:
#         print("Fuck off")

# user = int(input("Введите число не кратно двум: "))

# number(user)  


# """
# 7) Напишите функцию, которая будет принимать строку и проверять является ли она палиндромом. Пробелы и регистр учитывать не нужно.
# (Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.)
# """
# def palindrom(j):
#     return j == j[::-1]

# j = input("Ввeдите строку: ")
# print(palindrom(j))

# """
# 8)  Создайте функцию которая принимает от пользователя два числа. Она должна сравнить эти числа между собой и вывести максимальное значение.
# """

# def max_number(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число; "))
# print(max_number(num1, num2))




# """
# 9) Напишите функцию, которая принимает список чисел и возвращает их произведение.
# # """
# def composition(num):
#     count = 1
#     for i in num:
#         count *= i
#     return count

# num = [1, 45, 67, 89]
# print(composition(num))


# """
# 10) Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр. Например, число 123 --> 6
# """

# def sum_numbers(num):
#     # integer = int(input("Enter an integer number: "))
#     integer = 0
#     for i in num:
#         integer += int(i)
#     return integer
# num = input('vvedte chislo')
# print(sum_numbers(num))