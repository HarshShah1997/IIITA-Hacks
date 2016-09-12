import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('DELETE FROM data WHERE 1')
conn.commit()
conn.close()

