key = {
'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&', 'F': '*', 'G': '(',
'H': ')', 'I': '!', 'J': '^', 'K': '_', 'L': '+', 'M': '~', 'N': '`',
'O': '-', 'P': '=', 'Q': '{', 'R': '}', 'S': '[', 'T': ']', 'U': ';',
'V': ':', 'W': '"', 'X': "'", 'Y': '<', 'Z': '>', ' ': ' '}



def decrypt(stroke: str, keys: dict):
    for i in keys:
        stroke = stroke.replace(f"{keys[i]}", f"{i}")
    return stroke


cipher = input("Введіть код для дешифрування: ")
print(decrypt(cipher, key))



