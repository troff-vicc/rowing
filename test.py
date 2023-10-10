import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect('rowing.db')
cur = con.cursor()
cur.execute("SELECT * from rowingFor1")
row = cur.fetchall()
name = input()
name = name[:name.find(' ')] + ',' + name[name.find(' '):]
print(name)
sportman = []
for data in row:
    if data[8] == name:
        sportman.append(data)
for t in sportman:
    print(t[-1], t[8])