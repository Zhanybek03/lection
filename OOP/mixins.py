# Mixins

# Миксины - классы которые используются для наследования и передачи дочерним классам опеределенных методов, но от них не создаются Объекты
# для чего:
# 1. вы хотите предоставить множество доп методов для классов
# 2. вы хотите использовать один конкретный метод во множеству разных классов


# class EngineMixin:
#     def start_engine(self):
#         print('started engine')
    
# class RadioMixin:
#     def play_radio(self):
#         print('music is playing')

# class Auto(EngineMixin, RadioMixin):
#     pass

# class Plane(EngineMixin):
#     pass

# class Smartphone(RadioMixin):
#     pass

# class Train(EngineMixin, RadioMixin):
#     pass


# class FlyMixin:
#     def fly(self):
#         print('I can fly!')

# class WalkMixin:
#     def walk(self):
#         print('I can walk!')
    
# class SwimMixin:
#     def swim(self):
#         print('I can swim!')



# class Human(WalkMixin, SwimMixin):
#     name = 'human'

#     def talk():
#         print('I can talk!')

# class Fish(SwimMixin):
#     name = 'fish'

# class Volans(SwimMixin, FlyMixin):
#     name = 'volan'

# class Duck(SwimMixin, FlyMixin, WalkMixin):
#     name = 'duck'

# obj = Human()
# obj.walk()
# obj.swim()
#####
#####
#####
#####
#####
#####
#####
##########
#####
#####
#####
#####
#####
#####
##########
#####
#####
#####
#####
#####
#####
##########
#####
#####
#####
#####
#####
#####
###