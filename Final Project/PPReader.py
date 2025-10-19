import pandas as pd
import customtkinter as ctk
from customtkinter import CTkImage
from matplotlib import pyplot as plt
import os
from tkinter import ttk
from PIL import Image
import numpy as np

fig = None
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
img_label = ctk.CTkLabel(app, text="")

method_select = ctk.CTkOptionMenu(
    master=app,
    values=[
        "Кількість",
        "Середнє значення",
        "Стандартне відхилення",
        "Нижній квартиль (25%)",
        "Медіана (50%)",
        "Верхній квартиль (75%)",
        "Максимум",
        "Мода",
    ],
)

column_select = ctk.CTkOptionMenu(master=app)

method_select2 = ctk.CTkOptionMenu(
    master=app,
    values=["Лінійна", "Кругова", "Стовпчаста"],
)

column_select2 = ctk.CTkOptionMenu(master=app)
column_select2_2 = ctk.CTkOptionMenu(master=app)

copy_button = ctk.CTkButton(app, text="Копіювати", font=ctk.CTkFont(size=35))


def info_opening(choice):
    global df
    method_select.place_forget()
    column_select.place_forget()
    copy_button.place_forget()
    info_label.place_forget()
    method_select2.place_forget()
    column_select2.place_forget()
    column_select2_2.place_forget()
    img_label.place_forget()


    df = pd.read_csv(choice).dropna()
    df_operable_columns = list(df.select_dtypes(include=["number"]).columns)
    df_describe = df.describe()

    def button_info_def():
        method_select2.place_forget()
        column_select2.place_forget()
        column_select2_2.place_forget()
        img_label.place_forget()

        decorlabel2.place(rely=0.86, relx=-0.08, anchor="w")
        info_label.place(rely=0.18, relx=0.02, anchor="nw")

        method_select.set("Виберіть метод")
        method_select.place(rely=0.25, relx=0.85, anchor="center")

        column_select.configure(values=df_operable_columns)
        if not df_operable_columns:
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
                app.clipboard_append(str(info_label.cget("text")))

        copy_button.configure(command=copy_text)
        copy_button.place(rely=0.95, relx=0.35, anchor="center")
        method_select.configure(command=option_menu_info_def)
        column_select.configure(command=option_menu_info_def)

    def button_diagram_def():
        global fig
        method_select.place_forget()
        column_select.place_forget()
        copy_button.place_forget()
        info_label.place_forget()
        decorlabel2.place_forget()

        method_select2.set("Виберіть метод")
        method_select2.place(rely=0.25, relx=0.85, anchor="center")

        column_select2.configure(values=df_operable_columns)
        if not df_operable_columns:
            column_select2.set("Тут немає даних")
        else:
            column_select2.set("Виберіть колонку")
        column_select2.place(rely=0.3, relx=0.85, anchor="center")

        column_select2_2.configure(values=df_operable_columns)
        if not df_operable_columns:
            column_select2_2.set("Тут немає даних")
        else:
            column_select2_2.set("Виберіть колонку")
        column_select2_2.place(rely=0.35, relx=0.85, anchor="center")

        def option_menu_info_def2(*_):
            global fig
            ms2 = method_select2.get()
            cs2 = column_select2.get()
            cs2_2 = column_select2_2.get()

            if (ms2 != "Тут немає даних" and ms2 != "Виберіть метод"
                    and cs2 != "Тут немає даних" and cs2 != "Виберіть колонку"
                    and cs2_2 != "Тут немає даних" and cs2_2 != "Виберіть колонку"):
                if fig is not None:
                    plt.close(fig)

                if ms2 == "Лінійна":
                    fig, ax = plt.subplots(figsize=(7, 4), dpi=120)
                    fig.patch.set_facecolor("#242424")
                    ax.set_facecolor("#242424")
                    line_color = "#1F6AA5"
                    ax.plot(df[cs2].values, df[cs2_2].values, color=line_color, linewidth=3)
                    ax.tick_params(colors="white", labelsize=10)
                    for spine in ax.spines.values():
                        spine.set_color("white")
                    ax.xaxis.label.set_color("white")
                    ax.yaxis.label.set_color("white")
                    ax.title.set_color("white")
                    ax.set_xlabel(f"{cs2}", color="white")
                    ax.set_ylabel(f"{cs2_2}", color="white")
                    ax.grid(True, color="#3A3A3A")
                    ax.set_title(f"Лінійний графік {cs2} і {cs2_2}", color="white")

                elif ms2 == "Кругова":
                    labels = [cs2, cs2_2]
                    sizes = [float(df[cs2].sum()), float(df[cs2_2].sum())]
                    colors = plt.get_cmap("Blues")(np.linspace(0.25, 0.8, len(labels)))
                    fig, ax = plt.subplots(figsize=(7, 4), dpi=120)
                    fig.patch.set_facecolor("#242424")
                    ax.set_facecolor("#242424")
                    wedges, texts, autotexts = ax.pie(
                        sizes,
                        labels=labels,
                        colors=colors,
                        autopct="%1.1f%%",
                        startangle=90,
                        wedgeprops={"edgecolor": "#242424", "linewidth": 1.5},
                        textprops={"color": "white", "fontsize": 10},
                    )
                    for t in autotexts:
                        t.set_color("white")
                        t.set_fontsize(9)
                        t.set_fontweight("bold")
                    ax.set_title(f"Кругова діаграма для {cs2} і {cs2_2}", color="white", fontsize=12)

                elif ms2 == "Стовпчаста":
                    labels = [cs2, cs2_2]
                    values = [float(df[cs2].sum()), float(df[cs2_2].sum())]

                    colors = plt.get_cmap("Blues")(np.linspace(0.25, 0.8, len(values)))
                    fig, ax = plt.subplots(figsize=(8, 5), dpi=130)
                    fig.patch.set_facecolor("#242424")
                    ax.set_facecolor("#242424")
                    bars = ax.bar(labels, values, color=colors, edgecolor="#242424", width=0.6)
                    ax.tick_params(colors="white", labelsize=10)
                    for spine in ax.spines.values():
                        spine.set_color("white")
                    ax.set_xlabel("Категорія", color="white")
                    ax.set_ylabel("Сума", color="white")
                    ax.set_title(f"Стовпчаста діаграма для {cs2} і {cs2_2}", color="white")
                    for bar in bars:
                        h = bar.get_height()
                        ax.text(
                            bar.get_x() + bar.get_width() / 2,
                            h,
                            f"{h:.2f}",
                            ha="center",
                            va="bottom",
                            color="white",
                            fontsize=9,
                            fontweight="bold",
                        )
                    plt.tight_layout()

                plt.savefig(
                    "Grafik.png",
                    dpi=160,
                    facecolor=fig.get_facecolor(),
                    edgecolor=fig.get_edgecolor(),
                    bbox_inches="tight",
                    pad_inches=0.1,
                )

                img = Image.open("Grafik.png")
                img_size = tuple(int(i / 1.6) for i in img.size)
                ctk_img = CTkImage(light_image=img, dark_image=img, size=img_size)

                img_label.configure(image=ctk_img)
                img_label.place(rely=0.55, relx=0.35, anchor="center")

        method_select2.configure(command=option_menu_info_def2)
        column_select2.configure(command=option_menu_info_def2)
        column_select2_2.configure(command=option_menu_info_def2)

    button_info_reader = ctk.CTkButton(master=app, text="Інформація")
    button_diagram = ctk.CTkButton(master=app, text="Діаграма")
    button_info_reader.configure(command=button_info_def)
    button_info_reader.place(rely=0.1, relx=0.3, anchor="center")
    button_diagram.configure(command=button_diagram_def)
    button_diagram.place(rely=0.1, relx=0.7, anchor="center")


decorlabel1 = ctk.CTkLabel(
    master=app,
    text="＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿",
    font=("Arial", 55, "bold"),
    text_color="#181818",
)
decorlabel1.place(rely=0.12, relx=0.5, anchor="center")
decorlabel2 = ctk.CTkLabel(
    master=app,
    text="＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿",
    font=("Arial", 55, "bold"),
    text_color="#181818",
)
decorlabel3 = ctk.CTkLabel(
    master=app,
    text="│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│",
    font=("Arial", 30),
    text_color="#181818",
)
decorlabel3.place(rely=0.15, relx=0.7, anchor="nw")

file_select = ctk.CTkOptionMenu(
    master=app,
    values=files,
    command=info_opening,
)
if not files:
    file_select.set("Тут немає ніякого файла з розширенням .csv")
else:
    file_select.set("Виберіть файл")
file_select.place(rely=0.05, relx=0.5, anchor="center")

app.mainloop()