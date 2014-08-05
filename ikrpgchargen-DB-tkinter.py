import os
import sqlite3 as lite
import sys
import csv
from tkinter import *
from tkinter import ttk
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
con = lite.connect('firsttest.db')
skilTab = str(char.name + "Skills")
abilTab = str(char.name + "Abilities")
spelTab = str(char.name + "Spells")
equiTab = str(char.name + "Equipment")
weapTab = str(char.name + "Weapons")
armoTab = str(char.name + "Armor")
with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS " + char.name)
	cur.execute("DROP TABLE IF EXISTS " + skilTab)
	cur.execute("DROP TABLE IF EXISTS " + abilTab)
	cur.execute("DROP TABLE IF EXISTS " + spelTab)
	cur.execute("DROP TABLE IF EXISTS " + equiTab)
	cur.execute("DROP TABLE IF EXISTS " + weapTab)
	cur.execute("DROP TABLE IF EXISTS " + armoTab)
	cur.execute("""CREATE TABLE """ + char.name + """
					(name,race,archtype,phy,spd,str,agl,prw,poi,int,arc,per,willpower,skills,equipment,mat,matpow,rat,ratrange,ratpow,def,arm,lifespiral,featpoints,career1,career2,sex,faith,height,weight,xp,init,commandrange,abilities,spells)
				""")
	cur.execute('CREATE TABLE ' + skilTab + ' (name,linked,description)')
	cur.execute('CREATE TABLE ' + abilTab + ' (name,preq,description)')
	cur.execute('CREATE TABLE ' + spelTab + ' (name,cost,range,aoe,pow,up,off,description)')
	cur.execute('CREATE TABLE ' + equiTab + ' (name,description)')
	cur.execute('CREATE TABLE ' + weapTab + ' (name,cost,skill,attmod,pow,description)')
	cur.execute('CREATE TABLE ' + armoTab + ' (name,cost,spdmod,defmod,armmod,description)')
	cur.execute("INSERT INTO " + char.name +"(name) VALUES ('"+ str(char.name)+"')")
	cur.execute('UPDATE ' + char.name + ' SET race= "'+ str(char.race)+'"')
	cur.execute('UPDATE ' + char.name + ' SET archtype= "'+ str(archEntry)+'"')
	cur.execute('UPDATE ' + char.name + ' SET phy= "'+ str(char.phy)+'"')
	cur.execute('UPDATE ' + char.name + ' SET spd= "'+ str(char.spd)+'"')
	cur.execute('UPDATE ' + char.name + ' SET str= "'+ str(char.stg)+'"')
	cur.execute('UPDATE ' + char.name + ' SET agl= "'+ str(char.agl)+'"')
	cur.execute('UPDATE ' + char.name + ' SET prw= "'+ str(char.prw)+'"')
	cur.execute('UPDATE ' + char.name + ' SET poi= "'+ str(char.poi)+'"')
	cur.execute('UPDATE ' + char.name + ' SET int= "'+ str(char.itl)+'"')
	cur.execute('UPDATE ' + char.name + ' SET arc= "'+ str(char.arc)+'"')
	cur.execute('UPDATE ' + char.name + ' SET per= "'+ str(char.per)+'"')
	cur.execute('UPDATE ' + char.name + ' SET willpower= "'+ str(char.willpower)+'"')
	cur.execute('UPDATE ' + char.name + ' SET init= "'+ str(char.initiative)+'"')
	cur.execute('UPDATE ' + char.name + ' SET def= "'+ str(char.defense)+'"')
	cur.execute('UPDATE ' + char.name + ' SET arm= "'+ str(char.armor)+'"')
	cur.execute('UPDATE ' + char.name + ' SET commandrange= "'+ str(char.cmdrange)+'"')
	cur.execute('UPDATE ' + char.name + ' SET career1= "'+ str(char.career1)+'"')
	cur.execute('UPDATE ' + char.name + ' SET career2= "'+ str(char.career2)+'"')
	cur.execute('Select * from Tony')
	"""rows = cur.fetchall()
	generic = []
	reliable = []
	for u in rows[0]:
		generic.append(u)
	cur.execute('PRAGMA table_info(Tony)')
	lines = cur.fetchall()
	for j in lines:
		reliable.append(j[1])
	g = 0
	while g < len(variables):
		print('{:<12} {:}'.format(reliable[g],generic[g]))
		g+=1"""
