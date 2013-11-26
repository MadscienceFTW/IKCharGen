import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('defaults.db')

dat = input('Do you want to add another Weapon?')
while dat.lower() == 'yes':
	name = input('Name?')
	cost = input('Cost?')
	skill = input('Skill?')
	attmod = input('Attack Modifier?')
	pow = input('POW?')
	descr = input('Description?')
	entry = (name,cost,skill,attmod,pow,descr)
	with con:
		cur = con.cursor() 
		cur.execute('INSERT INTO Weapons VALUES(?,?,?,?,?,?)', entry)
	dat = input('Do you want to add another Weapon?')