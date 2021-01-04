#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:00:15 2020

@author: guillaumeorset
"""
from JLLv2 import baseJLL
from sqlalchemy import create_engine
from CBRE import baseCBRE
import pandas as pd
import schedule 
import time 

def immoWebscrapping():
    """ Script pour lancer les deux threads concernant chaque site """
    try:
        #Je lance deux fois la base JLL car il n'y a pas toujours le même nombre d'annonces
        dfCBRE= baseCBRE()
        dfJLL= baseJLL()
        dfJLL2=baseJLL()
        dfJLL.start()
        dfJLL2.start()
        dfCBRE.start()
        dfJLL.join()
        dfJLL2.join()
        dfCBRE.join()
        dfCBRE=dfCBRE.baseCBRE
        dfJLL=dfJLL.baseJLL
        dfJLL2=dfJLL2.baseJLL
        dfJLLFinal = pd.concat([dfJLL,dfJLL2])
        dfJLLFinal.drop_duplicates(inplace=True)
        final=pd.concat([dfCBRE,dfJLLFinal])
        final.sort_values(by="code_postal",inplace=True)
        final.reset_index(inplace=True,drop=True)
        #Nettoyage de certaines données
        final["adresse"]= final["adresse"].apply(lambda x: x[1:] if x.find(" ")==0 else x)
        final.loc[final["contact"]=="","contact"]="N/R"
        final["lien_photo"]= final["lien_photo"].apply(lambda x: "https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled-1150x647.png" if x.find("h")!=0 else x)
        #Pour le moment, s'il y a plusieurs photos on garde que la première
        final["lien_photo"]= final["lien_photo"].apply(lambda x: x[:x.find(",")] if x.find(",")!=-1 else x)
        final.loc[final["adresse"]=="","adresse"]="N/R"
        final.loc[final["ville"]=="","ville"]="N/R"
        final.loc[final["nom_annonce"]=="","nom_annonce"]="N/R"
        final["ville"]=final["ville"].apply(lambda x: x.upper())
        final.insert(loc=0, column="id", value=final.index+1)
    
        final["prix_integer"]=final["prix"]
        final.loc[final["prix"]=="N/R","prix_integer"]=0 
        final["prix_integer"]= final["prix_integer"].apply(lambda x: x[str(x).rfind(" ",1,13)+1:-1] if str(x).find("A partir de")!=-1 else x)
        final["prix_integer"]= final["prix_integer"].apply(lambda x: int(str(x).replace(" ","")))
    except:
        print("Problème lors du scrapping")
    
    """ Connection à MYSQl """
    database_username = 'root'
    database_password = 'eisti0001'
    database_ip       = 'localhost'
    
    sqlEngine= create_engine('mysql://{0}:{1}@{2}'.format(database_username, database_password, database_ip))
    dbConnection    = sqlEngine.connect()
    
    #D'abord, on créé la database immobilier 
    try:
        dbConnection.execute("CREATE DATABASE IF NOT EXISTS immobilier DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;")
        sqlEngine= create_engine('mysql://{0}:{1}@{2}/immobilier'.format(database_username, database_password, database_ip))
        dbConnection    = sqlEngine.connect()
        print("Database créée ou bien présente")
    except:
        print("Problème de création de la DataBase")
        
    tableName = "annonce"
    
        
    #On met celle qui était actuelle dans l'ancienne et on charge la DB actuelle
    try:
        final.to_sql(tableName, dbConnection, if_exists='replace',index=False)
        dbConnection.execute("ALTER TABLE immobilier.`annonce` CHANGE COLUMN id id BIGINT UNSIGNED NOT NULL ,ADD PRIMARY KEY (id),ADD UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE;")
        dbConnection.execute("ALTER TABLE `immobilier`.`annonce` CHANGE COLUMN `id` `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT ;")
        
    except ValueError as vx:
    
        print(vx)
    
    except Exception as ex:   
    
        print(ex)
    
    else:
    
        print("Table {} créée avec succès".format(tableName));   


immoWebscrapping()
schedule.every(5).minutes.do(immoWebscrapping)
while True:
    schedule.run_pending()
    time.sleep(1)