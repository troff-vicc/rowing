import sqlite3


def sporsmen_data(name):
    name = name[:name.find(' ')] + ',' + name[name.find(' '):]
    con = sqlite3.connect('/Users/trofimovviktor/PycharmProjects/rowing/rowing.db')
    cur = con.cursor()
    cur.execute(f'''SELECT * from rowingFor1 WHERE sportsman = "{name}" ''')
    row = cur.fetchall()
    if row == []:
        fail = False
    else:
        fail = True
    return fail, row
