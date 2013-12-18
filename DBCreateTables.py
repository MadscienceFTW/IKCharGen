import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('defaults.db')

with con:
	cur = con.cursor() 

	cur.execute("DROP TABLE IF EXISTS Equipment")
	cur.execute("DROP TABLE IF EXISTS Weapons")
	cur.execute("DROP TABLE IF EXISTS MeleeWeapons")
	cur.execute("DROP TABLE IF EXISTS RangedWeapons")
	cur.execute("DROP TABLE IF EXISTS Armor")
	cur.execute("DROP TABLE IF EXISTS Spells")

	cur.execute('CREATE TABLE Equipment (name,cost,description)')
	cur.execute('CREATE TABLE MeleeWeapons (name,cost,skill,attmod,pow,description)')
	cur.execute('CREATE TABLE RangedWeapons (name,cost,ammo,effrange,extrange,skill,attmod,pow,aoe,description)')
	cur.execute('CREATE TABLE Armor (name,cost,spdmod,defmod,armmod,description)')
	cur.execute('CREATE TABLE Spells (name,cost,range,aoe,pow,upk,offen,descr)')