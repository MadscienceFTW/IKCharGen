import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('firsttest.db')

with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Abilities")
	cur.execute("CREATE TABLE Abilities(Name TEXT, Description TEXT)")
	with open('newabilities.txt','r') as fin:
		dr = csv.reader(fin)
		for x in dr:
			for y in x:
				y = (y,)
				cur.execute("INSERT INTO Abilities(Name) values (?)",y)