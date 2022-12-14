def import_db(db):
    if (len(db.split())) == 4:
        with open('db.csv', 'a', encoding='cp1251') as file:
            file.write(db + '\n')
            print('Запись успешно добавлена')
    else:
        print('Введеные данные некорректны.')