import hashlib

# Вхідний текст
text = "hello"

# Створення хешу за допомогою SHA-256
hash_object = hashlib.sha256(text.encode())

# Виведення хешу
print("Хеш: ", hash_object.hexdigest())