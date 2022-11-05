from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg


class UI:
    def __init__(self, mainWindow, graf01, graf02, graf03, graf04):   
        # Main interface objects
        Interface = QtWidgets.QWidget()
        gridInterface = QtWidgets.QGridLayout(Interface)

        # ======================================

        # TAB WIDGET
        groupTabWidget = QtWidgets.QTabWidget(Interface)
        groupTabWidget.setFixedSize(QtCore.QSize(270, 270))
        gridInterface.addWidget(groupTabWidget, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)


        ## PAG 1 - 'Toma de datos'
        groupTabWidget_Pag1 = QtWidgets.QWidget()
        gridTabWidget_Pag1 = QtWidgets.QGridLayout(groupTabWidget_Pag1)
        groupTabWidget.addTab(groupTabWidget_Pag1, "Toma de datos")
        groupTabWidget.setStatusTip("Menu para iniciar/detener toma de datos")

        ### Descriptive text
        Pag1_MainText = QtWidgets.QLabel(groupTabWidget_Pag1)
        Pag1_MainText.setAlignment(QtCore.Qt.AlignCenter)
        Pag1_MainText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag1_MainText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag1_MainText.setWordWrap(True)
        Pag1_MainText.setText("Texto descriptivo de toma de datos - CAMBIAR")

        ### Elapsed time
        Pag1_TimeText = QtWidgets.QLabel(groupTabWidget_Pag1)
        Pag1_TimeText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag1_TimeText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag1_TimeText.setText("Tiempo [s]")
        Pag1_TimeLCD = QtWidgets.QLCDNumber(groupTabWidget_Pag1)
        Pag1_TimeLCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        Pag1_TimeLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        Pag1_TimeLCD.setProperty("value", 0)

        ### Push buttons
        Pag1_ButtonStart = QtWidgets.QPushButton(groupTabWidget_Pag1)
        Pag1_ButtonStart.setText("Iniciar")
        Pag1_ButtonStart.setToolTip("Iniciar guardado de datos")
        Pag1_ButtonStop = QtWidgets.QPushButton(groupTabWidget_Pag1)
        Pag1_ButtonStop.setText("Detener")
        Pag1_ButtonStop.setToolTip("Detener guardado de datos")

        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed)

        ### Light
        Pag1_Light = QtWidgets.QProgressBar(groupTabWidget_Pag1)
        Pag1_Light.setProperty("value", 0)
        Pag1_Light.setTextVisible(False)

        ### Authors/credits box
        Pag1_CreditsBox = QtWidgets.QLabel(groupTabWidget_Pag1)
        Pag1_CreditsBox.setFrameShape(QtWidgets.QFrame.Box)
        Pag1_CreditsBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        Pag1_CreditsBox.setAlignment(QtCore.Qt.AlignCenter)
        Pag1_CreditsBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag1_CreditsBox.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag1_CreditsBox.setWordWrap(True)
        Pag1_CreditsBox.setText("Versión 1.0\n\n"
        "Desarrollado por\n"
        "Simón Zuluaga\n\n"
        "Semillero de investigación - Delta V\n"
        "Universidad de Antioquia")

        ### Adding widgets to tab widget page 1 - 'Toma de datos'
        gridTabWidget_Pag1.addWidget(Pag1_MainText, 0, 0, 1, 2)
        gridTabWidget_Pag1.addWidget(Pag1_TimeText, 1, 0, 1, 1)
        gridTabWidget_Pag1.addWidget(Pag1_TimeLCD, 1, 1, 1, 1)
        gridTabWidget_Pag1.addWidget(Pag1_ButtonStart, 2, 0, 1, 1)
        gridTabWidget_Pag1.addWidget(Pag1_ButtonStop, 2, 1, 1, 1)
        gridTabWidget_Pag1.addWidget(Pag1_Light, 3, 0, 1, 2)
        gridTabWidget_Pag1.addItem(spacerItem, 4, 0, 1, 2)
        gridTabWidget_Pag1.addWidget(Pag1_CreditsBox, 5, 0, 1, 2)

        # Timer
        def TimerStart():
            pass

        def TimerStop():
            pass

        # Light ON-OFF functions
        def LightON():
            Pag1_Light.setProperty("value", 100)

        def LightOFF():
            Pag1_Light.setProperty("value", 0)

        # Tab Widget actions
        Pag1_ButtonStart.clicked.connect(LightON)
        Pag1_ButtonStop.clicked.connect(LightOFF)


        ## PAG 2 - 'Detalles'
        groupTabWidget_Pag2 = QtWidgets.QWidget()
        gridTabWidget_Pag2 = QtWidgets.QGridLayout(groupTabWidget_Pag2)
        groupTabWidget.addTab(groupTabWidget_Pag2, "Detalles")
        groupTabWidget.setStatusTip("Detalles de la prueba")

        Pag2_NameText = QtWidgets.QLabel(groupTabWidget_Pag2)
        Pag2_NameText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag2_NameText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag2_NameText.setText("Nombre")
        Pag2_ManufacturerText = QtWidgets.QLabel(groupTabWidget_Pag2)
        Pag2_ManufacturerText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag2_ManufacturerText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag2_ManufacturerText.setText("Proveedor")
        Pag2_DateText = QtWidgets.QLabel(groupTabWidget_Pag2)
        Pag2_DateText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag2_DateText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag2_DateText.setText("Fecha [DD/MM/AAAA]")
        Pag2_DiameterText = QtWidgets.QLabel(groupTabWidget_Pag2)
        Pag2_DiameterText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag2_DiameterText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag2_DiameterText.setText("Diametro [mm]")
        Pag2_HeightText = QtWidgets.QLabel(groupTabWidget_Pag2)
        Pag2_HeightText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag2_HeightText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag2_HeightText.setText("Altura [mm]")
        Pag2_PropweightText = QtWidgets.QLabel(groupTabWidget_Pag2)
        Pag2_PropweightText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag2_PropweightText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag2_PropweightText.setText("Peso del propelente [g]")
        Pag2_MotorweightText = QtWidgets.QLabel(groupTabWidget_Pag2)
        Pag2_MotorweightText.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Pag2_MotorweightText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        Pag2_MotorweightText.setText("Peso del motor [g]")

        ### User entry text
        Pag2_NameText_edit = QtWidgets.QLineEdit(groupTabWidget_Pag2)
        Pag2_NameText_edit.setStatusTip("Nombre del motor")
        Pag2_ManufacturerText_edit = QtWidgets.QLineEdit(groupTabWidget_Pag2)
        Pag2_ManufacturerText_edit.setStatusTip("Proveedor del motor")
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
        graphsView = pg.GraphicsView()
        graphsView2 = pg.GraphicsView()
        graphsView3 = pg.GraphicsView()
        graphsView4 = pg.GraphicsView()

        graphsView.addItem(graf01)
        graphsView2.addItem(graf02)
        graphsView3.addItem(graf03)
        graphsView4.addItem(graf04)

        graphsView.setCentralItem(graf01)
        graphsView2.setCentralItem(graf02)
        graphsView3.setCentralItem(graf03)
        graphsView4.setCentralItem(graf04)

        graphsView.setStatusTip("Descripción grafica 1")
        graphsView2.setStatusTip("Descripción grafica 2")
        graphsView3.setStatusTip("Descripción grafica 3")
        graphsView4.setStatusTip("Descripción grafica 4")

        gridInterface.addWidget(graphsView, 0, 1, 1, 1)
        gridInterface.addWidget(graphsView2, 0, 2, 1, 1)
        gridInterface.addWidget(graphsView3, 1, 1, 1, 1)
        gridInterface.addWidget(graphsView4, 1, 2, 1, 1)

        # ======================================

        # MENU BAR
        mainWindow.setCentralWidget(Interface)
        menuBar = QtWidgets.QMenuBar()
        statusBar = QtWidgets.QStatusBar(mainWindow)
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

        # Menu bar actions
        Tab1_Action_Close.triggered.connect(mainWindow.close)
        Tab2_Action_HideTabWidget.triggered.connect(groupTabWidget.setVisible)
        Tab2_Action_HideGraph1.triggered.connect(graphsView.setVisible)
        Tab2_Action_HideGraph2.triggered.connect(graphsView2.setVisible)
        Tab2_Action_HideGraph3.triggered.connect(graphsView3.setVisible)
        Tab2_Action_HideGraph4.triggered.connect(graphsView4.setVisible)