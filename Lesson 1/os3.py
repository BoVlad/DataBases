try:
    with open("quotes.txt", "r", encoding="UTF-8") as f:
        data = f.readlines()
except FileNotFoundError:
    print("Помилка")
    exit()

for i in data:
    i = i.replace("\n", "")
    if "щастя" in i.lower():
        print(i)
