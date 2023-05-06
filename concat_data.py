import pandas as pd


def read_csv_file(file_name):
    df = pd.read_csv(file_name, sep=';', decimal=',', parse_dates=[['Data', 'Hora (UTC)']]) # type: ignore
    df = df.rename(columns={'Data_Hora (UTC)': 'Data_Hora'})
    df = df.set_index('Data_Hora')
    return df


file_names = ['2016_since_03_06.csv',
              '2017.csv',
              '2018.csv',
              '2019.csv',
              '2020.csv',
              '2021.csv',
              '2022.csv',
              '2023_uni_05_05.csv']


# read files and concatenate ignoring index
df = pd.concat([read_csv_file(file_name) for file_name in file_names], ignore_index=True)

print(df.head())

# save to csv
df.to_csv('out/weather_data.csv')





