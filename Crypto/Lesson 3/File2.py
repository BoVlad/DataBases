import random as r
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord("A") if char.isupper() else ord("a")
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            #34-64
            # encrypted_text += chr(r.randint(34, 64))
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord("A") if char.isupper() else ord("a")
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            if char == " ":
                decrypted_text += char

    return decrypted_text

text = input("Input text: ")
shift = 3
encrypted = caesar_cipher(text, shift)
print(encrypted)
decrypted = decrypt("D5s0s*o+h2 l3v- f'd@s>l6w%d8o6 r)i= X*n:u:d/l=q&h+", shift)
print(decrypted)