"""1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
"""

# class Auto:
#     def ride(self):
#         return('Riding on a ground')

# class Boat:
#     def swim(self):
#         return('floating on water')
# class Amphibian(Auto, Boat):
#     def ride(self):
#         return super().ride()
#     def swim(self):
#         return super().swim()
# obj = Amphibian()
# print(obj.ride())
# print(obj.swim())
    

"""2) Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""



# class RadioMixin:
#     def play_music(self, name_of_music):
#         return name_of_music
# class Auto(RadioMixin):
#     def __init__(self) -> None:
#         super().__init__()
# class Boat(RadioMixin):
#     def __init__(self) -> None:
#         super().__init__()
# class Amphibian(RadioMixin):
#     def __init__(self) -> None:
#         super().__init__()
# obj = RadioMixin()
# print(obj.play_music('Photogrph'))

    

"""3) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""
# from datetime import datetime

# class Clock:
#     def current_time(self):
#         now = datetime.now()
#         return now
# class Alarm:
#     def turn_on(self):
#         print('Пара вставать!')
#     def turn_off(self):
#         print('Ложись спать!')
        
# class AlarmClock(Clock, Alarm):
#     def set_alarm(self):
#         return self.turn_on()
    
# obj = AlarmClock()
# obj.set_alarm()





"""4) Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""
# from abc import abstractmethod, ABC
# class Coder:
#     def __init__(self, expierence, count_code_time = 0) -> None:
#         self.expierence = expierence
#         self.count_code_time = count_code_time
#     @abstractmethod
#     def get_info(self):
#         pass
#     @abstractmethod
#     def coding(self):
#         pass

# class Backend(Coder):
#     def __init__(self, languages_backend, expierence, count_code_time=0) -> None:
#         super().__init__(expierence, count_code_time)
#         self.languages_backend = languages_backend

#     def get_info(self, hours):
#         self.count_code_time += hours
#         return super().get_info()

# class Frontend(Coder):
#     def __init__(self, languages_frontend, expierence, count_code_time=0) -> None:
#         super().__init__(expierence, count_code_time)
#         self.languages_frontend = languages_frontend

#     def get_info(self, hours):
#         self.count_code_time += hours
#         return super().get_info()
    
# class FullStack(Backend, Frontend):
#     def __init__(self, languages_backend, languages_frontend, expierence, count_code_time=0) -> None:
#         self.languages_frontend = languages_frontend

#         super().__init__(languages_backend, expierence, count_code_time)
   
    


# dev = Backend('Python', '6 months')
# print(dev.get_info(1008))
# print(dev.coding())
# dev = Frontend('JavaScript', '6 months')
# print(dev.get_info(1008))
# print(dev.coding())
# dev = FullStack('Python', 'JavaScript', '6 months')
# print(dev.get_info(2016))
# print(dev.coding())




from abc import abstractmethod, ABC

class Coder(ABC):
    def __init__(self, experience, count_code_time=0) -> None:
        self.experience = experience
        self.count_code_time = count_code_time

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def coding(self):
        pass

class Backend(Coder):
    def __init__(self, languages_backend, experience, count_code_time=0) -> None:
        super().__init__(experience, count_code_time)
        self.languages_backend = languages_backend

    def get_info(self, hours):
        self.count_code_time += hours
        return f"Backend Developer with {self.experience} of experience. Coding time: {self.count_code_time} hours."

    def coding(self):
        return "Coding as a backend developer."

class Frontend(Coder):
    def __init__(self, languages_frontend, experience, count_code_time=0) -> None:
        super().__init__(experience, count_code_time)
        self.languages_frontend = languages_frontend

    def get_info(self, hours):
        self.count_code_time += hours
        return f"Frontend Developer with {self.experience} of experience. Coding time: {self.count_code_time} hours."

    def coding(self):
        return "Coding as a frontend developer."

class FullStack(Backend, Frontend):
    def __init__(self, languages_backend, languages_frontend, experience, count_code_time=0) -> None:
        Backend.__init__(self, languages_backend, experience, count_code_time)
        Frontend.__init__(self, languages_frontend, experience, count_code_time)
    
    def get_info(self, hours):
        return super().get_info(hours)

    def coding(self):
        return "Coding as a full-stack developer."

dev = Backend('Python', '6 months')
print(dev.get_info(1008))
print(dev.coding())

dev = Frontend('JavaScript', '6 months')
print(dev.get_info(1008))
print(dev.coding())

dev = FullStack('Python', 'JavaScript', '6 months')
print(dev.get_info(2016))
print(dev.coding())
