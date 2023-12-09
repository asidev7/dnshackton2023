# dnshackton2023

##Configuration Requise

    Python 3.10 ou supérieur
    Django 4.1.3
    Bootstrap 4.0

#installation 
veuillez cloner le project sur votre dosier de travail 


git clone https://github.com/asidev7/dnshackton2023.git 

puis acceder au dossier 

cd dnshackton2023

1. Création d'un Environnement Virtuel

Ouvrez votre terminal et naviguez vers le dossier du project. Créez un environnement virtuel en utilisant Python 3, ou une version supérieure :

    python3 -m venv venv

2. Activation de l'Environnement Virtuel

Activez l'environnement virtuel (selon votre système d'exploitation) :
Sur Mac/Linux :

    source venv/bin/activate

3. Installation des Dépendances

Installez les dépendances requises en utilisant la commande :
    
    pip install -r requirements.txt

4. Configuration de la Base de Données

Créez une base de données MySQL et configurez les paramètres de la base de données dans settings.py. (nous allons utilise la base de donnee Mysql) 

5. Migrations de la Base de Données

Effectuez les migrations de la base de données en utilisant la commande :

    python manage.py migrate

6. Lancement du Serveur de Développement

Lancez le serveur de développement avec la commande :
    python manage.py runserver

##Fonctionnalités

(Détails sur les fonctionnalités du projet)
 - Rechercher et reserver un nom de domaine 
 - S'authentifier pour reserver le nom de domaine 
 - Page de panel sur l'adresse : https://localost:8000/admin
 - Voir les details de domaine reservee par le client

