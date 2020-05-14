#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
import pandas as pd
import easygui as eg
from collections import defaultdict
from PyQt5 import QtCore as qtc


class file_entry():
    def __init__(self,route_response_label,route_destiny_label):
        self.route_response_label=route_response_label
        self.route_destiny_label=route_destiny_label
        self.dwc_terms=self.dict_loader() #Diccionario 

    def dict_loader(self): #Apertura del dict
        dict_path=r"documents\dwc_terms\dwc_fieldName_dict.pkl"
        with open(dict_path , 'rb') as dict_file:
            return pickle.load(dict_file)

    def file_opener(self): #Apertura del archivo, con el index correcto, se borran columnas sin datos
        try:
            file_path=self.route_response_label
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                data=pd.read_excel(file_path,header=0)
            elif file_path.endswith('.csv'):
                data=pd.read_csv(file_path,header=0,sep=';') #ver como variar de ; o ,
        except:
            print("No hemos podido encontrar la ruta del archivo Excel")
        try:
            data.dropna(axis=1, how='all',inplace=True)
        except:
            pass
        return data

    def darwinizer(self):  #Encuentra match entre el df y el diccionario
        dataframe=self.file_opener() #proveniente de la funcion file opener
        dwc_terms_keys=self.dwc_terms.keys()
        dataframe_columns=dataframe.columns.tolist()
        darwinizer_list=[] #generar una lista que contenga tuplas verbatimFieldName,stdFieldName
        #iterador para encontrar tuplas verbatimFieldName,stdFieldName
        for verbatimFieldName in dataframe_columns:
            for stdFieldName in dwc_terms_keys:
                if verbatimFieldName in self.dwc_terms.get(stdFieldName):
                    darwinizer_list.append((verbatimFieldName,stdFieldName)) #tupla del match
        return dataframe,darwinizer_list

    def set_df_index(self,data):
        columns_df=data.columns.tolist()
        msg="Seleccione una columna para ser el indice de la base de datos\n Este debe ser un valor unico para cada especimen"
        title="Seleccion"       
        indexo=eg.choicebox(msg,title,columns_df)
        data=data.set_index(indexo, drop = True)
        return data 

    def dataframe_label_transformer(self,data,listWidget,darwinizer_list):
        column_dict=defaultdict()
        selected_indexes=[x.row() for x in listWidget.selectedIndexes()]
        if not selected_indexes: 
            column_dict=dict(darwinizer_list)
        else:
            i=0
            while i<=len(darwinizer_list)-1:
                if i not in selected_indexes:
                    column_dict[darwinizer_list[i][0]]=darwinizer_list[i][1]  #Fix this  method not proud of it
                else: pass        
                i=i+1
        data=data.rename(columns=column_dict)
        os.makedirs(os.path.dirname(f"{self.route_destiny_label}\dwc_terms\df_column_dict_rename.pkl"), exist_ok=True)
        f = open(f"{self.route_destiny_label}\dwc_terms\df_column_dict_rename.pkl","wb")
        pickle.dump(column_dict,f)
        f.close()
        os.makedirs(os.path.dirname(f"{self.route_destiny_label}\dwc_terms\df_columns_renamed.pkl"), exist_ok=True)
        f = open(f"{self.route_destiny_label}\dwc_terms\df_columns_renamed.pkl","wb")
        pickle.dump(data.columns.tolist(),f)
        f.close()
        listWidget.clear()
        #return data

    def dwc_label_checker(self,listWidget):
        with open(f"{self.route_destiny_label}\dwc_terms\df_columns_renamed.pkl", 'rb') as f:
            df_columns = pickle.load(f)
        not_recommended_labels=[]
        for labels in df_columns:
            if labels not in self.dwc_terms.keys():
                not_recommended_labels.append(labels)
        listWidget.addItems(df_columns)
        for i in not_recommended_labels:
            matching_items = listWidget.findItems(i, qtc.Qt.MatchExactly)
            for item in matching_items:
                item.setSelected(True)
        return df_columns

    
    def dwc_label_transformer(self,listWidget,df_columns):
        selected_indexes=[x.row() for x in listWidget.selectedIndexes()]
        df_selected_dwc_labels=[]
        i=0
        while i <= len(df_columns)-1:
            if i not in selected_indexes:
                df_selected_dwc_labels.append(df_columns[i])
            i=i+1
        os.makedirs(os.path.dirname(f"{self.route_destiny_label}\dwc_terms\df_selected_dwc_labels.pkl"), exist_ok=True)
        f = open(f"{self.route_destiny_label}\dwc_terms\df_selected_dwc_labels.pkl","wb")
        pickle.dump(df_selected_dwc_labels,f)
        f.close()
        listWidget.clear()
    
    def visitors_label_filler(self,listWidget):
        with open(f"{self.route_destiny_label}\dwc_terms\df_columns_renamed.pkl", 'rb') as f:
            df_columns = pickle.load(f)
        listWidget.addItems(df_columns)
        return df_columns

    def visitors_label_transformer(self,listWidget,df_columns):
        selected_indexes=[x.row() for x in listWidget.selectedIndexes()]
        df_selected_visitors_labels=[]
        i=0
        while i <= len(df_columns)-1:
            if i not in selected_indexes:
                df_selected_visitors_labels.append(df_columns[i])
            i=i+1
        os.makedirs(os.path.dirname(f"{self.route_destiny_label}\dwc_terms\df_selected_visitors_labels.pkl"), exist_ok=True)
        f = open(f"{self.route_destiny_label}\dwc_terms\df_selected_visitors_labels.pkl","wb")
        pickle.dump(df_selected_visitors_labels,f)
        f.close()
        listWidget.clear()


    def sensitive_data(self):
        pass

      
#Visitors va a seguir quedando en script refresh data base
#leer columnas de lista de dwc_file, visitors_file, estas se deben leer para refresh data base igual, esto queda para refresh data base
#Comparar columnas dwcorear

#quiero guardar una lista con columnas de dwc del archivo y otras para visitor
#  así ya esta predefinido cuando se abra nuevamente

#Esta función debe ir en refresh data base o en darwinizer, 
# mejor no ya que al guarar listas de columnas solo debo hacer esto una vez

#Borar dynamic links user info y todos los dwc_terms

#Herramienta para normalizar horas

#Georreferenciación

#Guardar df como csv y ese pasarlo para refreshdatabase