# Задача 1: Валидация пароля

# Пользователь хочет установить пароль для своей учетной записи. Пароль должен соответствовать следующим критериям:

# Длина пароля должна быть не менее 8 символов.
# Пароль должен содержать хотя бы одну заглавную букву (A-Z).
# Пароль должен содержать хотя бы одну строчную букву (a-z).
# Пароль должен содержать хотя бы одну цифру (0-9).
# Пароль должен содержать хотя бы один специальный символ из множества: !@#$%^&*()_-+=<>?/
# Напишите программу, которая запрашивает у пользователя пароль и затем проверяет, удовлетворяет ли он всем критериям. Если пароль удовлетворяет всем критериям, программа должна сообщить, что пароль принят. В противном случае, программа должна вывести сообщение об ошибке, указывая, какие критерии не выполняются.
def validate(password):
    # password = input('Enter your password: ')
    if len(password) < 8:
        print('Your password is too short!')
    elif not any (cahr.isupper() for cahr in password):
        print ('Your password must contain at least one uppercase letter!')
    elif not any (cahr.islower() for cahr in password):
        print ('Your password must contain at least one lowercase letter!')
    elif not any (cahr.isdigit() for cahr in password):
        print ('Your password must contain at least one digit!')
    elif not any (cahr in '!@#$%^&*()_-+=<>?/' for cahr in password):
        print ('Your password must contain at least one special character!')
    else:
        print('Your password is accepted!')
        return True




# Задача 2: Обработка ошибок при работе с элементами списка:

# Создайте список чисел и попробуйте выполнить некоторые операции над элементами списка. Обработайте исключения, такие как IndexError, ValueError и ZeroDivisionError.
# ls = [23, 56, 67, 988, 89]

# try:
#     print(ls[5])
# except IndexError:
#     print('Error index')
# except ValueError:
#     print('Error value')
# except ZeroDivisionError:
#     print('Error zero')


# Задача 3: Поиск значения в словаре с обработкой исключения:

# Создайте словарь с данными (например, словарь с именами и возрастами людей). Затем запросите у пользователя имя и попробуйте найти возраст этой персоны в словаре. Обработайте исключение, если имя не найдено.



# dict = {
#     'John'  : 23,
#     'Azamat': 24,
#     'Maria' : 25,
#     'Aiperi': 26}

# try: 
#     name = input('Enter your name: ')
#     print(dict[name])
# except KeyError:
#     print('Error User not found')

    

