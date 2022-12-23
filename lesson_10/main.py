import telebot
from random import randint
import horoscope as hr
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

"""Command START"""


def rnd(message):
    rnd_number = randint(1, 6)
    if message.text == str(rnd_number):
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, вы угадали')
    else:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, вы не угадали. Я загадал {rnd_number}')


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = telebot.types.KeyboardButton('Игра "Угадай число"')
    button_2 = telebot.types.KeyboardButton('Черты знаков зодиака')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, 'Выбирите одну из функций чата', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == 'Игра "Угадай число"':
        msg = bot.send_message(message.chat.id,
                               f'{message.from_user.first_name}, я загадал число от 1 до 5. Угадай его.')
        bot.register_next_step_handler(msg, rnd)
    elif message.text == 'Черты знаков зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=3)
        im1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        im2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')
        im3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='Близнецы')
        im4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')
        im5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')
        im6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')
        im7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')
        im8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')
        im9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')
        im10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')
        im11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')
        im12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='Рыбы')
        markup.add(im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11, im12)
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, выбирите знак зодиака', reply_markup=markup)
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG97xjpcI8GWPgIb6GtV6Zaz_j8lir_AACCQADwDZPE-_NG6JK_3GVLAQ')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_button(call):
    bot.send_message(call.message.chat.id, hr.hr[call.data])


bot.polling(none_stop=True)
