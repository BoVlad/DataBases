# 1. Створи програму, яка дозволяє користувачеві зареєструватися, ввівши ім'я користувача та пароль;
#
# 2. Програму потрібно налаштувати так, щоб пароль хешувався за допомогою bcrypt перед збереженням у "базу даних" (у нашому випадку це просто список);
#
# 3. Додай функціонал для авторизації користувача: після введення імені користувача та пароля програма повинна перевіряти, чи співпадає введений пароль з хешем, збереженим у "базі даних";
#
# 4. Якщо все правильно – вивести повідомлення про успішну авторизацію, якщо пароль неправильний – вивести повідомлення про помилку.
#
# Приклад структури списку (він слугуватиме базою даних):
import sqlite3
import bcrypt

conn = sqlite3.connect('users_db.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    hashed_password TEXT
)
''')
conn.commit()

# cursor.execute("INSERT INTO dishes (dish_name, category, price, available) VALUES(?, ?, ?, ?)", (dish_name, category, price, available))
# conn.commit()
#
# cursor.execute("SELECT dish_name FROM dishes "
#                     "WHERE dish_name LIKE ?",('паста%',))
# print(cursor.fetchall())

while True:
    choice = input("Це система користувачів. 1 - Реєстрація, 2 - Логін, 3 - Вихід: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            username_input = input("Введіть ваш логін: ")
            password_input = input("Введіть ваш пароль: ")

            cursor.execute("SELECT username FROM userdata WHERE username = ?", (username_input,))
            existing = cursor.fetchall()

            if len(existing) > 0:
                print("Такий користувач вже існує!")
                continue

            salt = bcrypt.gensalt()
            password_input_hashed = bcrypt.hashpw(password_input.encode('utf-8'), salt)
            cursor.execute("INSERT INTO userdata (username, hashed_password) VALUES(?, ?)",
                               (username_input, password_input_hashed))
            conn.commit()
            print("Користувач додан!")
        elif choice == 2:
            username_input = input("Введіть ваш логін: ")
            password_input = input("Введіть ваш пароль: ")
            cursor.execute("SELECT username, hashed_password FROM userdata WHERE username = ?", (username_input,))
            user_data = cursor.fetchall()

            if len(user_data) == 0:
                print("Такого користувача немає.")
                continue

            username_from_db = user_data[0]
            password_from_db = user_data[0]
            if bcrypt.checkpw(password_input.encode('utf-8'), password_from_db):
                print(f"Авторизація успішна!")
                break
            else:
                print("Неправильний пароль!")
        elif choice == 3:
            break
        else:
            print("Такого вибору немає!")
    else:
        print("Ви не ввели цифру!")