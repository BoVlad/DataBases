import customtkinter as ctk
import sqlite3
import bcrypt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Система авторизації пентагона")
root.resizable(False, False)
root.geometry("500x240")

conn = sqlite3.connect('file3_db.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    hashed_password TEXT
)
''')
conn.commit()


def register():
    username_input = username_entry.get().strip()
    password_input = password_entry.get().strip()

    cursor.execute("SELECT username FROM userdata WHERE username = ?", (username_input,))
    existing = cursor.fetchall()

    if len(existing) > 0:
        info_label.configure(text="Такий користувач вже існує")
        username_entry.delete("0", "end")
        password_entry.delete("0", "end")
    else:
        if username_input and password_input != "":
            salt = bcrypt.gensalt()
            password_input_hashed = bcrypt.hashpw(password_input.encode('utf-8'), salt)
            cursor.execute("INSERT INTO userdata (username, hashed_password) VALUES(?, ?)",
                           (username_input, password_input_hashed))
            conn.commit()
            info_label.configure(text="Користувач додан")
            username_entry.delete("0", "end")
            password_entry.delete("0", "end")
        else:
            info_label.configure(text="Ви нічого не ввели!")
            username_entry.delete("0", "end")
            password_entry.delete("0", "end")

def login():
    username_input = username_entry.get().strip()
    password_input = password_entry.get().strip()

    cursor.execute("SELECT username, hashed_password FROM userdata WHERE username = ?", (username_input,))
    user_data = cursor.fetchall()

    if len(user_data) == 0:
        info_label.configure(text="Такого користувача немає")
        username_entry.delete("0", "end")
        password_entry.delete("0", "end")
        return

    if username_input and password_input != "":
        password_from_db = user_data[0][1]
        if bcrypt.checkpw(password_input.encode('utf-8'), password_from_db):
            username_entry.pack_forget()
            password_entry.pack_forget()
            register_button.pack_forget()
            login_button.pack_forget()
            info_label.configure(text="Авторизація успішна", text_color="white", font=("Arial", 40, "bold"))

        else:
            info_label.configure(text="Неправильний пароль")
            password_entry.delete("0", "end")
    else:
        info_label.configure(text="Ви нічого не ввели!")
        username_entry.delete("0", "end")
        password_entry.delete("0", "end")


info_label = ctk.CTkLabel(root, text="", text_color="red")
info_label.pack(pady=5)

username_entry = ctk.CTkEntry(root, width=300, placeholder_text="Username")
username_entry.pack(pady=5)
password_entry = ctk.CTkEntry(root, width=300, placeholder_text="Password")
password_entry.pack(pady=10)

register_button = ctk.CTkButton(root, text="Зареєструватися", width=200, command=register)
register_button.pack(pady=5)
login_button = ctk.CTkButton(root, text="Увійти у систему", width=200, command=login)
login_button.pack(pady=3)

root.mainloop()