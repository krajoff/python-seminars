import random
import time
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler
)

from set_field import set_field
from correct_empty import correct_empty
from skip_get import first_page_skip, get_captcha
from create_driver import photo_path

FIRSTNAME, SURNAME, DATE_EVENT, TIME_EVENT, PLACE_EVENT, MODEL, SIGN, EMAIL, CAPTCHA, PHOTO = range(10)
data = {"firstname": "", "surname": "", "email": "", "time": "",  "date": "",
        "year": "", "place": "", "model": "", "sign": "", "photo": "",  "captcha": ""}
END = ConversationHandler.END


def start(update, _):
    update.message.reply_text(
        'Полуавтоматическая система подачи обращения на '
        'парковку на тратуаре. Команда /cancel, чтобы '
        'прекратить работу.\n\n Введите ваше имя')
    return FIRSTNAME


def firstname(update, _):
    first_page_skip()
    data["firstname"] = update.message.text
    update.message.reply_text(
        'Введите вашу фамилию'
    )
    return SIGN


def surname(update, _):
    data["surname"] = update.message.text
    update.message.reply_text(
        'Введите дату нарушения (например, 12.09.2023)'
    )
    return DATE_EVENT


def date_event(update, _):
    data["date"] = update.message.text
    update.message.reply_text(
        'Введите время нарушения (например, 13:00)'
    )
    return TIME_EVENT


def time_event(update, _):
    data["time"] = update.message.text
    update.message.reply_text(
        'Введите место нарушения '
        '(например, ул. Мариинская, д. 1)'
    )
    return PLACE_EVENT


def place_event(update, _):
    data["place"] = update.message.text
    update.message.reply_text(
        'Введите марку автомобиля (например, BMW)'
    )
    return MODEL


def model(update, _):
    data["model"] = update.message.text
    update.message.reply_text(
        'Введите регистрационный знак '
        'автомобиля (например, х666хх66)'
    )
    return SIGN


def sign(update, _):
    data["sign"] = update.message.text
    update.message.reply_text(
        'Загрузите файл, где видно нарушение')
    return PHOTO


def photo(update, _):
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(photo_path)
    data["photo"] = photo_path
    update.message.reply_text(
        'Введите действующую электронную почту. '
        'На неё придёт код подтверждения от МВД')
    return EMAIL


def email(update, _):
    data["email"] = update.message.text
    update.message.reply_text('Введите изображение с кэпчи')
    file_path = get_captcha()
    update.message.bot.send_photo(update.message.chat.id, open(file_path, 'rb'))
    return CAPTCHA


def captcha(update, _):
    data["captcha"] = update.message.text
    correct_data = correct_empty(data)
    update.message.reply_text('Все данные введены. '
                              'Формируется отбращение')
    set_field(correct_data)
    return END


def cancel(update, _):
    update.message.reply_text('До новых встреч')
    return END
