default_ciphers_dict = {"🥗 Шифр Цезаря": "caesar_cipher", "🗿 Масонській Шифр": "masson_cipher"}
default_ciphers_dict_invert = {V: K for K, V in default_ciphers_dict.items()}

key = {
'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&', 'F': '*', 'G': '(',
'H': ')', 'I': '!', 'J': '^', 'K': '_', 'L': '+', 'M': '~', 'N': '`',
'O': '-', 'P': '=', 'Q': '{', 'R': '}', 'S': '[', 'T': ']', 'U': ';',
'V': ':', 'W': '"', 'X': "'", 'Y': '<', 'Z': '>', ' ': ' '}
key_invert = {V: K for K, V in key.items()}

def caesar_cipher(text: str, shift: int) -> str:
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord("A") if char.isupper() else ord("a")
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def masson_cipher_enc(text: str) -> str:
    global key
    text = text.upper()
    new_text = ""
    for i in text:
        if i in key:
            new_text = new_text + key[i]
        else:
            new_text = new_text + i
    return new_text

def masson_cipher_dec(text: str) -> str:
    global key_invert
    new_text = ""
    for i in text:
        if i in key_invert:
            new_text = new_text + key_invert[i]
        else:
            new_text = new_text + i
    return new_text










