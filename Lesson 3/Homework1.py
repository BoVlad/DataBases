import sqlite3



conn = sqlite3.connect('likedinteresses.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    genre TEXT,
    year INTEGER,
    rating INTEGER
)
''')

def new_book(name: str, genre: str, year: int, rating: int):
    cursor.execute("INSERT INTO books (name, genre, year, rating) VALUES(?, ?, ?, ?)", (name, genre, year, rating))
    conn.commit()


cursor.execute("SELECT name, genre, year, rating FROM books "
                    "WHERE year > 2007" )
print(cursor.fetchall())



cursor.execute("SELECT name, genre, year, rating FROM books "
                    "WHERE genre LIKE ?",('Фентезі%',))
print(cursor.fetchall())



cursor.execute("SELECT name, genre, year, rating FROM books "
                    "WHERE rating < 700")
print(cursor.fetchall())

