# Projet Annonces Immo

## Pour démarrer l'application

1. Installer le JDK Java 15.
2. Installer Maven 3.6.3+.
3. Configurer les répertoires correspondants dans le fichier cli.cmd à la racine du projet (version windows, faire le script équivalent si Linux).
4. Lancer le script.
5. Pour builder l'application, exécuter la commande :
      > **mvn clean package**
   
Cela permettra de télécharger les dépendances du projet ainsi que construire le jar de l'application dans **/target**.

6. Pour démarrer le serveur d'application, exécuter la commande :
      > **mvn spring-boot:run**

7. Si besoin de modifier les paramètres de connexion à la base de données, modifier le fichier **/src/main/resources/application.properties**.
      
L'application est désormais lancée, le serveur écoute sur le port **8080**.

## Pour tester l'application

Il est possible d'utiliser le client REST **Postman**.

a. Installer Postman
b. Importer dans Postman le fichier .json à la racine du projet. Il permet de requêter l'ensemble des services de l'application. Bien démarrer le serveur au préalable.

## Pour déployer l'application

1. Builder l'application, exécuter la commande :
      > **mvn clean package**
      
Ou bien, utiliser directement le .jar de la release 1.0 dans Github.

2. Lancer la commande à partir du cli.cmd :
      > **java -jar annonces-immo-1.0.jar**
