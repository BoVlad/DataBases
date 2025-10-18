import pandas as pd

# Завантаження даних з файлу
df = pd.read_csv("movies_dataset.csv") #.dropna(

# Відобразимо перші 5 рядків
print(df.head)
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.dropna())
print(df.dropna(how='all'))
print(df.dropna(subset=['A', 'B']))