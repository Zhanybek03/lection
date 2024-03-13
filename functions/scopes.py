# Облясти видимости и пространство имен (scopes)
# тезнология которая определяет контекст имени, в рамках которого мы можем ее использовать

# a = 5 

# def func():
#     b = 10
#     print(a)
#     print(b)

# func()
# # print(b)

# build-ins(встроеннная область видимости) - print(), len()
# global(глобальная) - область одного файла
# <enclosed>(замкнутая (не локальная, non local))
# local(локальная) -> область внутри одной функции

# a =10 # global
# print # built-in

# def hello(): #global
#     a = 'Hello' # local
#     print(a, 'total, inside in func!')    


# hello()
# print(a, 'global')

# LEGB - local enclosed global built-in
        # ------------>>>>>>>>>>>

#-------------------------------
# enclosed 
# - замкнутое просторанство имен - локальное пространство, у которого естьт внутреннее(вложенное) локальное пространство

# x = 'global'
# print(x, '1') # global

# def enclosed(): # global
#     x = 'enclosed'

#     def local(): #enclosed
#         x = 'local'
#         print(x, '3') # local
    
#     print(x, '2') # enclosed
#     local()
#     print(x, '4') # enclosed

# enclosed()
# print(x, '5') # global
 

# var = 0


# def increment(): #LEGB
#     global var 
#     var = var + 1

# increment()

# print(var)

# global -> позваляет изменить значение глобальной переменной внутри локальной области

# nonlocal -> позваляет изменить значение не локальной(замкнуутой) переменной находясь внутри локальной области

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c_steps = counter()

# c_jumps = counter()

# print(c_steps)
# for _ in range(1, 10000):
#     c_steps()

# print(c_steps(), 'steps')
# print(c_jumps(), 'jumps')
# print(c_jumps(), 'jumps')
# print(c_jumps(), 'jumps')