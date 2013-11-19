import sqlite3 as lite
import sys

con = lite.connect('firsttest.db')

maxes = (
	("HumanHero",7,7,6,5,5,5,5,4,5),
	("HumanVet",8,7,7,6,6,6,6,6,6),
	("HumanEpic",8,7,8,7,7,7,7,8,7),
	("DwarfHero",7,5,6,5,5,4,5,4,4),
	("DwarfVet",7,6,7,6,6,5,6,6,6),
	("DwarfEpic",8,6,8,7,7,6,7,7,7),
	("GobberHero",6,7,4,5,5,5,4,0,4),
	("GobberVet",7,7,5,6,6,6,5,0,4),
	("GobberEpic",7,7,6,7,7,7,6,0,5),
	("IosanHero",7,7,5,5,5,5,6,4,5),
	("IosanVet",7,7,6,6,6,6,6,6,6),
	("IosanEpic",7,7,7,7,7,7,7,8,7),
	("NyssHero",7,7,6,5,5,5,5,4,5),
	("NyssVet",7,7,7,6,6,6,6,6,6),
	("NyssEpic",8,7,8,7,7,7,6,7,6),
	("OgrunHero",7,6,8,5,5,4,5,0,4),
	("OgrunVet",8,6,9,5,6,5,5,0,5),
	("OgrunEpic",9,6,10,6,7,6,6,0,6),
	("TrollkinHero",8,6,7,5,5,4,4,4,4),
	("TrollkinVet",9,6,8,6,6,5,5,6,5),
	("TrollkinEpic",10,6,9,7,7,6,6,7,6),
	("SatyxisHero",5,6,5,3,4,3,3,0,3),
	("SatyxisVet",5,6,5,3,4,3,3,0,3),
	("SatyxisEpic",5,6,5,3,4,3,3,0,3)
)


with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Maxes")
	cur.execute("CREATE TABLE Maxes(Name TEXT, PHY INT, SPD INT, STR INT, AGL INT, PRW INT, POI INT, INT INT, ARC INT, PER INT)")
	cur.executemany("INSERT INTO Maxes VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", maxes)