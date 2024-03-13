# Инкапсуляция:
# 1. Языковая конструкция, которая помогает связать с методами для их обработки и управления (связь между данными и методами которые управляют ими) (класс - капсула)
# 2. Механизм сокрытия, при помощи которого можно ограничить доступ данного компенета программы к другому

# Инкапсуляция ка связь
# class Phone:
#     number = '+996708812390'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')
#         print(f'Мой номер: {Phone.number}')

# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как механизм сокрытия 
# 3 уровня сокрытия данных в питоне
    # 1. Публичный(public) - number, print_number
    # 2. Защизенный(_protected) - _number
    # 3. Приватный(__private) - __number


# class Car:
#     _country = 'Germany'
#     __motor = 'GT Line'
    
#     def __init__(self) -> None:
#         self.marka = 'BMW' #public
#         self._model = '18' #protected
#         self.__color = 'black' # private
# obj = Car()
# print(obj.marka)
# print(obj._country, obj._model)
# print(obj._Car__color, obj._Car__motor)
# print(dir(obj))

# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 17

#     def call(self) -> None:
#         print(f'{self._caller} звонит вам!')
#         question = input('Взять трубку(yes/no): ')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('сбросили трубку! ')

#     def __turn_on(self):
#         self.__increment_calls()
#         print('Aloo')
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')

#     def __increment_calls(self):
#         self.__count_of_calls += 1

# john = Phone()
# print(john.username)
# john.call()
# john.call()
# john.call()
# john.call()



# class Person:
#     def __init__(self, name , age) -> None:
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} years old!')
# obj = Person('John', 18)
# obj.display_info()

# obj.name = [1, 2, 3, 4]
# obj.age = -25
# obj.display_info()


# -------------------------

# getter & setter
# они нужны чтобы избежать прямого обращения к сокрытым атрибутам
# при этом можно добавить логику валидация(проверки) данных которые будет установленны в атрибут

class Person:
    def __init__(self, name , age) -> None:
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f'My name is {self.__name} and I\'m {self.__age} years old!')
    # getter
    def set_name(self): return self.__name

    def age(self): return self.__age

    # setter
    def set_age(self, age):
        if not isinstance(age, int) or not 0 <= age < 150:
            print('Invalid value for age')
        else:
            self.__age = age



obj = Person('John', 24)
obj.display_info()
obj.set_name()
obj.set_age(-18) 
obj.display_info()
obj.set_name()
obj.set_age(26)
obj.display_info()
