import customtkinter as ctk

def encrypt():
    text = input_text.get("1.0", "end")
    shift = shift_entry.get()
    if shift.isdigit():
        shift = int(shift)
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_base = ord("A") if char.isupper() else ord("a")
                encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                encrypted_text += char
    else:
        encrypted_text = "ПОМИЛКА"
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def decrypt():
    text = input_text.get("1.0", "end")
    shift = shift_entry.get()
    if shift.isdigit():
        shift = int(shift)
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_base = ord("A") if char.isupper() else ord("a")
                encrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            else:
                encrypted_text += char
    else:
        encrypted_text = "ПОМИЛКА"
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Шифр Цезаря")
root.resizable(False, False)
root.geometry("500x500")


label1 = ctk.CTkLabel(root, text="Введіть текст:")
label1.pack(pady=5)
input_text = ctk.CTkTextbox(root, width=400, height=120)
input_text.pack()

label2 = ctk.CTkLabel(root, text="На скільки здвинути:")
label2.pack(pady=5)
shift_entry = ctk.CTkEntry(root, width=60)
shift_entry.insert(0, "3")
shift_entry.pack()



encrypt_button = ctk.CTkButton(root, text="Зашифрувати", command=encrypt)
encrypt_button.pack(pady=5)
decrypt_button = ctk.CTkButton(root, text="Розшифрувати", command=decrypt)
decrypt_button.pack(pady=5)

label3 = ctk.CTkLabel(root, text="Результат:")
label3.pack(pady=5)
output_text = ctk.CTkTextbox(root, width=400, height=120)
output_text.pack()

root.mainloop()
