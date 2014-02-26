#!/usr/bin/python

"""
PiBooth Main GUI
"""

from PyQt4 import QtCore, QtGui, uic


class MainWindow(QtGui.QWidget):
	"""Main application window class. aka business logic"""
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent) # Qt has to do some initializing
		self.ui = uic.loadUi("lib/ui/MainWindow.ui", self) # This will compile the Designer file and return an object to which we can reference
		self.view_locked = False 
		self.ui.view.setCurrentIndex(0) # Precautionary measure

	def keyPressEvent(self, event): 
		""" Override the keypress handler """
		if self.view_locked == False:
			if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
				self.ui.view.setCurrentIndex(self.ui.view.currentIndex() + 1)

			elif event.key() == QtCore.Qt.Key_Backspace:
				self.ui.view.setCurrentIndex(self.ui.view.currentIndex() - 1)

			elif event.key() == QtCore.Qt.Key_B:
				# TODO: Fix focus issues 
				# See http://stackoverflow.com/questions/14482878/prevent-default-action-in-qt
				self.ui.button.click()

			elif event.key() == QtCore.Qt.Key_T:
				self.ui.timed_countdown.click() # TODO: Fix focus issues

			elif event.key() == QtCore.Qt.Key_Up:
				self.ui.countdown_time.setValue(self.ui.countdown_time.value() + 1)

			elif event.key() == QtCore.Qt.Key_Down:
				self.ui.countdown_time.setValue(self.ui.countdown_time.value() - 1)

	def closeEvent(self, event):
		""" Prevent close (This blocks Alt-F4!!!) """
		event.ignore()

	def reset_ui():
		""" Reset all of the UI elements to default values """
		pass # TODO: reset_ui
