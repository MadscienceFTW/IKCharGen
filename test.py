baseStats = ["PHY","SPD","STR","AGL","PRW","POI","INT","ARC","PER"]
charStats = []
charArch = []
archEntry = []
charCareers = []
careers = []
humanStats = [5,6,4,3,4,4,3,"-",3,["gifted","intellectual","mighty","skilled"]]
humanMax = [7,7,6,5,5,5,5,4,5]
dwarfStats = [6,4,5,3,4,3,4,"-",3,["gifted","intellectual","mighty","skilled"]]
gobberStats = [4,6,3,4,4,3,3,"-",3,["intellectual","mighty","skilled"]]
iosanStats = [5,6,4,3,4,4,4,"-",3,["gifted","intellectual","mighty","skilled"]]
nyssStats = [5,6,4,4,4,4,3,"-",3,["gifted","mighty","skilled"]]
ogrunStats = [6,5,6,3,4,3,3,"-",2,["mighty","skilled"]]
trollkinStats = [6,5,5,3,4,2,3,"-",3,["gifted","mighty","skilled"]]
satyxisStats = [5,6,5,3,4,3,3,"-",3,["gifted","mighty","skilled"]]
baseRaces = {"human":humanStats,"dwarf":dwarfStats,"gobber":gobberStats,"iosan":iosanStats,"nyss":nyssStats,"ogrun":ogrunStats,"trollkin":trollkinStats,"satyxis":satyxisStats}

humanStats = [5,6,4,3,4,4,3,0,3,["gifted","intellectual","mighty","skilled"]]

def changingStats(race):
	newStats = list(race)
	return newStats


charCareer = []
careers = ["alchemist","arcane mechanik","arcanist","aristocrat","bounty hunter",
	"cutthroat","duelist","explorer","fell caller","field mechanik","gun mage",
	"highwayman","investigator","iron fang","knight","mage hunter","man-at-arms",
	"military officer","pirate","priest of morrow","priest of menoth","rifleman",
	"soldier","sorcerer","spy","stormblade","thief","trencher","warcaster","pistoleer","ranger"]


print(charStats)
charStats = changingStats(baseRaces["human"])
print(charStats)
bonus = input("Which Base Stat is your Exceptional Potential? PHY, AGL or INT?")
if bonus in ["PHY","AGL","INT"]:
	upgrade = baseStats.index(bonus)
	charStats[upgrade]+= 1
else:
	print("That isnt upgradable.")
print(charStats)