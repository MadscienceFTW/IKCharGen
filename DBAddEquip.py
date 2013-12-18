import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('defaults.db')

dat = input('Do you want to add another piece of Equipment?')
while dat.lower() == 'yes':
	name = input('Name?')
	cost = input('Cost?')
	descr = input('Description?')
	entry = (name,cost,descr)
	with con:
		cur = con.cursor()
		with con:
			cur = con.cursor() 
			cur.execute('INSERT INTO Equipment VALUES(?,?,?)', entry)
	dat = input('Do you want to add another piece of Equipment?')