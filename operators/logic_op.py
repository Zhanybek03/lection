# operatory sravnenia 
# Uslovnye operatory
# Logicheskiye operatory
# < > ==(Равно), !=(не равно), <= , >=
# 1 < 5 
# a = 'A'
# print(ord(a))
# b = 1100
# print(chr(b))




# Условные операторы
# if
# elif
# else

# if <condition>:
#     <body if> сработает если в condition if придет True 
# [elif] <condition>:
#     <body elif>
# [else]:
#     <body else> сработает если во всех выше стоящих условиях пришло False

# string = input('Enter something: ').lower()
# print(string)
# if string == 'hello':
#     print('Hello, It\'s me, I was wondering if after all these years you\'d like to meet!')
# elif string == 'john':
#     print('Welcome back John Snow! The king of North!!')
# elif string == 'abra-kadabra':
#     print('Sim salamon kadabra!')
# else:
#     print('NO match found!')



# print('Registration Form: ')

# email = input('Enter your email: ')
# if '@' not in email:
#     raise ValueError('Email is INvalid! @ - must be!')
# password = input('Enter the password: ')
# if len(password) < 8:
#     raise ValueError('Too short! At least 8 symbols!')
# elif password.isdigit():
#     raise ValueError('INvalid Password! ONly digits!')
# elif password.isalpha():
#     raise ValueError('Invalid Password! Only alphabet!')

# password2 = input('Enter password confirmation: ')
# if password != password2:
#     raise ValueError('Passwords did\'t match!!')

# index = email.find('@')
# print(f'Successfully registered! Hello Mr/Mrs {email[:index]}!')


# age = int(input('Enter your age: '))

# if age.isgigit():
#     age = int(age)
# else:
#     raise Exception('Invalid value for age!')

# if age < 18:
#     print(f'Access Denid! Come again after{18 - age}')
# else:
#     print('You can buy it!')


# ----------------------
# логические операторы
# and - логические и
# or - лог или
# not - лог отрицание

money = 1_000_001
status = 'Base'

if money > 1_000_000 and status == 'premium':
    print('You\'re president of our club!')
if money > 1_000_000 or status == 'premium':
    print('You\'re minister of our club!')
else:
    print('You\'re honorable member of our club!')





