#!/usr/bin/python

import sys
from PyQt4 import QtGui
from lib import MainWindow

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())