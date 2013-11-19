import sqlite3 as lite
import sys
import os

con = lite.connect('firsttest.db')

careers = []
career = ()
if os.name == 'nt':
	data = open('f:\Dropbox\Dev\IK\careers.txt')
elif os.name == 'posix':
	data = open('~/Dropbox/Dev/IK/careers.txt')
for each_line in data:
	careers.append(each_line.rstrip('\n'))
data.close()
print(careers)

with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Careers")
	cur.execute("CREATE TABLE Careers(Name TEXT)")
	cur.execute('''.separator "\n"''')
	cur.execute(".import f:\Dropbox\Dev\IK\careers.txt")