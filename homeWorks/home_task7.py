# Задача 1. Сумма чисел (10 баллов)

# Напишите функцию summa_n, которая принимает одно целое положительное число N и выводит сумму всех чисел от 1 до N включительно. 7

# def summa_n(num):
#     count = 0
#     for i in range(1, num + 1):
#         count += i
#     return count

    
    
# while True:
    
#     sum = input("Введите одно целое положительное число: ")
#     if sum == 'Exit':
#         break
#     else:
#         print(summa_n(int(sum)))


# Пример работы программы:

# Введите число: 5

# Вывести сообщение: Я знаю, что сумма чисел от 1 до 5 равна 15

# Реализуйте через цикл while, для выхода из цикла пользователь должен ввести "выход" (5 баллов)

# Задача 2. Функция в функции (15 баллов)

# Асан проходит специальный тест по программированию. У него всё шло хорошо, пока он не наткнулся на тему «Функции». Задание звучит так:

# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода. Это вызов функции test(). В ней запрашивается на ввод целое число. Если оно положительное, то вызывается функция positive(), тело которой содержит команду вывода на экран слова «Положительное». Если число отрицательное, то вызывается функция negative(), её тело содержит выражение вывода на экран слова «Отрицательное».

# def test():
#     t = int(input('Введите целое число: '))
#     if t > 0:
#         print("positive")
#     elif t < 0:
#         print("negative")
#     return t
# print(test())

# Задача 3. Площади (15 баллов)

# Муниципалитет хочет построить необычный парк в одном из районов города. Власти остановились на трёх вариантах: изображение на карте в виде круга, прямоугольника или треугольника. Однако им также нужно понять, какую площадь будет занимать тот или иной вариант при разных значениях.

# Напишите программу, которая в зависимости от выбора пользователя вычисляет площадь круга, прямоугольника или треугольника. Для вычисления площади каждой фигуры должна быть написана отдельная функция. (Формулы нахождения площадей попробуйте найти в интернете)))


# def circle(r): # Круг
#     return 3.14 * r**2
# def rectangle(a, b): # прямоугольника
#     return a * b
# def triangle(a, b): # треугольника
#     return a * b / 2



# choice = input('Выбор 1-круг, 2-прямоугольника 3-треугольника: ')

# if choice ==  '1':
#     r = int(input('r: '))
#     print(circle(r))

# elif choice == '2':
#     a = int(input('a: '))
#     b = int(input('b: '))
#     print(rectangle(a, b))

# elif choice == '3':
#     a = int(input('a: '))
#     b = int(input('b: '))
#     print(triangle(a, b))







# Задача 4. Число наоборот (15 баллов)

# Вводится число. Реализуйте функцию, которая принимает в качестве параметра число, переворачивает его и выводит на экран.
# def paramater(c, h):
def reverse_number(number):
    reversed_number = number[::-1]
    return reversed_number
# numbers = int(input("Введите число я его разверну: "))
# while numbers == 0:
#     print("Программа завершена!")
#     if numbers == 0:
#         break
#     print(numbers)
# reversed = reverse_number(numbers)
# print(reversed)


# Пример:

# Введите число: 1234

# Число наоборот: 4321

# Введите число: 1993

# Число наоборот: 3991

# Введите число: 0

# Программа завершена! 

# Реализовать через цикл while, соответственно для выхода из цикла, пользователь должен будет ввести 0 и вывести сообщение "Программа завершена!" (5 баллов)

# Дополнительно: добейтесь такого вывода чисел, в начале которых идут нули

 

# Введите число: 1000

# Число наоборот: 0001

# Задача 5. Копейки (20 баллов)

# На одном складе нашли старые кассовые аппараты, в которых, как выяснилось, до сих пор остались лежать копейки разного достоинства. Даже однокопеечные есть! Все найденные копейки собрали в кучу и закинули в специальное устройство, которое сканирует все монеты и в результате выдаёт, сколько всё это будет в рублях.

# Напишите функцию, которая будет считать количество мелких монеток достоинством в 1, 5, 10 и 50 копеек. Функция должна выводить общую сумму.


# def count_coins(one_kopeck, five_kopecks, ten_kopecks, fifty_kopecks):
#     total_amount = one_kopeck * 0.01 + five_kopecks * 0.05 + ten_kopecks * 0.10 + fifty_kopecks * 0.50
#     return total_amount

# total_rubles = count_coins(3, 6, 7, 2)
# print(f"Всего у нас {total_rubles:.2f} рубля")  

# # Пример:

# Монет по 1 копейке: 3

# Монет по 5 копеек: 6

# Монет по 10 копеек: 7

# Монет по 50 копеек: 2

# Всего у нас 2.03 рубля

# Задава 6. Калькулятор (продолжение) (15 баллов)

# Реализуйте калькулятор из прошлого д/з через функцию

# def calculator(first, second):
#     return first + second,  first - second, first ** second, first // second
    


# first = int(input("Введите первое число: "))
# second = int(input("Введите второе число: "))
# print(calculator(first, second))