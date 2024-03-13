# 1) Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра.

# def func():
#     counter_upper = 0
#     counter_lower = 0 
#     user = input('Введите что-нибудь: ')
#     for i in user:
#         if i.isupper():
#             counter_upper += 1
#         elif i.islower():
#             counter_lower +=1
#     return f'Upper: {counter_upper}, Lower: {counter_lower}'
# print(func())

# 2) Напишите функцию, которая принимает число n и генерирует словарь, чьи ключи состоят из чисел от 1 до n, а их значения -- куб ключей. Пример: передано число 5. В результате должны получить словарь {1: 1, 2: 8, 3: 27, 4: 64}
# chel = int(input('Enter the a number: '))
# dict_ = {}
# def dictionary(n):
    
#     for i in range(1, n):
#         dict_[i] = pow(i, 3)
#     return dict_
    
# print(dictionary(chel))




# 3) Напишите функцию sum_range(start, end), которая суммирует все целые числа
#     от значения «start» до величины «end» включительно. Если пользователь задаст
#     первое число большее чем второе, просто поменяйте их местами.

human = int(input('Enter your first number Moron: '))
human2 = int(input('Enter your second number dude: '))
def sum_range(start, end):
    counter = 0
    if start > end:
        for i in range(end, start):
            counter += i
    else:
        for i in range(start, end):
            counter += i
    return counter
print(sum_range(human, human2))

        