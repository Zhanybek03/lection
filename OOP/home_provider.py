# 1# Напишите класс Subscriber, у которого есть переменные экземпляра:
# # firstname
# # lastname

# 2# Сделайте так, чтобы метод __repr__ возвращал firstname + lastname
# # Напишите класс Provider, у которого есть:
# # переменный экземпляра name -- название провайдера
# # переменный экземпляра subscribers -- список, в котором будут храниться экземпляры класса Subscriber
# # переменный экземпляра payments -- словарь, ключём которого является экземпляр класса Subscriber, значением является сумма (вещественное число)
# # метод register_payment, который принимает экземпляр класса Subscriber, и сумму, затем проверяет, есть ли такой экземпляр Subscriber в списке subscribers. 
# # Если есть, записывает экземпляр в словарь payments в качестве ключа, а сумму в качестве значения
# # Если нет, выкидывает (raise) ошибку ValueError

class Subscriber:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
    def __repr__(self):
       return self.firstname + self.lastname
class Provider:
    name = 'Beeline'
    subscribers = []
    payment = {}
    def register_payment(self, subscriber, amount):
        if subscriber in self.subscribers:

            self.payment [subscriber]=amount
        else:
            raise ValueError
    def add(self, subscriber):
        self.subscribers.append(subscriber)

obj = Subscriber('Azamat', 'Mukambetov')
obj.__repr__()
obj2 = Provider()
obj2.add(obj)
obj2.register_payment(obj, 3000)
print(obj2.payment,)
        
# 3# Напишите класс Terminal, у которого есть
# # переменная экземпляра amount = 0
# # переменная экземпляра providers = [ ]
# # Регистрировать провайдера через метод register, который принимает экземпляр класса Provider и добавляет в providers
# # Принимать деньги в счет провайдера (pay), который принимает экземпляр класса Provider, экземпляр класса Subscriber и сумму (вещественное число). Внутри метода должен вызываться метод register_payment экземпляра класса Provider. register_payment успешно сработал, то в переменую amount нужно добавить сумму.


class Terminal:
    amount = 0
    prooviders = []
    def register(self, provider):
        self.prooviders.append(provider)
    def pay(self, provider, subscriber, amount):
        provider.register_payment(subscriber, amount)
        self.amount += amount
        return f'{self.amount} успешно срботало!'
obj3 = Terminal()
obj3.register(obj2)
print(obj3.pay(obj2, obj, 3000))
print(obj3.amount)



    