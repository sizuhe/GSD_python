from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class AppMain(QMainWindow):
    def __init__(self):
        super(AppMain, self).__init__()
        self.resize(767,544)
        self.setWindowTitle("BP Datalogger")
         # self.setIconSize(QtCore.QSize(24, 24))
        self.UI()
       

    def UI(self):       
        # Main interface objects
        self.interfaz = QtWidgets.QWidget(self)
        self.gridInterfaz = QtWidgets.QGridLayout(self.interfaz)

        # ======================================

        # TAB WIDGET
        self.grupoDetallesTW = QtWidgets.QTabWidget(self.interfaz)
        self.grupoDetallesTW.setMinimumSize(QtCore.QSize(225, 240))
        self.grupoDetallesTW.setMaximumSize(QtCore.QSize(225, 240))
        self.gridInterfaz.addWidget(self.grupoDetallesTW, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        
        ## PAG 1 - 'Detalles'
        self.grupoDetallesPag1 = QtWidgets.QWidget()
        self.gridDetallesPag1 = QtWidgets.QGridLayout(self.grupoDetallesPag1)
        self.grupoDetallesTW.addTab(self.grupoDetallesPag1, "Detalles")
        self.grupoDetallesTW.setStatusTip("Detalles de la prueba")

        self.detallesNombre = QtWidgets.QLabel(self.grupoDetallesPag1)
        self.detallesNombre.setText("Nombre")
        self.detallesFecha = QtWidgets.QLabel(self.grupoDetallesPag1)
        self.detallesFecha.setText("Fecha")
        self.detallesDescripcion = QtWidgets.QLabel(self.grupoDetallesPag1)
        self.detallesDescripcion.setText("Descripción")

        ### User entry text
        self.detallesNombreEdit = QtWidgets.QLineEdit(self.grupoDetallesPag1)
        self.detallesNombreEdit.setStatusTip("Nombre de la prueba")
        self.detallesFechaEdit = QtWidgets.QDateEdit(self.grupoDetallesPag1)
        self.detallesFechaEdit.setStatusTip("Fecha de la prueba")
        self.detallesDescripcionEdit = QtWidgets.QTextEdit(self.grupoDetallesPag1)
        self.detallesDescripcionEdit.setStatusTip("Descripción de la prueba")

        ### Adding widgets to tab widget page 1 - 'Detalles'
        self.gridDetallesPag1.addWidget(self.detallesNombre, 0, 0, 1, 1)
        self.gridDetallesPag1.addWidget(self.detallesDescripcion, 2, 0, 1, 1)
        self.gridDetallesPag1.addWidget(self.detallesFecha, 1, 0, 1, 1)
        self.gridDetallesPag1.addWidget(self.detallesNombreEdit, 0, 1, 1, 1)
        self.gridDetallesPag1.addWidget(self.detallesDescripcionEdit, 2, 1, 1, 1)
        self.gridDetallesPag1.addWidget(self.detallesFechaEdit, 1, 1, 1, 1)


        ## PAG 2 - 'Toma de datos'
        self.grupoDetallesPag2 = QtWidgets.QWidget()
        self.gridDetallesPag2 = QtWidgets.QGridLayout(self.grupoDetallesPag2)
        self.grupoDetallesTW.addTab(self.grupoDetallesPag2, "Toma de datos")

        ### Descriptive text
        self.tomadatosDescripcion = QtWidgets.QLabel(self.grupoDetallesPag2)
        self.tomadatosDescripcion.setAlignment(QtCore.Qt.AlignCenter)
        self.tomadatosDescripcion.setWordWrap(True)
        self.tomadatosDescripcion.setText("Texto descriptivo de toma de datos - CAMBIAR")

        ### Push buttons
        self.tomadatosBotIniciar = QtWidgets.QPushButton(self.grupoDetallesPag2)
        self.tomadatosBotIniciar.setText("Iniciar")
        self.tomadatosBotIniciar.setToolTip("Iniciar guardado de datos")
        self.tomadatosBotDetener = QtWidgets.QPushButton(self.grupoDetallesPag2)
        self.tomadatosBotDetener.setText("Detener")
        self.tomadatosBotDetener.setToolTip("Detener guardado de datos")

        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed)

        ### Authors/credits box
        self.tomadatosAutores = QtWidgets.QLabel(self.grupoDetallesPag2)
        self.tomadatosAutores.setFrameShape(QtWidgets.QFrame.Box)
        self.tomadatosAutores.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tomadatosAutores.setAlignment(QtCore.Qt.AlignCenter)
        self.tomadatosAutores.setWordWrap(True)
        self.tomadatosAutores.setText("Versión 1.0\n\n"
        "Desarrollado por:\n"
        "Simón Zuluaga y Mateo Lezama\n\n"
        "Semillero de investigación - Delta V\n"
        "Universidad de Antioquia")

        ### Adding widgets to tab widget page 2 - 'Toma de datos'
        self.gridDetallesPag2.addWidget(self.tomadatosDescripcion, 0, 0, 1, 2)
        self.gridDetallesPag2.addWidget(self.tomadatosBotIniciar, 1, 0, 1, 1)
        self.gridDetallesPag2.addWidget(self.tomadatosBotDetener, 1, 1, 1, 1)
        self.gridDetallesPag2.addItem(spacerItem, 2, 0, 1, 2)
        self.gridDetallesPag2.addWidget(self.tomadatosAutores, 4, 0, 1, 2)        
    
        # ======================================

        # GRAPHS
        self.graphicsView = QtWidgets.QGraphicsView(self.interfaz)
        self.graphicsView.setStatusTip("Descripción grafica 1")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.interfaz)
        self.graphicsView_2.setStatusTip("Descripción grafica 2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.interfaz)
        self.graphicsView_3.setStatusTip("Descripción grafica 3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.interfaz)
        self.graphicsView_4.setStatusTip("Descripción grafica 4")
        self.gridInterfaz.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.gridInterfaz.addWidget(self.graphicsView_2, 0, 2, 1, 1)
        self.gridInterfaz.addWidget(self.graphicsView_3, 1, 1, 1, 1)
        self.gridInterfaz.addWidget(self.graphicsView_4, 1, 2, 1, 1)
    
        # ======================================

        # MENU BAR
        self.setCentralWidget(self.interfaz)
        self.menubar = QtWidgets.QMenuBar(self)
        self.statusbar = QtWidgets.QStatusBar(self)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 21))
        self.setMenuBar(self.menubar)
        self.setStatusBar(self.statusbar)

        ## Menu bar submenus
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setTitle("Archivo")
        self.menuVer = QtWidgets.QMenu(self.menubar)
        self.menuVer.setTitle("Ver")

        ### 'Archivo' submenus
        self.menuPuertos = QtWidgets.QMenu(self.menuArchivo)
        self.menuPuertos.setTitle("Puerto serial")
        self.menuExportar = QtWidgets.QMenu(self.menuArchivo)
        self.menuExportar.setTitle("Exportar")

        ### 'Archivo' menu actions
        self.accionCSVTXT = QtWidgets.QAction(self)
        self.accionCSVTXT.setText("CSV, TXT")
        self.accionPDF = QtWidgets.QAction(self)
        self.accionPDF.setText("PDF")
        self.accionSalir = QtWidgets.QAction(self)
        self.accionSalir.setText("Salir")

        ### 'Ver' menu actions
        self.accionDetallesInf = QtWidgets.QAction(self)
        self.accionDetallesInf.setCheckable(True)
        self.accionDetallesInf.setChecked(True)
        self.accionDetallesInf.setText("Detalles del informe")
        self.accionDetallesInf.setShortcut("Ctrl+D")
        self.accionGraf1 = QtWidgets.QAction(self)
        self.accionGraf1.setCheckable(True)
        self.accionGraf1.setChecked(True)
        self.accionGraf1.setText("Grafica 1")
        self.accionGraf1.setShortcut("Ctrl+1")
        self.accionGraf2 = QtWidgets.QAction(self)
        self.accionGraf2.setCheckable(True)
        self.accionGraf2.setChecked(True)
        self.accionGraf2.setText("Grafica 2")
        self.accionGraf2.setShortcut("Ctrl+2")
        self.accionGraf3 = QtWidgets.QAction(self)
        self.accionGraf3.setCheckable(True)
        self.accionGraf3.setChecked(True)
        self.accionGraf3.setText("Grafica 3")
        self.accionGraf3.setShortcut("Ctrl+3")
        self.accionGraf4 = QtWidgets.QAction(self)
        self.accionGraf4.setCheckable(True)
        self.accionGraf4.setChecked(True)
        self.accionGraf4.setText("Grafica 4")
        self.accionGraf4.setShortcut("Ctrl+4")
        
        ## Adding objects to 'Archivo' menu
        self.menuArchivo.addAction(self.menuPuertos.menuAction())
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.menuExportar.menuAction())
        self.menuExportar.addAction(self.accionCSVTXT)
        self.menuExportar.addAction(self.accionPDF)
        self.menuExportar.setEnabled(False)     # --- SE DEBE PROGRAMAR ANTES DE ACTIVAR ---
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.accionSalir)

        ## Adding objects to 'Ver' menu
        self.menuVer.addAction(self.accionDetallesInf)
        self.menuVer.addSeparator()
        self.menuVer.addAction(self.accionGraf1)
        self.menuVer.addAction(self.accionGraf2)
        self.menuVer.addAction(self.accionGraf3)
        self.menuVer.addAction(self.accionGraf4)

        # Adding 'Archivo' and 'Ver' menus to general Menu Bar
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())

        # Push buttons actions
        self.accionSalir.triggered.connect(self.close)
        self.accionDetallesInf.triggered.connect(self.grupoDetallesTW.setVisible)
        self.accionGraf1.triggered.connect(self.graphicsView.setVisible)
        self.accionGraf2.triggered.connect(self.graphicsView_2.setVisible)
        self.accionGraf3.triggered.connect(self.graphicsView_3.setVisible)
        self.accionGraf4.triggered.connect(self.graphicsView_4.setVisible)


    def window():
        app = QApplication(sys.argv)
        win = AppMain()
        win.show()
        sys.exit(app.exec())



if __name__ == "__main__":
    AppMain.window()