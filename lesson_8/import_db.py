import pandas as pd


def import_db(db):
    if (len(db.split())) == 4:
        df = pd.DataFrame({'Фамилия': db.split()[0],
                           'Имя': db.split()[1],
                           'Отчество': db.split()[2],
                           'Телефон': db.split()[3]})
        df.to_csv('db.csv', index=False)
        print('Запись успешно добавлена')
    else:
        print('Введеные данные некорректны.')