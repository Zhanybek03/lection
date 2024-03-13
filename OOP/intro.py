# OOP - Обьектно - ориентированное програмирование 

# class(класс) - это описание того, как должен выглядеть обьект, то есть в классе мы описываем какими свойствами (данными) и поведением(функцием) должен обладать обьект
# object(Обьект) - это некая сущность которую мы создаем от класса, у обьекта есть собственное состояние свойсв(данные)

# аттрибуты - обычные переменные внутри класса
# методы - это функции внутри класса
# -----------------

# class Human:
#     age = 0
#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, job: {self.job}, Citizen: {self.citizen}' 
# john = Human('John', 'Snow', 'King of North', 'Northerner')
# anvar = Human('Anvar', 'Lanister', 'Programmer', 'KR')
# # print(john)
# # print(type(john))
# # print(dir(john))
# print(john.show_info())
# print(anvar.show_info())
# john.age = 24
# john.job = 'King of Westeros'
# print()
# print(john.show_info())


#  -------------------------
# class Dog:
#     # аттрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name: str, color: str) -> None:
#         """"Инициализаторы, именно здесь создаются аттрибуты обьекта"""
#         # self  - ссылка на обьект который создается 
#         self.name = name
#         self.color = color 
#     def bark(self):
#         print(f'{self.name} лает!')
#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, color: {self.color}, ushi: {self.ushi}')
# rex = Dog('Rex', 'black')
# pluto = Dog(name='Pluto', color='brown')
# aktosh = Dog('Aktosh', 'gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.age = 2
# pluto.age = 7
# aktosh.age = 1
# aktosh.ushi = False


# rex.show_info()
# pluto.show_info()
# aktosh.show_info()


# rex.bark()
# pluto.bark()
# aktosh.bark()


# class Human: 
#     def __init__(self, name) -> None:
#         self.name = name
#         self.hungry = 100
        
#     def walk(self):
#         print(f'{self.name} walking around!')
#         self.hungry += 30

#     def work(self):
#         print(f'{self.name} rabotu raboatet!')
#         self.hungry += 50

#     def eat(self, meal, finish=True):
#         print(f'{self.name} покушала {meal}!')
#         self.hungry -= 60 if finish else 30

#     def info(self):
#         print(f'{self.name} --> {self.hungry}')
# obj = Human('Raychel')
# obj.info()
# obj.eat('Kurasan')
# obj.eat('Sandwitch', finish=False)
# obj.info()
# obj.walk()
# obj.work()
# obj.info()
# obj.eat('Burger')
# obj.eat('Fried Potato', finish=False)
# obj.info()
