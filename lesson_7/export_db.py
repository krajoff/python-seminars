def export_db(sn):
    cnt = 0
    with open('db.csv', 'r', encoding='cp1251') as file:
        for line in file:
            if  line.split()[0] == sn:
                print(line, end='')
                cnt += 1
        if cnt == 0:
            print('Записи с такой фамилией не найдены.')
        else:
            print(f'Количество найденных записей: {cnt} шт.')
