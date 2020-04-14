#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import easygui as eg
import pandas as pd
import filecmp
import shutil
from python_firebase_url_shortener.url_shortener import UrlShortener
import time
import pyqrcode
from PIL import Image


class refreshdatabase():
    def file_organizer(self,route_response_label):
        try:
            file_path=route_response_label
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                data=pd.read_excel(file_path,sheet_name='Hoja1',header=0)
            elif file_path.endswith('.csv'):
                data=pd.read_csv(file_path,header=0,sep=';') #ver como variar de ; o ,
        except:
            print("No hemos podido encontrar la ruta del archivo Excel")
        columns_df=data.columns.tolist()
        msg="Seleccione una columna para ser el indice de la base de datos\n Este debe ser un valor unico para cada especimen"
        title="Seleccion"       
        indexo=eg.choicebox(msg,title,columns_df)
        data=data.set_index(indexo, drop = True)
        full_df=data.copy()
        full_df_columns=full_df.columns.tolist()
        columns_dwc=pd.read_csv('documents\dwc_terms\simple_dwc_horizontal.csv',header=0,sep=';').columns.tolist() #ver como variar de ; o , 
        columns_difference=list(set(columns_df)-set(columns_dwc))
        if not columns_difference:
            pass
        else:
            msg="Las columnas a continuacion no se encuentran en nuestra base de datos de DwC\n\Seleccione las que desee borrar"
            title="Seleccion"      
            choicebox=eg.multchoicebox(msg,title,columns_difference)
            try:
                for label in choicebox:
                    data.drop(label,axis=1,inplace=True)
            except:
                pass
        try:
            data.dropna(axis=1, how='all',inplace=True)
            full_df.dropna(axis=1, how='all',inplace=True)
        except:
            pass
        return full_df,data,indexo,full_df_columns

    def comparefiles(self,ID,info,option,pathway):  #option invited, dwc_files
        filename1 = f"{pathway}/temp/{ID}.txt"
        if option=="invited":
            filename2= f"{pathway}/showroom_files/{ID}.txt"
        elif option=="dwc_files":
            filename2= f"{pathway}/files/{ID}.txt"
        os.makedirs(os.path.dirname(filename1), exist_ok=True)
        with open(filename1,'w') as fil:
            fil.write(str(info))
        if os.path.isfile(filename2)==True:
            if filecmp.cmp(filename1,filename2)==False:
                print(f"He encontrado cambios desde la ultima vez, en el archivo... {ID}.txt")
                print("Se han guardado los cambios")
                shutil.move(filename1,filename2)
            else:
                pass
        else:
            print(f"Se ha encontrado una nueva entrada,Se ha cread el archivo... {ID}.txt")
            os.makedirs(os.path.dirname(filename2), exist_ok=True)
            with open(filename2,'w') as fil:
                fil.write(str(info))
        shutil.rmtree(f"{pathway}/temp", ignore_errors=False, onerror=None)
        return 

    def infowriting(self,ID,info,option,pathway):  #option invited, dwc_files
        try: 
            if option =="dwc_files":
                filename = f"{pathway}/files/{ID}.txt" 
            elif option=="invited":
                filename = f"{pathway}/showroom_files/{ID}.txt" 
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename,'w') as fil:
                fil.write(str(info))
            print(f'a new entry has been found, file...{ID}.txt has been created.')
        except:
            print(f'permission to write in {filename} has been denied...')
        return 

    def visitors_file_maker(self,full_df): 
        showroom_df=full_df.copy()
        msg="Seleccione las columnas que desea mostrar a sus invitados"
        title='Seleccion'
        choicebox=eg.multchoicebox(msg,title,full_df.columns.tolist())
        try:
            showroom_df=showroom_df[choicebox]
        except:
            pass
        pass
        return showroom_df
        
    def df_to_csv(self,dataframe,pathway):
        if not os.path.exists(f"{pathway}/csv/"):
            os.makedirs(f"{pathway}/csv/")
        else:    
            pass
        file_pathway=f"{pathway}/csv/full_df.csv"
        dataframe.to_csv(file_pathway,sep=",",encoding="utf-8")

class qr_tools():
    def __init__(self,api_key,sub_domain,GitHub_user,GitHub_repo,path,IDs,option):
        self.api_key=api_key 
        self.sub_domain=sub_domain
        self.GitHub_user=GitHub_user
        self.GitHub_repo=GitHub_repo
        self.option=option
        self.path=path
        self.IDs=IDs

    def dynamiclinks(self,id): #option invited, dwc_file
        if self.option=="dwc_files":
            longurl=f'https://raw.githubusercontent.com/{self.GitHub_user}/{self.GitHub_repo}/master/files/{id}.txt'
        elif self.option=="invited":
            longurl=f'https://raw.githubusercontent.com/{self.GitHub_user}/{self.GitHub_repo}/master/showroom_files/{id}.txt'
        try:
            url_shortener = UrlShortener(self.api_key,self.sub_domain)
            shorturl=url_shortener.get_short_link(longurl)
        except:
            print('Oops! you have reached the limit of urls')
        time.sleep(0.2) #to not break the limits of firebase
        return shorturl

    def qr_creator(self,short_url,image_pathway): #option invited, dwc_file
        try:
            filename=image_pathway
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            quick_response_code= pyqrcode.create(short_url)
            with open(filename, 'wb') as f:
                    quick_response_code.png(f, scale=8,module_color=(0,102,0,255),background=(255, 255, 255, 255))
            try:
                img = Image.open(filename)
                width, height = img.size
                logo_size =50
                logo = Image.open('documents\logo.png')
                xmin = ymin = int((width / 2) - (logo_size / 2))
                xmax = ymax = int((width / 2) + (logo_size / 2))
                logo = logo.resize((xmax - xmin, ymax - ymin))
                img.paste(logo, (xmin, ymin, xmax, ymax))
                img.save(filename)
            except:
                pass
        except:
            print(f'permission to write in {filename} has been denied...')

    def qr_manager(self):
        if self.option=="dwc_files":
            pathway=f"{self.path}/qrs"
        elif self.option=="invited":
            pathway=f"{self.path}/qrs_showroom"
        try:
            if os.path.isdir(pathway)==True:
                for id in self.IDs:
                    print(f'file {id} of file {self.IDs[-1]}',end='\r', flush=True)
                    image_path=f"{pathway}/{id}.png"
                    if os.path.isfile(image_path)==False:
                        short_url=self.dynamiclinks(id)
                        self.qr_creator(short_url,image_path)
                    else:
                        pass
            else:
                for id in self.IDs:
                    print(f'file {id} of file {self.IDs[-1]}',end='\r', flush=True)
                    image_path=f"{pathway}/{id}.png"
                    short_url=self.dynamiclinks(id)
                    self.qr_creator(short_url,image_path)
            if self.option=="dwc_files": 
                print("Se han terminado de crear los codigos Qr que dirigen a tus archivos DwC")
            elif self.option=="invited":
                print("Se han terminado de crear los codigos Qr que dirigen a tus archivos de invitados")
        except:
            if self.option=="dwc_files":
                print("Ha ocurrido un error en la creacion de los codigos Qr de DwC")
            elif self.option=="invited":
                print("Ha ocurrido un error en la creacion de los codigos Qr de invitados")

