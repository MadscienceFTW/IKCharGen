from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Race Display")
race = StringVar()
phys = StringVar()
sped = StringVar()
stre = StringVar()
agil = StringVar()
prow = StringVar()
pois = StringVar()
inte = StringVar()
arca = StringVar()
perc = StringVar()

def getrace():
	foo = racedrop.get()
	print(foo)
	if foo == 'Human':
		makeHuman()
	elif foo == "Dwarf":
		makeDwarf()
def makeHuman():
	phys.set('5')
	sped.set('6')
	stre.set('4')
	agil.set('3')
	prow.set('4')
	pois.set('4')
	inte.set('3')
	arca.set('0')
	perc.set('3')
def makeDwarf():
	phys.set('6')
	sped.set('4')
	stre.set('5')
	agil.set('3')
	prow.set('4')
	pois.set('3')
	inte.set('4')
	arca.set('0')
	perc.set('3')
def makeGobber():
	phys.set('4')
	sped.set('6')
	stre.set('3')
	agil.set('4')
	prow.set('4')
	pois.set('3')
	inte.set('3')
	arca.set('0')
	perc.set('3')
def makeNyss():
	phys.set('5')
	sped.set('6')
	stre.set('4')
	agil.set('4')
	prow.set('4')
	pois.set('4')
	inte.set('3')
	arca.set('0')
	perc.set('3')
def makeIosan():
	phys.set('5')
	sped.set('6')
	stre.set('4')
	agil.set('3')
	prow.set('4')
	pois.set('4')
	inte.set('4')
	arca.set('0')
	perc.set('3')
def makeTrollkin():
	phys.set('6')
	sped.set('5')
	stre.set('5')
	agil.set('3')
	prow.set('4')
	pois.set('2')
	inte.set('3')
	arca.set('0')
	perc.set('3')
def makeOgrun():
	phys.set('6')
	sped.set('5')
	stre.set('6')
	agil.set('3')
	prow.set('4')
	pois.set('3')
	inte.set('3')
	arca.set('0')
	perc.set('2')
def makeSatyxis():
	phys.set('5')
	sped.set('6')
	stre.set('5')
	agil.set('3')
	prow.set('4')
	pois.set('3')
	inte.set('3')
	arca.set('0')
	perc.set('3')

mainframe = ttk.Frame(root, padding="12", relief="groove")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

"""racedrop = ttk.Combobox(mainframe, textvariable = race)
racedrop['values'] = ('Human', 'Dwarf')
racedrop.grid(column=1, row=1, sticky=W)
racedrop.bind('<<ComboboxSelected>>', getrace())"""
humanbutton = ttk.Button(mainframe, text="Human", command=makeHuman)
humanbutton.grid(column=1, row=1, sticky=W)
dwarfbutton = ttk.Button(mainframe, text="Dwarf", command=makeDwarf)
dwarfbutton.grid(column=3, row=1, sticky=W)
gobberbutton = ttk.Button(mainframe, text="Gobber", command=makeGobber)
gobberbutton.grid(column=5, row=1, sticky=W)
nyssbutton = ttk.Button(mainframe, text="Nyss", command=makeNyss)
nyssbutton.grid(column=7, row=1, sticky=W)
iosanbutton = ttk.Button(mainframe, text="Iosan", command=makeIosan)
iosanbutton.grid(column=11, row=1, sticky=W)
trollkinbutton = ttk.Button(mainframe, text="Trollkin", command=makeTrollkin)
trollkinbutton.grid(column=13, row=1, sticky=W)
ogrunbutton = ttk.Button(mainframe, text="Ogrun", command=makeOgrun)
ogrunbutton.grid(column=15, row=1, sticky=W)
satyxisbutton = ttk.Button(mainframe, text="Satyxis", command=makeSatyxis)
satyxisbutton.grid(column=17, row=1, sticky=W)

ttk.Label(mainframe, text="PHY").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, textvariable=phys).grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="SPD").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=sped).grid(column=4, row=2, sticky=W)
ttk.Label(mainframe, text="STR").grid(column=5, row=2, sticky=W)
ttk.Label(mainframe, textvariable=stre).grid(column=6, row=2, sticky=W)
ttk.Label(mainframe, text="AGL").grid(column=7, row=2, sticky=W)
ttk.Label(mainframe, textvariable=agil).grid(column=8, row=2, sticky=W)
ttk.Label(mainframe, text="PRW").grid(column=9, row=2, sticky=W)
ttk.Label(mainframe, textvariable=prow).grid(column=10, row=2, sticky=W)
ttk.Label(mainframe, text="POI").grid(column=11, row=2, sticky=W)
ttk.Label(mainframe, textvariable=pois).grid(column=12, row=2, sticky=W)
ttk.Label(mainframe, text="INT").grid(column=13, row=2, sticky=W)
ttk.Label(mainframe, textvariable=inte).grid(column=14, row=2, sticky=W)
ttk.Label(mainframe, text="ARC").grid(column=15, row=2, sticky=W)
ttk.Label(mainframe, textvariable=arca).grid(column=16, row=2, sticky=W)
ttk.Label(mainframe, text="PER").grid(column=17, row=2, sticky=W)
ttk.Label(mainframe, textvariable=perc).grid(column=18, row=2, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
