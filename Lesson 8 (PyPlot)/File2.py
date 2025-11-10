import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df = pd.read_csv("billionaires.csv")

# Підрахунок кількості мільярдерів у кожній індустрії
industry_counts = df["Industry"].value_counts()
industry_counts = industry_counts.sort_values(ascending=False).head(10)

# Побудова стовпчастої діаграми
plt.figure(figsize=(12, 6))
plt.bar(industry_counts.index, industry_counts.values, color=["gold", "blue", "green", "red"])

# Оформлення графіку
plt.xlabel("Індустрія")
plt.ylabel("Кількість мільярдерів")
plt.title("Розподіл мільярдерів за індустріями 💰")
plt.xticks(rotation=45) # Повертаємо підписи на осі X для зручності

# Показуємо графік
plt.show()