import sqlite3 as lite
import sys
import os
import csv
import xml.etree.ElementTree as ET

variables = []
testbed = []
con = lite.connect('firsttest.db')
csvWriter = csv.writer(open("output.txt", "w"))
with con:
	cur = con.cursor()
	cur.execute('Select * from Tony')
	rows = cur.fetchall()
	csvWriter.writerows(rows)
#data2 = open('f:\\Dev\\IKChargen\\variables.txt')
#for each_line in data2:
#	variables.append(each_line.split(','))
#data2.close()
spamReader = csv.reader(open('variables.txt',newline=''))
for row in spamReader:
	variables.append(row)
for x in variables[0]:
	testbed.append(x)
#print(testbed)
tree = ET.parse('IKTestSheet.svg')
root = tree.getroot()
#print(root[4][2][0].attrib) # prints PHY tspan text
for rank in root[4].findall(".//*[@id='PHY']"):
	newtext = "Anthony"
	rank.text = str(newtext)
tree.write('IKTestSheet.svg')