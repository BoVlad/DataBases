import pandas as pd
import customtkinter as ctk
from matplotlib import pyplot
import os
from tkinter import ttk


df = None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("PPReader")
app.geometry("1200x750")
app.resizable(False, False)


files = os.listdir()
files = [i for i in files if i.endswith(".csv")]

info_label = ctk.CTkLabel(master=app, text="Інформація", font=ctk.CTkFont(size=50))

method_select = ctk.CTkOptionMenu(
    master=app,
    values=["Кількість",
            "Середнє значення",
            "Стандартне відхилення",
            "Нижній квартиль (25%)",
            "Медіана (50%)",
            "Верхній квартиль (75%)",
            "Максимум",
            "Мода"]
)

column_select = ctk.CTkOptionMenu(
    master=app
)

copy_button = ctk.CTkButton(app, text="Копіювати", font=ctk.CTkFont(size=35))
button_info_reader = ctk.CTkButton(master=app, text="Інформація")
button_diagram = ctk.CTkButton(master=app, text="Діаграма")

def info_opening(choice):
    global df
    df = pd.read_csv(choice).dropna()
    df_columns = list(df.columns)
    df_operable_columns = list(df.select_dtypes(include=["number"]).columns)
    df_describe = df.describe()
    df_mode = df.mode()
    def button_info_def():
        decorlabel2.place(rely=0.86, relx=-0.08, anchor="w")
        info_label.place(rely=0.18, relx=0.02, anchor="nw")

        if not df_columns:
            method_select.set("Тут немає даних")
        else:
            method_select.set("Виберіть метод")
        method_select.place(rely=0.25, relx=0.85, anchor="center")

        column_select.configure(values=df_operable_columns)
        if not df_columns:
            column_select.set("Тут немає даних")
        else:
            column_select.set("Виберіть колонку")
        column_select.place(rely=0.3, relx=0.85, anchor="center")

        def option_menu_info_def(*_):
            ms = method_select.get()
            cs = column_select.get()
            if (ms != "Тут немає даних" and ms != "Виберіть метод"
                    and cs != "Тут немає даних" and cs != "Виберіть колонку"):
                if ms == "Кількість":
                    info_label.configure(text=df_describe[cs]["count"])
                elif ms == "Середнє значення":
                    info_label.configure(text=df_describe[cs]["mean"])
                elif ms == "Стандартне відхилення":
                    info_label.configure(text=df_describe[cs]["std"])
                elif ms == "Нижній квартиль (25%)":
                    info_label.configure(text=df_describe[cs]["25%"])
                elif ms == "Медіана (50%)":
                    info_label.configure(text=df_describe[cs]["50%"])
                elif ms == "Верхній квартиль (75%)":
                    info_label.configure(text=df_describe[cs]["75%"])
                elif ms == "Максимум":
                    info_label.configure(text=df_describe[cs]["max"])
                elif ms == "Мода":
                    info_label.configure(text=df[cs].mode().iloc[0])

        def copy_text():
            if info_label.cget("text") != "Інформація":
                app.clipboard_clear()
                app.clipboard_append(info_label.cget("text"))

        copy_button.configure(command=copy_text)
        copy_button.place(rely=0.95, relx=0.35, anchor="center")
        method_select.configure(command=option_menu_info_def)
        column_select.configure(command=option_menu_info_def)

    def button_diagram_def():
        pass


    button_info_reader.configure(command=button_info_def)
    button_info_reader.place(rely=0.1, relx=0.3, anchor="center")
    button_diagram.configure(command=button_diagram_def)
    button_diagram.place(rely=0.1, relx=0.7, anchor="center")



decorlabel1 = ctk.CTkLabel(master=app, text="＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿",
                           font=("Arial", 55, "bold"),
                           text_color="#181818")
decorlabel1.place(rely=0.12, relx=0.5, anchor="center")
decorlabel2 = ctk.CTkLabel(master=app, text="＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿",
                           font=("Arial", 55, "bold"),
                           text_color="#181818")
decorlabel3 = ctk.CTkLabel(master=app, text="│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│",
                           font=("Arial", 30),
                           text_color="#181818")
decorlabel3.place(rely=0.15, relx=0.7, anchor="nw")

file_select = ctk.CTkOptionMenu(
    master=app,
    values=files,
    command=info_opening
)
if not files:
    file_select.set("Тут немає ніякого файла з розширенням .csv")
else:
    file_select.set("Виберіть файл")
file_select.place(rely=0.05, relx=0.5, anchor="center")


app.mainloop()


# translate_stats = {
#     "count": "кількість",
#     "mean": "середнє значення",
#     "std": "стандартне відхилення",
#     "min": "мінімум",
#     "25%": "25-й перцентиль (нижній квартиль)",
#     "50%": "медіана (50-й перцентиль)",
#     "75%": "75-й перцентиль (верхній квартиль)",
#     "max": "максимум"
# }