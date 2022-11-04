from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys

# Scripts
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



def UI():     
    # Main interface objects
    Interface = QtWidgets.QWidget()
    gridInterface = QtWidgets.QGridLayout(Interface)

    # ======================================

    # TAB WIDGET
    groupTabWidget = QtWidgets.QTabWidget(Interface)
    groupTabWidget.setMinimumSize(QtCore.QSize(225, 240))
    groupTabWidget.setMaximumSize(QtCore.QSize(225, 240))
    gridInterface.addWidget(groupTabWidget, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)


    ## PAG 1 - 'Toma de datos'
    groupTabWidget_Pag1 = QtWidgets.QWidget()
    gridTabWidget_Pag1 = QtWidgets.QGridLayout(groupTabWidget_Pag1)
    groupTabWidget.addTab(groupTabWidget_Pag1, "Toma de datos")
    groupTabWidget.setStatusTip("Menu para iniciar/detener toma de datos")

    ### Descriptive text
    Pag1_MainText = QtWidgets.QLabel(groupTabWidget_Pag1)
    Pag1_MainText.setAlignment(QtCore.Qt.AlignCenter)
    Pag1_MainText.setWordWrap(True)
    Pag1_MainText.setText("Texto descriptivo de toma de datos - CAMBIAR")

    ### Push buttons
    Pag1_ButtonStart = QtWidgets.QPushButton(groupTabWidget_Pag1)
    Pag1_ButtonStart.setText("Iniciar")
    Pag1_ButtonStart.setToolTip("Iniciar guardado de datos")
    Pag1_ButtonStop = QtWidgets.QPushButton(groupTabWidget_Pag1)
    Pag1_ButtonStop.setText("Detener")
    Pag1_ButtonStop.setToolTip("Detener guardado de datos")

    spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed)

    ### Authors/credits box
    Pag1_CreditsBox = QtWidgets.QLabel(groupTabWidget_Pag1)
    Pag1_CreditsBox.setFrameShape(QtWidgets.QFrame.Box)
    Pag1_CreditsBox.setFrameShadow(QtWidgets.QFrame.Sunken)
    Pag1_CreditsBox.setAlignment(QtCore.Qt.AlignCenter)
    Pag1_CreditsBox.setWordWrap(True)
    Pag1_CreditsBox.setText("Versión 1.0\n\n"
    "Desarrollado por\n"
    "Simón Zuluaga\n\n"
    "Semillero de investigación - Delta V\n"
    "Universidad de Antioquia")

    ### Adding widgets to tab widget page 1 - 'Toma de datos'
    gridTabWidget_Pag1.addWidget(Pag1_MainText, 0, 0, 1, 2)
    gridTabWidget_Pag1.addWidget(Pag1_ButtonStart, 1, 0, 1, 1)
    gridTabWidget_Pag1.addWidget(Pag1_ButtonStop, 1, 1, 1, 1)
    gridTabWidget_Pag1.addItem(spacerItem, 2, 0, 1, 2)
    gridTabWidget_Pag1.addWidget(Pag1_CreditsBox, 4, 0, 1, 2)        


    ## PAG 2 - 'Detalles'
    groupTabWidget_Pag2 = QtWidgets.QWidget()
    gridTabWidget_Pag2 = QtWidgets.QGridLayout(groupTabWidget_Pag2)
    groupTabWidget.addTab(groupTabWidget_Pag2, "Detalles")
    groupTabWidget.setStatusTip("Detalles de la prueba")

    Pag2_NameText = QtWidgets.QLabel(groupTabWidget_Pag2)
    Pag2_NameText.setText("Nombre")
    Pag2_ManufacturerText = QtWidgets.QLabel(groupTabWidget_Pag2)
    Pag2_ManufacturerText.setText("Manufacturador")
    Pag2_DateText = QtWidgets.QLabel(groupTabWidget_Pag2)
    Pag2_DateText.setText("Fecha")
    Pag2_DiameterText = QtWidgets.QLabel(groupTabWidget_Pag2)
    Pag2_DiameterText.setText("Diametro [mm]")
    Pag2_HeightText = QtWidgets.QLabel(groupTabWidget_Pag2)
    Pag2_HeightText.setText("Altura [mm]")
    Pag2_PropweightText = QtWidgets.QLabel(groupTabWidget_Pag2)
    Pag2_PropweightText.setText("Peso del propelente [gr]")
    Pag2_MotorweightText = QtWidgets.QLabel(groupTabWidget_Pag2)
    Pag2_MotorweightText.setText("Peso del motor [gr]")

    ### User entry text
    Pag2_NameText_edit = QtWidgets.QLineEdit(groupTabWidget_Pag2)
    Pag2_NameText_edit.setStatusTip("Nombre del motor")
    Pag2_ManufacturerText_edit = QtWidgets.QLineEdit(groupTabWidget_Pag2)
    Pag2_ManufacturerText_edit.setStatusTip("Manufacturador del motor")
    Pag2_DateText_edit = QtWidgets.QDateEdit(groupTabWidget_Pag2)
    Pag2_DateText_edit.setStatusTip("Fecha de la prueba")
    Pag2_DiameterText_edit = QtWidgets.QLineEdit(groupTabWidget_Pag2)
    Pag2_DiameterText_edit.setStatusTip("Diametro del motor")
    Pag2_HeightText_edit = QtWidgets.QLineEdit(groupTabWidget_Pag2)
    Pag2_HeightText_edit.setStatusTip("Altura del motor")
    Pag2_PropweightText_edit = QtWidgets.QLineEdit(groupTabWidget_Pag2)
    Pag2_PropweightText_edit.setStatusTip("Peso del propelente del motor (PesoMotor_Lleno - PesoMotor_Vacio)")
    Pag2_MotorweightText_edit = QtWidgets.QLineEdit(groupTabWidget_Pag2)
    Pag2_MotorweightText_edit.setStatusTip("Peso del motor con propelente")

    Pag2_NameText_edit.setMaxLength(5)
    Pag2_ManufacturerText_edit.setMaxLength(10)
    Pag2_DiameterText_edit.setMaxLength(5)
    Pag2_HeightText_edit.setMaxLength(5)
    Pag2_PropweightText_edit.setMaxLength(5)
    Pag2_MotorweightText_edit.setMaxLength(5)

    ### Adding widgets to tab widget page 1 - 'Detalles'
    gridTabWidget_Pag2.addWidget(Pag2_NameText, 0, 0, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_ManufacturerText, 1, 0, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_DateText, 2, 0, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_DiameterText, 3, 0, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_HeightText, 4, 0, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_PropweightText, 5, 0, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_MotorweightText, 6, 0, 1, 1)

    gridTabWidget_Pag2.addWidget(Pag2_NameText_edit, 0, 1, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_ManufacturerText_edit, 1, 1, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_DateText_edit, 2, 1, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_DiameterText_edit, 3, 1, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_HeightText_edit, 4, 1, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_PropweightText_edit, 5, 1, 1, 1)
    gridTabWidget_Pag2.addWidget(Pag2_MotorweightText_edit, 6, 1, 1, 1)

    # ======================================

    # GRAPHS
    graphicsView = pg.GraphicsView()
    graphicsView2 = pg.GraphicsView()
    graphicsView3 = pg.GraphicsView()
    graphicsView4 = pg.GraphicsView()

    graphicsView.addItem(graf01)
    graphicsView2.addItem(graf02)
    graphicsView3.addItem(graf03)
    graphicsView4.addItem(graf04)

    graphicsView.setCentralItem(graf01)
    graphicsView2.setCentralItem(graf02)
    graphicsView3.setCentralItem(graf03)
    graphicsView4.setCentralItem(graf04)

    graphicsView.setStatusTip("Descripción grafica 1")
    graphicsView2.setStatusTip("Descripción grafica 2")
    graphicsView3.setStatusTip("Descripción grafica 3")
    graphicsView4.setStatusTip("Descripción grafica 4")

    gridInterface.addWidget(graphicsView, 0, 1, 1, 1)
    gridInterface.addWidget(graphicsView2, 0, 2, 1, 1)
    gridInterface.addWidget(graphicsView3, 1, 1, 1, 1)
    gridInterface.addWidget(graphicsView4, 1, 2, 1, 1)

    # ======================================

    # MENU BAR
    mainWindow.setCentralWidget(Interface)
    menuBar = QtWidgets.QMenuBar()
    statusBar = QtWidgets.QStatusBar(mainWindow)
    # menuBar.setGeometry(QtCore.QRect(0, 0, 767, 21))
    mainWindow.setMenuBar(menuBar)
    mainWindow.setStatusBar(statusBar)

    ## Menu bar submenus
    menuBar_Tab1 = QtWidgets.QMenu(menuBar)
    menuBar_Tab1.setTitle("Archivo")
    menuBar_Tab2 = QtWidgets.QMenu(menuBar)
    menuBar_Tab2.setTitle("Ver")

    ### 'Archivo' submenus
    Tab1_Ports = QtWidgets.QMenu(menuBar_Tab1)
    Tab1_Ports.setTitle("Puerto serial")
    Tab1_Export = QtWidgets.QMenu(menuBar_Tab1)
    Tab1_Export.setTitle("Exportar")

    ### 'Archivo' menu actions
    Tab1_Action_OpenRocket = QtWidgets.QAction(mainWindow)
    Tab1_Action_OpenRocket.setText("OpenRocket")
    Tab1_Action_Close = QtWidgets.QAction(mainWindow)
    Tab1_Action_Close.setText("Salir")

    ### 'Ver' menu actions
    Tab2_Action_HideTabWidget = QtWidgets.QAction(mainWindow)
    Tab2_Action_HideTabWidget.setCheckable(True)
    Tab2_Action_HideTabWidget.setChecked(True)
    Tab2_Action_HideTabWidget.setText("Detalles del informe")
    Tab2_Action_HideTabWidget.setShortcut("Ctrl+D")
    Tab2_Action_HideGraph1 = QtWidgets.QAction(mainWindow)
    Tab2_Action_HideGraph1.setCheckable(True)
    Tab2_Action_HideGraph1.setChecked(True)
    Tab2_Action_HideGraph1.setText("Grafica 1")
    Tab2_Action_HideGraph1.setShortcut("Ctrl+1")
    Tab2_Action_HideGraph2 = QtWidgets.QAction(mainWindow)
    Tab2_Action_HideGraph2.setCheckable(True)
    Tab2_Action_HideGraph2.setChecked(True)
    Tab2_Action_HideGraph2.setText("Grafica 2")
    Tab2_Action_HideGraph2.setShortcut("Ctrl+2")
    Tab2_Action_HideGraph3 = QtWidgets.QAction(mainWindow)
    Tab2_Action_HideGraph3.setCheckable(True)
    Tab2_Action_HideGraph3.setChecked(True)
    Tab2_Action_HideGraph3.setText("Grafica 3")
    Tab2_Action_HideGraph3.setShortcut("Ctrl+3")
    Tab2_Action_HideGraph4 = QtWidgets.QAction(mainWindow)
    Tab2_Action_HideGraph4.setCheckable(True)
    Tab2_Action_HideGraph4.setChecked(True)
    Tab2_Action_HideGraph4.setText("Grafica 4")
    Tab2_Action_HideGraph4.setShortcut("Ctrl+4")
    
    ## Adding objects to 'Archivo' menu
    menuBar_Tab1.addAction(Tab1_Ports.menuAction())
    menuBar_Tab1.addSeparator()
    menuBar_Tab1.addAction(Tab1_Export.menuAction())
    Tab1_Export.addAction(Tab1_Action_OpenRocket)
    Tab1_Export.setEnabled(False)     # --- SE DEBE PROGRAMAR ANTES DE ACTIVAR ---
    menuBar_Tab1.addSeparator()
    menuBar_Tab1.addAction(Tab1_Action_Close)

    ## Adding objects to 'Ver' menu
    menuBar_Tab2.addAction(Tab2_Action_HideTabWidget)
    menuBar_Tab2.addSeparator()
    menuBar_Tab2.addAction(Tab2_Action_HideGraph1)
    menuBar_Tab2.addAction(Tab2_Action_HideGraph2)
    menuBar_Tab2.addAction(Tab2_Action_HideGraph3)
    menuBar_Tab2.addAction(Tab2_Action_HideGraph4)

    # Adding 'Archivo' and 'Ver' menus to general Menu Bar
    menuBar.addAction(menuBar_Tab1.menuAction())
    menuBar.addAction(menuBar_Tab2.menuAction())

    # Push buttons actions
    Tab1_Action_Close.triggered.connect(mainWindow.close)
    Tab2_Action_HideTabWidget.triggered.connect(groupTabWidget.setVisible)
    Tab2_Action_HideGraph1.triggered.connect(graphicsView.setVisible)
    Tab2_Action_HideGraph2.triggered.connect(graphicsView2.setVisible)
    Tab2_Action_HideGraph3.triggered.connect(graphicsView3.setVisible)
    Tab2_Action_HideGraph4.triggered.connect(graphicsView4.setVisible)



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

    UI()
    mainWindow.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    window()