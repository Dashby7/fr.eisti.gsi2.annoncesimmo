# Projet Annonces Immobilières (ING2 Projet JavaEE - CYTECH)

## Pour démarrer l'application

1. Installer le JDK Java 15 (https://www.oracle.com/fr/java/technologies/javase-downloads.html).
2. Installer Maven 3.6.3+ (https://maven.apache.org/download.cgi).
3. Configurer les répertoires correspondants dans le fichier cli.cmd à la racine du projet (version windows, faire le script équivalent si Linux).
4. Lancer le script python (src/main/resources/database/python/DataBase.py). Pour cela, il recommandé d'avoir Anaconda (https://www.anaconda.com/products/individual#Downloads) et d'installer les packages si nécessaire.

5. Pour builder l'application, exécuter la commande (depuis le terminal lancé avec cli.cmd) :
      > **mvn clean package**
   
Cela permettra de télécharger les dépendances du projet ainsi que construire le jar de l'application dans **/target**.

9. Pour démarrer le serveur d'application, exécuter la commande :
      > **mvn spring-boot:run**

10. Si besoin de modifier les paramètres de connexion à la base de données, modifier le fichier **/src/main/resources/application.properties**.
      
L'application est désormais lancée, le serveur écoute sur le port **8080**.

Note : **MySQL Server doit être lancé pour que le script python et l'application fonctionnent (root, eisti0001)**.

## Pour tester l'application

0. Lancer son navigateur web et entrer l'URL suivante : **localhost:8080/index**

Il est auusi possible d'utiliser le client REST **Postman**.

1. Installer Postman (https://www.postman.com/downloads/).
2. Importer dans Postman le fichier .json à la racine du projet. Il permet de requêter l'ensemble des services de l'application, cela permettra de savoir si tout fonctionne bien. Penser à bien démarrer le serveur au préalable.

## Pour déployer l'application

1. Builder l'application, exécuter la commande :
      > **mvn clean package**
      
Ou bien, utiliser directement le .jar dans la release 3.0 sur GitHub (https://github.com/Dashby7/fr.eisti.gsi2.annoncesimmo) et disponible également à la racine du projet.

2. Entrer la commande à partir du cli.cmd (ou un terminal) pour lancer l'exécutable :
      > **java -jar annonces-immo-3.0.jar**
      
3. Sinon, vous pouvez aussi utiliser le fichier **.war** disponible à la racine du projet.