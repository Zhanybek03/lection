# """
# Задания по comprehensions.
# """
# """
# 0) Мурат с друзьями на выходных решил собраться и пойти в ночной клуб.
# Но в ночной клуб пропускают только тех, кому 17+.
# Мурату - 24 года, Эржану - 21 год, Карине - 24 года, Алтынай - 17 лет, Айбеку - 16 лет.

# dict1 = {
#     'Мурат': 24,
#     'Erjan': 21,
#     'Karina': 24,
#     'Altynai': 17,
#     'Aibek': 16,

# }
# for key, value in dict1.items():
#     age = input('enter your name: ')
#     if dict1[age] > 17:
#         print(f'you can enter mr/mrs {key}')
#     else:
#         raise ValueError('Go home you are not 17!!!')
    

# Напишите программу, которая определяет кого пустить в ночной клуб, а кого нет. (работа со словарем)
# """

# """
# Задание 0.1
# Запросите у пользователя число от 1 до 10 в переменную n. Затем пройдитесь по промежутку чисел от 1 до 500(включительно) и запишите в словарь dict_, только те числа, которые кратны числу n (делятся на число n без остатка), введенное пользователем. Ключом будет само число, а 
# значением его квадрат.
# """
# user = int(input('Vvedite chislo ot 1 do 10: '))
# dict_ = {}
# for i in range(1, 501):
#     if i % user == 0:
#         dict_[i] = i**2
# print(dict_)

        

    






# """
# 1) Создайте список из целых чисел от 1 до 100.
# """
# ls = list(range(1,101))
# print(ls)    
# """
# 2) Создайте список из нечётных целых чисел в промежутке от 1 до 50.
# """
# ls = []
# for x in range(0, 50):
#     if x % 3 == 0:
#         ls.append(x)

# print(ls)

# comprehensions---------------


# ls = [x for x in range(0, 50) if x % 3 == 0]
# print(ls)
# """
# 3) Создайте список используя int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4] и запишите в новый список только четные числа, которые больше нуля.
# """
# int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# new_list = []
# for i in int_list:
#     if i % 2 == 0 and i > 0:
#         new_list.append(i)

# print(new_list)

# """
# 4) Создайте список из квадратов всех чисел от 1 до 25 (включительно).
# """

# ls = []
# for x in range(1, 26):

#     print(x**2)

# """
# 5) Объявите новый список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] и конвертируйте строковые данные в целочисленные.

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# """
# # писать код здесь
# """
# 6)  Пройдитесь по промежутку чисел от 1 до 10 (включительно), если число нечётное, запишите в список само число, если же чётное, то квадрат этого числа.
# """
# # писать код здесь
# """
# 7) Пройдитесь по промежутку чисел от 1 до 10 и запишите в список True, если число чётное и False в противном случае.
# """
# # писать код здесь
# """
# 😍 Создайте список из 10 произвольных имён, затем пройдитесь по данному списку и если имя состоит меньше чем из 4 букв замените имя на 'shorter', а если больше на 'longer'.
# """
# # писать код здесь
# """
# 9) Дан словарь, в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам. Замените оценки названием предмета, по которому студент имеет высший балл. Например: a = {'John': {'history': 90, 'math': 95, 'literature': 91}, 'Rose': {'history': 92, 'math': 96, 'literature': 81}, 'Kelly': {'history': 84, 'math': 85, 'literature': 87}}
# -Результат: {'John': 'math', 'Rose': 'math', 'Kelly': 'literature'}
# """
# # писать код здесь
# """
# 10) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Например: 
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} #-> #{'first': 1, 'second': 2}
# """


my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
d = my_dict.fromkeys(['first', 'second'], 75 )
print(d)