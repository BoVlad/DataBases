# 📋 Використовуючи модуль os, створи папку my_folder, а всередині неї — ще одну папку sub_folder.
#
# Перевір, чи папка my_folder вже існує. Якщо ні, створи її.
# Виведи список усіх файлів і папок у директорії, в якій ти працюєш.
#
# Підказка. Використовуй методи os.makedirs() і os.listdir().


import os


if not os.path.exists('my_folder'):
    os.mkdir('my_folder')
    os.mkdir("my_folder/sub_folder")

data = os.listdir()
for i in data:
    print(i)