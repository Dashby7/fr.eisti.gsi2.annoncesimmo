# Projet Annonces Immobilières

## Pour démarrer l'application

1. Installer le JDK Java 15 (https://www.oracle.com/fr/java/technologies/javase-downloads.html).
2. Installer Maven 3.6.3+ (https://maven.apache.org/download.cgi).
3. Configurer les répertoires correspondants dans le fichier cli.cmd à la racine du projet (version windows, faire le script équivalent si Linux).
4. Lancer le script.
5. Lancer MySQL (username : root, password : eisti0001).
6. Charger la table annonce avec le script Python.
7. Via MySQLWorkbench (qu'on a normalement quand on fait l'installation de MySQL, faire **File > Open Script SQL** et sélectionner le fichier .sql dans src/main/resources/database/sql/changement_table_annonce.sql

8. Pour builder l'application, exécuter la commande :
      > **mvn clean package**
   
Cela permettra de télécharger les dépendances du projet ainsi que construire le jar de l'application dans **/target**.

9. Pour démarrer le serveur d'application, exécuter la commande :
      > **mvn spring-boot:run**

10. Si besoin de modifier les paramètres de connexion à la base de données, modifier le fichier **/src/main/resources/application.properties**.
      
L'application est désormais lancée, le serveur écoute sur le port **8080**.

Note : **Une dépendance à Thymeleaf a déjà été intégrée au projet.**

## Pour tester l'application

Il est possible d'utiliser le client REST **Postman**.

1. Installer Postman (https://www.postman.com/downloads/).
2. Importer dans Postman le fichier .json à la racine du projet. Il permet de requêter l'ensemble des services de l'application, cela permettra de savoir si tout fonctionne bien. Penser à bien démarrer le serveur au préalable.

## Pour déployer l'application

1. Builder l'application, exécuter la commande :
      > **mvn clean package**
      
Ou bien, utiliser directement le .jar de la release 1.0 dans Github.

2. Lancer la commande à partir du cli.cmd :
      > **java -jar annonces-immo-1.0.jar**
