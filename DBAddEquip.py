import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('defaults.db')

with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Equipment")
	cur.execute("DROP TABLE IF EXISTS Weapons")
	cur.execute("DROP TABLE IF EXISTS Armor")

	cur.execute('CREATE TABLE Equipment (name,description)')
	cur.execute('CREATE TABLE Weapons (name,cost,skill,attmod,pow,description)')
	cur.execute('CREATE TABLE Armor (name,cost,spdmod,defmod,armmod,description)')