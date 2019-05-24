# FightingFowl
This web app allows one to upload two specific json files and compare them.

## Design Decisions
Django was choosen as a framework for this app because it's great at handling json data and it is easy 
to deploy on multiple plateforms. Also, I wanted to challenge myself and relearn a new framework I haven't 
worked with in years.

## Assumptions
It is assumed that the two files will have the same json scheme as the test files given in the problem statement
and they will be named ``orders.json`` and ``restocks.json``

## Instructions for running the app
#### Must have:
 - Django 1.8 or later
 - Python 2.7 or later

#### Installation
  - ``git clone https://github.com/thepinkturtle/FightingFowl.git``
  - ``cd FightingFowl``
  - run ``python manage.py runserver``
  - upload the ``orders.json`` and ``restock.json`` files
  - click on the 'Process' button
  - view the results. 
  - Notes: if the terminal doesn't give you the URL to access the app type ``http://127.0.0.1:8000/`` into your browser address bar
