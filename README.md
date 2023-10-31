# assement documentation

## Pour lancer correctement le projet
- Cloner le dépôt GitHub: Vous devez doit cloner le dépôt GitHub sur votre machine machine

- Installer Pipenv: Assurez-vous d'installer Pipenv. Vous Pouvez l'installer en utilisant la commande 'pip install pipenv'

- Naviguer vers le répertoire du projet: en utilisant la commande cd.

- Installer les dépendances: Pour installer les dépendances du projet, vous devez exécuter la commande 'pipenv install'.

- Activer l'environnement virtuel: Vous devez activer l'environnement virtuel en utilisant la commande 'pipenv shell'

- Lancer l'application: Une fois l'environnement virtuel activé, vous pouvez lancer l'application en utilisant la commande 'python manage.py runserver'


## User et BD
### Ma base de donnee n'etant pas commiter en ligne, voici les etapes qui vous permettrons de creer la votre afin de faire des tests sur l'api :
- Vous executer la commande : python manage.py createsuperuser, pour creer un utilisateur 

- En suite vous appliquer les migrations avec les commandes dans l'ordre suivant :
   * python manage.py makemigrations
   * python manage.py migrate 

- Vous pouvez donc lancer le serveur et aller au 127.0.0.1:8000/admin, qui vous permettra de vous connecter via l'admin de django a la base de donnee en entrant votre nom d'utilisateur et mot de passe


## Endpoints
### Durant le developpement j'ai utiliser l'outil postman pour faire les tests 

- type: GET, Endpoint: http://127.0.0.1:8000/health_check/, Authenticated: Public 
####  Cette requette donne en quelque sorte l'etat de sante de l'API et renvoi un  HTTP 200 OK si tout fonctionne comme prévu.

- type: POST, Endpoint: http://127.0.0.1:8000/polymers/, Authenticated: Authenticated
### Ceci est la route qui permet d'ajouter des polymeres dans la base de donnee

- type: GET, Endpoint: http://127.0.0.1:8000/polymers/, Authenticated: Authenticated
### Est la route qui renvoie un ensemble de polymères appartenant à un intervalle donné, ex: GET/polymers?start=2023-07-10T08:00:00Z&end=2023-07-10T08:05:00Z

- type: GET, Endpoint: http://127.0.0.1:8000/reactor/, Authenticated: Authenticated
### Retourne un polymer réagi. ex: GET /reactor?start=2023-07-10T14:00:00Z&end=2023-07-20T23:59:59Z

## NB: Pour pouvoir effectuer ces requettes vous aurez besoin d'autorisation, la seule requette public est http://127.0.0.1:8000/health_check/. Et donc pour cela avec les informations de votre compte utilisateur que vous avez cree, vous aller effectuer une requette post sur cette url : http://127.0.0.1:8000/api-token-auth/ avec le body remplis comme suit: {"username": "votre_nom_utilisateur", "password": "votre_password"}, vous recevrer un token qui vous permettra d'effectuer les requette qui requiere une autorisation.
- Et pour specifier cela quand vous effectuer une requette, vous allez juste dans l'onglet Authorization, type: API Key. Vous verer des lignes dans les quelles vous entrerer respectivement :
1- Authorization, 2- Token "votre_token_generer.