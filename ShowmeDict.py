import sqlite3 as lite


con = lite.connect('firsttest.db')    
y = 'Human'
with con:

	con.row_factory = lite.Row

	cur = con.cursor() 
	cur.execute("SELECT * FROM stats")

	rows = cur.fetchall()

	for row in rows:
		print('{:>12} PHY:{:2} AGL:{:2} INT:{:2}'.format(row["Name"], row["PHY"], row["AGL"], row["INT"]))