# # Даны 2 списка:

# list_a = [1, 2, 39, 5, -6, 7, 8.1, 9, 10, -43, -134, 3.14, 2.55, "Lenovo", "Acer", "Asus"]

# list_b  = [123, -1.85, 43, -4.4, 8.16, -5, 3.26, 21, 22, -43.97, "Dell", "HP", "Lenovo", "Acer" ]


# Создать новые списки и вывести их результаты:
# list_int = []
# list_float = []
# list_str = []
# for i in list_a + list_b:
#     if type(i) == int and i > 4:
#         list_int.append(i)
#     elif type(i) == float and i < 0:
#         list_float.append(i)
#     elif type(i) == str:
#         list_str.append(i)
# print(list_int)
# print(list_float)
# print(list_str)

# integers_greater_than_4 = [x for x in list_a + list_b if isinstance(x, int) and x > 4]

# negative_floats = [x for x in list_a + list_b if isinstance(x, float) and x < 0]

# laptop_manufacturers = [x for x in list_a + list_b if isinstance(x, str)]

# print("Целые числа больше 4:", integers_greater_than_4)
# print("Числа с плавающей точкой, имеющие отрицательное значение:", negative_floats)
# print("Наименования производителей ноутбуков:", laptop_manufacturers)

# Где будут только целые числа, которые больше 4
# Где будут только числа с плавающей точкой, имеющие отрицательное значение
# Где будут только наименования производителей ноутбуков
# Продолжить работу со списками, содержащие цифры и вывести их результат:

#  Вставить в середину каждого списка новое значение(любое)
# list_a.insert(len(list_a) // 2, 564)
# list_b.insert(len(list_b) // 2, 234)


# Найти сумму элементов в каждом списке
# num1 = sum(list_int)
# num2 = sum(list_float)
# print(num1, num2)
# num3 = sum(list_str)
# print(num3)
# Посчитать количество элементов в каждом списке
# print(len(list_int),len(list_float), len(list_str)) 

# В списках с наименованиями (вывести результат):




# Проверить наличие повторяющихся данных, если есть удалить.
# repeat = set(list_str)
# print(repeat)
# list1 = list(repeat)
# print(list1) 


# Добавить в начало и конец по одному производителю.
# list1.append('Apple')
# list1.insert(0, 'Nokia')
# print(list1)

# Задание 2 (20 баллов)

# Напишите программу имитирует регистрацию пользователя.


# user_name = input('ENTER YOUR NAME:')
# user_email = input('Enter your email:')
# user_password = input('Enter your password:')
# print(f'{user_name}, Вы успешно зарегистрировались, информация отправлена на {user_email}')
# print('{}, Вы успешно зарегистрировались, информация отправлена на {}'.format(user_name, user_email))
# print('%s, Вы успешно зарегистрировались, информация отправлена на %s' % (user_name, user_email))


# Программа должна запросить у Вас:

# Name

# Email

# Password

# Программа должна вывести сообщение:
# <name>, Вы успешно зарегистрировались, информация отправлена на <Email>

# Используйте разные методы форматирования сторок (3 методов) и напишите в комментариях какой метод вам больше всего понравился и почему.

# Продолжение задание №2 (20 баллов)

#  Ваша программа должна проверить:

# введенное имя на наличие в конце хотя бы одной цифры
# введенный пароль на наличие только чисел
# введенный email на окончание символами ".kg" 
# в случае ошибки выдавать соответствуещее сообщение
# user_name = input('Enter your name :')
# if user_name[-1].isalpha():
#     raise ValueError('Your name has to contain digits!')
# user_email = input('Enter your email:')
# if user_email[-3 ::] != '.kg':
#     raise ValueError('Your email has to end with . kg!!')
# user_password = input('Enter your password: ')
# if user_password.isalpha():
#     raise ValueError('Your password has to contain only digits!!')

# Задание №3 (20 баллов)

# Напишите программу, которое учитывает количество уникальных букв в слове. Уникальные буквы — это те, которые встречаются всего один раз.

 

# Пример 1:

# Введите слово: привет
# Кол-во уникальных букв: 6

# Пример 2:

# Введите слово: лава
# Кол-во уникальных букв: 2

user1  = input('Enter a word')
counter = 1
for letter in user1:
    if user1.count(letter) == 1:
        counter += 1
print(counter)
# Задание №4 (10 баллов)

# Асан слишком ленивый чтобы считать длину окружности и решил написать программу которая будет считать вместо него длину, помогите написать ему программу, которая спрашивает у Асана радиус окружности и выдает (округленный до верхнего значения ответ, если радиус окружности больше или равен 10) ответ (использовать библиотеку math)  

while True:
    r = int(input('Пишете радус окуружности'))
    c  = 2 * 3.14 * r
    if c >= 10:
        print(c)