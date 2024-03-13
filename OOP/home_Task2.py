"""

1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.

"""

# class Class1:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year

#     def get_info(self):
#         return {'model': self.model, 'color': self.color, 'year': self.year}
# class Class2(Class1):
#     def __init__(self, model, color, year):
#         super().__init__(model, color, year)
        
#     def get_info(self):
#         return super().get_info()
# res = Class2('Bmw', 'Dark-Blue', 2022)
# print(res.get_info())

"""

2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.

"""

# class A:
#     def method1(self):
#         return ('Основной функционал')
# class B(A):
#     def method1(self):
#         res = super().method1()
#         print(res)
#         print('Дополнительный функционал')
# result = B()
# result.method1()   


"""

3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:

append, который будет принимать строку и добавлять её в конец исходной

pop, который удаляет из строки последний элемент и возвращает его.

Пример:

# example = MyString('String')

# example.append('hello')

# print(example) -> 'Stringhello'

# print(example.pop()) -> 'o'

# print(example) -> 'Stringhell'

"""


# class Mystring(str):
#     def __init__(self, str):
#         self.str = str
        
    
#     def append(self, string):
#         return self.str + string
#     def pop(self):
#         return self.str[-1]
# obj = Mystring('Hello it is me!')
# print(obj.append(' I was wondering'))
# obj = Mystring('Wonderfull')
# print(obj.pop())
    





"""

4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.

"""

# class MyDict(dict):
#     def __init__(self, obj):
#         self.obj = obj
#     def get(self, key):
#         if self.obj.get(key) == None:
        
#             return 'Are you kidding?' 
#         else: 
#             return self.obj.get(key)


# object = MyDict({
#     1: 'Hub',
#     2: 'Car'
# })
# print(object.get(3))




"""

5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.

Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.

"""

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#     def display(self):
#         return f'Имя: {self.name} Возраст: {self.age}'
# class Student(Person):
#     def __init__(self, name, age, direction) -> None:
#         super().__init__(name, age)
#         self.direction = direction
#     def display_student(self):
#         res = super().display()
#         return f'{res}, direction: {self.direction}'
# result = Student('Paul', 20, 'Artificial inteligents')
# print(result.display_student())



"""

6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.

"""

# class ContactList(list):
#     def __init__(self, ls):
#         self.list = ls
#     def search_by_name(self, name):
#         ls = []

#         for i in self.list:
#             if i == name:
#                 ls.append(i)
#         return ls     
#     def all_contacts(self):
#         return self.list

# contacts = ContactList(['Anvar', 'Adilet', 'Alihan', 'Zhoomart'])
# print(contacts.all_contacts())
# print()
# print(contacts.search_by_name('Anvar'))

"""

7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию
должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.
У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.
Создайте два дочерних класса от Smartphone - Iphone и Samsung.
У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.
А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.
Создайте объекты от данных классов и примените все методы.

"""

# class Smartphone:
#     def __init__(self, name, color, memory, battery = 0) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery
#     def __str__(self):
#         return f'Name: {self.name} Memory: {self.memory}'
#     def charge(self, procent):
#         self.battery += procent
#         return f'Ваша зарядка заряжена на {self.battery}%'

# class Iphone(Smartphone):
#     def __init__(self, name, ios, color, memory, battery = 0) -> None:
#         super().__init__(name, color, memory, battery)
#         self.ios = ios
#     def send_imessage(self):
#         return f'Это сообщения выслано от {self.name}'
# from datetime import datetime 
# class Android(Smartphone):
#     def __init__(self, name, android, color, memory, battery = 0) -> None:
#         super().__init__(name, color, memory, battery)
#         self.android = android
#     def show_time(self):
#         hours = datetime.now()
#         return f'текущее время: {hours}'

# phones = Iphone('Iphone 14 pro max', 'Purple', '256 gb', '69 %' )
# print(phones.send_imessage())
# phones2 = Android('Samsung Galaxy s13 ultra', 'black', '512 gb', '98 %')
# print(phones2.show_time())
        


"""

8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula - полное произношение заклинания.
У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.
Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:
Открытие замков: Alohomora
позволяет магу попасть в любую комнату,
способно открыть любую закрытую замочную скважину.
Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы

"""
# class Spell:
#     def __init__(self, name, formula, description) -> None:
#         self.name = name
#         self.formula = formula
#         self.description = description

#     def get_description(self):
#         return self.description
#     def execute(self):
#         return self.formula
#     def str(self):
#         return f'{self.name}: {self.formula} {self.description}'

# spells = Spell('Открытие замков', 'Alohomora', 'позволяет магу попасть в любую комнату, способно открыть любую закрытую замочную скважину.')
# print(spells.str())

"""

9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом
чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.
Создайте исключение от этого класса с сообщением:
"ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"
Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:
Traceback (most recent call last):

  File "inheritance.py", line 121, in <module>

    check_letters(a)

  File "inheritance.py", line 117, in check_letters

    raise capitals_error

main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ

"""
# class CustomError(Exception):
#     def __init__(self, message) -> None:
#         self.sms = message
#     def check_latters(self):
#         if any([i.islower() for i in self.sms]):
#             raise CustomError('Enter a latters with uppercase!')
#         else:
#             return 'Красавчик!'
# res = CustomError('KING')
# print(res.check_latters())

 

"""

10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:
power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
Класс должен иметь методы:
give_weapon - выбирает случайное оружие из списка
give_role - выбирает случайную роль из списка, к примеру:
["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:
char1.give_powers('ловкость', 5)
увеличит ловкость вашего героя.
Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn,
дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character.
"""
import random
class Character:
    power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
    roles = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
    weapons = ['AK-47, M16, AR-15', 'Remington 700, Ruger 10/22', 'Winchester Model 70', 'Barrett M82', 'FN SCAR', 'Heckler & Koch G3', 'Mosin-Nagant']
    def __init__(self, name) -> None:
        self.name = name
        self.weapon = None
        self.role = None
    def give_weapon(self):
        self.weapon = random.choice(self.weapons)
        return f'{self.name} получает {self.weapon}!'

    def give_role(self):
        self.role = random.choice(self.roles)
        return f'{self.name}получает роль {self.role}!'
    
    def give_power(self,key, value):
        self.power_list[key] = value
        return self.power_list

# char1 = Character('Варвар')
# print(char1.give_power('Варвар', 5))
class Elf(Character):
    def __init__(self, name, archery) -> None:
        super().__init__(name)
        self.archery = archery
    def give_archery(self):
        return 'Эльф попал в Орга!'

class Orc(Character):
    def __init__(self, name, orc) -> None:
        super().__init__(name)
        self.orc = orc
    def give_orc(self):
        return 'Орг попал в Эльфа'

class DragonBorn(Character):
    def __init__(self, name, dragon) -> None:
        super().__init__(name)
        self.dragon = dragon
    def give_dragon(self):
        return 'Драгон сжег Эльфа и Орга!'


elf1 = Elf('Zhanybek', 'shoot')
print(elf1.give_role())
print(elf1.give_power('мудрость', 50))
print(elf1.give_weapon())
print(elf1.give_archery())

orc1 = Orc('Alihan', 'shoot')
print(orc1.give_role())
print(orc1.give_power('харизма', 70))
print(orc1.give_weapon())
print(orc1.give_orc())



drago = DragonBorn('Azamat', 'shoot')
print(drago.give_role())
print(drago.give_power('ловкость', 30))
print(drago.give_weapon())
print(drago.give_dragon())


