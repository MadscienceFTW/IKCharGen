from tkinter import *
from tkinter import ttk
races = ["Human", "Dwarf", "Gobber", "Nyss", "Iosan", "Trollkin", "Ogrun", "Satyxis"]
raceArch = []
careers = []
def getRace():
	try:
		alpha = races.selection()
		raceArch = ["Gifted", "Mighty", "Intellectual", "Skilled"]
		print(alpha)
	except ValueError:
		pass
con = lite.connect('firsttest.db')
with con:
	cur = con.cursor()
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
root = Tk()
root.title("Race Stats")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=N)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Name").grid(column=1, row=1)
ttk.Entry(mainframe).grid(column=2, row=1)
ttk.Label(mainframe, text="Race").grid(column=3, row=1)
raceEntry = ttk.Combobox(mainframe, values=races).grid(column=4, row=1)
ttk.Label(mainframe, text="Archetype").grid(column=5, row=1)
ttk.Combobox(mainframe, values=raceArch).grid(column=6, row=1)
ttk.Button(mainframe, text="GetRace", command=getRace).grid(column=7, row=1)

subframe = ttk.Frame(root, padding="3 3 12 12")
subframe.grid(column=0, row=1, sticky=W)
subframe.columnconfigure(0, weight=1)
subframe.rowconfigure(0, weight=1)

ttk.Label(subframe, text="Career1").grid(column=1, row=1)
ttk.Combobox(subframe, text=careers).grid(column=2, row=1)
ttk.Label(subframe, text="Career2").grid(column=3, row=1)
ttk.Combobox(subframe, text=careers).grid(column=4, row=1)

attframe = ttk.Frame(root, padding="3 3 12 12")
attframe.grid(column=0, row=2, sticky=W)

ttk.Label(attframe, text="PHY:").grid(column=1, row=2, sticky=W)
ttk.Label(attframe, text=1).grid(column=2, row=2)
ttk.Label(attframe, text="SPD:").grid(column=3, row=1, sticky=(N,E))
ttk.Label(attframe, text=2).grid(column=4, row=1)
ttk.Label(attframe, text="STR:").grid(column=3, row=3, sticky=E)
ttk.Label(attframe, text=3).grid(column=4, row=3)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()

'''root = Tk()
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

root.mainloop()'''