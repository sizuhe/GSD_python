from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
import time
import ctypes
import sys

from serialcomm import SerialComm
from datasave import DataSave
from graphs import GraphPlot



# Create main window
app = QApplication(sys.argv)
mainWindow = QMainWindow()
mainWindow.resize(767,544)

# Details of app
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('icons')
mainWindow.setWindowIcon(QtGui.QIcon('icons/DeltaV.png'))
mainWindow.setWindowTitle("Multipurpose Datalogger")

# Instance of each graph
graph1_ins = GraphPlot()
graph2_ins = GraphPlot()
graph3_ins = GraphPlot()
graph4_ins = GraphPlot()
graph5_ins = GraphPlot()
graph6_ins = GraphPlot()
graph7_ins = GraphPlot()
graph8_ins = GraphPlot()

# Data save instance
#? Parameter: number of graphics to be save. If changed, line 386 must also be changed.
datasave_ins = DataSave(8)

# Serial communication instance
serialcomm_ins = SerialComm()



#* ===== User Interface =====

# Main interface objects
Interface = QtWidgets.QWidget()
gridInterface = QtWidgets.QGridLayout(Interface)

#* ----------------------------------------

# TAB WIDGET
groupTabWidget = QtWidgets.QTabWidget(Interface)
groupTabWidget.setMinimumSize(QtCore.QSize(270, 270))
groupTabWidget.setMaximumSize(QtCore.QSize(270, 300))
gridInterface.addWidget(groupTabWidget, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

# --------------------
## PAGE 1 - 'Data collection'
groupTabWidget_Pag1 = QtWidgets.QWidget()
gridTabWidget_Pag1 = QtWidgets.QGridLayout(groupTabWidget_Pag1)
groupTabWidget.addTab(groupTabWidget_Pag1, "Data collection")

#### BoldText
boldText = QtGui.QFont()
boldText.setBold(True)

### Test mode status
Pag1_TestmodeON = QtWidgets.QLabel(groupTabWidget_Pag1)
Pag1_TestmodeON.setFrameShape(QtWidgets.QFrame.Box)
Pag1_TestmodeON.setFrameShadow(QtWidgets.QFrame.Sunken)
Pag1_TestmodeON.setAlignment(QtCore.Qt.AlignCenter)
Pag1_TestmodeON.setText("Testmode ON")
Pag1_TestmodeOFF = QtWidgets.QLabel(groupTabWidget_Pag1)
Pag1_TestmodeOFF.setFrameShape(QtWidgets.QFrame.Box)
Pag1_TestmodeOFF.setFrameShadow(QtWidgets.QFrame.Sunken)
Pag1_TestmodeOFF.setAlignment(QtCore.Qt.AlignCenter)
Pag1_TestmodeOFF.setText("Testmode OFF")

### Connected port details
Pag1_ArduinoText = QtWidgets.QLabel(groupTabWidget_Pag1)
Pag1_ArduinoText.setAlignment(QtCore.Qt.AlignRight)
Pag1_ArduinoText.setText("Details")
Pag1_ArduinoText.setFont(boldText)
arduinoName = serialcomm_ins.getArduinoName()
Pag1_ArduinoName = QtWidgets.QLabel(groupTabWidget_Pag1)
Pag1_ArduinoName.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
Pag1_ArduinoName.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
Pag1_ArduinoName.setText(arduinoName)

# Horizontal line
Pag1_horizontalLine = QtWidgets.QFrame(groupTabWidget_Pag1)
Pag1_horizontalLine.setFrameShape(QtWidgets.QFrame.HLine)
Pag1_horizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)

### Elapsed time
Pag1_TimeText = QtWidgets.QLabel(groupTabWidget_Pag1)
Pag1_TimeText.setFont(QtGui.QFont("default",12))
Pag1_TimeText.setAlignment(QtCore.Qt.AlignCenter)
Pag1_TimeText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
Pag1_TimeText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
Pag1_TimeText.setText("Time [s]")
Pag1_TimeLCD = QtWidgets.QLCDNumber(groupTabWidget_Pag1)
Pag1_TimeLCD.setFrameShape(QtWidgets.QFrame.NoFrame)
Pag1_TimeLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
Pag1_TimeLCD.setProperty("value", 0)

