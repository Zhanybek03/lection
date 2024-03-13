# Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .
# class Car:
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.horsepower = 85
#     def get_auto(self):
#         print(f'Это машина {self.brand} год машины {self.year} цвет машины {self.color}')
#     def get_year(self):
#         print(f'Возраст вашего автомобиля: {2024 - self.year}')
    
#     def add_horsepower(self):
#         if self.brand == 'Mers':
#             self.horsepower += 40
#         elif self.brand == 'Bmw':
#             self.horsepower += 40
#         elif self.brand == 'Porshe':
#             self.horsepower += 40
#         else:
#             self.horsepower += 20
#             print(f'Это машина {self.brand}, лошадинных сил {self.horsepower}') 
# res = Car('Bmw', 2023, 'White-Black')
# res.get_auto() 
# res.get_year()
# res.add_horsepower()

# Добавьте атрибут horsepower, который равен 85.

# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

# Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.

# Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto





# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

# Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода для каждого студента.
# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def get_student(self):
#         print(f'information of stusents: Name: {self.name} Age: {self.age} Course: {self.course}')
#     def get_birth_year(self):
#         print(f'Год рождения студента: {2024 - self.age}')

# students = Student('Rinat', 19, 2)
# students.get_student()
# students.get_birth_year()