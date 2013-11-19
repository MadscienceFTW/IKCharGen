import sqlite3 as lite
import sys

con = lite.connect('firsttest.db')
testCol = ['name', 'rank']

with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Character")
	cur.execute("""CREATE TABLE Character
					(name,race,archtype,phy,spd,str,agl,prw,poi,int,arc,per,willpower,skills,equipment,mat,matpow,rat,ratrange,ratpow,def,arm,lifespiral,featpoints,careers,sex,faith,height,weight,xp,init,commandrange,abilities,spells)
				""")

