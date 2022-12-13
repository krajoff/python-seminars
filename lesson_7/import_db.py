def import_db(db):
    with open('db.csv', 'a', encoding='cp1251') as file:
        file.write(db)
