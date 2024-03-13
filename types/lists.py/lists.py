bi# Индексация в списках
# ls = [1,2, 3, 4, 5,'String', [[1, 2, 3],True, False, None], 5]
# print(ls, len(ls))
# print(ls[5], ls[-1])
# print(ls[6][0][0])
# print(ls[3:6])

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# ls = range(1, 11)
# for num in ls:
#     print(num)
# ls = ['John', 'Sansa', 'Tirion', 'Eddart', 'Jamie']
# for x in ls:
#     print(f'Hello mr/mrs {x}! Welcome to the club!')
# for num in range(1, 21):
#     if num % 2 == 0 :
#         print(f'Число {num} четное число квадрат: {num ** 2}')
#     else:
#         print(f'Число {num} нечетное число куб: {num ** 3}')
 

# ---------------------------------


# методы списков
# print(dir(list))
# append(element) - Добовляет елемент в конец списка
# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('Hello world')
# ls.append([True, False])
# print(ls)

# extend('контейнер') - расширяет список
# ls = [1, 2, 3]
# ls.append('Hello world')
# print(ls)
# ls.extend('Hello world')
# ls.extend([True, False])
# print(ls)

# ls = [1, 2, 3]
# ls1 = [4, 5, 6]
# print(ls + ls1)

# sort() - сортирует списокб если передать reverse = True, 
# то список отсортируется в убывающем порядке
# from random import randint

# ls = []
# for x in range(1, 101):
#     num = randint(1,100)
#     ls.append(num)

# print(ls)
# ls = list(set(ls))
# ls.sort(reverse= True)
# print('After:\n', ls, len(ls))

# insert(index, element) - добавляет элемент по указанному index
# ls = ['string', 2, 3, False]
# ls.insert(1, 1)
# ls.insert(4, 'Hello world')
# print(ls)
# remove(element) - удаляет element из списка если такого нет то выводится ошибка
# pop([index]) - удаляет и возврощяет элемент из списка по index, но если index не передать, то удоляет последний элемент
# ls = [5, 1, 2, 4, 5, 5, 5]
# print(ls)
# ls.pop()
# ls.pop(0)
# print(ls)
# ls.remove(5)
# print(ls)
# while 5 in ls:
#     ls.remove(5)

# print(ls)

# ls = [1, 2, 3]
# deleted = ls.pop()
# print(ls)
# print(deleted)

# update -__________________---
ls = [1, 2, 'T', 4, 5, 6, None, 8]
ls[2] = 3
print(ls)
i = ls.index(None)
ls[i] = 7
print(ls)
print(ls)
