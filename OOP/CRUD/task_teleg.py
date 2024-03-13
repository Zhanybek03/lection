"""
1. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
"""



# class MyList(list):
#     def __getitem__(self, index):
#         return super(MyList, self).__getitem__(index - 1)
# x = MyList([1,2,3,4,5])
# print(x[1])

"""
2. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
Также в методе new напишите условие для удаления
пробелов и пустых строк в созданных словах.
"""


# class Word: 
#     def __new__(cls, obj):
#         obj = obj.replace(' ', '')
#         return obj
    
#     def __init__(self, obj ) -> None:
#         super().__new__()
#         self.obj = obj
#     def __gt__(self, other):

#         print(self, '<', other)
#         if len(self) > len(other):
#             return self
#         elif len(self) < len(other):
#             return other
#         else: 
#             return 'equal'
                
#     def __lt__(self, other) -> bool:
#         return len(self) < len(other)
    
#     def __eq__(self, other) -> bool:
#         return len(self) == len(other)
# obj = Word(' The weather is wonderfull')
# obj2 = Word('what do u think about taking a walk?')

# print(obj > obj2)
# print(obj < obj2)
# print(obj == obj2)

"""
3. Создайте класс BankAccount, представляющий банковский счет. Реализуйте магические методы init, str, add и sub, чтобы поддерживать инициализацию счета, вывод информации о счете и операции пополнения и снятия средств.
"""


# class BankAccount:
    
#     def __init__(self) -> None:
#         self.bank_account = 0     
#     def __str__(self): 
#         return f'{self.bank_account}'
#     def __add__(self, other):
#         self.bank_account += other 
#         print(f'Вы пополнили баланс! Ваш текущий баланс: {self.bank_account}')
#         return self.bank_account + other
#     def __sub__(self, other):
#         self.bank_account -= other 
#         print(f'С вашего баланса были сняти средства в размере {other}\nу вас осталось {self.bank_account}')
#         return self.bank_account
    

# a = BankAccount()
# a + 90
# a - 69
# print(a)
    
