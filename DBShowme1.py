import sqlite3 as lite
import sys

con = lite.connect('firsttest.db')
listy = []

with con:

	cur = con.cursor()    
	cur.execute("SELECT * FROM Stats")

	while True:

		row = cur.fetchone()

		if row == None:
			break
		listy.append(row[0])

print(listy)
for x in listy:
	print(x)