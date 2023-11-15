import sqlite3
con = sqlite3.connect('rowing.db')
cur = con.cursor()
cur.execute(f'''SELECT * from rowingSportsman WHERE sportsman = "Тонких, Никита"''')
all = cur.fetchall()
print(all)
con.commit()

