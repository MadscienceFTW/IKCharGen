from tkinter import *
from tkinter import ttk
races = ["Human", "Dwarf", "Gobber", "Nyss", "Iosan", "Trollkin", "Ogrun", "Satyxis"]
raceArch = []
careers = []
def getRace():
	try:
		race = "Human"
		raceArch = ["Gifted", "Mighty", "Intellectual", "Skilled"]
		print(raceArch)
	except ValueError:
		pass
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