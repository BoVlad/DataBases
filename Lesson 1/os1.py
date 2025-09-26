# 🔑 Основні функції:
#
# os.mkdir('folder_name') — створює папку;
# os.remove('file_name') — видаляє файл;
# os.rename('old_name', 'new_name') — перейменовує файл чи папку;
# os.listdir('path') — повертає список файлів і папок у вказаній директорії;
# os.path.exists('file_or_folder') — перевіряє, чи існує файл або папка.
#
# Завдання!
#
#  Напиши програму, яка створює папку з назвою "SecretFolder";
# потім додає в неї файл "secret.txt" із текстом "Це таємний файл!"
# і виводить повідомлення: "Таємний сховок створено!".
#
#  Перевір, чи справді твій файл створився на твоєму комп'ютері.
import os


if not os.path.exists('SecretFolder'):
    os.mkdir('SecretFolder')

if not os.path.exists('secret.txt'):
    with open("SecretFolder/secret.txt", "w", encoding="UTF-8") as f:
        f.write("Це таємний файл!")
    print("Таємний сховок створено!")
else:
    print("Нічого такого")





