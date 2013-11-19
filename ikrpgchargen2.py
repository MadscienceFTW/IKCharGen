import os
baseStats = ["PHY","SPD","STR","AGL","PRW","POI","INT","ARC","PER"]
charStats = []
charArch = []
archEntry = []
charCareers = []
humanBaseStats = [5,6,4,3,4,4,3,0,3]
humanStats = [5,6,4,3,4,4,3,0,3,["gifted","intellectual","mighty","skilled"]]
dwarfBaseStats = [6,4,5,3,4,3,4,0,3]
dwarfStats = [6,4,5,3,4,3,4,0,3,["gifted","intellectual","mighty","skilled"]]
gobberBaseStats = [4,6,3,4,4,3,3,0,3]
gobberStats = [4,6,3,4,4,3,3,0,3,["intellectual","mighty","skilled"]]
iosanBaseStats = [5,6,4,3,4,4,4,0,3]
iosanStats = [5,6,4,3,4,4,4,0,3,["gifted","intellectual","mighty","skilled"]]
nyssBaseStats = [5,6,4,4,4,4,3,0,3]
nyssStats = [5,6,4,4,4,4,3,0,3,["gifted","mighty","skilled"]]
ogrunBaseStats = [6,5,6,3,4,3,3,0,2]
ogrunStats = [6,5,6,3,4,3,3,0,2,["mighty","skilled"]]
trollkinBaseStats = [6,5,5,3,4,2,3,0,3]
trollkinStats = [6,5,5,3,4,2,3,0,3,["gifted","mighty","skilled"]]
satyxisBaseStats= [5,6,5,3,4,3,3,0,3]
satyxisStats= [5,6,5,3,4,3,3,0,3,["gifted","mighty","skilled"]]
careers = ["alchemist","arcane mechanik","arcanist","aristocrat","bounty hunter",
	"cutthroat","duelist","explorer","fell caller","field mechanik","gun mage",
	"highwayman","investigator","iron fang","knight","mage hunter","man-at-arms",
	"military officer","pirate","priest of morrow","priest of menoth","rifleman",
	"soldier","sorcerer","spy","stormblade","thief","trencher","warcaster","pistoleer","ranger"]

def displayStats(race):
	os.system('cls')
	os.system('clear')
	print(raceEntry)
	print "PHY:" + str(race[0]) + " SPD:" + str(race[1]) + " STR:" + str(race[2]) +\
	" AGI:" + str(race[3]) + " PRW:" + str(race[4]) + " POI:" + str(race[5]) \
	+ " INT:" + str(race[6]) + " ARC:" + str(race[7]) + " PER:" + str(race[8])
	print archEntry
	for x in charCareers:
		print x
def displayArch(race):
	for item in race[9]:
		print str(item)
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

raceEntry = raw_input("What race would you like to play?")
raceEntry = raceEntry.lower()
if raceEntry == 'human':
	charStats = changingStats(humanBaseStats)
	os.system('cls')
	os.system('clear')
	print "Here are that races stats and options:"
	displayStats(charStats)
	displayArch(humanStats)
elif raceEntry == 'dwarf':
	charStats = changingStats(dwarfBaseStats)
	os.system('cls')
	os.system('clear')
	print "Here are that races stats and options:"
	displayStats(charStats)
	displayArch(dwarfStats)
elif raceEntry == 'gobber':
	charStats = changingStats(gobberBaseStats)
	os.system('cls')
	os.system('clear')
	print "Here are that races stats and options:"
	displayStats(charStats)
	displayArch(gobberStats)
elif raceEntry == 'iosan':
	charStats = changingStats(iosanBaseStats)
	os.system('cls')
	os.system('clear')
	print "Here are that races stats and options:"
	displayStats(charStats)
	displayArch(iosanStats)
elif raceEntry == 'nyss':
	charStats = changingStats(nyssBaseStats)
	os.system('cls')
	os.system('clear')
	print "Here are that races stats and options:"
	displayStats(charStats)
	displayArch(nyssStats)
