# first = ord("1")
# for i in range(200):
#     first += 3
#     print(chr(first), end)
# def shifr(text: str, rotate: int):
#     new_text = ""
#     for i in text:
#         new_text = new_text + chr(ord(i) + rotate)
#     return new_text

def encrypt(text: str, rotate: int):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord("A") if char.isupper() else ord("a")
            encrypted_text += chr((ord(char) - shift_base + rotate) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text: str, rotate: int):
    decrypt_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord("A") if char.isupper() else ord("a")
            decrypt_text += chr((ord(char) - shift_base - rotate) % 26 + shift_base)
        else:
            decrypt_text += char
    return decrypt_text


var_1 = input("Введіть текст для шифрування: ")
var_2 = int(input("Введіть зміщення: "))
print(encrypt(var_1, var_2))


