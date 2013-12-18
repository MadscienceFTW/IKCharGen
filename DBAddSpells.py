import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('defaults.db')
dat = input('Do you want to add another Spell?')
while dat.lower() == 'yes':
	name = input('Name?')
	cost = input('Cost?')
	range = input('RNG?')
	aoe = input('AOE?')
	pow = input('POW?')
	upk = input('Upkeep Spell?')
	offen = input('Offensive Spell?')
	descr = input('Description?')
	entry = (name,cost,range,aoe,pow,upk,offen,descr)
	with con:
		cur = con.cursor()
		cur.execute('INSERT INTO Spells VALUES(?,?,?,?,?,?,?,?)', entry)
	dat = input('Do you want to add another Spell?')