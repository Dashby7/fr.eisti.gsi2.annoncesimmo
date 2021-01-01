
from threading import Thread
from bs4 import BeautifulSoup as soup
import pandas as pd
import json
import requests
class JLLClasse:
    """ Classe qui s'occuper de scraper toutes les données du site France de JLL """

    def __init__(self):
        self.liste_nom_annonce_jll = []
        self.liste_adresse_jll = []
        self.liste_ville_jll = []
        self.liste_dispo_jll = []
        self.liste_surface_jll = []
        self.liste_prix_jll = []
        self.liste_type_bien_jll = []
        self.liste_type_locaux_jll = []
        self.liste_postal_jll=[]
        self.liste_photo_jll = []
        self.liste_divisible_jll=[]
        self.liste_lien_jll=[]
        self.liste_reference_jll=[]
        self.liste_contact_jll=[]
        self.type_bien = ["rent","sale"]
        self.type_locaux = ["office","industrial","coworking","warehouse","retail"]
        self.jll = "https://immobilier.jll.fr"


    def scrap(self,bien,local,page):
        print("type de bien :{}, type de local : {}, nombre pages : {}, page actuelle {} ".format(bien,local,self.nbPages,page))
        my_url = "https://immobilier.jll.fr/search?tenureType="+str(bien)+"&propertyType="+str(local)+"&sortBy=rank&orderBy=asc&page="+str(page)
        source = requests.get(my_url).text
        #html parser
        page_soup = soup(source,"html.parser")
        containers=json.loads(page_soup.find("script",{"id":"__NEXT_DATA__"}).string)
        containers=containers["props"]["pageProps"]["properties"]
        
        for container in containers:
            
            try:
                title = container["title"]
            except:
                title = "N/R"
            try:
                if container["addressLine2"]!='':
                    adresse_complete = [container["addressLine1"],container["addressLine2"]]
                    adresse_complete =  ",".join(adresse_complete)
                else:
                    adresse_complete=container["addressLine1"]
            except:                
                adresse_complete = "N/R"
            try: 
                postal = container["postcode"]
            except:
                postal="N/R"
            try:
                disponibilite=container["availabilityLabel"]
            except:
                disponibilite="N/R"
            try: 
                ville = container["city"]
            except:
                ville="N/R"
            try:
                
                if container["tenureType"][0]=="rent":
                    loyer = container["rentLabel"]
                    
                else:
                    loyer = container["saleLabel"]
                    
            except:
                loyer = "N/R"
            try:
                surface = container["maxSurfaceArea"]
                if container["surfaceAreaMetrics"][0]["min"]!=0:
                    divisible = "Divisible à partir de "+str(container["minSurfaceArea"])+" m²"
                else:
                    divisible ="Non divisible"
            except:
                surface = "N/R"
                divisible="N/R"
            try:
                ref_annonce = self.jll+container["pageUrl"]
            except:
                ref_annonce="N/R"
            try:
                ref_photo= ",".join(container["images"])
            except:
                ref_photo="N/R"
            try:
                reference=container["refId"]
            except:
                reference="N/R"
            try:
                contact=str(container["brokers"][0]["telephone"])+", "+str(container["brokers"][0]["email"])
            except:
                contact="N/R"
            self.liste_nom_annonce_jll.append(title)
            self.liste_adresse_jll.append(adresse_complete)
            self.liste_postal_jll.append(postal)
            self.liste_ville_jll.append(ville)
            self.liste_dispo_jll.append(disponibilite)
            self.liste_prix_jll.append(loyer)
            self.liste_divisible_jll.append(divisible)
            self.liste_surface_jll.append(surface)
            self.liste_type_bien_jll.append(bien)
            self.liste_type_locaux_jll.append(local)
            self.liste_lien_jll.append(ref_annonce)
            self.liste_photo_jll.append(ref_photo)
            self.liste_reference_jll.append(reference)
            self.liste_contact_jll.append(contact)
    def launchScrap(self):
        for local in self.type_locaux:
            for bien in self.type_bien:
                
                #On récupère le nombre de pages à parcourir tout d'abord
                my_url = "https://immobilier.jll.fr/search?tenureType="+str(bien)+"&propertyType="+str(local)+"&sortBy=rank&orderBy=asc&page=1"
                source = requests.get(my_url).text
                page_soup = soup(source,"html.parser")
                try:
                    self.nbPages=int(page_soup.find("nav",{'class':"Pagination"}).find_all("a")[-2].text)
                    for page in range(1,self.nbPages+1):
                        self.scrap(bien,local,page)
                except:
                    self.nbPages=1
                    self.scrap(bien,local,1)
    
        df = pd.DataFrame({"nom_annonce":self.liste_nom_annonce_jll,"ville": self.liste_ville_jll,"adresse":self.liste_adresse_jll,"code_postal":self.liste_postal_jll,
                           "prix":self.liste_prix_jll,"surface":self.liste_surface_jll,"divisibilite": self.liste_divisible_jll,
                           "disponibilite":self.liste_dispo_jll,
                           "type_transaction":self.liste_type_bien_jll,"type_bien":self.liste_type_locaux_jll,"lien":self.liste_lien_jll,
                           "lien_photo":self.liste_photo_jll,
                           "contact":self.liste_contact_jll,"site":"JLL","reference_du_site":self.liste_reference_jll})
        
        df.loc[df["type_bien"]=="office","type_bien"]="bureau"
        df.loc[df["type_bien"]=="industrial","type_bien"]="Activités/Entrepôts"
        df.loc[df["type_bien"]=="Activités/Entrepôts","nom_annonce"]="non indiqué"
        df.loc[df["type_bien"]=="warehouse","type_bien"]="Plateformes Logistiques"
        df.loc[df["type_bien"]=="retail","type_bien"]="commerce"
        df.loc[df["type_transaction"]=="rent","type_transaction"]="à louer"
        df.loc[df["type_transaction"]=="sale","type_transaction"]="à vendre"
        df.loc[df["lien_photo"]=="/static/FR_fr/default-img-small@2x.jpg","lien_photo"]="pas de photo"
        
        
        df.loc[df["prix"]=="€ - Nous consulter","prix"]="N/R"
        df["indication_prix"] = df["prix"].apply(lambda x: x[x.find("€"):] if x.find("€")!=-1 else "N/R")
        df.loc[df["prix"]=="N/R","indication_prix"]="N/R"
        df["prix"] = df["prix"].apply(lambda x: x[:x.find("€")] if x.find("€")!=-1 else "N/R")
        #on est obligé de remplacer des valeurs et faire différents casts pour avoir le bon type
        df["prix"] = df["prix"].apply(lambda x: x.replace(",","."))
        df["prix"] = df["prix"].apply(lambda x: x.replace(" ",""))
        df["prix"] = df["prix"].apply(lambda x: int(float(x)) if x!="N/R" else str(x))
        print(len(df['reference_du_site'])-len(df['reference_du_site'].drop_duplicates()))
        df.drop_duplicates(inplace=True)
        return df

""" Je définis mon thread JLL pour pouvoir le faire tourner en même temps que les autres sites """
class baseJLL(Thread):
    """Thread chargé de récupérer toutes les annonces JLL"""

    def __init__(self):
        Thread.__init__(self)
    def run(self):
        self.objetJLL = JLLClasse()
        self.baseJLL = self.objetJLL.launchScrap()

