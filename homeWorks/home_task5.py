
# palindrom = input('Введите строку палиндрома: ')
# # Сравнить первый символ с последним, второй с предпоследним и так далее, двигаясь к центру строки.
# if palindrom == palindrom[::-1]:
#     print("slovo palindrom")
# else:
#     print('vasha slovo ne yavlaetsa palindromom')
    
# 2) Подсчет слов:

# Программа должна принимать текст и слово. Напишите программу, которая подсчитывает количество слов в этом предложении.

# Так же вам нужно подсчитать количество введенного слова в этом тексте
# text = input('enter a sentence: ')
# slove = input('enter a word: ')
# print(len(text.split()))
# print(text.count(slove))


# 3) Генерация пароля:

# Напишите программу, которая генерирует случайный пароль заданной длины. Пароль должен содержать как буквы, так и цифры.

# from random import choice
# import string
# user = int(input('enter a leng password: '))
# list_= list(string.ascii_letters + string.digits)
# pas = ''
# for i in range(user):
#     symbol = choice(list_)
#     pas += symbol

# print(pas)

# 4) Поиск повторяющихся символов:

# Напишите программу, которая проверяет, есть ли в веденной строке повторяющиеся символы.
# user = input('enter a string: ')
# flag = 'net'
# for i in user: #hello
#     if user.count(i) > 1:
#         flag = 'povtorayshiesya est'

# print(flag)

# 5) Подсчет гласных и согласных:

# Введите строку, а затем напишите программу, которая подсчитывает количество гласных и согласных букв в ней.

# user = input('enter a sentence: ')
# g = 'auoiye'
# count_g = 0
# count_s = 0
# for i in user:
#     if i in g:
#         count_g += 1
#     else:
#         count_s += 1
# print(count_s)
# print(count_g)
