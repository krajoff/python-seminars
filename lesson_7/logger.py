from datetime import datetime as dt
from datetime import date


def logger(data):
    time = dt.now().strftime('%H:%M')
    day = date.today().strftime('%d/%m/%y')
    with open('log.csv', 'a') as file:
        file.write('{} {} {}\n'.format(day, time, data))
