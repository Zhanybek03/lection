# 1) Проверить введенное пользователем число и если оно больше 5 то вывести “True”, иначе “False”.
# user = int(input('enter a integer: '))
# if user > 5:
#     print(True)
# else:
#     print(False)

# 2) Проверить введенные пользователем данные и если длина строки больше или равна 5 символам вывести “True” иначе “False”.
# user = input('Enter a string: ')
# if len(user) >= 5:
#     print(True)
# else:
#     print(False)

# 3) Проверить введенное пользователем значение если оно больше или равно 90, вывести “Отлично ваша оценка 5”, если значение больше или равно 80, вывести “Здорово ваша оценка 4”, если значение больше или равно 70, вывести “Хорошо ваша оценка 3”, если значение больше или равно 60, вывести “Вам стоит подучить материал", в других случаях “вы не сдали экзамен”.
# user = int(input('Enter a value: '))
# if user >= 90:
#     print('Отлично ваша оценка 5')
# elif user >= 80:
#     print('Здорово ваша оценка 4')
# elif user >= 70:
#     print('Хорошо ваша оценка 3')
# elif user >= 60:
#     print('Вам стоит подучить материал')
# else:
#     print('Вы не здали экзамен!')

# 6.Проверить введенное пользователем число если оно отрицательное то вывести “negative”, если положительное то “positive”, если оно равно 0 то вывести “Zero”
# user = int(input('enter an integer: '))
# if user < 0:
#     print('Negative!')
# if user > 0: 
#     print('Positive!!')

# 5) Даны два целых числа. Выведите значение наименьшего из них.
# int1 = int(input('Enter an integer1: '))
# int2 = int(input('Enter an integer2: '))
# if int1 < int2:
#     print('int1: ', int1)
# elif int1 > int2:
#     print('int2: ', int2)

# 6) Даны три целых числа. Выведите значение наименьшего из них.

# int1 = int(input('Enter a first number: '))
# int2 = int(input('Enter a second number: '))
# int3 = int(input('Enter a third number: '))

# if int1 < int2 and int1 < int3:
#     print('int1: ', int1)
# elif int2 < int1 and int2 < int3:
#     print('int2: ', int2)
# elif int3 < int1 and int3 < int2:
#     print('int3: ', int3)

# 7) Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
# num1 = int(input('Enter a number1: '))
# num2 = int(input('Enter a number2: '))
# num3 = int(input('Enter a number3: '))
# if num1 == num2 == num3:
#     print('3')
# elif num3 == num2 or num3 == num1 or num1 == num2:
#     print('2')
# else:
#     print('1')


# 8) Вводятся два целых числа. Проверить делится ли первое на второе. Вывести на экран сообщение об этом, частное (в любом случае), а также остаток от деления (если он есть). input: 678 23 
# output: 678 не делится на 23 
# Частное: 29 
# Остаток: 11

# a = int(input())
# b = int(input())
# if a%b == 0:
#     print(" делится на " % (a,b))
# else:
#     print(" не делится на" % (a,b))
#     print("Остаток: " % (a%b))
# print("Частное: " % (a//b))

# 9) Дано номер года. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# number1 = input('Enter an year: ')
# if number1 % 4 == 0 and number1 % 100 != 0 or number1 % 400 == 0:
#     print('Yes')
# else:
#     print('NO')

# 8) Вводятся два целых числа. Проверить делится ли первое на второе. Вывести на экран сообщение об этом, частное (в любом случае), а также остаток от деления (если он есть). input: 678 23 
# output: 678 не делится на 23 
# Частное: 29 
# Остаток: 11

user_1 = int(input('Enter an integer: '))
user_2 = int(input('Enter an integer: '))
if user_1 % user_2 != 0 :
    print(f'output: {user_1} не делится {user_2}')
elif user_1 % user_2 == 0:
    print(f'Частное: {user_1 // user_2} ')
else:
    print(f'Остаток: {user_1 % user_2} ')