### Push buttons
Pag1_ButtonStart = QtWidgets.QPushButton(groupTabWidget_Pag1)
Pag1_ButtonStart.setText("Start")
Pag1_ButtonStop = QtWidgets.QPushButton(groupTabWidget_Pag1)
Pag1_ButtonStop.setText("Stop")

### Light
Pag1_Light = QtWidgets.QProgressBar(groupTabWidget_Pag1)
Pag1_Light.setProperty("value", 0)
Pag1_Light.setTextVisible(False)

### Spacer
Pag1_spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed)

### Authors/credits box
Pag1_CreditsBox = QtWidgets.QLabel(groupTabWidget_Pag1)
Pag1_CreditsBox.setFrameShape(QtWidgets.QFrame.Box)
Pag1_CreditsBox.setFrameShadow(QtWidgets.QFrame.Sunken)
Pag1_CreditsBox.setAlignment(QtCore.Qt.AlignCenter)
Pag1_CreditsBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
Pag1_CreditsBox.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
Pag1_CreditsBox.setWordWrap(True)
####################!
Pag1_CreditsBox.setText("V1.0 beta 13.1\n\n"
"Developed by\n"
"Simón Zuluaga y Mateo Lezama\n\n"
"Delta V - Student research group\n"
"Universidad de Antioquia")
####################!

### Adding widgets to tab widget page 1 - 'Data collection'
gridTabWidget_Pag1.addWidget(Pag1_TestmodeON, 0, 0, 1, 1)
gridTabWidget_Pag1.addWidget(Pag1_TestmodeOFF, 0, 1, 1, 1)
gridTabWidget_Pag1.addWidget(Pag1_ArduinoText, 1, 0, 1, 1)
gridTabWidget_Pag1.addWidget(Pag1_ArduinoName, 1, 1, 1, 1)
gridTabWidget_Pag1.addWidget(Pag1_horizontalLine, 2, 0, 1, 2)
gridTabWidget_Pag1.addWidget(Pag1_TimeText, 3, 0, 1, 1)
gridTabWidget_Pag1.addWidget(Pag1_TimeLCD, 3, 1, 1, 1)
gridTabWidget_Pag1.addWidget(Pag1_ButtonStart, 4, 0, 1, 1)
gridTabWidget_Pag1.addWidget(Pag1_ButtonStop, 4, 1, 1, 1)
gridTabWidget_Pag1.addWidget(Pag1_Light, 5, 0, 1, 2)
gridTabWidget_Pag1.addItem(Pag1_spacerItem, 6, 0, 1, 2)
gridTabWidget_Pag1.addWidget(Pag1_CreditsBox, 7, 0, 1, 2)

# Datasave light ON-OFF functions
def Light_ON():
    Pag1_Light.setProperty("value", 100)
def Light_OFF():
    Pag1_Light.setProperty("value", 0)

# Test mode light ON-OFF
if serialcomm_ins.getTestStatus() == True:
    Pag1_TestmodeON.setStyleSheet("background-color: rgb(46,180,87)")
    Pag1_TestmodeON.setFont(boldText)
else:
    Pag1_TestmodeOFF.setStyleSheet("background-color: rgb(220,40,57)")
    Pag1_TestmodeOFF.setFont(boldText)

# Data saving functions
def dataStop():
    return datasave_ins.Stop(Pag1_TimeLCD)

# Tab Widget buttons actions
Pag1_ButtonStart.clicked.connect(Light_ON)
Pag1_ButtonStart.clicked.connect(datasave_ins.signalStart)
Pag1_ButtonStop.clicked.connect(Light_OFF)
Pag1_ButtonStop.clicked.connect(dataStop)

#* ----------------------------------------

# GRAPHS
gridGraphs = QtWidgets.QGridLayout()

graphsView1 = pg.GraphicsView()
graphsView2 = pg.GraphicsView()
graphsView3 = pg.GraphicsView()
graphsView4 = pg.GraphicsView()
graphsView5 = pg.GraphicsView()
graphsView6 = pg.GraphicsView()
graphsView7 = pg.GraphicsView()
graphsView8 = pg.GraphicsView()

graphsView1.setCentralItem(graph1_ins)
graphsView2.setCentralItem(graph2_ins)
graphsView3.setCentralItem(graph3_ins)
graphsView4.setCentralItem(graph4_ins)
graphsView5.setCentralItem(graph5_ins)
graphsView6.setCentralItem(graph6_ins)
graphsView7.setCentralItem(graph7_ins)
graphsView8.setCentralItem(graph8_ins)

