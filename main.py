import sys
import easygui
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from GUI.guitemplate import Ui_MainWindow
from scripts.refreshdatabase import *


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        
        self.setupUi(self)
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Darwin Connect")
        # Main UI code goes here
        """Barra de menu"""

        self.actionOpen.triggered.connect(lambda: self.filesearcher()) #Boton Abrir de la barra menu
        self.actionSalir.triggered.connect(self.close) #Boton Salir de la barra menu
        
        """Ventana principal"""
        self.refresh_button.clicked.connect(self.refres_button_func)

        #End main UI code
        self.show
    
    def filesearcher(self): #Funcion para obtener directorio del archivo excel a analizar
        route= easygui.fileopenbox()
        self.xlsx_route_response_label.setText(route)
        #Verificar como obtener el return en la función principal si no guardar esto en un archivo temporal.... o ver de como copiar info de label

    def refres_button_func(self):
        route=refreshdatabase().diropenbox()
        self.route_destiny_response_label.setText(route)

if __name__=="__main__":
    app=qtw.QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    sys.exit(app.exec())
