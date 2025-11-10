import bcrypt

password = "mysecretpassword"

# Генерація "солі" та хешування пароля
salt = bcrypt.gensalt()

print(salt)

hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

print(hashed_password)

entered_password = "mysecretpassword"

# Перевірка пароля
if bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password):
    print("Пароль правильний!")
else:
    print("Невірний пароль!")
