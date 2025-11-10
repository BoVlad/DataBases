import customtkinter as ctk


classic_key = {
    'А': '@', 'Б': '#', 'В': '$', 'Г': '%', 'Ґ': '&',
    'Д': '*', 'Е': '(', 'Є': ')', 'Ж': '+', 'З': '-',
    'И': '=', 'І': '_', 'Ї': '{', 'Й': '}', 'К': '[',
    'Л': ']', 'М': ':', 'Н': ';', 'О': "'", 'П': '"',
    'Р': '|', 'С': '/', 'Т': '7', 'У': '~', 'Ф': '^',
    'Х': '?', 'Ц': '!', 'Ч': '1', 'Ш': '2', 'Щ': '3',
    'Ь': '4', 'Ю': '5', 'Я': '6', " ": " "
}


latin_key = {
    'А': 'Q', 'Б': 'W', 'В': 'E', 'Г': 'R', 'Д': 'T', 'Е': 'Y', 'Є': 'U', 'Ж': 'I',
    'З': 'O', 'И': 'P', 'І': 'A', 'Ї': 'S', 'Й': 'D', 'К': 'F', 'Л': 'G', 'М': 'H',
    'Н': 'J', 'О': 'K', 'П': 'L', 'Р': 'Z', 'С': 'X', 'Т': 'C', 'У': 'V', 'Ф': 'B',
    'Х': 'N', 'Ц': 'M', 'Ч': '1', 'Ш': '2', 'Щ': '3', 'Ь': '4', 'Ю': '5', 'Я': '6',
    " ": " "
}


cyrillic_key = {
    'А': 'Є', 'Б': 'Ж', 'В': 'З', 'Г': 'И', 'Ґ': 'І', 'Д': 'Ї', 'Е': 'Й', 'Є': 'К',
    'Ж': 'Л', 'З': 'М', 'И': 'Н', 'І': 'О', 'Ї': 'П', 'Й': 'Р', 'К': 'С', 'Л': 'Т',
    'М': 'У', 'Н': 'Ф', 'О': 'Х', 'П': 'Ц', 'Р': 'Ч', 'С': 'Ш', 'Т': 'Щ', 'У': 'Ь',
    'Ф': 'Ю', 'Х': 'Я', 'Ц': 'Ґ', 'Ч': 'Д', 'Ш': 'Е', 'Щ': 'Б', 'Ь': 'А', 'Ю': 'В',
    'Я': 'Г', " ": " "
}


method_select_list =["Класичний", "Латинський", "Кириличний"]

root = ctk.CTk()

root.title("Шифратор")
root.geometry("500x400")

def crypt():
    global classic_key, latin_key, cyrillic_key
    stroke = str(text_input.get("0.0", "end")).upper()

    ms = method_select.get()
    cipher_dict = None
    if ms == method_select_list[0]:
        cipher_dict = classic_key
    elif ms == method_select_list[1]:
        cipher_dict = latin_key
    elif ms == method_select_list[2]:
        cipher_dict = cyrillic_key

    new_stroke = ""
    for i in stroke:
        if i in cipher_dict:
            new_stroke = new_stroke + cipher_dict.get(i)
    text_output.delete("0.0", "end")
    text_output.insert("0.0", new_stroke)

def decrypt():
    global classic_key, latin_key, cyrillic_key
    stroke = str(text_input.get("0.0", "end")).upper()

    ms = method_select.get()
    cipher_dict = None
    if ms == method_select_list[0]:
        cipher_dict = classic_key
    elif ms == method_select_list[1]:
        cipher_dict = latin_key
    elif ms == method_select_list[2]:
        cipher_dict = cyrillic_key

    new_stroke = ""
    cipher_dict_reverse = {v: k for k, v in cipher_dict.items()}
    for i in stroke:
        if i in cipher_dict_reverse:
            new_stroke = new_stroke + cipher_dict_reverse.get(i)
    text_output.delete("0.0", "end")
    text_output.insert("0.0", new_stroke)



text_input = ctk.CTkTextbox(root, width=450, height=100)
text_input.place(relx=0.5, rely=0.2, anchor="center")

encrypt_button = ctk.CTkButton(root, text="Шифрувати", command=crypt)
encrypt_button.place(relx=0.19, rely=0.45, anchor="center")

decrypt_button = ctk.CTkButton(root, text="Розшифрувати", command=decrypt)
decrypt_button.place(relx=0.19, rely=0.55, anchor="center")

method_select = ctk.CTkOptionMenu(
    master=root,
    values=method_select_list,
)
method_select.set(method_select_list[0])
method_select.place(relx=0.67, rely=0.5, anchor="w")



text_output = ctk.CTkTextbox(root, width=450, height=100)
text_output.place(relx=0.5, rely=0.8, anchor="center")


root.mainloop()