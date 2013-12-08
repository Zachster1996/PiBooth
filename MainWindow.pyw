#!/usr/bin/python

"""
PiBooth Main GUI
"""

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QWidget):
    """Main application window class"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def initUI(self):

        # Set up window stuff
        self.showFullScreen()
        self.setWindowTitle('PiBooth')
        #self.setFocusPolicy(QtCore.Qt.StrongFocus) # Currently not working

        # Add objects
        main_label = QtGui.QLabel("PiBooth", self)

        # Set Layouts
        main_layout = QtGui.QHBoxLayout()
        main_layout.addStretch(1)
        main_layout.addWidget(main_label)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

        # Render window
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()