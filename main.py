import sys
import easygui
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from GUI.MainWindow import Ui_MainWindow
from GUI.RefreshDataBasePopButton import Ui_RefreshDataBasePopButton
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
        self.actionDestino.triggered.connect(lambda: self.diropenbox())
        self.actionSalir.triggered.connect(self.close) #Boton Salir de la barra menu
        
        """Ventana principal"""
        self.refresh_button.clicked.connect(lambda: self.refresh_button_UI())

        #End main UI code
        self.show
    
    def filesearcher(self): #Funcion para obtener directorio del archivo excel a analizar
        route= easygui.fileopenbox()
        self.xlsx_route_response_label.setText(route)
        #Verificar como obtener el return en la función principal si no guardar esto en un archivo temporal.... o ver de como copiar info de label

    def diropenbox(self):
        easygui.msgbox(msg="Seleccione un directorio en el cual se guardaran los archivos creados.\nSi ya ha hecho este proceso con este archivo seleccione el mismo directorio",ok_button="Ok")
        route_destiny_response_label=easygui.diropenbox()
        self.route_destiny_response_label.setText(route_destiny_response_label)
    
    def refresh_button_UI(self):
        self.build=RefreshDataBaseButton(self.xlsx_route_response_label.text(),self.route_destiny_response_label.text())
        self.build.show()

class RefreshDataBaseButton(qtw.QWidget, Ui_RefreshDataBasePopButton):
    def __init__(self,OriginPathWay,DestinyPathWay):
        """MainWindow constructor"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Darwin Connect")
        # Var Definitions
        self.OriginPathWay=OriginPathWay
        self.DestinyPathway=DestinyPathWay
        # Main UI code goes here
        self.xlsx_route_response_label.setText(OriginPathWay)
        self.route_destiny_response_label.setText(DestinyPathWay)
        self.exitbutton.clicked.connect(self.close)
        self.execute_button.clicked.connect(lambda: self.refresh_button_func())
        #End main UI code
        self.show()
    
    def refresh_button_func(self):
        route=self.route_destiny_response_label.text() #Ruta de destino de archivos 
        full_df,organized_df,index,full_df_columns=refreshdatabase().file_organizer(self.xlsx_route_response_label.text()) #Abrir archivo excel
        IDs=organized_df.index.tolist() #no considerar para file_creation 
       
        print('compare/create files...')

        if os.path.isdir(f"{self.route_destiny_response_label.text()}/files")==True:
            for id in IDs:
                refreshdatabase().comparefiles(id,organized_df.loc[id],0,self.route_destiny_response_label.text())
        else:
            for id in IDs:
                refreshdatabase().infowriting(id,organized_df.loc[id],0,self.route_destiny_response_label.text())
        
        """ SECCION PARA SHOWROOM
        if self.question_1_pos_ans.isChecked()==True:
            showroom_option_answer=True
        elif self.question_1_neg_ans.isChecked():
            showroom_option_answer=False
        if showroom_option_answer==True:
            if os.path.isdir(f'{self.route_destiny_response_label}\showroom_files')==True:
                for id in IDs:
                    refreshdatabase().comparefiles(id,data_showroom.loc[id],1)
            else:
                for id in IDs:
                    refreshdatabase().infowriting(id,data_showroom.loc[id],1)"""
        
        print ('there is nothing more to do here...')



if __name__=="__main__":
    app=qtw.QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    sys.exit(app.exec())
