"""
1. Создайте класс BankAccount, в конструкторе которого определена переменная
экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
который будет отнимать сумму от баланса и возвращать текущий баланс. Также
добавьте метод deposit, который также имеет параметр amount и соответсвенно
добавляет сумму к балансу, возвращает баланс.
"""
# class BankAccount:
#     balance = 0

#     def withdraw(self, amount):
#         self.balance -= amount
#         return f'Total balance: {self.balance}'
#     def deposit(self, amount):
#         self.balance += amount
#         return f'Total balance: {self.balance}'
# loot = BankAccount()
# print(loot.withdraw(100000))
# print(loot.deposit(200000))

"""
2. Вам дан такой код:

winner1 = Nobel("Литература", 1971, "Пабло Неруда")
print(winner1.category, winner1.year, winner1.winner)
print(winner1.get_year())

winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
print(winner2.category, winner2.year, winner2.winner)
print(winner2.get_year())

который выводит в терминал такие значения:

Литература 1971 Пабло Неруда
выиграл 50 лет назад

Литература 1994 Кэндзабуро Оэ
выиграл 27 лет назад

Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код вывел указанные значения в терминале. Даты внутри класса не хардкодить.
"""


# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#     def get_year(self):
#         get_years = 2024 - self.year
#         return f'выиграл {get_years} лет нзад'
# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())    

    






"""
3. Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:
- пароль должен быть минимум 8 символов, но меньше 15
- пароль должен содержать цифры
- пароль должен содержать буквы
- пароль должен содержать хотя бы один из символов:
    '@', '#', '&', '$', '%', '!', '~', '*'

если одно из условий не выполнено, выводите кастомное исключение, 
если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.

Также переопределите метод str, чтобы при попытке распечатать
сам пароль, вам выдавалась строка из звездочек,
к примеру пароль - 'joe@123456'
в терминале выйдет - ******
"""

# class Password:
#     def __init__(self, password):
#         self.password = password
#     def validate(self):
#         if len(self.password) < 8 and len(self.password) > 15:
#             raise ValueError('You password is short')
#         elif len([x for x in self.password if x.isalpha()]) == 0:
#             raise ValueError('you password not given str')
#         elif len([x for x in self.password if x.isupper()]) == 0:
#             raise ValueError('you password not given uppercase')
#         elif len([x for x in self.password if x.islower()]) == 0:
#             raise ValueError('you password not given lowercase')
#         elif len([x for x in self.password if x.isdigit()]) == 0:
#             raise ValueError('you password not given digit')
#         elif len([x for x in self.password if x in '!@#$%^&*()_-+=<>?/']) == 0:
#             raise ValueError('you password not given symbols')
#         else:
#             return('You passoword is saved successfully ')
#     def __str__(self) -> str:
#         return '*' * len(self.password)

# password1 = Password("Janybek23@32435")
# print(password1.validate())
# print(password1)

        
"""
4. Создайте класс Math, экземпляром которого должно быть число.
У классa Math должно быть 3 метода:
- get_factorial - выводит факториал числа
- get_sum - выводит сумму цифр числа
- get_mul_table - выводит таблицу умножения для числа до 10. Создайте экземпляр класса и примените к нему все методы. 
"""
# class Math:
#     def __init__(self, num):
#         self.num = num
#     def get_factorial(self):
#         counter = 1
#         for i in range(1, self.num):
#             counter *= i
#         return f'Число факториала: {counter}'
            
            
#     def get_sum(self):
#         sum = 1
#         for i in range(1, self.num):
#             sum += i
#         return f'Сумма чисел: {sum}'
#     def get_mul_table(self):
#         number = self.num
#         print(f'Таблица числа {number}: ')
#         for i in range(1, number):
#             res = number * i
#             print(f'{i} x {number} = {res}')

# # num = int(input('Enter your number: '))
# res = Math(10)
# print(res.get_factorial())
# print(res.get_sum())
# res.get_mul_table()
"""
5. Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д)

У класса есть метод give_priority который записывает вашу задачу в список(переменная класса) с ключом в виде числа, 
приоритет который вы даете вашей задаче -
к примеру {3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

У класса должен быть метод list_of_tasks, который выдает вам список отсортированных задач 
по приоритету:
[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]


"""


class ToDo:
    dict_ = {}
    def __init__(self, d_plan):
        self.d_plan = d_plan
    def give_priority(self, priority):
        self.dict_[priority] = self.d_plan
    def list_of_tasks(self):
        res = sorted(self.dict_.items(), key=lambda x: x[0])
        print(res)

per1 = ToDo('happy')
per1.give_priority(1)
per2 = ToDo('healthy')
per2.give_priority(2)
per3 = ToDo('read book')
per3.give_priority(3)
print(per1.dict_)
per1.list_of_tasks()
per2.list_of_tasks()
per3.list_of_tasks()




        
