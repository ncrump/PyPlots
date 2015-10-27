"""
Example GUI using pyQt4

Common modules include:
    QtCore    - core gui functionality
    QtGui     - graphical gui components
    QtNetwork - network programming
    QtXml     - xml support
    QtSvg     - graphical xml applications
    QtOpenGL  - graphics redering using openGL
    QtSql     - database support    
"""

import sys
import numpy as np
from PyQt4 import QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavToolbar
plt.ioff()

# gui is best done object oriented

# make class for the window object 
class ExampleGUI(QtGui.QWidget):
    
    
    # method to create gui
    def __init__(self):
        
        super(ExampleGUI, self).__init__()
        self.initUI()
                
    # method to set window functions
    def initUI(self):
        
        # setup a grid layout for objects
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)
        
        # create buttons
        btnA = QtGui.QPushButton('A')
        btnB = QtGui.QPushButton('B')
        btnC = QtGui.QPushButton('C')
        btnD = QtGui.QPushButton('D')
        entr = QtGui.QPushButton('Enter')
        plts = QtGui.QPushButton('Plot')
        
        # create labels
        winLab1 = QtGui.QLabel('Input 1')
        winLab2 = QtGui.QLabel('Input 2')
        
        # create input window
        self.window1 = QtGui.QLineEdit(self)       
        self.window2 = QtGui.QLineEdit(self) 
        
        # create drop down list
        self.dropdown = QtGui.QComboBox(self)
        self.dropdown.addItems(['cat','dog','bird','fish'])
        
        # create check box
        self.chkbox = QtGui.QCheckBox('Activate Laser',self)
        
        # create matplotlib plot window
        self.figure = plt.figure(figsize=(4,4))
        self.canvas = FigCanvas(self.figure)
        self.navbar = NavToolbar(self.canvas,self)
        
        # add objects to grid
        grid.addWidget(btnA,2,0)
        grid.addWidget(btnC,3,0) 
        
        grid.addWidget(btnB,2,1)
        grid.addWidget(btnD,3,1)
        
        grid.addWidget(self.navbar,0,2,1,8)
        grid.addWidget(self.canvas,1,2,8,8) 
        
        grid.addWidget(plts,9,5,1,2) 
        
        grid.addWidget(winLab2,6,11)
        grid.addWidget(winLab1,7,11)
        
        grid.addWidget(self.dropdown,2,12)
        grid.addWidget(self.chkbox,5,12)
        grid.addWidget(self.window1,6,12)
        grid.addWidget(self.window2,7,12)
        grid.addWidget(entr,9,12)
       
        # set button tip
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        btnA.setToolTip('button tip')
        btnB.setToolTip('button tip')
        btnC.setToolTip('button tip')
        btnD.setToolTip('button tip')
        
        # set button click event
        btnA.clicked.connect(self.buttonClicked)            
        btnB.clicked.connect(self.buttonClicked)
        btnC.clicked.connect(self.buttonClicked)            
        btnD.clicked.connect(self.buttonClicked)
        entr.clicked.connect(self.buttonClicked)
        plts.clicked.connect(self.genPlot)
        
        # draw window
        self.setGeometry(300,300,650,380)
        self.setWindowTitle('Example GUI')
        self.setWindowIcon(QtGui.QIcon('img.png'))        
        self.show()
        
    # method to handle button clicks
    def buttonClicked(self):
        # get buttons pressed
        sender = self.sender()
        sval   = sender.text()
        print 'Button ' + sval + ' was pressed'
        
        # button functions
        if sval == 'A':
            print 'do nothing'
        if sval == 'B':
            print 'do nothing'
        if sval == 'C':
            print 'do nothing'
        if sval == 'D':
            print 'do nothing'
        if sval == 'Enter':
            input1 = self.window1.text()
            input2 = self.window2.text()
            dropdn = self.dropdown.currentText()
            if input1 == '': input1 = 'Empty'
            if input2 == '': input2 = 'Empty'
            print input1
            print input2
            print dropdn
            if self.chkbox.isChecked():
                print 'Activate Laser'
            else: print 'No Laser ;('
            
    # method to generate plot
    def genPlot(self):
        # generate data
        x = range(10)
        y = np.random.rand(10)
        print 'plotting'
        
        # draw plot
        ax = self.figure.add_subplot(111)
        ax.hold(False)
        ax.plot(x,y)
        ax.set_ylim(0,1)
        self.canvas.draw()
            
# main startup method
def main():
    app = QtGui.QApplication(sys.argv)
    ex = ExampleGUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()