import sqlite3 as lite
import sys

con = lite.connect('firsttest.db')

with con:
	cur = con.cursor() 
	cur.execute("DROP TABLE IF EXISTS " + sys.argv[1])
