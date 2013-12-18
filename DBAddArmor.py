import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('defaults.db')

dat = input('Do you want to add another Armor?')
while dat.lower() == 'yes':
	name = input('Name?')
	cost = input('Cost?')
	spdmod = input('Speed Modifier?')
	defmod = input('Defense Modifier?')
	armmod = input('Armor Modifier?')
	descrip = input('Description?')
	entry = (name,cost,spdmod,defmod,armmod,descrip)
	with con:
		cur = con.cursor() 
		cur.execute('INSERT INTO Armor VALUES(?,?,?,?,?,?)', entry)
	dat = input('Do you want to add another Armor?')