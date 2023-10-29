import sqlite3
import matplotlib.pyplot as plt
name = input()
newName = name[:name.find(',')] + ' ' + name[name.find(',') + 2:]
print(newName)