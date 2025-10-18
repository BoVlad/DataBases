import sqlite3
import customtkinter as ctk

updating = False
updating_name, updating_age = "", 0

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER

)
''')



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CTkSQLite")
app.geometry("600x450")

def filed_clearing():
    entry.delete(0, ctk.END)
    entry2.delete(0, ctk.END)

def grammatic():
    if entry.get() == "":
        label.configure(text="Поля вводу імені не повинно бути пустим!")
        return None
    else:
        if len(entry.get()) < 25:
            name = entry.get()
        else:
            label.configure(text="Ім'я завелике!")
            return None
    if entry2.get() == "":
        label.configure(text="Поля вводу віку не повинно бути пустим!")
        return None
    else:
        if not entry2.get().isdigit():
            label.configure(text="Поля вводу віку не повинно містити букви!")
            return None
        else:
            age = int(entry2.get())
            if not 5 < age < 100:
                label.configure(text="Вік або завеликий, або замаленький")
                return None
    return name, age

def new_info_on_screen():
    global cursor
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    text1 = "ID\n\n"
    text2 = "NAME\n\n"
    text3 = "AGE\n\n"
    for i in data:
        text1 = text1 + f"{str(i[0])}\n"
        text2 = text2 + f"{str(i[1])}\n"
        text3 = text3 + f"{str(i[2])}\n"
    label_info1.configure(text=text1)
    label_info2.configure(text=text2)
    label_info3.configure(text=text3)

def button_add_info():
    global cursor
    try:
        name, age = grammatic()
    except TypeError:
        return
    cursor.execute("INSERT INTO users (name, age) VALUES(?, ?)", (name, age))
    conn.commit()
    filed_clearing()
    new_info_on_screen()

def button_update_info():
    global cursor, updating, updating_name, updating_age
    if updating:
        if entry.get() != "" and entry.get().isdigit():
            cursor.execute("UPDATE users SET name = (?), age = (?) WHERE id = (?)",
                           (updating_name, updating_age, int(entry.get())))
        else:
            try:
                name, age = grammatic()
            except TypeError:
                return
            cursor.execute("UPDATE users SET name = (?), age = (?) WHERE name = (?) and age = (?)",
                           (updating_name, updating_age, name, age))
            conn.commit()
            button2.configure(text="Оновлення інформації (Введіть на \nщо змінити, а потім що змінити \n(або айді у полі імені)")
            filed_clearing()
            updating = False
    else:
        try:
            updating_name, updating_age = grammatic()
        except TypeError:
            return
        button2.configure(text="А потім що змінити \n(або айді у полі імені))\nНатисніть для підтвердження")
        filed_clearing()
        updating = True
    filed_clearing()
    new_info_on_screen()

def button_delete_info():
    global cursor
    try:
        name, age = grammatic()
    except TypeError:
        return
    cursor.execute("DELETE from users WHERE name like (?) AND age like (?)", (name, age))
    conn.commit()
    filed_clearing()
    new_info_on_screen()



label = ctk.CTkLabel(app, text="Це тест SQL на CTk")
label.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Ім'я")
entry.pack(pady=10)

entry2 = ctk.CTkEntry(app, placeholder_text="Вік")
entry2.pack()


button = ctk.CTkButton(app, text="Додавання інформації", command=button_add_info)
button.place(relx=0.2, rely=0.35, anchor="center")

button2 = ctk.CTkButton(app, text="Оновлення інформації (Введіть на \nщо змінити, а потім що змінити \n(або айді у полі імені)",
                        command=button_update_info, font=ctk.CTkFont(size=10))
button2.place(relx=0.5, rely=0.35, anchor="center")

button3 = ctk.CTkButton(app, text="Видалення інформації", command=button_delete_info)
button3.place(relx=0.8, rely=0.35, anchor="center")

label2 = ctk.CTkLabel(app, text="База даних:")
label2.place(relx=0.5, rely=0.43, anchor="center")

label_info1 = ctk.CTkLabel(app, text="")
label_info1.place(relx=0.08, rely=0.46, anchor="nw")

label_info2 = ctk.CTkLabel(app, text="")
label_info2.place(relx=0.4, rely=0.46, anchor="nw")

label_info3 = ctk.CTkLabel(app, text="")
label_info3.place(relx=0.7, rely=0.46, anchor="nw")


new_info_on_screen()

app.mainloop()