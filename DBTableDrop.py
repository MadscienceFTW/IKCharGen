import sqlite3 as lite
import sys

con = lite.connect('firsttest.db')
skilTab = str(str(sys.argv[1]) + "Skills")
abilTab = str(str(sys.argv[1]) + "Ablilities")
spelTab = str(str(sys.argv[1]) + "Spells")
equiTab = str(str(sys.argv[1]) + "Equipment")
weapTab = str(str(sys.argv[1]) + "Weapons")
armoTab = str(str(sys.argv[1]) + "Armor")
with con:
	cur = con.cursor() 
	cur.execute("DROP TABLE IF EXISTS " + sys.argv[1])
	cur.execute("DROP TABLE IF EXISTS " + skilTab)
	cur.execute("DROP TABLE IF EXISTS " + abilTab)
	cur.execute("DROP TABLE IF EXISTS " + spelTab)
	cur.execute("DROP TABLE IF EXISTS " + equiTab)
	cur.execute("DROP TABLE IF EXISTS " + weapTab)
	cur.execute("DROP TABLE IF EXISTS " + armoTab)