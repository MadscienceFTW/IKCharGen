import os
import sqlite3 as lite
import sys
import csv
from tkinter import *
from tkinter import ttk

archEntry = []
careers = []
variables = []
tempbed = []
tembed = []
num = 0
spaReader = csv.reader(open('newcareers.txt'))
for row in spaReader:
	for x in row:
		careers.append(x)

spamReader = csv.reader(open('variables.txt'))
for row in spamReader:
	for x in row:
		variables.append(x)
for row in careers:
	num+=1
print(num)