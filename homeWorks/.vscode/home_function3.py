# 1) Создайте функцию, которая генерирует рандомное (случайно сгенерированное) число и выводит на окно терминала через команду print(). Далее создайте декоратор, который журналирует это событие. То есть функция декоратор должна писать в dict() предложение: «Функция …………… была запущена успешно», а ключом будет уникальный идентификатор (id).   (10 баллов)

# from random import randint

# def decor(func):
#     def wrapper(*args, **kwargs):
#         print(f'функция {func.__name__} была вызвана успешно {func()}')


#     return wrapper


# @decor
# def random_num():
#     random_id = randint(1, 12423423)
#     # print(random_id)
#     return random_id

# random_num()






# 2) Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- FYI и т.п. (10 баллов)



# user = input('Введите что-нибудь я сокращy: ').upper().split()
# def phrase(word):
#     ls = []
#     for i in word:
#         ls.append(i[0])

#     return ''.join(ls)
# print(phrase(user))

        

    
# 3) '''Напишите декоратор, который проверяет, что функция вызывается с определенными типами аргументов.''' (15 баллов)

# def func(a, b, c):
#     def wrapper(*args):
#         print(a, b, c)
#     return wrapper
# @func
# def args():
#     check = ()
#     return check
# args('2', 3, 4)



# 4) '''Создайте декоратор, который автоматически преобразует результат функции в другой тип данных,''' (15 баллов)

# def authomatics()



# 5) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.''' (20 баллов)


# 6) '''Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции.''' (15 баллов)

 

# 7) '''Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям.''' (15 баллов) 