#? Graphs name and description
graph1_ins.title('Humidity [%]')
graph2_ins.title('Temperature [ºC]')
graph3_ins.title('Pressure [hPa]')
graph4_ins.title('Altitude [m]')
graph5_ins.title('Vertical acceleration [g]')
graph6_ins.title('Magnetic field [uT]')
graph7_ins.title('Other graph 1')
graph8_ins.title('Other graph 2')

# Graphs position
gridGraphs.addWidget(graphsView1, 0, 1, 1, 1)
gridGraphs.addWidget(graphsView2, 1, 1, 1, 1)
gridGraphs.addWidget(graphsView3, 2, 1, 1, 1)
gridGraphs.addWidget(graphsView4, 3, 1, 1, 1)
gridGraphs.addWidget(graphsView5, 0, 2, 1, 1)
gridGraphs.addWidget(graphsView6, 1, 2, 1, 1)
gridGraphs.addWidget(graphsView7, 2, 2, 1, 1)
gridGraphs.addWidget(graphsView8, 3, 2, 1, 1)

gridInterface.addLayout(gridGraphs, 0,1,1,1)

#* ----------------------------------------

# MENU BAR
mainWindow.setCentralWidget(Interface)
menuBar = QtWidgets.QMenuBar()
statusBar = QtWidgets.QStatusBar(mainWindow)
mainWindow.setMenuBar(menuBar)
mainWindow.setStatusBar(statusBar)

## Menu bar submenus
menuBar_Tab1 = QtWidgets.QMenu(menuBar)
menuBar_Tab1.setTitle("File")
menuBar_Tab2 = QtWidgets.QMenu(menuBar)
menuBar_Tab2.setTitle("View")

## Adding 'File' and 'View' submenus to menuBar
menuBar.addAction(menuBar_Tab1.menuAction())
menuBar.addAction(menuBar_Tab2.menuAction())

# --------------------
## Submenu - 'File'
### Submenus actions
Tab1_Action_Close = QtWidgets.QAction(mainWindow)
Tab1_Action_Close.setText("Exit")

### Actions connections
Tab1_Action_Close.triggered.connect(mainWindow.close)

### Adding actions to menuBar
menuBar_Tab1.addSeparator()
menuBar_Tab1.addAction(Tab1_Action_Close)

# --------------------
## Submenu - 'View'
### Actions
Tab2_Action_HideTabWidget = QtWidgets.QAction(mainWindow)
Tab2_Action_HideTabWidget.setCheckable(True)
Tab2_Action_HideTabWidget.setChecked(True)
Tab2_Action_HideTabWidget.setText("Data collection details")
Tab2_Action_HideTabWidget.setShortcut("Ctrl+D")
Tab2_Action_HideGraph1 = QtWidgets.QAction(mainWindow)
Tab2_Action_HideGraph1.setCheckable(True)
Tab2_Action_HideGraph1.setChecked(True)
Tab2_Action_HideGraph1.setText("Humidity graph")
Tab2_Action_HideGraph1.setShortcut("Ctrl+1")
Tab2_Action_HideGraph2 = QtWidgets.QAction(mainWindow)
Tab2_Action_HideGraph2.setCheckable(True)
Tab2_Action_HideGraph2.setChecked(True)
Tab2_Action_HideGraph2.setText("Temperature graph")
Tab2_Action_HideGraph2.setShortcut("Ctrl+2")
Tab2_Action_HideGraph3 = QtWidgets.QAction(mainWindow)
Tab2_Action_HideGraph3.setCheckable(True)
Tab2_Action_HideGraph3.setChecked(True)
Tab2_Action_HideGraph3.setText("Pressure graph")
Tab2_Action_HideGraph3.setShortcut("Ctrl+3")
Tab2_Action_HideGraph4 = QtWidgets.QAction(mainWindow)
Tab2_Action_HideGraph4.setCheckable(True)
Tab2_Action_HideGraph4.setChecked(True)
Tab2_Action_HideGraph4.setText("Altitude graph")
Tab2_Action_HideGraph4.setShortcut("Ctrl+4")
Tab2_Action_HideGraph5 = QtWidgets.QAction(mainWindow)
Tab2_Action_HideGraph5.setCheckable(True)
Tab2_Action_HideGraph5.setChecked(True)
Tab2_Action_HideGraph5.setText("Vertical accel graph")
Tab2_Action_HideGraph5.setShortcut("Ctrl+5")
Tab2_Action_HideGraph6 = QtWidgets.QAction(mainWindow)
Tab2_Action_HideGraph6.setCheckable(True)
Tab2_Action_HideGraph6.setChecked(True)
Tab2_Action_HideGraph6.setText("Magnetic field graph")
Tab2_Action_HideGraph6.setShortcut("Ctrl+6")
Tab2_Action_HideGraph7 = QtWidgets.QAction(mainWindow)
Tab2_Action_HideGraph7.setCheckable(True)
Tab2_Action_HideGraph7.setChecked(True)
Tab2_Action_HideGraph7.setText("Other graph 1")
Tab2_Action_HideGraph7.setShortcut("Ctrl+7")
Tab2_Action_HideGraph8 = QtWidgets.QAction(mainWindow)
Tab2_Action_HideGraph8.setCheckable(True)
Tab2_Action_HideGraph8.setChecked(True)
Tab2_Action_HideGraph8.setText("Other graph 2")
Tab2_Action_HideGraph8.setShortcut("Ctrl+8")

