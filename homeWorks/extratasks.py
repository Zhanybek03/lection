# """
# 1) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
# """
# list_ = [1, 2, 3, 4]
# res = 0
# for i in list_:
#     if type(i) == int:
#         res += i
# print(res)
# # """
# 2) Дан списка из чисел. Проверьте, что все числа больше трёх.
# """
# list_ = [1, 2, 3, 4]
# res = all(map(lambda x: x > 3, list_))
# print(res)

    


# """
# 3) Даны список из чисел. Проверьте, что в нём есть отрицательные числа.
# """
# ls = [1, 2, 3, -4]
# print(any(map(lambda x: x < 0, ls)))

# """
# 4) Дан список, состоящий из числами. Создайте новый список, состоящий из квадратов этих чисел.
# """
# ls = [2, 4, 5, 6, 7, 8, 9]
# newls = []
# res = (list(map(lambda x: x ** 2, ls)))
# newls.append(res)
# print(newls)

# """
# 5) Дан список с числами. Отфильтруйте этот список, оставив только чётные числа.
# """
# ls = [2, 4, 5, 6, 7, 8, 9]
# print(list(filter(lambda x: x if x % 2 == 0 else 0, ls )))

# """
# 6) Дан список, со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов.
# """

# ls = ['poppy', 'its getting', 'LOL']
# print(list(filter(lambda x: len(x) > 7, ls)))
# # """
# 7) Дан список list_ = [5, 6, 7, 8]. Выведите произведение всех этих чисел.
# """
# from functools import reduce
# list_ = [5, 6, 7, 8]
# print(reduce(lambda x, y: x * y, list_))


# """
# 8) Дан список, с числами. Посчитате количество чётных и нечётных чисел в этом списке.
# """
# ls = [23, 44, 55, 78, 90, 23]
# even = []
# odd = []
# for x in ls:
#     if x in ls % 2 == 0:
#         x.append(odd)
#     else:
#         x.append(even)
# print(even, odd)

# even_count = len(list(filter(lambda x: x % 2 == 0, ls)))
# odd_count = len(list(filter(lambda x: x % 2 != 0, ls)))

# print(even_count)
# print(odd_count)

# 9) Дан список list_ = [-1, 2, 3, 0, 5, -3, 7,]. Если число в списке меньше 0, замените его на False, если больше, то на True .
# """
# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# print(list(map(lambda x: x < 0, list_)))

# """
# 10) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
# """
# from functools import reduce
# names = ['Zhanybek', 'Elvira', 'Baktybek', 'Azamat', 'Akjol', 'Aichurok']

# longest_name = reduce(lambda x, y: x if len(x) > len(y) else y, names)
# print(longest_name)