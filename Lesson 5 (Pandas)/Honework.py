import pandas as pd

data = {
    "Title": [
        "Avengers: Endgame", "Titanic", "The Lion King", "Spider-Man: No Way Home",
        "Frozen", "The Dark Knight", "Black Panther", "Avatar", "Inception", "Joker"
    ],
    "Genre": [
        "Action", "Romance", "Animation", "Action", "Animation",
        "Action", "Action", "Science Fiction", "Sci-Fi/Thriller", "Drama/Thriller"
    ],
    "Year": [2019, 1997, 1994, 2021, 2013, 2008, 2018, 2009, 2010, 2019],
    "Box Office ($M)": [2797, 2187, 968, 1850, 1280, 1005, 1347, 2847, 836, 1280]
}

df = pd.DataFrame(data)

print(f"Медіана: {df.describe()["Box Office ($M)"]["50%"]}")
print(f"Мода: {df["Box Office ($M)"].mode()[0]}")
print(f"Середнє значення касових зборів: {df.describe()["Box Office ($M)"]["mean"]}")
print(f"Найменші касові збори: {df.describe()["Box Office ($M)"]["min"]}")
print(f"Найбільші касові збори: {df.describe()["Box Office ($M)"]["max"]}")
