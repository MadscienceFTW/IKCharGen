import sqlite3 as lite


con = lite.connect('firsttest.db')
baseRaces = []
finalStats = []
newStats = []
with con:

	cur = con.cursor()    
	cur.execute("SELECT * FROM Stats")

	while True:

		row = cur.fetchone()

		if row == None:
			break
		baseRaces.append(row[0])

count = 0
for x in baseRaces:
	print(str(count) + str(baseRaces[count]))
	count+=1
entry = input("Enter a number of the race you would like:")
y = baseRaces[entry]
with con:

	con.row_factory = lite.Row

	cur = con.cursor() 
	cur.execute("SELECT * FROM stats WHERE Name = '"+y+"'")

	rows = cur.fetchall()

	for row in rows:
		print('{:>12} PHY:{:2} AGL:{:2} INT:{:2}'.format(row["Name"], row["PHY"], row["AGL"], row["INT"]))
	for x in rows:
		newStats = list(x)

print(newStats)