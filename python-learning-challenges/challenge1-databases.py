

import sqlite3

conn = sqlite3.connect(':memory:')
cur = conn.cursor()

with conn:
    cur.execute('CREATE TABLE IF NOT EXISTS Roster \
                (Name TEXT, Species TEXT, IQ INT)')
    cur.execute('INSERT INTO Roster (Name, Species, IQ)\
                VALUES ("Jean-Babtiste Zorg", "Human", 122),\
                        ("Korben Dallas", "Meat Popsicle", 100),\
                        ("Ak\'not", "Mangalore",-5)')
    cur.execute('UPDATE Roster SET Species="Human" WHERE Name="Korben Dallas"')
    cur.execute('SELECT IQ, Name FROM Roster WHERE Species = "Human"')
    for row in cur.fetchall():
        print(row)
    