elif raceEntry == 'ogrun':
	charStats = changingStats(ogrunBaseStats)
	os.system('cls')
	os.system('clear')
	print "Here are that races stats and options:"
	displayStats(charStats)
	displayArch(ogrunStats)
elif raceEntry == 'trollkin':
	charStats = changingStats(trollkinBaseStats)
	os.system('cls')
	os.system('clear')
	print "Here are that races stats and options:"
	displayStats(charStats)
	displayArch(trollkinStats)
elif raceEntry == 'satyxis':
	charStats = changingStats(satyxisBaseStats)
	os.system('cls')
	os.system('clear')
	print "Here are that races stats and options:"
	displayStats(charStats)
	displayArch(satyxisStats)
else:
	print "That is not one of the IK races."
	
archEntry = raw_input("Which Archetype would you like to use?")
archEntry = archEntry.lower()
if raceEntry == 'human':
	if archEntry in humanStats[9]:
		os.system('cls')
		os.system('clear')
		print archEntry
	else:
		print "That is not one of the Archetypes available."
elif raceEntry == 'dwarf':
	if archEntry in dwarfStats[9]:
		os.system('cls')
		os.system('clear')
		print archEntry
	else:
		print "That is not one of the Archetypes available."
elif raceEntry == 'gobber':
	if archEntry in gobberStats[9]:
		os.system('cls')
		os.system('clear')
		print archEntry
	else:
		print "That is not one of the Archetypes available."
elif raceEntry == 'iosan':
	if archEntry in iosanStats[9]:
		os.system('cls')
		os.system('clear')
		print archEntry
	else:
		print "That is not one of the Archetypes available."
elif raceEntry == 'nyss':
	if archEntry in nyssArch:
		os.system('cls')
		os.system('clear')
		print archEntry
	else:
		print "That is not one of the Archetypes available."
elif raceEntry == 'ogrun':
	if archEntry in ogrunArch:
		os.system('cls')
		os.system('clear')
		print archEntry
	else:
		print "That is not one of the Archetypes available."
elif raceEntry == 'trollkin':
	if archEntry in trollkinArch:
		os.system('cls')
		os.system('clear')
		print archEntry
	else:
		print "That is not one of the Archetypes available."
elif raceEntry == 'satyxis':
	if archEntry in satyxisArch:
		os.system('cls')
		os.system('clear')
		print archEntry
	else:
		print "That is not one of the Archetypes available."
else:
	print "That is not one of the races Archetypes."
uppoints = 3
os.system('cls')
os.system('clear')
displayStats(charStats)
while uppoints > 0:
	print "You have " + str(uppoints) + " upgrades remaining."
	stat = raw_input("Which stat would you like to upgrade?")
	stat = stat.upper()
	if stat == "PHY":
		charStats[0]+= 1
		uppoints-=1
		displayStats(charStats)
	elif stat == "SPD":
		charStats[1]+= 1
		uppoints-=1
		displayStats(charStats)
	elif stat == "STR":
		charStats[2]+= 1
		uppoints-=1
		displayStats(charStats)
		print(archEntry)
	elif stat == "AGI":
		charStats[3]+= 1
		uppoints-=1
		displayStats(charStats)
	elif stat == "PRW":
		charStats[4]+= 1
		uppoints-=1
		displayStats(charStats)
	elif stat == "POI":
		charStats[5]+= 1
		uppoints-=1
		displayStats(charStats)
	elif stat == "INT":
		charStats[6]+= 1
		uppoints-=1
		displayStats(charStats)
	elif stat == "ARC":
		charStats[7]+= 1
		uppoints-=1
		displayStats(charStats)
	elif stat == "PER":
		charStats[8]+= 1
		uppoints-=1
		displayStats(charStats)

careerCount = 2
while careerCount > 0:
	print "You have two choices for career from the following list:"
	for x in careers:
		print x
	choice = raw_input("What is your choice?")
	if choice in careers:
		if choice in charCareers:
			print "You already chose that career."
		else:
			careerChoice(choice)
			careerCount-=1
	else:
		print "That is not a selectable career."
displayStats(charStats)

