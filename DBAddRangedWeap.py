import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('defaults.db')

dat = input('Do you want to add another Ranged Weapon?')
while dat.lower() == 'yes':
	name = input('Name?')
	cost = input('Cost?')
	ammo = input('Ammo?')
	effrange = input('Effective Range?')
	extrange = input('Extreme Range?')
	skill = input('Skill?')
	attmod = input('Attack Modifier?')
	pow = input('POW?')
	aoe = input('AOE?')
	descr = input('Description?')
	entry = (name,cost,ammo,effrange,extrange,skill,attmod,pow,aoe,descr)
	with con:
		cur = con.cursor() 
		cur.execute('INSERT INTO RangedWeapons VALUES(?,?,?,?,?,?,?,?,?,?)', entry)
	dat = input('Do you want to add another Ranged Weapon?')