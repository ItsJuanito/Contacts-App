# Contacts-App
This application allows users to create a contact list.
# Master Folder
  - app.py: this is the main file that contains python source code. 
  - contacts.db: this file contains contact database information.
# Templates Folder
  - index.html: this file is the main file to run, contains Python formatted scripts and source code.
  - edit.html: contains the forms and user input to edit a contact.
  - contacts.html: html page that lists all contacts in order in which they were made.
# __Pycache__ Folder
  - cache(stores data for a future repsonse).
# Activate Virtual Enviornment
  Before running the appilcation make sure you have the enviornment files activated.
  (How to activate venv)
  - ~$ venv\Scripts\activate (Windows)
  - ~$ . venv/bin/activate (iOS)
# How to Run
  - ~$ pip install Flask
  - ~$ pip install Flask-SQLAlchemy
  - ~$ set FLASK_APP=app.py
  - ~$ set FLASK_ENV=development
  - ~$ flask run


Demo App: https://contacts-flask-app.herokuapp.com/