### Actions connections
Tab2_Action_HideTabWidget.triggered.connect(groupTabWidget.setVisible)
Tab2_Action_HideGraph1.triggered.connect(graphsView1.setVisible)
Tab2_Action_HideGraph2.triggered.connect(graphsView2.setVisible)
Tab2_Action_HideGraph3.triggered.connect(graphsView3.setVisible)
Tab2_Action_HideGraph4.triggered.connect(graphsView4.setVisible)
Tab2_Action_HideGraph5.triggered.connect(graphsView5.setVisible)
Tab2_Action_HideGraph6.triggered.connect(graphsView6.setVisible)
Tab2_Action_HideGraph7.triggered.connect(graphsView7.setVisible)
Tab2_Action_HideGraph8.triggered.connect(graphsView8.setVisible)

### Adding actions to menuBar
menuBar_Tab2.addAction(Tab2_Action_HideTabWidget)
menuBar_Tab2.addSeparator()
menuBar_Tab2.addAction(Tab2_Action_HideGraph1)
menuBar_Tab2.addAction(Tab2_Action_HideGraph2)
menuBar_Tab2.addAction(Tab2_Action_HideGraph3)
menuBar_Tab2.addAction(Tab2_Action_HideGraph4)
menuBar_Tab2.addAction(Tab2_Action_HideGraph5)
menuBar_Tab2.addAction(Tab2_Action_HideGraph6)
menuBar_Tab2.addAction(Tab2_Action_HideGraph7)
menuBar_Tab2.addAction(Tab2_Action_HideGraph8)

#* ========================================

if __name__ == "__main__":
    # Time elapsed
    counterGraph_time, saveTime = 0, 0
    
    def dataUpdater():
        global counterGraph_time, saveTime
        # Graph updating
        try:
            dataPacket = serialcomm_ins.dataPacket_Read()
            
            # Updating every 0.5 s
            if (time.monotonic() - counterGraph_time) >= 0.5:
                counterGraph_time = time.monotonic()
                graph1_ins.update(dataPacket[0])
                graph2_ins.update(dataPacket[1])
                graph3_ins.update(dataPacket[2])
                graph4_ins.update(dataPacket[3])
                graph5_ins.update(dataPacket[4])
                graph6_ins.update(dataPacket[5])
                graph7_ins.update(dataPacket[6])
                graph8_ins.update(dataPacket[7])
                
                # Data saving on file
                #? Change if parameter on line 48 was changed.
                datasave_ins.Save(saveTime,
                                    dataPacket[0],
                                    dataPacket[1],
                                    dataPacket[2],
                                    dataPacket[3],
                                    dataPacket[4],
                                    dataPacket[5],
                                    dataPacket[6],
                                    dataPacket[7])
                
                # LCD time updater
                saveTime += 0.5
                if ((saveTime*2)%2) == 0:
                    datasave_ins.LCD(Pag1_TimeLCD)
        except Exception as error:
            print("Error main - dataUpdater")
            print(error)
    
    # Real time data updater
    dataUpdate = pg.QtCore.QTimer(timeout = dataUpdater)
    dataUpdate.start(0)
    
    mainWindow.show()
    sys.exit(app.exec())
    