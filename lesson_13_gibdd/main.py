from commands import *
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler
)
from config import TOKEN

FIRSTNAME, SURNAME, DATE_EVENT, TIME_EVENT, PLACE_EVENT, MODEL, SIGN, EMAIL, CAPTCHA, PHOTO = range(10)
if __name__ == '__main__':
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CAPTCHA: [MessageHandler(Filters.text & ~Filters.command, captcha)],
            FIRSTNAME: [MessageHandler(Filters.text & ~Filters.command, firstname)],
            SURNAME: [MessageHandler(Filters.text & ~Filters.command, surname)],
            DATE_EVENT: [MessageHandler(Filters.text & ~Filters.command, date_event)],
            TIME_EVENT: [MessageHandler(Filters.text & ~Filters.command, time_event)],
            PLACE_EVENT: [MessageHandler(Filters.text & ~Filters.command, place_event)],
            MODEL: [MessageHandler(Filters.text & ~Filters.command, model)],
            SIGN: [MessageHandler(Filters.text & ~Filters.command, sign)],
            PHOTO: [MessageHandler(Filters.photo, photo)],
            EMAIL: [MessageHandler(Filters.text & ~Filters.command, email)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
        conversation_timeout=600
    )

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
