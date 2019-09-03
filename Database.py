import sqlite3

conn = sqlite3.connect("music.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Tracks")
cur.execute("CREATE TABLE Tracks(title TEXT,plays INTEGER)")

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Work',20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Number Nane',20))

print('Tracks')
cur.execute('SELECT title, plays From Tracks')
for row in cur:
    print(row)
conn.close()