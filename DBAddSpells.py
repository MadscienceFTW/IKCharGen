import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('firsttest.db')

with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Spells")
	cur.execute("CREATE TABLE Spells(name,cost,range,aoe,pow,up,off,description)")
	with open('newspells.txt','r') as fin:
		dr = csv.reader(fin)
		for x in dr:
			for y in x:
				y = (y,)
				cur.execute("INSERT INTO Spells(Name) values (?)",y)