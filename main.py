#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import easygui
import pandas as pd
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from GUI.MainWindow import Ui_MainWindow
from GUI.RefreshDataBasePopButton import Ui_RefreshDataBasePopButton
from GUI.StatsPopButton import Ui_StatsPopButton
from GUI.DarwinizerPopButton import Ui_Darwinizer
from scripts.refreshdatabase import *
from scripts.graph_and_stats import *
from scripts.darwinizer import *

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
        self.stats_button.clicked.connect(self.stats_button_UI)
        self.darwinizer_button.clicked.connect(self.darwinizer_button_UI)

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

    def stats_button_UI(self):
        self.build=StatsButton(self.route_destiny_response_label.text())
        self.build.show()

    def darwinizer_button_UI(self):
        self.build=DarwinizerButton(self.xlsx_route_response_label.text(),self.route_destiny_response_label.text())
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
        full_df,organized_df,indexo=refreshdatabase().file_organizer(self.xlsx_route_response_label.text(),self.route_destiny_response_label.text()) #Abrir archivo excel, organized_df just dwc values
        IDs=organized_df.index.tolist()
        print('compare/create files...')
        if os.path.isdir(f"{self.route_destiny_response_label.text()}/files")==True:
            for id in IDs:
                refreshdatabase().comparefiles(id,organized_df.loc[id],"dwc_files",self.route_destiny_response_label.text())
        else:
            for id in IDs:
                refreshdatabase().infowriting(id,organized_df.loc[id],"dwc_files",self.route_destiny_response_label.text())
        
        """SECCION PARA SHOWROOM"""
        if self.question_1_pos_ans.isChecked()==True:
            showroom_option_answer=True
        elif self.question_1_neg_ans.isChecked():
            showroom_option_answer=False
        if showroom_option_answer==True:
            showroom_df=refreshdatabase().visitors_file_maker(full_df,self.route_destiny_response_label.text(),indexo)
            #aca va la funcion de organizacion de showroom
            if os.path.isdir(f'{self.route_destiny_response_label}\showroom_files')==True:
                for id in IDs:
                    refreshdatabase().comparefiles(id,showroom_df.loc[id],"invited",self.route_destiny_response_label.text())
            else:
                for id in IDs:
                    refreshdatabase().infowriting(id,showroom_df.loc[id],"invited",self.route_destiny_response_label.text())
        print ('No hay nada más que hacer por el momento...')
        #************************************************************************#
        print("Creando codigos Qr")
        api_key=self.Firebase_key_ans.text()
        sub_domain=self.Firebase_domain_ans.text()
        GitHub_user=self.GitHub_user_ans.text()
        GitHub_repo=self.GitHub_repository_ans.text()
        qr_tools_class=qr_tools(api_key,sub_domain,GitHub_user,GitHub_repo,self.route_destiny_response_label.text(),IDs,"dwc_files")
        qr_tools_class.qr_manager()
        if showroom_option_answer==True:
            qr_tools_class=qr_tools(api_key,sub_domain,GitHub_user,GitHub_repo,self.route_destiny_response_label.text(),IDs,"invited")
            qr_tools_class.qr_manager()
        else:
            pass
        refreshdatabase().df_to_csv(full_df,self.DestinyPathway) #save full_df to a csv

class StatsButton(qtw.QWidget,Ui_StatsPopButton):
    def __init__(self,DestinyPathWay,stat_df=pd.DataFrame()):
        """MainWindow Constructor"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Darwin Connect")
        # Var Definitions
        self.DestinyPathway=DestinyPathWay
        self.stat_df=stat_df
        #Read df
        self.stat_df=pd.read_csv(f"{DestinyPathWay}/csv/full_df.csv",header=0,sep=',')
        # Main UI code goes here
        self.route_destiny_response_label.setText(DestinyPathWay)
        self.graphbutton.clicked.connect(lambda: self.graph_button_func())
        self.exitbutton.clicked.connect(self.close)
        #Populate ComboBox
        self.dwc_label_response.addItems(self.stat_df.columns.tolist())
        #End main UI code
        self.show()
    
    def graph_button_func(self):
        dwc_graph().make_graph(self.stat_df,self.dwc_label_response.currentText(),self.graph_kind_response.currentText(),self.graph_title_response.text())

class DarwinizerButton(qtw.QWidget,Ui_Darwinizer):
    def __init__(self,OriginPathWay,DestinyPathWay):
        """MainWindow constructor"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Darwin Connect")
        self.listWidget.setSelectionMode(qtw.QAbstractItemView.ExtendedSelection)
        # Var Definitions
        self.OriginPathWay=OriginPathWay
        self.DestinyPathway=DestinyPathWay
        self.darwinizerClass=file_entry(self.OriginPathWay,self.DestinyPathway)
        # Main UI code goes here
        self.xlsx_route_response_label.setText(OriginPathWay)
        self.route_destiny_response_label.setText(DestinyPathWay)
        #self.exitbutton.clicked.connect(self.close)
        self.DarwinizerButton.clicked.connect(lambda: self.darwin_analyzer())
        self.DwCButton.clicked.connect(lambda: self.dwc_label_selecter())
        self.VisitorsButton.clicked.connect(lambda: self.visitors_label_selecter())
        #End main UI code
        self.show()
    
    def darwin_analyzer(self):
        self.listWidget.clear()
        full_dataframe,darwinizer_list=self.darwinizerClass.darwinizer()
        list_widget=[]
        for verbatim,standard in darwinizer_list:
            list_widget.append(f"{verbatim} -> {standard}")
        self.listWidget.addItems(list_widget)
        self.ReadyButton.clicked.connect(lambda: self.darwinizerClass.dataframe_label_transformer(full_dataframe,self.listWidget,darwinizer_list))

    def dwc_label_selecter(self):
        df_columns=self.darwinizerClass.dwc_label_checker(self.listWidget)
        self.ReadyButton_2.clicked.connect(lambda: self.darwinizerClass.dwc_label_transformer(self.listWidget,df_columns)) 

    def visitors_label_selecter(self):
        df_columns=self.darwinizerClass.visitors_label_filler(self.listWidget)
        self.ReadyButton_3.clicked.connect(lambda: self.darwinizerClass.visitors_label_transformer(self.listWidget,df_columns)) 


if __name__=="__main__":
    app=qtw.QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    sys.exit(app.exec())
