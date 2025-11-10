import hashlib

text = input("Введіть текст: ")
hash_object = hashlib.sha256(text.encode())

while True:
    print("Хеш:", hash_object.hexdigest())
    choice = input()
    if choice.lower() == "дякую":
        break
