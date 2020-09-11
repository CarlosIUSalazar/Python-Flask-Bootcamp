import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #pip install Flask-Migrate

basedir = os.path.abspath(os.path.dirname(__file__)) #__file__ when a module is loaded in python this file variable is built in and is set to the name of the actual file.  __file__ will be set automatically to the name of the file, in this case basic.py.  Then we get the directoryname from where the file is.
print(basedir) #To see the entire base directory, where we want to build the database.ArithmeticError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')  #sets the database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #we dont want to track every single modification for now. By default is True.

db = SQLAlchemy(app)

#lines 5 - 13 sets up the DB
Migrate(app,db) #this connects your application to your database to add migration capabilities
#input in terminal:  export FLASK_APP=basic.py   (set instead of export in Windows)
#input in terminal: flask db init   (this creates the migrations folder)
#input in terminal: flask db migrate -m "created puppy table"
#input in terminal: flask db upgrade    this runs the migrations

# flask db migrate -m "added breed column"   after adding new column in this basic.py code
# flask db upgrade     this runs the new migration and adds the breed column
##############################
class Puppy(db.Model):

    #MANUAL TABLE NAME CHOICE!
    __tablename__= 'puppies'
    
    #CREATE COLUMNS
    id = db.Column(db.Integer, primary_key=True) #whithin the puppy class which is a model we have an attribute called id and we're setting it qual to a column and the first argument is of time integer, and primary key means is the unique identifier for the actual rows. 
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    #now we add a new column
    breed = db.Column(db.Text)

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        #added breed column for migration
        self.breed = breed

    def __repr__(self): #gives you the string representation of the object. If you want to print out a row of the column, whithout this line it doesnt work.
        return f"Puppy {self.name} is {self.age} year/s old"

    



