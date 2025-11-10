import hashlib

def register_user(username, password):
    hash_object = hashlib.sha256(password.encode())
    userhash = hash_object.hexdigest()
    with open("users.txt", "a", encoding="UTF-8") as f:
        f.write(f"{username}:{userhash}\n")
    print("Користувача додано")

def login_user(username, password):
    hash_object = hashlib.sha256(password.encode())
    entered_hash = hash_object.hexdigest()

    try:
        with open("users.txt", "r", encoding="UTF-8") as f:
            for line in f:
                name, saved_hash = line.strip().split(":")
                if name == username and saved_hash == entered_hash:
                    print("Авторизація успішна")
                    return
    except FileNotFoundError:
        print("Файл не знайдено")
        return
    print("Невірний логін або пароль")


while True:
    choice = input("1 - Реєстрація, 2 - Вхід, 3 - Вихід: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            user = input("Логін: ")
            password = input("Пароль: ")
            register_user(user, password)
        elif choice == 2:
            user = input("Логін: ")
            password = input("Пароль: ")
            login_user(user, password)
        elif choice == 3:
            break
        else:
            print("Ви не ввели правильний пункт меню!")
    else:
        print("Ви не ввели цифру!")
