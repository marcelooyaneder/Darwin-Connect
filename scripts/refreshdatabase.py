import os
import easygui as eg
import pandas as pd
import filecmp
import shutil

class refreshdatabase():
    def diropenbox(self):
        """esta funcion sera para encontrar el directorio o 
        para crear un directorio que contendra todos los archivos"""
        route_destiny_response_label=eg.diropenbox()
        return route_destiny_response_label

    def file_organizer(self,route_response_label):
        try:
            file_path=route_response_label
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                data=pd.read_excel(file_path,sheet_name='Hoja1',header=0)
            elif file_path.endswith('.csv'):
                data=pd.read_csv(file_path,header=0,sep=';') #ver como variar de ; o ,
        except:
            print("no hemos podido encontrar la ruta del archivo excel")
        columns_df=data.columns.tolist()
        msg='select a column to be the index of the dataframe'
        title='select index'       
        indexo=eg.choicebox(msg,title,columns_df)
        data=data.set_index(indexo, drop = True)
        full_df=data.copy()
        full_df_columns=full_df.columns.tolist()
        columns_dwc=pd.read_csv('documents\dwc_terms\simple_dwc_horizontal.csv',header=0,sep=';').columns.tolist() #ver como variar de ; o , 
        columns_difference=list(set(columns_df)-set(columns_dwc))
        if not columns_difference:
            pass
        else:
            msg='the followings columns do not belong to DwC, select the ones you wish to delete'
            title='select to delete'       
            choicebox=eg.multchoicebox(msg,title,columns_difference)
            try:
                for label in choicebox:
                    data.drop(label,axis=1,inplace=True)
            except:
                pass
        try:
            data.dropna(axis=1, how='all',inplace=True)
            full_df.dropna(axis=1, how='all',inplace=True)
            #full_df.to_csv('online_dataframe.csv',sep=',')
        except:
            pass
        return full_df,data,indexo,full_df_columns

    def comparefiles(self,ID,info,option):  #option 1 for showroom, 0 files 
        filename1 = f"temp/{ID}.txt"
        if option==1:
            filename2= f"showroom_files/{ID}.txt"
        elif option==0:
            filename2= f"files/{ID}.txt"
        os.makedirs(os.path.dirname(filename1), exist_ok=True)
        with open(filename1,'w') as fil:
            fil.write(str(info))
        if os.path.isfile(filename2)==True:
            if filecmp.cmp(filename1,filename2)==False:
                print(f'ive found some changes since the last time, on file... {ID}.txt')
                print('changes has been saved')
                shutil.move(filename1,filename2)
            else:
                pass
        else:
            print(f'a new entry has been found, file... {ID}.txt has been created.')
            os.makedirs(os.path.dirname(filename2), exist_ok=True)
            with open(filename2,'w') as fil:
                fil.write(str(info))
        shutil.rmtree('temp/', ignore_errors=False, onerror=None)
        return 

    def infowriting(self):
        pass
    def dynamiclinks(self):
        pass
    def qr_manager(self):
        pass

