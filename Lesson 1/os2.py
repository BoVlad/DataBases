import os

if not os.path.exists('secret.txt'):
    with open("secret.txt", "w", encoding="UTF-8") as f:
        f.write("Швидше за пулю\n"
                "Полярний експрес\n")