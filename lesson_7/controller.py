import user_interface as ui
import logger as lg
import export_db as edb
import import_db as idb


def button_click():
    rate = ui.introduce()
    if rate == 'э':
        edb.export_db()
        lg.logger('Выполнен поиск по фамилии')
    elif rate == 'и':
        data = input('Введите фамилию, имя, отчество и телефон через пробел: ')
        idb.import_db(data)
        lg.logger(f'Выполнена новая запить: {data}')
    else:
        print('Режим выбран некорректно. Повторите ввод ещё раз.')
        button_click()
