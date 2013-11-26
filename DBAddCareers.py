import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('defaults.db')

with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Careers")
	cur.execute("CREATE TABLE Careers(Name TEXT)")
	with open('newcareers.txt','r') as fin:
		dr = csv.reader(fin)
		for x in dr:
			for y in x:
				y = (y,)
				cur.execute("INSERT INTO Careers(Name) values (?)",y)