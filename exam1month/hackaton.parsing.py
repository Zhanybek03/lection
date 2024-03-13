# Hackathon: Parsing
# 100 баллов
# Проекты на выбор по уровням сложности.
# Сложность: Легкая - 80 б.
# Сложность: Средняя - 90 б.
# Сложность: Сложная -100 б.


# 1)ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: легкая)
# Вы должны спарсить сайт
# https://www.kivano.kg/mobilnye-telefony. Как результат вы должны
# получить:
# 1. Наименование всех телефонов
# 2. Цену каждого продукта(в KGS)
# 3. И ссылка к фотографии
# 4. Все это записать в CSV файл
# Дополнительно(по желанию):
# 1. Ваш парсинг скрипт должен выполняться каждые 60 минут

# from bs4 import BeautifulSoup
# import requests
# import csv
# import lxml

# url = 'https://www.kivano.kg/mobilnye-telefony'
# html = requests.get(url)
# # def parsing_phone(url):
# response = requests.get(url)
# soup = BeautifulSoup(html.text, 'lxml')
# # print(soup)
# container = soup.find('div', class_="product-index product-index oh")
# phones = container.find_all('div', class_="item product_listbox oh")
# result = []
# for phone in phones:
#     name = phone.find('div', class_="listbox_title oh").text.strip()
#         # print(name)
#     img = phone.find('img', class_="" ).get('src')
#     price = phone.find('div', class_="listbox_price text-center").text.strip()
#     data = {'name': name, 'price': price, 'img':'https://www.kivano.kg' + img}
#     result.append(data)
# for item in result:
#         print(item)
#     # return result

# # print(parsing_phone(url))

# def prepare_csv():
#     with open('mobilka.csv', 'w') as file:
#         fieldnames = ['№', 'name', 'img', 'price']
#         writer =csv.DictWriter(file, fieldnames)
#         writer.writerow({
#             '№': '№',
#             'name': 'Name:',
#             'img': 'Image Url:',
#             'price': 'Price:',
#         })
# def write_to_scv(data, count):
#     with open('mobilka.csv', 'a') as file:
#         # global count
#         fieldnames = ['№', 'name', 'img', 'price']
#         writer =csv.DictWriter(file, fieldnames)
#         for mobilka in data:
#             writer.writerow({
#                 '№': count,
#                 'name':  mobilka['name'],
#                 'price': mobilka['price'],
#                 'img': mobilka['img']
#             })
#             count += 1
#     return count
 
# count = 1
# prepare_csv()
# count = write_to_scv(result, count)

# 2)ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя)
# ● Спарсить kolesa.kz, категорию:
# 1.Название всех моделей.
# 2.Цену всех моделей
# 3.Изображение всех моделей
# 4.Краткое описание всех моделей
# 5.Записать все в csv файл


# 2 )# 'https://auto312.kg/'
# вытащите цену, 
# описание, 
# фотки, 
# # номер продавца
# from bs4 import BeautifulSoup
# import requests
# import csv
# import lxml

# url = 'https://auto312.kg/'

# html = requests.get(url)
# soup = BeautifulSoup(html.text, 'lxml')
# # print(soup)
# container = soup.find('div', class_="dj-items-rows")
# cars = container.find_all('div', class_="item_row_in")
# # print(cars)
# result = []
# for car in cars:
#     name = car.find('div', class_="item_title").text.strip()
#     price = car.find('div', class_="item_price").text.strip()
#     desc =car.find('div', class_="item_content_in").text.strip()
#     img = car.find('img', class_="").get('src')
#     data = {'name': name, 'price': price, 'desc': desc, 'img':'https://www.auto312.kg' + img}
#     # print(data)
#     result.append(data)
# print(result)
# for item in result:
#     print(item)
# def prepare_csv():
#     with open('cars.csv', 'w') as file:
#         fieldnames = ['№', 'name', 'price', 'desc', 'img']
#         writer =csv.DictWriter(file, fieldnames)
#         writer.writerow({
#             '№': '№',
#             'name': 'Name:',
#             'price': 'Price:',
#             'desc': 'desc:',
#             'img': 'Image Url:'
#         })
# def write_to_scv(data, count):
#     with open('cars.csv', 'a') as file:
#         fieldnames = ['№', 'name', 'price', 'desc', 'img']
#         writer =csv.DictWriter(file, fieldnames)
#         for auto in data:
#             writer.writerow({
#                 '№': count,
#                 'name':  auto['name'],
#                 'price': auto['price'],
#                 'desc': auto['desc'],
#                 'img': auto['img']
#             })
#             count += 1
#     return count
 
