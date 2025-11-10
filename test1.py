import customtkinter as ctk
from tkinter import filedialog
import os

# Настройка темы
ctk.set_appearance_mode("dark")  # dark / light / system
ctk.set_default_color_theme("blue")

# Главное окно
app = ctk.CTk()
app.title("Работа с файлами")
app.geometry("500x400")

# --- Глобальная переменная для хранения пути ---
current_file_path = None


# --- Функция: открыть файл ---
def open_file():
    global current_file_path
    file_path = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        textbox.delete("1.0", "end")
        textbox.insert("1.0", content)
        current_file_path = file_path
        status_label.configure(text=f"Открыт: {os.path.basename(file_path)}")


# --- Функция: сохранить в папку проекта ---
def save_file():
    global current_file_path
    save_path = os.path.join(os.getcwd(), "saved_text.txt")
    content = textbox.get("1.0", "end").strip()

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(content)

    status_label.configure(text=f"Файл сохранён в проект: {save_path}")


# --- Функция: сохранить как... ---
def save_file_as():
    global current_file_path
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if file_path:
        content = textbox.get("1.0", "end").strip()
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        current_file_path = file_path
        status_label.configure(text=f"Сохранено как: {os.path.basename(file_path)}")


# --- Элементы интерфейса ---
open_btn = ctk.CTkButton(app, text="📂 Открыть файл", command=open_file)
open_btn.pack(pady=10)

save_btn = ctk.CTkButton(app, text="💾 Сохранить в проект", command=save_file)
save_btn.pack(pady=5)

save_as_btn = ctk.CTkButton(app, text="📝 Сохранить как...", command=save_file_as)
save_as_btn.pack(pady=5)

textbox = ctk.CTkTextbox(app, width=450, height=200)
textbox.pack(pady=15)

status_label = ctk.CTkLabel(app, text="Файл не открыт", text_color="gray")
status_label.pack(pady=10)

# Запуск приложения
app.mainloop()