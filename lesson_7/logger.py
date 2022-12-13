from datetime import datetime as dt


def logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} {}\n'.format(time, data))
