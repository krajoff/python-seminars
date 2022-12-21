import pandas as pd


def export_db(sn):
    df = pd.read_csv('db.csv', sep=' ')
    print(df.loc[df['Фамилия'] == sn])
