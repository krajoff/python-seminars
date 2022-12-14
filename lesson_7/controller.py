import user_interface as ui
import logger as lg
import export_db as edb
import import_db as idb


def button_click():
    rate = ui.introduce()
    if rate == 'э':
        surname = input('Введите фамилию для поиска: ')
        if surname:
            edb.export_db(surname)
            lg.logger(f'Выполнен поиск по фамилии: {surname}')
        else:
            print('Фамилия не введена. Повторите ввод ещё раз.')
            button_click()
    elif rate == 'и':
        data = input('Введите фамилию, имя, отчество и телефон через пробел: ')
        idb.import_db(data)
        lg.logger(f'Выполнена новая запить: {data}')
    else:
        print('Режим выбран некорректно. Повторите ввод ещё раз.')
        button_click()
