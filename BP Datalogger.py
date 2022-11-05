from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys

# Scripts
from userInterface import UI
from serialComm import SerialComm
from graphs.graphPrueba1 import Graph1
from graphs.graphPrueba2 import Graph2
from graphs.graphPrueba3 import Graph3
from graphs.graphPrueba4 import Graph4



# Create main window
app = QApplication(sys.argv)
mainWindow = QMainWindow()
mainWindow.resize(767,544)
mainWindow.setWindowTitle("BP Datalogger")
# setIconSize(QtCore.QSize(24, 24))

# Instace of each graph
graf01 = Graph1()
graf02 = Graph2()
graf03 = Graph3()
graf04 = Graph4()


def window():
    def dataUpdate():
        dataPacket = SerialComm.dataPacket_Read()
        graf01.update(dataPacket[0])
        graf02.update(dataPacket[1])
        graf03.update(dataPacket[2])
        # graf04.update(data[3])

    # Real time plotting
    # timer = pg.QtCore.QTimer()
    # timer.timeout.connect(dataUpdate)
    # timer.start(0)

    UI(mainWindow, graf01, graf02, graf03, graf04)
    mainWindow.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    window()