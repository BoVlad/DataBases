# 1. Побудуй стовпчастий графік, який показує середній бюджет фільмів по країнах виробництва
#    (вибери топ-10 країн з найбільшим бюджетом);
# 2. Побудуй лінійний графік, який демонструє зміну загального доходу (grossWorldWide) фільмів за роками;
# 3. Побудуй кругову діаграму, яка показує розподіл фільмів за жанрами
#    (групуй фільми за жанром і покажи, скільки фільмів належать до кожного жанру)

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('movies_dataset.csv').dropna()

data1 = df["budget"].sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(df["countries_origin"][data1.index], data1.values, color=["gold", "blue", "green", "red"])


plt.xlabel("Бюджети")
plt.ylabel("Бюджет")
plt.title("Країна")
plt.xticks(rotation=45)


plt.show()




data2 = (df.groupby("Year")["grossWorldWide"]).sum()


# Створюємо лінійний графік
plt.figure(figsize=(10,6))
plt.plot(data2.index, data2.values, marker='o', color='b')

# Додаємо заголовок та підписи до осей
plt.title('Зміна загального доходу', fontsize=14)
plt.xlabel('Рік', fontsize=12)
plt.ylabel('Загалний дохід', fontsize=12)

# Показуємо графік
plt.grid(True)
plt.show()

# plt.figure(figsize=(10,6))
# plt.plot(brazil_data['Year'], brazil_data['Share of population with at least some basic education'], marker='o', color='b')
#
#
# plt.title('Зміни частки населення з базовою освітою в Бразилії', fontsize=14)
# plt.xlabel('Рік', fontsize=12)
# plt.ylabel('Частка населення з базовою освітою (%)', fontsize=12)


# plt.grid(True)
# plt.show()