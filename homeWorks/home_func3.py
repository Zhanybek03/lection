# # 1) Создайте функцию, которая генерирует рандомное (случайно сгенерированное) число и выводит на окно терминала через команду print(). Далее создайте декоратор, который журналирует это событие. То есть функция декоратор должна писать в dict() предложение: «Функция …………… была запущена успешно», а ключом будет уникальный идентификатор (id).   (10 баллов)

# from random import randint

# # def random_():
# #     def wrapper(*args, **kwargs):
# #         print()
# #         random_()
# #     return wrapper

# # print(random_())


# def decor(func):
#     def wrapper(*args, **kwargs):
#         print(f'функция {func.name} была вызвана успешно {func()}')


#     return wrapper


# @decor
# def random_num():
#     random_id = randint(1, 12423423)
#     # print(random_id)
#     return random_id

# random_num()






# # # 2) Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
# # # Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- FYI и т.п. (10 баллов)



# # user = input('Введите что-нибудь я сокращy: ').upper().split()
# # def phrase(word):
# #     ls = []
# #     for i in word:
# #         ls.append(i[0])

# #     return ''.join(ls)
# # print(phrase(user))

        

    
# # # 3) '''Напишите декоратор, который проверяет, что функция вызывается с определенными типами аргументов.''' (15 баллов)
# # def decor(func):
# #     def wrapper(*args, **kwargs):
# #         try:
# #             print(func(*args, **kwargs))
# #         except:
# #             print('Вы ввели аргументы разного типа данных!')
# #     return wrapper




# # @decor
# # def func(a, b, c):
# #     return a + b + c

# # func(2, 3, 4)



# # # 4) '''Создайте декоратор, который автоматически преобразует результат функции в другой тип данных,''' (15 баллов)

# # def decor(func):
# #     def wrapper(*args, **kwargs):

# #         print(type(func(*args, **kwargs)))
# #         return (type(str(func(*args, **kwargs))))

# #     return wrapper

# # @decor
# # def func(a, b, c):
# #     return a + b + c

# # print(func(2, 3, 4))



# # # 5) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.''' (20 баллов)


# def decor(func):
#     counter = 0
#     def wrapper(*args, **kwargs):
#         nonlocal counter
#         if counter < 3:
#             print(func(*args, **kwargs))
#             counter += 1

#         else:
#             print('Макс количество функций вызвано!')

#     return wrapper

# @decor
# def func(Alihan, Aigerim, Aisulu):
#     return Alihan * Aigerim // Aisulu

# func(12, 34, 67)
# func(12, 34, 67)
# func(12, 34, 67)
# func(12, 34, 67)



# # 6) '''Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции.''' (15 баллов)

# def decor(func):
#     def wrapper(*args, **kwargs):
#         try:
#             print(func(*args, **kwargs))
#         except:
#             print('Вы ввели некоректный аргумент! ')
#     return wrapper

# @decor
# def func(q, r, s):
#     return q + r // s
# func(2, 8, 0)



# # 7) '''Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям.''' (15 баллов)

# def decor(func):
#     dostup = ['Alihan', 'Janybek', 'Anvar', 'Abdulla']
#     def wrapper(*args, **kwargs):
#         name = input('Введите ваше имя: ')
#         if name in dostup:
#             return func(*args, **kwargs)
#         else:
#             return 'Доступ запрещен!'
            
#     return wrapper


# @decor
# def func(a, v, b):
#     return a + v + b

# print(func('John ', 'Snow ', 'sfdfds!'))