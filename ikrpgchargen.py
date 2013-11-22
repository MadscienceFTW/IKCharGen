import os
import sqlite3 as lite
import sys
import csv
baseStats = ["PHY","SPD","STR","AGL","PRW","POI","INT","ARC","PER"]
charStats = []
charArch = []
archEntry = []
charCareers = []
careers = []
variables = []
tempbed = []
humanStats = [5,6,4,3,4,4,3,"-",3,["gifted","intellectual","mighty","skilled"]]
humanMax = [7,7,6,5,5,5,5,4,5]
dwarfStats = [6,4,5,3,4,3,4,"-",3,["gifted","intellectual","mighty","skilled"]]
dwarfMax = [7,5,6,5,5,4,5,4,4]
gobberStats = [4,6,3,4,4,3,3,"-",3,["intellectual","mighty","skilled"]]
gobberMax = [6,7,4,5,5,5,4,"-",4]
iosanStats = [5,6,4,3,4,4,4,"-",3,["gifted","intellectual","mighty","skilled"]]
iosanMax = [7,7,5,5,5,5,6,4,5]
nyssStats = [5,6,4,4,4,4,3,"-",3,["gifted","mighty","skilled"]]
nyssMax = [7,7,6,5,5,5,5,4,5]
ogrunStats = [6,5,6,3,4,3,3,"-",2,["mighty","skilled"]]
ogrunMax = [7,6,8,5,5,4,5,"-",4]
trollkinStats = [6,5,5,3,4,2,3,"-",3,["gifted","mighty","skilled"]]
trollkinMax = [8,6,7,5,5,4,4,4,4]
satyxisStats = [5,6,5,3,4,3,3,"-",3,["gifted","mighty","skilled"]]
satyxisMax = [7,7,7,7,7,7,7,7,7]
baseRaces = {"human":humanStats,"dwarf":dwarfStats,"gobber":gobberStats,"iosan":iosanStats,"nyss":nyssStats,"ogrun":ogrunStats,"trollkin":trollkinStats,"satyxis":satyxisStats}
if os.name == 'nt':
	data = open('f:\\Dev\\IKChargen\\careers.txt')
elif os.name == 'posix':
	data = open('/home/ap/Dropbox/Dev/IK/careers.txt')
for each_line in data:
	careers.append(each_line.rstrip('\n'))
data.close()
spamReader = csv.reader(open('variables.txt'))
for row in spamReader:
	tempbed.append(row)
for x in tempbed[0]:
	variables.append(x)
def displayStats(race):
	os.system(clearingScreen())
	print(raceEntry.title())
	print(printStats(race))
	print(printArch(race).title())
	for x in charCareers:
		print(x)
def printStats(race):
	print("PHY:" + str(race[0]) + " SPD:" + str(race[1]) + " STR:" + str(race[2]) + 
	" AGL:" + str(race[3]) + " PRW:" + str(race[4]) + " POI:" + str(race[5]) 
	+ " INT:" + str(race[6]) + " ARC:" + str(race[7]) + " PER:" + str(race[8]))
def firstStats(race):
	os.system(clearingScreen())
	print("Here are that races stats and options:")
	print(printStats(race))
	displayArch(race)
def printArch(race):
	return (race[9])
def displayArch(race):
	for item in race[9]:
		print(str(item))
def changingStats(race):
	newStats = list(race)
	return newStats
def careerChoice(choice):
	charCareers.append(careers[careerNumber(choice)])
def careerNumber(entry):
	count = 0
	for x in careers:
		if x == entry:
			return count
		else:
			count+=1
def clearingScreen():
	if os.name == 'nt':
		return 'cls'
	elif os.name == 'posix':
		return 'clear'
charName = input("What is your characters name?")
if len(charName) < 1:
	print("That wasn't a long enough name, please try again.")
	charName = input("What is your characters name?")
else:
	print("Thank you")
raceCount = 1
while raceCount > 0:
	raceEntry = input("What race would you like to play?")
	raceEntry = raceEntry.lower()
	if raceEntry == 'human':
		charStats = changingStats(baseRaces[str(raceEntry)])
		count = 1
		while count > 0:
			firstStats(charStats)
			bonus = input("Which Base Stat is your Exceptional Potential? PHY, AGL or INT?")
			if bonus in ["PHY","AGL","INT"]:
				upgrade = baseStats.index(bonus)
				charStats[upgrade]+= 1
				count -= 1
			else:
				print("That isnt upgradable.")
		firstStats(charStats)
		raceCount -= 1
	elif raceEntry in baseRaces:
		charStats = changingStats(baseRaces[str(raceEntry)])
		firstStats(charStats)
		raceCount -= 1
	else:
		print("That is not one of the IK races.")
num = 1
while num > 0:	
	archEntry = input("Which Archetype would you like to use?")
	archEntry = archEntry.lower()
	if archEntry in charStats[9]:
		charStats[9] = archEntry
		os.system(clearingScreen())
		displayStats(charStats)
		num -=1
		if archEntry == 'gifted':
			charStats[7] = 0
	else:
		print("That is not one of the Archetypes available.")
