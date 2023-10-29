import sqlite3

def rename(name, v = True):
    if v:
        newName = name[:name.find(' ')] + ',' + name[name.find(' '):]
    else:
        newName = name[:name.find(',')] + ' ' + name[name.find(',') + 2:]
    return newName
def sporsmen_data(name):
    name = rename(name)
    con = sqlite3.connect('rowing.db')
    cur = con.cursor()
    cur.execute(f'''SELECT * from rowingFor1 WHERE sportsman = "{name}" ''')
    row = cur.fetchall()
    if row == []:
        fail = False
    else:
        fail = True
    return fail, row

def nameID(name):
    name = rename(name)
    con = sqlite3.connect('rowing.db')
    cur = con.cursor()
    cur.execute(f'''SELECT sportsmanID from rowingFor1 WHERE sportsman = "{name}" ''')
    id = cur.fetchall()[0][0]
    return id

def idName(id):
    con = sqlite3.connect('rowing.db')
    cur = con.cursor()
    cur.execute(f'''SELECT sportsman from rowingFor1 WHERE sportsmanID = "{id}" ''')
    name = cur.fetchall()[0][0]
    name = rename(name, False)
    return name