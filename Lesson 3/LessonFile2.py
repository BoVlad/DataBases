import sqlite3



conn = sqlite3.connect('restourant.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_name TEXT,
    category TEXT,
    price INTEGER,
    available INTEGER
)
''')

def new_dish(dish_name: str, category: str, price: int, available: bool):
    if available:
        available = 1
    else:
        available = 0
    cursor.execute("INSERT INTO dishes (dish_name, category, price, available) VALUES(?, ?, ?, ?)", (dish_name, category, price, available))
    conn.commit()

cursor.execute("SELECT dish_name FROM dishes "
                    "WHERE dish_name LIKE ?",('паста%',))
print(cursor.fetchall())



cursor.execute("SELECT dish_name FROM dishes "
                    "WHERE category LIKE ?",('основні страви%',))
print(cursor.fetchall())



cursor.execute("SELECT dish_name FROM dishes "
                    "WHERE price > 15 AND available = ?",('1',))
print(cursor.fetchall())

# Перевірка результату (вибірка всіх записів)
# cursor.execute("SELECT * FROM dishes")
# data = cursor.fetchall()
# for d in data:
#     print(d)
#
# print(cursor.fetchall())  # Вивести всі записи з таблиці
#
# # Закриття з'єднання
# conn.close()