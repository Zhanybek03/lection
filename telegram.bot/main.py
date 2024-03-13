import telebot
from telebot import types
import random

token = '6818272082:AAFzeZILLrapjtJEuHiY2pk7lLOrpmRcdrY'


bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Играть!')
btn2 = types.KeyboardButton('Нет, я Пас!')
keyboard.add(btn1, btn2)


@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Привет Чемпион, начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Играть!':
        bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапазоне от 1 до 10 вкючительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)')
        number = random.randint(1, 10)
        print(number)
        game(message, 3, number)
    elif message.text == 'Нет, я Пас!':
        bot.send_message(message.chat.id, 'Нет так нет, Пока!')
    else:
        bot_message = bot.send_message(message.chat.id, 'Вы ввели неправильный ответ!\nВведите снова:', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)
def game(message, attempts, number):
    message_bot = bot.send_message(message.chat.id, 'Угадай число: ')
    bot.register_next_step_handler(message_bot, check_number, attempts-1, number)
    
def check_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Вы победили! Нарекаю вас удачливым!')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'You\'ve lost again and again!\n But you\'re still looking at your dreams!\nIt\'s not over until you win!')
        # with open('marko.mp3', 'rb') as file:
        #     bot.send_audio(message)
    else:
        bot.send_message(message.chat.id, 'Нет ты не угадал число, попробуй еще раз({attempts})!')
        game(message, attempts, number)


bot.polling()