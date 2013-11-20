import sqlite3 as lite
import sys
import os
import csv

con = lite.connect('firsttest.db')

careers = []
if os.name == 'nt':
	data = open("f:\\Dev\\IKCharGen\\newcareers.txt")
elif os.name == 'posix':
	data = open('~/Dropbox/Dev/IK/careers.txt')
for each_line in data:
	careers.append(each_line)
data.close()
with open('newcareers.txt','r') as fin:
	dr = csv.reader(fin)
	for x in dr:
		for y in x:
			print((y,))