# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

#     @abstractmethod
#     def breathe(self):
#         pass


# class Lion(Animal):
#     def eat(self):
#         print('Meal')
#     def breathe(self):
#         print('Lungs')

# obj = Lion()
# obj.eat()

# Абстракция(Абстрактный класс) - его можно рассматривать как набор методов, которые должны быть созданы и реализованы во всех дочерних классах, которые были унаследованы от абстрактного класса.

# Абстрактный метод - это метод, у которго есть объявление но нет реализации

from abc import ABC, abstractmethod
from math import pi

# class Shape(ABC):
#     def __init__(self, name):
#         self.name = name
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, lenght):
#         super().__init__('kvadrat')
#         self.lenght = lenght

#     def area(self):
#         return self.lenght ** 2


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         return round(pi * self.radius ** 2, 2)

# a = Square(4)
# print(a.area())
# b = Circle(3)
# print(b.area())
# print(b.name)


##-----------##-----------##-----------##-----------##-----------##-----------##-----------##-----------##-----------

# class ChessPiece(ABC):
#     #Общий метод кототый будет использовать все наследники это класса
#     def draw(self):
#         print("Drew a chess piece")

#     #абстрактный метод который необходимо переопределить для каждого дочернего класса
#     @abstractmethod
#     def move(self):
#         pass

# class Queen(ChessPiece):
#     def move(self):
#         print('The Queen can move everywhere she wants diagonally, vertically, horizontally')

# class Pawn(ChessPiece):
#     def move(self):
#         print('The Pawn can move directly to one or two cells!')

# q = Queen()
# q.draw()
# q.move()

# p = Pawn()
# p.draw()
# p.move()