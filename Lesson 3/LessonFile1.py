import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('my_database.db')

# Створення курсора
cursor = conn.cursor()

# Створення таблиці (якщо її ще немає)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
    
)
''')

# Вставка одного запису
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")

# Підтвердження змін
conn.commit()

# Перевірка результату (вибірка всіх записів)
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()
for d in data:
    print(d)

print(cursor.fetchall()) # Вивести всі записи з таблиці

# Закриття з'єднання
conn.close()