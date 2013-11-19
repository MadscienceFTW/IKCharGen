import sqlite3 as lite
import sys
charStats = []

con = lite.connect('firsttest.db')

with con:

	cur = con.cursor()    
	cur.execute("SELECT * FROM Stats")

	rows = cur.fetchall()

	for row in rows:
		charStats.append(row)

for x in charStats:
	print(x)