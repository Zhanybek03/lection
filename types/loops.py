# while <expression>:
#     <body>
# i = 0
# while 'string':
#     print(f'srabotala: {i} raz!')
#     i += 1 #increment


# i = 0
# while i < 10:
#     i += 1
#     print(f'Цикл сработал {i} раз!')


# ls = list(range(1, 51))
# ls.reverse()
# print(ls)
# while ls:
#     print(ls.pop())

# user = {'username': 'JohnSnow', 'password': 'ilovepython123'}
# i = 3
# password = None
# while password != user['password']:
#     password = input(f'{user["username"]} vvedite parol: ')
#     i -= 1
#     if i == 0:
#         print('Vy Zablokirovany!')
#         break
# else:
#     print(f'Vy uaspeshno zashli na Sait {user["username"]}')
#__________________________________________________________


# user = {'username': 'JohnSnow', 'password': 'ilovepython123'}
# i = 3
# while password := input(f'{user["username"]} vvedite parol') != user["password"]:
#     i -= 1
#     if i == 0:
#         print('Vy Zablokirovany!')
#         break
# else:
#     print(f'Vy uaspeshno zashli na Sait {user["username"]}')


# i = 0
# while i < 15:
#     i += 1
#     print(i)

# _______________________________________________________
# for <variable> in <iterable object>:
#     <body>

# range(1, 5) -> 1, 2, 3, 4, 5
# 'string' -> s t r i n g
# [1, False, 3, None, 5] -> 1, False, 3, None, 5
# 15 -> ----
# True -> ----

# i = iter('String')
# print(i)
# print(next(i)) # S
# print(next(i)) # t




# str1 = 'string'
# for x in str1:
#     if x == 'r':
#         continue
#     print(x)

# else:
#     print('The end')

# ls = ['Tirion', 'John', 'Sansa', 'Jamie', 'Eddart']
# for x in ls:
#     if x == 'Sansa':
#         continue
#     print(f'Hello mr/mrs {x}!')


# число 100
# надо найти все делители числа
# a = 1000_000_000_00
# b = int(a ** 0.5)
# d = []
# for i in range(1, b + 1):
#     print(i)
#     if a % i == 0:
#         d.extend({i, a // i})
# d.sort()
# print(d)


#___________________________________________
# import random
# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Besh-Barmak']
# p = m = k = l = b = 0
# for i in range(1000_000):
#     meal = random.choice(ls)
#     if meal == 'Plov':
#         p += 1
#     elif meal == 'Manty':
#         m += 1
#     elif meal == 'Kuurdak':
#         k += 1
#     elif meal == 'Lagman':
#         l += 1   
#     else:
#         b += 1
# print('Результат голодных игр:')
# dict_ = {'Plov': p, 'Besh-Barmak': b, 'Kuurdak': k, 'Lagman': l, 'Manty': m}
# print(dict_)





i = 1
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stop = False
while i < 10:
    if stop:
        break
    for x in ls:
        print(x, '1111')
        if x == 5 and i == 5:
            stop = True
    print(i, '!!!!!!!!!!!!!!!!!')
    i += 1