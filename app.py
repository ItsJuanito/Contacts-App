from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

# ~$ py -3 -m venv venv
# ~$ venv\Scripts\activate
# ~$ pip install Flask
# ~$ pip install Flask-SQLAlchemy
# ~$ set FLASK_APP=main.py
# ~$ set FLASK_ENV=development

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50))
    number = db.Column(db.String(20))
    type_of_number = db.Column(db.String(30))
    notes = db.Column(db.String(225))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/add", methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    type_of_number = request.form['type_of_number']
    notes = request.form['notes']

    new_contact = Contact(name=name, email=email, number=number, type_of_number=type_of_number, notes=notes)
    try:
        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for('contacts'))
    except:
        return 'There was an issue adding your contact'



@app.route('/contacts')
def contacts():
    contacts = Contact.query.all() # displays by name [a, b, c, ...]
    print(contacts)
    return render_template('contacts.html', contacts=contacts)

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    contact = Contact.query.get_or_404(id)

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        type_of_number = request.form['type_of_number']
        notes = request.form['notes']
        try:
            db.session.commit()
            return redirect(url_for("contacts"))
        except:
            return 'There was an error trying to edit your contact'
    else:
        return render_template('edit.html', contacts=contact)

@app.route('/delete/<int:id>')
def delete(id):
    contact = Contact.query.filter_by(id=id).first()
    try:
        db.session.delete(contact)
        db.session.commit()
        return redirect(url_for("contacts"))
    except:
        return 'There was an error trying to delete the contact'

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)