# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:38:49 2020

@author: Administrator
"""
from threading import Thread
from bs4 import BeautifulSoup as soup
import pandas as pd
import requests
class CBREClasse:
    """ Classe qui s'occuper de scraper toutes les données du site France de CBRE """
    def __init__(self):
        #Declaration des variables de bases qui vont être alimentées par les Data
        self.liste_nom_annonce = []
        self.liste_adresse = []
        self.liste_surface = []
        self.liste_prix = []
        self.liste_type_bien = []
        self.liste_type_locaux = []
        self.liste_photo = []
        self.liste_lien=[]
        self.liste_ville=[]
        self.liste_postal=[]
        self.liste_contact=[]
        self.liste_dispo=[]
        self.liste_reference=[]
        #On créé un dictionnaire en fonction de ce que l'on veut et des paramètres sur le site
        self.type_bien = {"a-vendre":0,"a-louer":1}
        self.type_locaux = {"bureaux":1,"entrepots":2,"terrains":4,"commerces":5,"coworking":6}
        #Penser à ne pas faire la boucle des coworking à la vente
        self.url ='https://immobilier.cbre.fr/ui/listpage/properties.aspx?'

    def launchScrap(self):
        for local,value in self.type_locaux.items():
            for bien,sitevalue in self.type_bien.items():
        
                #sort=0 pour trier au plus récent
                my_url=self.url+'ZPTID='+str(value)+'&TT='+str(sitevalue)+'&Paging=12&Page=0&Sort=0'
                source = requests.get(my_url).text
                page_soup = soup(source,"html.parser")
                nbAnnonces = page_soup.find("div",{'id':"container"})["itemcount"]
                #une fois qu'on a le nombre d'annonces on modifie l'URl avec Paging
                my_url=self.url+'ZPTID='+str(value)+'&TT='+str(sitevalue)+"&Paging="+str(nbAnnonces)+"&Page=0&Sort=0"
                print("type_de_bien :{}, type_de_local : {}, nombre annonces : {}".format(bien,local,nbAnnonces))
                source = requests.get(my_url).text
                page_soup = soup(source,"html.parser")
        
                #On commence le scrap
                containers = page_soup.find_all("div", {"class":"col-sm-6 col-lg-6 col-xl-4"})
                #on enlève le premier résultat car c'est de la pub
                containers=containers[1:]
                
                for container in containers:
                    try:
                        title = container.find_all("img")[0]["title"]
                    except:
                        title = "non indiqué"
                    try:
                        fin=container.find_all("a")[0]["href"].rfind("/")
                        debut=container.find_all("a")[0]["href"].rfind("/",1,fin)
                        ville = container.find_all("a")[0]["href"][debut+1:fin]
                        fin = debut
                        debut =container.find_all("a")[0]["href"].rfind("/",1,fin)
                        postal =  container.find_all("a")[0]["href"][debut+1:fin]
        
                    except:
                        ville = "N/R"
                        postal = "N/R"
                    try:
                        adresse = title[title.find(postal):]
                    except:
                        adresse = "N/R"
                   
                    try:
                        surface = container.find("div",{'class':"caption"}).find_next('p').find_next('p').text
                    except:
                        surface = "N/R"
                    try: 
                        loyer = container.find("div",{'class':"price"}).text
                    except:
                        loyer="N/R"
                    try: 
                        dispo = container.find("div",{'class':"caption"}).find_next('p').find_next('p').find_next('p').text
                    except:
                        dispo="N/R"
        
                    try:
                        ref_annonce = container.find_all("a")[0]["href"]
                    except:
                        ref_annonce="N/R"
                    try:
                        ref_photo=container.find_all("img")[0]["data-src"]
                    except:
                        ref_photo="N/R"
                    try:
                        contact = container.find("a",{'class':"fs-tel-offer"})["data-real-number"]
                    except:
                        contact="N/R"
                    try:
                        chaine = container.find("div",{'class':"cta"}).a["onclick"]
                        reference=chaine[chaine.rfind("=")+1:-2]
                    except:
                        reference="N/R"
                        
                    self.liste_nom_annonce.append(title)
                    self.liste_adresse.append(adresse)
                    self.liste_ville.append(ville)
                    self.liste_prix.append(loyer)
                    self.liste_surface.append(surface)
                    self.liste_type_bien.append(bien)
                    self.liste_postal.append(postal)
                    self.liste_type_locaux.append(local)
                    self.liste_lien.append(ref_annonce)
                    self.liste_photo.append(ref_photo)
                    self.liste_dispo.append(dispo)
                    self.liste_contact.append(contact)
                    self.liste_reference.append(reference)
        dfCBRE = pd.DataFrame({"nom_annonce":self.liste_nom_annonce,"ville":self.liste_ville,"adresse":self.liste_adresse,"code_postal":self.liste_postal,
                                       "prix":self.liste_prix,"surface":self.liste_surface,"disponibilite":self.liste_dispo,
                                       "type_transaction":self.liste_type_bien,"type_bien":self.liste_type_locaux,
                                       "lien":self.liste_lien,"lien_photo":self.liste_photo,
                                       "contact":self.liste_contact,"site":"CBRE","reference_du_site":self.liste_reference})
        #Mise au format général de toutes les DataBase
        dfCBRE.loc[dfCBRE["type_bien"]=="bureaux","type_bien"]="bureau"
        dfCBRE.loc[dfCBRE["type_bien"]=="entrepots","type_bien"]="Activités/Entrepôts"
        dfCBRE.loc[dfCBRE["type_bien"]=="terrains","type_bien"]="Terrain"
        dfCBRE.loc[dfCBRE["type_bien"]=="commerces","type_bien"]="commerce"
        dfCBRE.loc[dfCBRE["type_transaction"]=="a-louer","type_transaction"]="à louer"
        dfCBRE.loc[dfCBRE["type_transaction"]=="a-vendre","type_transaction"]="à vendre"
        dfCBRE["divisibilite"] = dfCBRE["surface"].apply(lambda x: x[x.find("m²")+3:])
        dfCBRE["divisibilite"] = dfCBRE["divisibilite"].apply(lambda x: x.replace("divisibles","Divisible"))
        dfCBRE["surface"] = dfCBRE["surface"].apply(lambda x: x[:x.find("m²")])
        dfCBRE["surface"] = dfCBRE["surface"].apply(lambda x: x.replace(" ",""))
        dfCBRE["surface"] = dfCBRE["surface"].apply(lambda x: x.replace(",","."))
        #On est obligé de faire deux casts car il y a des floats avec '.' comptés comme des string
        dfCBRE["surface"] = dfCBRE["surface"].apply(lambda x: int(float(x)))
        #mise au format du prix
        dfCBRE.loc[dfCBRE["prix"]=="Nous contacter","prix"]="N/R"
        dfCBRE["indication_prix"] = dfCBRE["prix"].apply(lambda x: x[x.find("€"):] if x.find("€")!=-1 else "N/R")
        dfCBRE["prix"]=dfCBRE["prix"].apply(lambda x: x[:x.find("€")] if x.find("€")!=-1 else "N/R")
        dfCBRE["prix"] = dfCBRE["prix"].apply(lambda x: int(x.replace(" ","")) if (x[:11]!='A partir de')&(x!="N/R") else x)
        #Généralisation des différentes indications de prix
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ /an HT HC')|(dfCBRE["indication_prix"]=='€ /an HT/HC')|(dfCBRE["indication_prix"]=='€ an / HT HC')|(dfCBRE["indication_prix"]=='€ AN / HT HC')|(dfCBRE["indication_prix"]=='€ an HC/HT')|(dfCBRE["indication_prix"]=='€ an HT HC')|(dfCBRE["indication_prix"]=='€ An HT HC')|(dfCBRE["indication_prix"]=='€ AN HT HC')|(dfCBRE["indication_prix"]=="€ an HT HC en l'état")|(dfCBRE["indication_prix"]=='€ an HT/HC')|(dfCBRE["indication_prix"]=='€ AN HT/HC')|(dfCBRE["indication_prix"]=='€ an/ HT HC')|(dfCBRE["indication_prix"]=='€ an/HT HC')|(dfCBRE["indication_prix"]=='€ an/HT/HC')|(dfCBRE["indication_prix"]=='€ AN/HT HC')|(dfCBRE["indication_prix"]=='€ HT / HC / an')|(dfCBRE["indication_prix"]=='€ HT HC / an')|(dfCBRE["indication_prix"]=='€ HT HC /an')|(dfCBRE["indication_prix"]=='€ HT HC an')|(dfCBRE["indication_prix"]=='€ HT HC/an')|(dfCBRE["indication_prix"]=='€ HT/HC/ an')|(dfCBRE["indication_prix"]=='€ HT/HC/AN')|(dfCBRE["indication_prix"]=='€ HT/HC/an'),"indication_prix"]="€ /an HT HC"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ /m² an HT HC')|(dfCBRE["indication_prix"]=='€ /m²/an HT HC')|(dfCBRE["indication_prix"]=='€ an HT HC / m²')|(dfCBRE["indication_prix"]=='€ an HT HC m²')|(dfCBRE["indication_prix"]=='€ HT / HC / m² / an')|(dfCBRE["indication_prix"]=='€ HT HC/CC/m²/an')|(dfCBRE["indication_prix"]=='€ HT HC/HC/m²/an')|(dfCBRE["indication_prix"]=='€ ht/hc/m²/an')|(dfCBRE["indication_prix"]=='€ HT/HC/M²/AN')|(dfCBRE["indication_prix"]=='€ HT/HC/m²/an')|(dfCBRE["indication_prix"]=='€ m²/an HT CC')|(dfCBRE["indication_prix"]=='€ m²/an HT HC')|(dfCBRE["indication_prix"]=='€ m²/an HT/HC')|(dfCBRE["indication_prix"]=='€ m²/an/ HT HC')|(dfCBRE["indication_prix"]=='€ m²/an/HT HC/HC')|(dfCBRE["indication_prix"]=='€ m²/an/HT/HC'),"indication_prix"]="€ /m² an HT HC"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ /lot/an/HT/HC')|(dfCBRE["indication_prix"]=='€ an HT HC/lot')|(dfCBRE["indication_prix"]=='€ lot/an HT HC')|(dfCBRE["indication_prix"]=='€ lot/HT/HC/an'),"indication_prix"]="€ /lot/an/HT/HC"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ an HC')|(dfCBRE["indication_prix"]=='€ an Hors Charges'),"indication_prix"]="€ /an HC"

        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ /poste/mois HT')|(dfCBRE["indication_prix"]=='€ HT/poste/mois')|(dfCBRE["indication_prix"]=='€ poste/mois HT'),"indication_prix"]="€ poste/mois HT"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HD')|(dfCBRE["indication_prix"]=='€ Hors droits'),"indication_prix"]="Hors Droits"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HD / Hors Honoraires')|(dfCBRE["indication_prix"]=='€ HD HH')|(dfCBRE["indication_prix"]=='€ HD Hors Honnoraires')|(dfCBRE["indication_prix"]=='€ HD Hors Honoraires')|(dfCBRE["indication_prix"]=='€ HD/HH')|(dfCBRE["indication_prix"]=='€ HD/Hors Honoraires')|(dfCBRE["indication_prix"]=='')|(dfCBRE["indication_prix"]=='€ HD/Hors honoraires'),"indication_prix"]="€ HD HH"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HD H. HT inclus')|(dfCBRE["indication_prix"]=='€ HD/Hono. HT inclus'),"indication_prix"]="€ HD H. HT inclus"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HD HT')|(dfCBRE["indication_prix"]=='€ HD/HT')|(dfCBRE["indication_prix"]=='€ HT HD')|(dfCBRE["indication_prix"]=='€ HT/HD'),"indication_prix"]="€ HD HT"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HD Net Vendeur')|(dfCBRE["indication_prix"]=='€ HD NET VENDEUR')|(dfCBRE["indication_prix"]=='€ HD net vendeur'),"indication_prix"]="€ HD Net Vendeur"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HD/HT net vendeur')|(dfCBRE["indication_prix"]=='€ HT / HD net vendeur'),"indication_prix"]="€ HD HT net vendeur"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HD/m²')|(dfCBRE["indication_prix"]=='€ m² HD'),"indication_prix"]="€ / m² HD"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HT')|(dfCBRE["indication_prix"]=='€ Hors TVA'),"indication_prix"]="€ HT"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HT / an')|(dfCBRE["indication_prix"]=='€ HT/an')|(dfCBRE["indication_prix"]=='€ /an H.T.')|(dfCBRE["indication_prix"]=='€ an HT'),"indication_prix"]="€ HT / an"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HT / HC / m² (RDC)|')|(dfCBRE["indication_prix"]=='€ m² HT HC'),"indication_prix"]="€ / m² HT HC"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HT / mois')|(dfCBRE["indication_prix"]=='€ HT/mois'),"indication_prix"]="€ HT / mois"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HT HC')|(dfCBRE["indication_prix"]=='€ HT/HC'),"indication_prix"]="€ HT HC"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HT HH')|(dfCBRE["indication_prix"]=='€ HT/Hors Honoraires')|(dfCBRE["indication_prix"]=='€ HT/Hors honoraires'),"indication_prix"]="€ HT HH"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HT Honoraires Inclus')|(dfCBRE["indication_prix"]=='€ HT Honoraires inclus'),"indication_prix"]="€ HT Honoraires Inclus"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HT/m²')|(dfCBRE["indication_prix"]=='€ m² HT'),"indication_prix"]="€ / m² HT"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ HT/m²/an')|(dfCBRE["indication_prix"]=='€ m²/an CC/Hors TVA'),"indication_prix"]="€ m² / an /HT"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ m²')|(dfCBRE["indication_prix"]=='€/m²')|(dfCBRE["indication_prix"]=='﻿€ / m²'),"indication_prix"]="€ / m²"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ m² HD/HT')|(dfCBRE["indication_prix"]=='€ m² HT HD')|(dfCBRE["indication_prix"]=='€ m² HT/HD'),"indication_prix"]="€ / m² HD HT"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ m²/an /HC')|(dfCBRE["indication_prix"]=='€ m²/an HC')|(dfCBRE["indication_prix"]=='€ m²/an/ HC'),"indication_prix"]="€ / m² an HC"
        dfCBRE.loc[(dfCBRE["indication_prix"]=='€ net vendeur')|(dfCBRE["indication_prix"]=='€ Net vendeur')|(dfCBRE["indication_prix"]=='€ Net Vendeur')|(dfCBRE["indication_prix"]=='€ NV'),"indication_prix"]="€ Net Vendeur"
        
        dfCBRE.loc[dfCBRE["divisibilite"]=="non Divisible","divisibilite"]="Non Divisible"
        dfCBRE["disponibilite"]=dfCBRE["disponibilite"].apply(lambda x: x[x.find(":")+2:] if x.find("Dispo")==0 else "Nous contacter")
        dfCBRE=dfCBRE[['nom_annonce', 'ville', 'adresse', 'code_postal', 'prix',
       'surface', 'divisibilite', 'disponibilite', 'type_transaction',
       'type_bien', 'lien', 'lien_photo', 'contact', 'site',
       'reference_du_site', 'indication_prix']]
        
        print(len(dfCBRE['reference_du_site'])-len(dfCBRE['reference_du_site'].drop_duplicates()))
        dfCBRE.drop_duplicates(inplace=True)

        return dfCBRE

""" Je définis mon thread CBRE pour pouvoir le faire tourner en même temps que les autres sites """
class baseCBRE(Thread):
    """Thread chargé de récupérer toutes les annonces CBRE"""

    def __init__(self):
        Thread.__init__(self)
    def run(self):
        self.objetCBRE = CBREClasse()
        self.baseCBRE = self.objetCBRE.launchScrap()
        
   
