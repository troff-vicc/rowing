import sqlite3
con = sqlite3.connect('rowing.db')
cur = con.cursor()
cur.execute("CREATE TABLE rowingFor1(competition text, race text, raceClass text, raceID text, raceDistance text, raceData text, link text, sportsmanID text, sportsman text, coach text, rank text, finish text)")

con.commit()