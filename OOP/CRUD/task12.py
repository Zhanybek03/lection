# Задача 1: "Dollar"
# Цель: Создать функцию dollarize, преобразующую числа в долларовый формат, и класс MoneyFmt для управления денежными суммами.
# Описание:
# Функция dollarize должна принимать дробное число и возвращать строку, представляющую сумму в долларовом формате.
# Класс MoneyFmt использует внутренний атрибут amount для хранения денежной суммы и предоставляет методы для обновления суммы, возвращения ее как строки в долларовом формате и как исходного числового значения.
# Пример использования:
# cash = MoneyFmt(12345678.021) 
# print(cash) -- выводит "$12,345,678.02" 
# cash.update(100000.4567) 
# print(cash) -- выводит "$100,000.46" 
# cash.update(-0.3) 
# print(cash) -- выводит "-$0.30" 
# repr(cash) -- выводит -0.3 

class MoneyFmt:
    def __init__(self, amount):
        self.amount = round(amount, 2)

    def update(self, new_amount):
        self.amount = round(new_amount, 2)

    def __repr__(self):
        return str(self.amount)

    def __str__(self):
        sign = '-' if self.amount < 0 else ''
        dollars, cents = divmod(abs(self.amount), 1)
        dollars = "{:,.0f}".format(dollars)
        cents = "{:0.2f}".format(cents)
        return f"{sign}${dollars}.{cents[2:]}"

def dollarize(number):
    return MoneyFmt(number)

cash = dollarize(12345678.021)
print(cash)  

cash.update(100000.4567)
print(cash) 

cash.update(-0.3)
print(cash) 

print(repr(cash)) 






# Задача 2: "Велосипед"
# Цель: Реализовать класс Bike, моделирующий велосипед с различными атрибутами и методами управления.
# Описание:
# Класс должен содержать атрибуты для стоимости, производителя, модели, года выпуска, состояния, цены продажи и статуса продажи.
# Методы должны позволять устанавливать цену продажи, учитывая минимальную прибыль, обслуживать велосипед, изменяя его состояние и стоимость ремонта, и продавать велосипед, изменяя его статус и рассчитывая прибыль.
# class Bike:
#     def init(self, cost, cost_remont, manufacturer, model, year, condition=None, selling_price=0, status=False) -> None:
#         self.cost_remont = cost_remont
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self.selling_price = selling_price
#         self.status = status
#         self.cost = cost

#     def set_sel_price(self, price):
#         self.selling_price = price

#     def pribyl(self, cost_remont):
#         res = self.selling_price - (cost_remont  + self.cost)
#         return f'Min profit: {res}'
    
#     def cond(self, cost_rem):
#         self.cost_remont = cost_rem
#         if 0 < cost_rem <= 1000:
#             self.condition = 'not bad'
#         elif 1000 < cost_rem <= 2000:
#             self.condition = 'good'
#         else:
#             self.condition = 'excellent'

#     def sel_bike(self, sel_price):
#         profit = sel_price - (self.cost  + self.cost_remont)
#         self.status = True
#         return f'Bike selling, Profit: {profit}'

# bike = Bike(10000, 0, 'bmx', '019', '2004')

# bike.set_sel_price(15000)
# print(bike.pribyl(2000)) 
# print(bike.cond(2000))
# print(bike.sel_bike(14000))





# Задача 3: "Герой"
# Цель: Разработать программу, имитирующую взаимодействие между солдатами и героями в контексте игры-стратегии.
# Описание:
# Необходимо создать классы для солдат и героев, каждый с уникальным номером и принадлежностью к команде.
# Солдаты могут "следовать" за героями своей команды, а герои могут повышать свой уровень.
# В программе должны генерироваться солдаты для двух команд, после чего сравнивается количество солдат в каждой команде, и у героя команды с большим числом солдат повышается уровень.
import random

class Hero:
    def __init__(self, unique_num, team, level=0) -> None:
        self.unique = unique_num
        self.team = team 
        self.level = level

    def level_up(self):
        self.level += 1
        return self.level


class Soldiers:
    def __init__(self, unique_num, team) -> None:
        self.unique = unique_num
        self.team = team 



soldiers = [Soldiers(i, random.choice(["DC", "Marvel"])) for i in range(100)]   
soldiers2 = [Soldiers(i, random.choice(["DC", "Marvel"])) for i in range(100)]   
superman = Hero(123, 'DC')
spiderman = Hero(124, 'Marvel')

def count_sold(soldiers):
    count_superman = 0
    count_spiderman = 0
    for i in soldiers:
        if i.team == superman.team:
            count_superman += 1
        else:
            count_spiderman += 1

    return superman if count_superman > count_spiderman else spiderman

a = count_sold(soldiers)
b = count_sold(soldiers2)
print(a.level_up(), a.team, a.unique) 
print(b.level_up(), b.team, b.unique) 


        






    
        




