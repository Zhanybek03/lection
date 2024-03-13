# Полиморфизм - способность метода(функции) использоваться в разных типах(классах)
# Широко распространенное определение: "один интерфейс - много реализаций"

# list.pop
# dict.pop
# set.pop

# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'It\'s a cat. Cats name is {self.name}, age: {self.age}')
#     def make_sound(self):
#         print('Meow, meow!')

# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'It\'s a dog. Cats name is {self.name}, age: {self.age}')
#     def make_sound(self):
#         print('Bark, Bark!')
        
# obj1 = Cat('Garfild', 5)
# obj1.info()
# obj1.make_sound()
# print()
# obj2 = Dog('Pluto', 7)
# obj2.info()
# obj2.make_sound()

class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        pass

    def info(self):
        print('Я геометрическая фигура!')

class Square(Shape):
    def __init__(self, length) -> None:
        super().__init__('Квадрат')
        self.len = length
    def area(self):
        return self.len ** 2
    def info(self):
        super().info()
        print('Все стороны равны и углы все 90 градусов!')

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__('Окружность')
        self.r = radius
    def area(self):
        from math import pi
        return round(pi * self.r ** 2, 2)
    def info(self):
        super().info()
        print('Диаметр равен двум радиусам!')

a = Square(8)
b = Circle(4)

a.info()
print(a.area())

b.info()
print(b.area())