uppoints = 3
displayStats(charStats)
while uppoints > 0:
	print("You have " + str(uppoints) + " upgrades remaining.")
	stat = input("Which stat would you like to upgrade?")
	stat = stat.upper()
	upgrade = baseStats.index(stat)
	if charStats[upgrade] != "-":
		if stat in baseStats:
			charStats[upgrade]+= 1
			uppoints-=1
			displayStats(charStats)
		else:
			print("That is not a stat.")
	else:
		print("Can't do that")
careerCount = 2
while careerCount > 0:
	os.system(clearingScreen())
	displayStats(charStats)
	print("You have two choices for career from the following list:")
	print(careers)
	for x in careers:
		print(x)
	choice = input("What is your choice?")
	if choice in careers:
		if choice in charCareers:
			print("You already chose that career.")
		else:
			careerChoice(choice)
			careerCount-=1
	else:
		print("That is not a selectable career.")
willpower = charStats[0] + charStats[6]
initiative = charStats[1] + charStats[4] + charStats[8]
defense = charStats[1] + charStats[3] + charStats[8]
armor = charStats[0]
cmdrange = charStats[6]
if raceEntry == "gobber":
	defense += 1
elif raceEntry == "nyss":
	initiative += 1
con = lite.connect('firsttest.db')
skilTab = str(str(charName) + "Skills")
abilTab = str(str(charName) + "Ablilities")
spelTab = str(str(charName) + "Spells")
equiTab = str(str(charName) + "Equipment")
weapTab = str(str(charName) + "Weapons")
armoTab = str(str(charName) + "Armor")
with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS " + charName)
	cur.execute("DROP TABLE IF EXISTS " + skilTab)
	cur.execute("DROP TABLE IF EXISTS " + abilTab)
	cur.execute("DROP TABLE IF EXISTS " + spelTab)
	cur.execute("DROP TABLE IF EXISTS " + equiTab)
	cur.execute("DROP TABLE IF EXISTS " + weapTab)
	cur.execute("DROP TABLE IF EXISTS " + armoTab)
	cur.execute("""CREATE TABLE """ + charName + """
					(name,race,archtype,phy,spd,str,agl,prw,poi,int,arc,per,willpower,skills,equipment,mat,matpow,rat,ratrange,ratpow,def,arm,lifespiral,featpoints,career1,career2,sex,faith,height,weight,xp,init,commandrange,abilities,spells)
				""")
	cur.execute('CREATE TABLE ' + skilTab + ' (name,linked,description)')
	cur.execute('CREATE TABLE ' + abilTab + ' (name,preq,description)')
	cur.execute('CREATE TABLE ' + spelTab + ' (name,cost,range,aoe,pow,up,off,description)')
	cur.execute('CREATE TABLE ' + equiTab + ' (name,description)')
	cur.execute('CREATE TABLE ' + weapTab + ' (name,cost,skill,attmod,pow,description)')
	cur.execute('CREATE TABLE ' + armoTab + ' (name,cost,spdmod,defmod,armmod,description)')
	cur.execute("INSERT INTO " + charName +"(name) VALUES ('"+ str(charName)+"')")
	cur.execute('UPDATE ' + charName + ' SET race= "'+ str(raceEntry)+'"')
	cur.execute('UPDATE ' + charName + ' SET archtype= "'+ str(archEntry)+'"')
	cur.execute('UPDATE ' + charName + ' SET phy= "'+ str(charStats[0])+'"')
	cur.execute('UPDATE ' + charName + ' SET spd= "'+ str(charStats[1])+'"')
	cur.execute('UPDATE ' + charName + ' SET str= "'+ str(charStats[2])+'"')
	cur.execute('UPDATE ' + charName + ' SET agl= "'+ str(charStats[3])+'"')
	cur.execute('UPDATE ' + charName + ' SET prw= "'+ str(charStats[4])+'"')
	cur.execute('UPDATE ' + charName + ' SET poi= "'+ str(charStats[5])+'"')
	cur.execute('UPDATE ' + charName + ' SET int= "'+ str(charStats[6])+'"')
	cur.execute('UPDATE ' + charName + ' SET arc= "'+ str(charStats[7])+'"')
	cur.execute('UPDATE ' + charName + ' SET per= "'+ str(charStats[8])+'"')
	cur.execute('UPDATE ' + charName + ' SET willpower= "'+ str(willpower)+'"')
	cur.execute('UPDATE ' + charName + ' SET init= "'+ str(initiative)+'"')
	cur.execute('UPDATE ' + charName + ' SET def= "'+ str(defense)+'"')
	cur.execute('UPDATE ' + charName + ' SET arm= "'+ str(armor)+'"')
	cur.execute('UPDATE ' + charName + ' SET commandrange= "'+ str(cmdrange)+'"')
	cur.execute('UPDATE ' + charName + ' SET career1= "'+ str(charCareers[0])+'"')
	cur.execute('UPDATE ' + charName + ' SET career2= "'+ str(charCareers[1])+'"')
	cur.execute('Select * from Tony')
	rows = cur.fetchall()
	for z in rows:
		tempbed.append(z)
	g = 0
	#while g < len(variables[0]):
		#print(variables[g],tempbed[0][g])
		#g+=1
#displayStats(charStats)

