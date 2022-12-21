import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
from datetime import datetime as dt
from datetime import date

"""Command START"""


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    export_db = telebot.types.KeyboardButton('Найти запись по фамилии')
    import_db = telebot.types.KeyboardButton('Добавить запись в БД')
    markup.add(export_db, import_db)
    bot.send_message(message.chat.id, 'Выбирите режим работы с базой данных', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_message(message):
    msg = message.text
    msg_list = msg.split()
    if msg == 'Найти запись по фамилии':
        bot.send_message(message.chat.id, 'Для поиска введите форму вида"/s Яшин"')
    elif msg_list[0] == '/s':
        if msg_list[1]:
            export_db(msg_list[1], message)
            logger(f'Выполнен поиск по фамилии: {msg_list[1]}')
        else:
            bot.send_message(message.chat.id, 'Фамилия не введена. Повторите ввод ещё раз.')
    elif msg == 'Добавить запись в БД':
        bot.send_message(message.chat.id, 'Для добавления введите форму вида "/d Яшин Николай Константинович 7-999-531-666"')
    elif msg_list[0] == '/d':
        if msg_list[1:]:
            data = ' '.join(msg_list[1:])
            import_db(data, message)
            logger(f'Выполнена новая запить: {data}')
        else:
            bot.send_message(message.chat.id, 'Данные не введены. Повторите ввод ещё раз.')
    else:
        bot.send_message(message.chat.id, 'Неверный ввод')


def export_db(sn, message):
    cnt = 0
    with open('db.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if line.split()[0] == sn:
                bot.send_message(message.chat.id, line)
                cnt += 1
        if cnt == 0:
            bot.send_message(message.chat.id, 'Записи с такой фамилией не найдены')


def import_db(db, message):
    if (len(db.split())) == 4:
        with open('db.csv', 'a', encoding='utf-8') as file:
            file.write(db + '\n')
            bot.send_message(message.chat.id, 'Запись успешно добавлена')
    else:
        bot.send_message(message.chat.id, 'Введеные данные некорректны.')


def logger(data):
    time = dt.now().strftime('%H:%M')
    day = date.today().strftime('%d/%m/%y')
    with open('log.csv', 'a') as file:
        file.write('{} {} {}\n'.format(day, time, data))


bot.polling(none_stop=True)
