import hashlib

hashlib1 = lambda x: (hashlib.sha256(x.encode()).hexdigest())

def hashlib2(text):
    data1 = hashlib.sha256(text.encode())
    data2 = hashlib.sha256(text.encode()).digest()
    return [data1, data2]

def hashlib3(*args):
    new_list = []
    for i in args:
        data = hashlib.sha256(str(i).encode())
        new_list.append(data)
    return new_list

def hashlib4(text1: str, text2: str):
    return text1 == text2

print("1.", hashlib1("hello"))
print("2.", hashlib2("hello"))
print("3.", hashlib3("hello", "World", "Apple", "banana"))
print("4.1.", hashlib4("hello", "World"))
print("4.2.", hashlib4("World", "World"))
