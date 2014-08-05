import csv
import sys
from PyQt4 import QtGui, QtCore
spaReader = []
careers = []
spaReader = csv.reader(open('newcareers.txt'))
for row in spaReader:
	for x in row:
		careers.append(x)

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()
	def initUI(self):
		grid = QtGui.QGridLayout()
		self.setLayout(grid)

		positions = [(i,j) for i in range(8) for j in range(7)]

		for position, name in zip(positions, careers):
			if name == '':
				continue
			button = QtGui.QPushButton(name)
			grid.addWidget(button, *position)

		self.move(300,150)
		self.setWindowTitle('Careers')
		self.show()
def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()