<div align="center">
  <a href="" target="_blank" rel="noreferrer">
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png">
  </a>
</div>

<h1 align="center">

Bienvenue ! Vous trouverez ici le Projet 11 du parcours<a href="https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python" target="_blank" rel="noreferrer"> Développeur d'application - Python</a> 👋

</h1>

## Améliorez une application Web Python par des tests et du débogage
# GÜDLFT Regional Outreach Platform

## 🚀 Introduction

Bienvenue dans le repo de la plateforme de **GÜDLFT** pour le **Regional Outreach**. Cette plateforme vise à aider les organisateurs régionaux à gérer facilement leurs compétitions de force.

<p align="center">
  <img src="https://user.oc-static.com/upload/2020/09/22/16007798203635_P9.png" alt="Logo de GÜDLFT">
</p>

## 📜 Contexte

Après 5 ans d'existence et de focus sur des compétitions pour les entreprises de vêtements de fitness de marque, GÜDLFT souhaite redonner aux clubs régionaux. L'objectif est de rationaliser la gestion des compétitions entre les clubs (hébergement, inscriptions, frais et administration).

## 📚 Spécifications

Le projet est divisé en plusieurs phases. Actuellement, la phase 1 est en cours de QA.
Nous intervenons ici pour résoudre plusieurs bugs et dans l'ajout d'une fonctionnalité en s'appuyant sur le gestionnaire de version Git pour le suivi des modifications. Une branche par bug, une branche pour la fonctionnalité et une branche la phase de QA seront donc créées.

## 🤝 Contribution

### Étapes initiales

1.  Clonez et forkez le repo.
2.  Exécutez `source venv/bin/activate` pour activer l'environnement virtuel.
3.  Exécutez `export FLASK_APP=server.py` pour configurer Flask.

### Dépendances

-   Flask
-   pytest
-   Locust

Pour installer les dépendances, exécutez :

``` bash
pip install -r requirements.txt

```

### Branches

Nous utilisons une structure de branches spécifique :

-   **bug/**\* pour les correctifs.
    -   `bug/booking-places-in-past-competitions`
    -   `bug/club-booking-limit`
    -   `bug/club-points-usage`
    -   `bug/point-updates-not-reflected`
    -   `bug/unknown-email-handling`
-   **feature/**\* pour les nouvelles fonctionnalités.
    -   `feature/points-display-board`
-   **qa/**\* pour l'assurance qualité.
    -   `qa/ocp11-release`
-   **master** pour la version stable.

### Tests

Nous utilisons `pytest` pour les tests unitaires. Un guide de test détaillé est disponible dans les spécifications fonctionnelles.

Nous utilisons `locust` pour les tests de performance. Un guide de test détaillé est disponible dans les spécifications fonctionnelles.

Pour exécuter les tests :

```
pytest tests/nom du bug ou de la fonctionnalité
```
Exemple :
```
pytest Tests/unitaires/test_booking_past_competitions.py
```
```

### Rapports

-   Un rapport de test est disponible à la fin de chaque phase.
-   Un rapport de performance est également requis.

```

# gudlift-registration

1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need.


    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally.


3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:

    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

    We also like to show how well we're testing, so there's a module called
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

