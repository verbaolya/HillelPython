import pandas as pd

# Чтение данных из CSV-файла
df = pd.read_csv('data.csv')

# Удаление столбца с возрастом
df = df.drop(columns=['Age'])

# Поворот таблицы на 90 градусов
df_transposed = df.T

# Сохранение данных в Excel-файл
df_transposed.to_excel('data_transposed.xlsx', index=False)

print('Data has been transposed and written to data_transposed.xlsx.')
