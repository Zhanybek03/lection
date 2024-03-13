# 1) Напишите программу, которая генерирует случайное число  от 1 до 100, а затем предлагает пользователю угадать это число. Программа должна предоставить подсказки о том, больше или меньше введенное число загаданного.
# import random
# random1 = random.randint(1, 100)
# print(random1)
# i = 0
# while i < 10 :
#     guessTheNumber = int(input('Please guess the number: '))
#     if guessTheNumber > random1:
#         print('Your guess is bigger!')
#     elif guessTheNumber < random1:
#         print('Your guess is small')
#     else:
#         print('YOu win!')
#         i = 10
#     i += 1


# 2)Напишите программу, которая преобразует температуру из градусов Цельсия в градусы Фаренгейта и наоборот. Позвольте пользователю выбирать тип преобразования.
# while True:
#     choose = int(input('Ведите 1 чтобы преобразовать ц в ф 2 чтобы ф в ц: '))
#     if choose == 1:
#         print(25 + 'C°' * 9 / 5 + 32)
#     elif choose == 2:
#         print((29 + 'F°' - 32) * 5 / 9  )
#     else: 
#         print('Unknown value')


# “””
# 3) Реализуйте программу, которая рассчитывает ежемесячные выплаты по ипотеке. Пользователь должен ввести сумму кредита, годовую процентную ставку и срок кредита. 
# ”””
        
credit = input('enter your credit: ')
stavka = input('enter your stavka: ')
srok = input('enter your srok: ')


# credit = 100000 com
# stavka = 5%
# srok = 2

print(credit + (credit / (stavka / 100) * srok))












    




