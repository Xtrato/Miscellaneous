#This script iterates through a SQLite database and creates a new database with any complete duplicates removed.
#Requires minor changes to the SQL statements to match the input database
import sqlite3
import os

#Connecting to original database
connOriginal = sqlite3.connect('/root/Documents/upnp.db')
connOriginal.text_factory = str
cOriginal = connOriginal.cursor()
databaseOriginal = cOriginal.execute("SELECT * from 'devices';")


os.system('rm /root/PycharmProjects/upnpEnumeration/upnpFinal.db')
#Connecting and creating the final database.
connNew = sqlite3.connect('upnpFinal.db')
connNew.text_factory = str
cNew = connNew.cursor()
cNew.execute('''CREATE TABLE devices (ip text, st text, usn text, server text, location text, date text, xml text)''')


uniqueEntries = []
for row in databaseOriginal:
    if row not in uniqueEntries:
        cNew.execute("INSERT INTO devices VALUES (?, ?, ?, ?, ?, ?, ?);", (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        uniqueEntries.append(row)
connNew.commit()
print 'End'