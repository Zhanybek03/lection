# Задание 1.
# Есть список list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]



#  Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЕРНУТЬ список состоящий из имен(строковых значений) и чтобы эти имена были с заглавной буквы и в алфавитном порядке
# Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЫВЕСТИ НА КОНСОЛЬ список из целочисленных значений в отсортированном виде но в обратном порядке, т.е от большого к маленькому
# Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЕРНУТЬ сложение всех чисел с плавающей точкой
# 1111111111111111111111111
# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
# def listok(a): 
#     b = []
#     for i in a:
#         if type(i) == str:
#             b.append(i.title())
#     return sorted(b)
# print(listok(list_1))
# 2222222222222222222222222
# from home_task7 import reverse_number
# def listok2(o):
#     chislo = []
#     for i in o:
#         if type(i) == int:
#             chislo.append(i)
#     chislo = sorted(chislo)
#     return reverse_number(chislo)
# print(listok2(list_1))
# 3333333333333333333333333333333

# def listok3(point):
#     dot = []
#     for i in point:
#         if type(i) == float:
#             dot.append(i)
#     a = 1
#     for i in dot:
#         a *= i
#     return a
# print(listok3(list_1))

# Задание 2.
# Сэндвичи: напишите функцию, которая получает первым аргументом размер сэндвича в виде строкового значения и список компонентов сэндвича.

# При вызове функции, функция должна выводить описание заказанного сэндвича например «Большой сэндвич со следующими ингредиентами: огурец, колбаса … » . Вызовите функцию три раза с разными количествами аргументов и разными размерами (Большой, средний, маленький)

 
# def sandwich(size, *args): 
#     print(f'{size} сэндвич со следующими ингредиентами:{args} ')

# print(sandwich)('middle', 'Огурец, колбаса')
# print("1 - big, 2 - middle, 3 - small")
# customer = input("Выберите размер сендвича: ")
# 1 = ('')




# Задание 3.
# Напишите функцию для сохранения информации об автомобиле в словаре . Функция всегда должна возвращать производителя и название модели, но при этом она может получать произвольное количество именованных аргументов . Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет и комплектация) . Ваша функция должна работать для вызовов следующего вида: car = make_car(‘subaru’, ‘outback’, colour=’blue’, engine='V8') и возвращать строку" Subaru Outback colour is blue, engine is V8


# def make_car(brand, model, **car):
#     car['brand'] = brand
#     car['model'] = model
#     print(car['brand'], car['model'], car['colour'], car['engine'])
    
#     return car


# car = make_car('subaru', 'outback', colour='blue', engine='V8')
# print(car)
# print("Subaru Outback colour is blue, engine is V8")




# Задача 4

# Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое в нём количество цифр и букв. Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.

# Реализовать в цикле while, для выхода пользователь должен ввести "выход"

# Пример:

# Введите текст: 100 лет в обед

# Какую цифру ищем? 0

# Какую букву ищем? л

 

# Количество цифр 0: 2

# Количество букв л: 1

# def count_letters():
#     user = input('введите текст: ')
#     while user != 'выход':
      
#         print('Какую цифру ищем?')
#         digit = input()
#         print('Какую букву ищем?')
#         letter = input()
#         if digit == 'выход'or letter == 'выход':
#             break
#         print(f'Количество цифр {digit}: {user.count(digit)}')
#         print(f'Количество букв {letter}: {user.count(letter)}')
# print(count_letters())

# Задача 5.

# Напишите функцию, которая в виде аргумента принимает словарь (данные с именами и должностями , где ключ это имя работника,  а значение его должность. Функция должна вернуть предложения, типа:  
# Работник Асан, занимает должность Директор
# def dictionary(name):
#     for k, v in name.items():
#         print(f'Работник {k}, занимает должность {v}')

# dictionary({'Асан': 'Директор'})

# Задача 6 (дополнительно)

# Напишите программу, которая будет суммировать все числа, введенные пользователем, игнорируя при этом нечисловой ввод. Выводите на экран текущую сумму чисел после каждого очередного ввода. Ввод пользователем значения, не являющегося числовым, должен приводить к появлению соответствующего предупреждения, после чего пользователю должно быть предложено ввести следующее число. Выход из программы будет осуществляться путем пропуска ввода. Удостоверьтесь, что ваша программа корректно обрабатывает целочисленные значения и числа с плавающей запятой. 
    
def sum_numbers():
    sum = 0
    while True:
        number = input('введите число: ')
        if number == 'конец':
            break
        try:
            number = int(number)
            sum += number
            print(f'Сумма: {sum}')
        except ValueError:
            print('Ошибка, введите только числа')
            continue

sum_numbers() 

    



# Пример:
 
# Введите число: 1

# Сумма: 1

# Введите число: 2

# Сумма: 3

# Введите число: 5

# Сумма: 8

# Введите число: кукарача

# Ошибка, введите только числа

# Введите число: 12

# Сумма: 20 (т.е. сумма не обнуляется, а продолжает "считать" (8 + 12 = 20)