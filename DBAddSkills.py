import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('defaults.db')

with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Skills")
	cur.execute("CREATE TABLE Skills(name,linked,description)")
	with open('newskills.txt','r') as fin:
		dr = csv.reader(fin)
		for x in dr:
			for y in x:
				y = (y,)
				cur.execute("INSERT INTO Skills(Name) values (?)",y)