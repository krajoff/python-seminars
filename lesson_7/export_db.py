import pandas as pd


def export_db():
    with open('db.csv', 'r', encoding='cp1251') as file:
        for line in file:
            print(line, end='')