#char.displayStats(char.charStats)
root = Tk()
root.title("Race Stats")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=N)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Name:").grid(column=1, row=1)
ttk.Label(mainframe, text=char.name.capitalize()).grid(column=2, row=1)
ttk.Label(mainframe, text="Race:").grid(column=3, row=1)
ttk.Label(mainframe, text=char.race.capitalize()).grid(column=4, row=1)
ttk.Label(mainframe, text="Archetype:").grid(column=5, row=1)
ttk.Label(mainframe, text=char.archetype.capitalize()).grid(column=6, row=1)
#ttk.Button(mainframe, text="GetRace").grid(column=7, row=1)

subframe = ttk.Frame(root, padding="3 3 12 12")
subframe.grid(column=0, row=1, sticky=W)
subframe.columnconfigure(0, weight=1)
subframe.rowconfigure(0, weight=1)
subframe['borderwidth'] = 3
subframe['relief'] = 'sunken'

ttk.Label(subframe, text="Career1:").grid(column=1, row=1)
ttk.Label(subframe, text=char.career1).grid(column=2, row=1)
ttk.Label(subframe, text="Career2:").grid(column=3, row=1)
ttk.Label(subframe, text=char.career2).grid(column=4, row=1)

att = ttk.Frame(root, padding="3 3 12 12")
att.grid(column=0, row=2, sticky=W)
att['borderwidth'] = 4
att['relief'] = 'raised'

ttk.Label(att, text="PHY:").grid(column=1, row=2, sticky=W)
ttk.Label(att, text=char.phy).grid(column=2, row=2, sticky=W)
ttk.Label(att, text="SPD:").grid(column=3, row=1)
ttk.Label(att, text=char.spd).grid(column=4, row=1)
ttk.Label(att, text="STR:").grid(column=3, row=3)
ttk.Label(att, text=char.stg).grid(column=4, row=3)
ttk.Label(att, text="AGL:").grid(column=1, row=5, sticky=W)
ttk.Label(att, text=char.agl).grid(column=2, row=5, sticky=W)
ttk.Label(att, text="PRW:").grid(column=3, row=4)
ttk.Label(att, text=char.prw).grid(column=4, row=4)
ttk.Label(att, text="POI:").grid(column=3, row=6)
ttk.Label(att, text=char.poi).grid(column=4, row=6)
ttk.Label(att, text="INT:").grid(column=1, row=8, sticky=W)
ttk.Label(att, text=char.itl).grid(column=2, row=8, sticky=W)
ttk.Label(att, text="ARC:").grid(column=3, row=7)
ttk.Label(att, text=char.arc).grid(column=4, row=7)
ttk.Label(att, text="PER:").grid(column=3, row=9)
ttk.Label(att, text=char.per).grid(column=4, row=9)

derived = ttk.Frame(root, padding="3 3 12 12")
derived.grid(column=1, row=2, sticky=(W, E))
derived['borderwidth'] = 2
derived['relief'] = 'sunken'
ttk.Label(derived, text="Def:").grid(column=1, row=1, sticky=W)
ttk.Label(derived, text=char.defense).grid(column=2, row=1, sticky=W)
ttk.Label(derived, text="Arm:").grid(column=1, row=2, sticky=W)
ttk.Label(derived, text=char.armor).grid(column=2, row=2, sticky=W)
ttk.Label(derived, text="Init:").grid(column=1, row=3, sticky=W)
ttk.Label(derived, text=char.initiative).grid(column=2, row=3, sticky=W)
ttk.Label(derived, text="CMD:").grid(column=1, row=4, sticky=W)
ttk.Label(derived, text=char.cmdrange).grid(column=2, row=4, sticky=W)
ttk.Label(derived, text="WP:").grid(column=1, row=5, sticky=W)
ttk.Label(derived, text=char.willpower).grid(column=2, row=5, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()