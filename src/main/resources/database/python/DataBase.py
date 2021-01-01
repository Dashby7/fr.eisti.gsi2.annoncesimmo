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

""" Script pour lancer les deux threads concernant chaque site """
try:
    dfCBRE= baseCBRE()
    dfJLL= baseJLL()
    dfJLL.start()
    dfCBRE.start()
    dfCBRE.join()
    dfJLL.join()
    dfCBRE=dfCBRE.baseCBRE
    dfJLL=dfJLL.baseJLL
    
    final=pd.concat([dfCBRE,dfJLL])
    final.sort_values(by="code_postal",inplace=True)
    final.reset_index(inplace=True,drop=True)
    #Nettoyage de certaines données
    final["adresse"]= final["adresse"].apply(lambda x: x[1:] if x.find(" ")==0 else x)
    final.loc[final["contact"]=="","contact"]="N/R"
    final.loc[final["lien_photo"]=="","lien_photo"]="N/R"
    final.loc[final["adresse"]=="","adresse"]="N/R"
    final.loc[final["ville"]=="","ville"]="N/R"
    final.loc[final["nom_annonce"]=="","nom_annonce"]="N/R"
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
    #J'autorise les accès
    #dbConnection.execute("GRANT ALL ON immobilier.* TO 'root'@'localhost';")
    #On se reconnecte directement à la Database et non avec Use immobilier car ca produit une erreur
    sqlEngine= create_engine('mysql://{0}:{1}@{2}/immobilier'.format(database_username, database_password, database_ip))
    dbConnection    = sqlEngine.connect()
    print("Database créée ou bien présente")
except:
    print("Problème de création de la DataBase")
    
tableName = "modifiee"

#Je récupère la base ancienne pour avoir une sauvegarde en cas de problème
# try:
#     ancienneDB = pd.read_sql("select * from {}".format(tableName), dbConnection);
#     #ancienneDB.drop(["index"], axis=1,inplace=True)
#     print("base précédente bien récupérée")
# except:
#     print("Récupération de l'ancienne base impossible")
    
#On met celle qui était actuelle dans l'ancienne et on charge la DB actuelle
try:
    #L'attribut replace ne marche pas donc je supprime et j'ajoute
    #ancienne = ancienneDB.to_sql("precedente", dbConnection, if_exists='replace',index=False)
    actuelle = final.to_sql(tableName, dbConnection, if_exists='replace',index=False)
except ValueError as vx:

    print(vx)

except Exception as ex:   

    print(ex)

else:

    print("Tables {} et precedente crées avec succès".format(tableName));   

