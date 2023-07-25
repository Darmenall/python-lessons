import sqlite3

db = sqlite3.connect('darmen.db')
# CREATE CURSOR
cursor = db.cursor()

# MB  Таблица жаратуу
cursor.execute("""CREATE TABLE IF NOT EXISTS articles(
    title TEXT,
    full_text TEXT,
    views INTEGER,
    avtor TEXT
)""")

# Маглумат косуу
cursor.execute("INSERT INTO articles VALUES ('Amazon is cool!','Amazon is really cool!', 400, 'Modest')")

# маглуматты алу ямаса сайлау
cursor.execute("SELECT ROWID, * FROM articles WHERE title <> 'Google is cool!' ")
print(cursor.fetchall())
# print(cursor.fetchmany(1))
# print(cursor.fetchone()[1])
#
# items = cursor.fetchall()
# for item in items:
#     print(item[1] + "\n" + item[4])

#ЫЗБЕ ЫЗЛИК ЯМАСА КЕРЫ
# cursor.execute("SELECT ROWID, * FROM articles WHERE ROWID < 5 ORDER BY views")  #DESC
# print(cursor.fetchall())
# print(cursor.fetchmany(1))
# print(cursor.fetchone()[1])
#
# items = cursor.fetchall()
# for item in items:
#     print(item[1] + "\n" + item[4])

# удалить етыу
# cursor.execute("DELETE FROM articles WHERE avtor = 'Admin'")
# cursor.execute("SELECT ROWID, * FROM articles WHERE ROWID < 5 ORDER BY views")  #DESC
# print(cursor.fetchall())
# print(cursor.fetchmany(1))
# print(cursor.fetchone()[1])

# items = cursor.fetchall()
# for item in items:
#     print(item[1] + "\n" + item[4])


# МАГЛУМАТТЫ ОЗГЕРТУ
# cursor.execute("UPDATE articles SET avtor = 'Admin', views = 1 WHERE title = 'Amazon is cool!'")
#
# cursor.execute("SELECT ROWID, * FROM articles WHERE ROWID < 5 ORDER BY views")  #DESC
# print(cursor.fetchall())
# print(cursor.fetchmany(1))
# print(cursor.fetchone()[1])

# items = cursor.fetchall()
# for item in items:
#     print(item[1] + "\n" + item[4])

db.commit()

db.close()
