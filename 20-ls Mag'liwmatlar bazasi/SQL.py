import sqlite3

db = sqlite3.connect('jurnal.db')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS jurnal (
    ati TEXT,
    jasi INTEGER,
    mazil TEXT,
    ball INTEGER
)""")


cursor.execute("INSERT INTO jurnal VALUES (?, ?, ?, ?)",('Artur', 18, 'Xojeli', 91))
cursor.execute("INSERT INTO jurnal VALUES (?, ?, ?, ?)",('Rasul', 19, 'Nokis', 66))
cursor.execute("INSERT INTO jurnal VALUES (?, ?, ?, ?)",('Bayram', 22, 'Xojeli', 84))
cursor.execute("INSERT INTO jurnal VALUES (?, ?, ?, ?)",('Jalgas', 20, 'Nokis', 56))

cursor.execute("SELECT ati, ball FROM jurnal WHERE mazil <> 'Nokis'")
items = cursor.fetchall()
# print(items)
for item in items:
    print("Sessyadan jigilganlar:")
    print(f"{item[0]} {item[1]}-ball")
    print(item[0])


db.commit()

db.close()