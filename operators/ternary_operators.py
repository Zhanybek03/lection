# sentence = input('Vvedite predlojeniye')


# res = 'Yes, viprosite\'noye!' if sentence[-1] == '?'
# else 'Normal one'
# print(res)


# if senctence[-1] == '?':
#     print('Yes, voprositel\'noye!')
# else:
#     print('Normal one!')    

# ------------------------------------------

# Terminal operators - (Терминальный оператор) это консрвукция кототрая по своему дейсвию аналлогично конструкции if/else, но при этом записывается в одну строчку
    
# num = int(input('Vvedite chislo: '))
# print('even number' if num % 2 == 0 else 'odd number')
       #четное                              нечетное

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite max/min: ').lower().strip()
# res = max(ls) if choice == 'max' else min(ls) if choice == 'min' else 'Invalid operator!'
# print(res)

# ----------------------------
flag = True
symbols = '0123456789' + '-' + '.'


while flag:
    print()
    num1 = input('Введите число: ')
    is_correct = True
    for x in num1:
        if x not in symbols:
            print("Вы ввели некоректное число! ")
            is_correct = False
            break
    if not is_correct:
        continue

    num2 = input('Введите второе число: ')
    is_correct = True
    for x in num2:
        if x not in symbols:
            print("Вы ввели некоректное число! ")
            is_correct = False
            break
    if not is_correct:
        continue



    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num1) if '.' in num2 else int(num2)


    # print(num1, type(num2))
    # print(num2, type(num2))

    operator = input('Введите операцию(+,-,*,/): ').strip()
    if operator == '+':
        print(f'Результат: {num1 + num2}')
    elif operator == '-':
        print(f'Результат: {num1 - num2}')
    elif operator == '*':
        print(f'Результат: {num1 * num2}')
    elif operator == '/':
        print(f'Результат: {num1 / num2}' if num2 !=0 
        else 'На ноль делить нельзя!')
    else:
        print('Вы ввели неверный оператор!')
    

    choice = input('Хотите продолжить(Yes/No)?: ')
    if choice.lower().strip() != 'yes':
        flag = False
        print('Пока пока! ЧАУ Dude!')

