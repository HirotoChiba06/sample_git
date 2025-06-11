import sqlite3

dbname = "test.db"
conn = sqlite3.connect(dbname)
#SQLite3を操作するカーソルオブジェクトを作成する。
cur = conn.cursor()

cur.execute(
    "CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)"
)

cur.execute("INSERT INTO persons(name) VALUES('Alice')")
cur.execute("INSERT INTO persons(name) VALUES('Momoi')")
cur.execute("INSERT INTO persons(name) VALUES('Midori')")
cur.execute("INSERT INTO persons(name) VALUES('Yuzu')")

conn.commit()
conn.close()