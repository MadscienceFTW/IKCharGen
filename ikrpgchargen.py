import os
baseStats = ["PHY","SPD","STR","AGL","PRW","POI","INT","ARC","PER"]
baseRaces = ["human","dwarf","gobber","iosan","nyss","ogrun","trollkin","satyxis"]
charStats = []
charArch = []
archEntry = []
charCareers = []
careers = []
humanStats = [5,6,4,3,4,4,3,"-",3,["gifted","intellectual","mighty","skilled"]]
dwarfStats = [6,4,5,3,4,3,4,"-",3,["gifted","intellectual","mighty","skilled"]]
gobberStats = [4,6,3,4,4,3,3,"-",3,["intellectual","mighty","skilled"]]
iosanStats = [5,6,4,3,4,4,4,"-",3,["gifted","intellectual","mighty","skilled"]]
nyssStats = [5,6,4,4,4,4,3,"-",3,["gifted","mighty","skilled"]]
ogrunStats = [6,5,6,3,4,3,3,"-",2,["mighty","skilled"]]
trollkinStats = [6,5,5,3,4,2,3,"-",3,["gifted","mighty","skilled"]]
satyxisStats= [5,6,5,3,4,3,3,"-",3,["gifted","mighty","skilled"]]
data = open('careers.txt')
for each_line in data:
	careers.append(each_line.rstrip('\n'))
data.close()
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
raceCount = 1
while raceCount > 0:
	raceEntry = input("What race would you like to play?")
	raceEntry = raceEntry.lower()
	if raceEntry == 'human':
		charStats = changingStats(humanStats)
		count = 1
		while count > 0:
			bonus = input("Which Base Stat is your Exceptional Potential? PHY, AGL or INT?")
			if bonus in ["PHY","AGL","INT"]:
				upgrade = baseStats.index(bonus)
				charStats[upgrade]+= 1
				count -= 1
			else:
				print("That isnt upgradable.")
		firstStats(charStats)
		raceCount -= 1
	elif raceEntry == 'dwarf':
		charStats = changingStats(dwarfStats)
		firstStats(charStats)
		raceCount -= 1
	elif raceEntry == 'gobber':
		charStats = changingStats(gobberStats)
		firstStats(charStats)
		raceCount -= 1
	elif raceEntry == 'iosan':
		charStats = changingStats(iosanStats)
		firstStats(charStats)
		raceCount -= 1
	elif raceEntry == 'nyss':
		charStats = changingStats(nyssStats)
		firstStats(charStats)
		raceCount -= 1
	elif raceEntry == 'ogrun':
		charStats = changingStats(ogrunStats)
		firstStats(charStats)
		raceCount -= 1
	elif raceEntry == 'trollkin':
		charStats = changingStats(trollkinStats)
		firstStats(charStats)
		raceCount -= 1
	elif raceEntry == 'satyxis':
		charStats = changingStats(satyxisStats)
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
displayStats(charStats)

