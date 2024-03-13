# Создайте класс мобильного телефона. Определите атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.
class Mobile_tel:
    def __init__(self, imei, oc) -> None:
        self.imei = imei
        self.batery = 100 
        self.oc = oc
    def info(self):
        self.batery -= 0.5
        return self.batery
    def listen_music(self):
        self.batery -= 5
        return self.batery
    
    def watch_video(self):
        self.batery -= 7
        return self.batery
    def check_batery(self):
        if self.batery < 10:
            print(f'Вы не сможете просмативать видео!')
        elif self.batery == 100:
            raise 'Phone is full%'
        return self.batery
tel = Mobile_tel('4395779875983798', 'ios')
tel.info()
print(tel.listen_music())
print(tel.watch_video())
print(tel.check_batery())
        
        
        

