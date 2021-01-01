Pour lancer l'application :

1. Installer le JDK Java 15
2. Installer Maven 3.6.3+
3. Configurer les répertoires correspondants dans le fichier cli.cmd à la racine du projet (version windows)
4. Lancer le script
5. Pour builder l'application, exécuter la commande :
      mvn clean package
   Cela permettra de télécharger les dépendances du projet ainsi que construire le jar de l'application dans /target
6. Pour démarrer le serveur d'application, exécuter la commande :
      mvn spring-boot:run
      
L'application est désormais lancée, le serveur écoute sur le port 8080.

Pour tester l'application, il est possible d'utiliser le client REST Postman.

a. Installer Postman
b. Importer le projet Postman, fichier .json à la racine du projet. Il permet de requêter l'ensemble des services de l'application.
