from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Race Display")
race = StringVar()
phys = StringVar()
stre = StringVar()
sped = StringVar()
agil = StringVar()
prow = StringVar()
pois = StringVar()
inte = StringVar()
arca = StringVar()
perc = StringVar()

def makeHuman():
	phys.set('5')
	stre.set('6')
	sped.set('4')
	agil.set('3')
	prow.set('4')
	pois.set('4')
	inte.set('3')
	arca.set('0')
	perc.set('3')
		
mainframe = ttk.Frame(root, padding="12", relief="groove")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

racedrop = ttk.Combobox(mainframe, textvariable = race, values = ('Human', 'Dwarf'))
racedrop.grid(column=1, row=1, sticky=W)
print(racedrop.get())
'''racedrop.bind('<<ComboboxSelected>>', makeHuman)'''
'''humanbutton = ttk.Button(mainframe, text="Human", command=makeHuman).grid(column=1, row=1, sticky=W)
dwarfbutton = ttk.Button(mainframe, text="Dwarf").grid(column=3, row=1, sticky=W)
gobberbutton = ttk.Button(mainframe, text="Gobber").grid(column=5, row=1, sticky=W)
nyssbutton = ttk.Button(mainframe, text="Nyss").grid(column=7, row=1, sticky=W)
iosanbutton = ttk.Button(mainframe, text="Iosan").grid(column=11, row=1, sticky=W)
trollkinbutton = ttk.Button(mainframe, text="Trollkin").grid(column=13, row=1, sticky=W)
ogrunbutton = ttk.Button(mainframe, text="Ogrun").grid(column=15, row=1, sticky=W)
satyxisbutton = ttk.Button(mainframe, text="Satyxis").grid(column=17, row=1, sticky=W)'''

ttk.Label(mainframe, text="PHY").grid(column=1, row=2, sticky=W)
'''ttk.'''
ttk.Label(mainframe, textvariable=phys).grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="STR").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=stre).grid(column=4, row=2, sticky=W)
ttk.Label(mainframe, text="SPD").grid(column=5, row=2, sticky=W)
ttk.Label(mainframe, textvariable=sped).grid(column=6, row=2, sticky=W)
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
