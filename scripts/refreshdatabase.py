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
            msg="Las columnas a continuacion no se encuentran en nuestra base de datos de DwC\n Seleccione las que desee borrar"
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
            #full_df.to_csv('online_dataframe.csv',sep=',')
        except:
            pass
        return full_df,data,indexo,full_df_columns

    def comparefiles(self,ID,info,option,pathway):  #option 1 for showroom, 0 files 
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

    def infowriting(self,ID,info,option,pathway):  #option 1 for showroom, 0 files
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

    def dynamiclinks(self,longurl):
        user_info=pd.read_csv("documents\dynamiclinks_user_info.csv",header=0,sep=';')
        api_key=user_info['api_key'][0] #this need to be created on the firebase webpage
        sub_domain=user_info['sub_domain'][0] #this need to be created on firebase webpage
        try:
            url_shortener = UrlShortener(api_key,sub_domain)
            shorturl=url_shortener.get_short_link(longurl)
        except:
            print('Oops! you have reached the limit of urls')
        time.sleep(0.2) #to not break the limits of firebase
        return shorturl
        
    def qr_manager(self,ID,short_url,option): #option 1 for showroom, 0 files
        try:
            if option ==0:
                filename = f"qrs/{ID}.png"
            elif option==1:
                filename = f"qrs_showroom/{ID}.png"
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


"""#######################################
########FILE MANAGEMENT SECTION########
#######################################

dataframe=refreshdatabase()
file_mng_button=eg.buttonbox(msg='select an option',title='select an option',choices=['Open a file','Create a custom dwc file'])
if file_mng_button=='Open a file':
    og_data,data,indexo,og_columns_df=dataframe.file_opener() #no considerar para file_creation
    IDs=data.index.tolist() #no considerar para file_creation 
    showroom_option_button=eg.buttonbox(msg='do you wish to create files for a showroom',title='select a option',choices=['Yes','No'])
    if showroom_option_button=='Yes':
        showroom_df=og_data.copy()
        msg='select the columns to keep on your showroom dataframe'
        title='select'
        choicebox=eg.multchoicebox(msg,title,og_columns_df)
        try:
            showroom_df=showroom_df[choicebox]
        except:
            pass
    elif showroom_option_button=='No':
        pass
elif file_mng_button=='Create a custom dwc file':
    data=dataframe.file_creation() #no considerar para file_opener
    data.to_csv('custom_dwc_frame.csv',sep=';', encoding='utf-8') #considerar para file opener
    print ('your file is ready....')
    print(data)
    exit()

print(data)

#compare files or create them
print('compare/create files...')
if os.path.isdir('files')==True:
    for id in IDs:
        comparefiles(id,data.loc[id],0)
else:
    for id in IDs:
        infowriting(id,data.loc[id],0)

if showroom_option_button=='Yes':
    if os.path.isdir('showroom_files')==True:
        for id in IDs:
            comparefiles(id,showroom_df.loc[id],1)
    else:
        for id in IDs:
            infowriting(id,showroom_df.loc[id],1)
print ('there is nothing more to do here...')

#compare qr files or create them
user_info=pd.read_csv("documents\dynamiclinks_user_info.csv",header=0,sep=';')
GitHub_username=user_info['GitHub_username'][0] #this need to be created on the GitHub webpage
Repository_name=user_info['Repository_name'][0] #this need to be created on the firebase webpage
print('create non existing qrs files...')
if os.path.isdir('qrs')==True:
    for id in IDs:
        print(f'file {id} of file {IDs[-1]}',end='\r', flush=True)
        path=f"qrs/{id}.png"
        if os.path.isfile(path)==False:
            longurl=f'https://raw.githubusercontent.com/{GitHub_username}/{Repository_name}/master/files/{id}.txt'            
            shorturl=dynamiclinks(longurl)
            qr_manager(id,shorturl,0)
        else:
            pass
else:
    for id in IDs:
        print(f'file {id} of file {IDs[-1]}',end='\r', flush=True)
        longurl=f'https://raw.githubusercontent.com/{GitHub_username}/{Repository_name}/master/files/{id}.txt'
        shorturl=dynamiclinks(longurl)
        qr_manager(id,shorturl,0)

if showroom_option_button=='Yes':
    print('create non existing qrs shorwoom files...')
    if os.path.isdir('qrs_showroom')==True:
        for id in IDs:
            print(f'file {id} of file {IDs[-1]}',end='\r', flush=True)
            path=f"qrs_showroom/{id}.png"
            if os.path.isfile(path)==False:
                longurl=f'https://raw.githubusercontent.com/{GitHub_username}/{Repository_name}/master/showroom_files/{id}.txt'
                shorturl=dynamiclinks(longurl)
                qr_manager(id,shorturl,1)
            else:
                pass
    else:
        for id in IDs:
            print(f'file {id} of file {IDs[-1]}',end='\r', flush=True)
            longurl=f'https://raw.githubusercontent.com/{GitHub_username}/{Repository_name}/master/showroom_files/{id}.txt'
            shorturl=dynamiclinks(longurl)
            qr_manager(id,shorturl,1)
else:
    pass
print ('there is nothing more to do here...')"""
