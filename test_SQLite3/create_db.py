import sqlite3

dbname = "test.db"
conn = sqlite3.connect(dbname)

conn.close()