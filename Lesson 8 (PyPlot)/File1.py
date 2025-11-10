import matplotlib.pyplot as plt

# Назви категорій
categories = ['USA', 'India', 'China', 'Germany', 'UK']

# Числові значення для кожної категорії
values = [20, 15, 30, 10, 25]

# Створення графіку з різними кольорами для кожного стовпця
colors = ['red', 'blue', 'green', 'purple', 'orange']
plt.bar(categories, values, color=colors)

# Підписи до осей
plt.xlabel('Країни')
plt.ylabel('Значення')
plt.title('Порівняння кількості для різних країн')

# Показуємо графік
plt.show()