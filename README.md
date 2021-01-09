# Contacts-App
This application creates a contact list.
# Master Folder
  - app.py: this is the main file that contains python source code. 
  - db.sqlite: this file contains the database information and all the attributes.
# Templates Folder
  - base.html: this file is the main file to run, contains Python formatted scripts and source code.
# __Pycache__ Folder
  - cache(stores data for a future repsonse).
# Activate venv
  Before running the appilcation make sure you have the enviornment files activated.
  (How to activate venv)
  - ~$ venv\Scripts\activate (Windows)
  - ~$ . venv/bin/activate (iOS)
# How to Run
  - ~$ pip install Flask
  - ~$ pip install Flask-SQLAlchemy
  - ~$ set FLASK_APP=main.py
  - ~$ set FLASK_ENV=development
  - ~$ flask run
Demo App: https://contacts-flask-app.herokuapp.com/contacts
