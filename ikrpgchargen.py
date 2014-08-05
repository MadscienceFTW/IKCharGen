import os
import sqlite3 as lite
import sys
import csv

class Character:
	name = False
	race = False
	archetype = False
	career1 = False
	career2 = False
	phy = 0
	stg = 0
	spd = 0
	agl = 0
	prw = 0
	poi = 0
	itl = 0
	arc = 0
	per = 0
	willpower = 0
	initiative = 0
	defense = 0
	armor = 0
	cmdrange = 0
	baseStats = ["PHY","SPD","STR","AGL","PRW","POI","INT","ARC","PER"]
	def __init__(self):
		self.charStats = []
	def setName(self, name):
		self.name = name
	def setRace(self, race):
		self.race = race
	def setStats(self):
		self.phy = self.charStats[0]
		self.spd = self.charStats[1]
		self.stg = self.charStats[2]
		self.agl = self.charStats[3]
		self.prw = self.charStats[4]
		self.poi = self.charStats[5]
		self.itl = self.charStats[6]
		self.arc = self.charStats[7]
		self.per = self.charStats[8]
	def printStats(self, race):
		count = 0
		while count < 9:
			print(self.baseStats[count] + ":" + str(race[count]))
			count +=1
	def newPrintStats(self, race):
		print(self.baseStats[0] + ": " + str(self.phy))
		print(self.baseStats[1] + ": " + str(self.spd))
		print(self.baseStats[2] + ": " + str(self.stg))
		print(self.baseStats[3] + ": " + str(self.agl))
		print(self.baseStats[4] + ": " + str(self.prw))
		print(self.baseStats[5] + ": " + str(self.poi))
		print(self.baseStats[6] + ": " + str(self.itl))
		print(self.baseStats[7] + ": " + str(self.arc))
		print(self.baseStats[8] + ": " + str(self.per))
	def firstStats(self, race):
		os.system(clearingScreen())
		print("Here are that races stats and options:")
		self.printStats(race)
		self.displayArch(race)
	def displayStats(self, race):
		os.system(clearingScreen())
		print(self.name.capitalize())
		print(self.race.capitalize())
		print(self.printArch(race).capitalize())
		self.newPrintStats(race)
		print(self.career1)
		print(self.career2)
	def displayArch(self, race):
		for item in race[9]:
			print(str(item))
	def printArch(self, race):
		return (race[9])
	def careerChoice(self, choice):
		count = 0
		for x in careers:
			if x == choice:
				self.charCareers.append(careers[count])
			else:
				count+=1
	def finalStats(self):
		self.willpower = self.phy + self.itl
		self.initiative = self.spd + self.prw + self.per
		self.defense = self.spd + self.agl + self.per
		self.armor = self.phy
		self.cmdrange = self.itl
		if self.race == "gobber":
			self.defense += 1
		elif self.race == "nyss":
			self.initiative += 1
archEntry = []
careers = []
variables = []
tempbed = []
tembed = []
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
spaReader = csv.reader(open('newcareers.txt'))
for row in spaReader:
	for x in row:
		careers.append(x)
spamReader = csv.reader(open('variables.txt'))
for row in spamReader:
	for x in row:
		variables.append(x)
def changingStats(race):
	newStats = list(race)
	return newStats
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
	char = Character()
	char.name = charName
	print("Thank you, Your character is " + char.name)
raceCount = 1
while raceCount > 0:
	raceEntry = input("What race would you like " +char.name + " to be?")
	raceEntry = raceEntry.lower()
	char.race = raceEntry
	if char.race == 'human':
		char.charStats = changingStats(baseRaces[str(char.race)])
		char.setStats()
		count = 1
		while count > 0:
			char.firstStats(char.charStats)
			bonus = input("Which Base Stat is your Exceptional Potential? PHY, AGL or INT?")
			if bonus in ["PHY","AGL","INT"]:
				upgrade = char.baseStats.index(bonus)
				char.charStats[upgrade]+= 1
				count -= 1
			else:
				print("That isnt upgradable.")
		char.firstStats(char.charStats)
		raceCount -= 1
	elif char.race in baseRaces:
		char.charStats = changingStats(baseRaces[str(char.race)])
		char.firstStats(char.charStats)
		char.setStats()
		raceCount -= 1
	else:
		print("That is not one of the IK races.")
num = 1
while num > 0:	
	archEntry = input("Which Archetype would you like to use?")
	archEntry = archEntry.lower()
	if archEntry in char.charStats[9]:
		char.charStats[9] = archEntry
		os.system(clearingScreen())
		char.displayStats(char.charStats)
		char.archetype = archEntry
		num -=1
		if archEntry == 'gifted':
			char.charStats[7] = 0
	else:
		print("That is not one of the Archetypes available.")
uppoints = 3
char.displayStats(char.charStats)
while uppoints > 0:
	print("You have " + str(uppoints) + " upgrades remaining.")
	stat = input("Which stat would you like to upgrade?")
	stat = stat.upper()
	if stat in char.baseStats:
		upgrade = char.baseStats.index(stat)
	else:
		print("That is not a stat.")
		stat = input("Which stat would you like to upgrade?")
		stat = stat.upper()
	if char.charStats[upgrade] != "-":
		if stat in char.baseStats:
			char.charStats[upgrade]+= 1
			uppoints-=1
			char.displayStats(char.charStats)
	else:
		print("Can't do that")

while char.career1 == False and char.career2 == False:
	os.system(clearingScreen())
	char.displayStats(char.charStats)
	count = 2
	while count > 0:
		print("You have two choices for career from the following list:")
		for x in careers:
			print(x)
		choice = input("What is your choice?")
		if choice in careers:
			if char.career1 == choice or char.career2 == choice:
				print("You already chose that career.")
			elif char.career1 == False:
				char.career1 = choice
				count -= 1
			else:
				char.career2 = choice
				count -= 1
		else:
			print("That is not a selectable career.")
os.system(clearingScreen())
char.finalStats()