# count = 1
# prepare_csv()
# count = write_to_scv(result, count)







# 3)ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: тяжелая)
# 1. При нажатии на кнопку start, телеграмм бот должен
# зайти на сайт KaktusMedia (https://kaktus.media/) и
# спарсить категорию “Все новости”
# 2. При вводе текста должны выйти первые 20
# заголовков статей с нумерацией. Должна быть
# возможность выбрать новости по нумерации или id
# (по желанию)
# 3. После выбора новости по нумерации, телеграмм
# бот должен отправить сообщение в виде “some
# title news you can see Description of this news
# and Photo” и пользователь отправит текст (либо
# нажмет кнопку) Description, то бот должен
# отправить описание именно текущего поста, также
# аналогично с Photo.
# 4. При нажатии на кнопку «Quit» бот должен
# отправить сообщение “До свидания“

from bs4 import BeautifulSoup
import requests
import csv
import lxml


url = 'https://kaktus.media/?lable=8&date=2024-02-15&order=time'

html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
container = soup.find('div', class_="Tag--articles")
sites = container.find_all('div', class_="ArticleItem")
# print(sites)
count = 1
result = {}
for site in sites:
    name = site.find('a', class_='ArticleItem--name').text.strip()
    desc = site.find('a', class_='ArticleItem--name').get('href')
    img = site.find('img').get('src')
    data = {'name': name, 'desc': desc, 'img': img}
    result[str(count)] = data
    count += 1
# print(result)

import telebot
from telebot import types
# import random

token = '6818272082:AAFzeZILLrapjtJEuHiY2pk7lLOrpmRcdrY'


bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Name')
btn2 = types.KeyboardButton('Description')
btn3 = types.KeyboardButton('Image')
keyboard.add(btn1, btn2, btn3)


@bot.message_handler(commands=['start'])
def start_message(message):
    res ='\n'.join([f'{k} --> {v["name"]}' for k, v in result.items()])
    # print(res)
    bot_message = bot.send_message(message.chat.id,res)
    bot_message = bot.send_message(message.chat.id,'Выберите новость: ')
# @bot_message = bot.send_message(bot_message, desc)
bot.message_handler(commands=['Name'])

def choice_user(message):
    if message.text in result:
        bot_message = bot.send_message(message.chat.id,'Вам описание фотки?',reply_markup=keyboard)
        # bot_message = bot.send_message(bot_message, desc)
    else:
        bot_message = bot.send_message(message.chat.id,'нет такой новости!')





    
bot.polling()


# def check_answer(message):
#     if message.text == result:
#         bot.send_message(message.chat.id, 'some title news you can see Description of this news and Photo', reply_markup=keyboard)


#         number = random.randint(1, 10)
#         print(number)
#         game(message, 3, number)
#     elif message.text == 'Нет, я Пас!':
#         bot.send_message(message.chat.id, 'Нет так нет, Пока!')
#     else:
#         bot_message = bot.send_message(message.chat.id, 'Вы ввели неправильный ответ!\nВведите снова:', reply_markup=keyboard)
#         bot.register_next_step_handler(bot_message, check_answer)
# def game(message, attempts, number):
#     message_bot = bot.send_message(message.chat.id, 'Угадай число: ')
#     bot.register_next_step_handler(message_bot, check_number, attempts-1, number)
    
# def check_number(message, attempts, number):
#     if message.text == str(number):
#         bot.send_message(message.chat.id, 'Вы победили! Нарекаю вас удачливым!')
#     elif attempts == 0:
#         bot.send_message(message.chat.id, 'You\'ve lost again and again!\n But you\'re still looking at your dreams!\nIt\'s not over until you win!')
#         # with open('marko.mp3', 'rb') as file:
#         #     bot.send_audio(message)
#     else:
#         bot.send_message(message.chat.id, 'Нет ты не угадал число, попробуй еще раз({attempts})!')
#         game(message, attempts, number)


# bot.polling()





# # Рекомендации:
# # 1. BeautifulSoup
# # 2. CSV
# # 3. lxml
# # 3. Requests

