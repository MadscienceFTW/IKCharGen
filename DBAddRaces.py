import sqlite3 as lite
import sys

con = lite.connect('firsttest.db')

stats = (
	("Human",5,6,4,3,4,4,3,0,3),
	("Dwarf",6,4,5,3,4,3,4,0,3),
	("Gobber",4,6,3,4,4,3,3,0,3),
	("Iosan",5,6,4,3,4,4,4,0,3),
	("Nyss",5,6,4,4,4,4,3,0,3),
	("Ogrun",6,5,6,3,4,3,3,0,2),
	("Trollkin",6,5,5,3,4,2,3,0,3),
	("Satyxis",5,6,5,3,4,3,3,0,3)
)


with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Stats")
	cur.execute("CREATE TABLE Stats(Name TEXT, PHY INT, SPD INT, STR INT, AGL INT, PRW INT, POI INT, INT INT, ARC INT, PER INT)")
	cur.executemany("INSERT INTO Stats VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", stats)