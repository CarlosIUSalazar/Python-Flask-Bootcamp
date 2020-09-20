import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #pip install Flask-Migrate

## Create a SQLite DB ##
basedir = os.path.abspath(os.path.dirname(__file__))  #This file variable is set to the name of the actual file.  Is set to basic.py essentially.  And then we want to get the directory name of basic.py   And then you want the absolute path of this file and directory name.
print(basedir)  #in this case is /Users/Carlos/Dropbox/CODECHRYSALIS/zPOST BOOTCAMP PROJECTS/UDEMY/Python and Flask Bootcamp/Python-Flask-Bootcamp/Flask-Databases82

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sq')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
## End Creation of DB

migrate = Migrate(app,db) #Connect our app with db.  

#remember to use export FLASK_APP=basic.py
# then flask db init
# flask db migrate -m "create puppy table"    This creates a migration file and this way you can leave comments for each migration
# flask db upgrade   This finally apply the migration to the database

#### DB Model Description ###
class Puppy(db.Model):

    __tablename__ = 'puppies' #this overrides the default table name to puppies

    id = db.Column(db.Integer,primary_key=True)  #is is a column that is primary key as well.
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)    #this column was added after the first db init so we need a migratio se below **


    def __init__(self,name,age):     #Id is auto passed so no need to type it in here
        self.name = name
        self.age = age
        self.breed = breed #this column was added after the first db init so we need a migratio se below **

    def __repr__(self):  #Gives you the string representation of the object, so you can print it out.
        return f"Puppy {self.name} is {self.age} years old"


# ** flask db migrate -m "Added breed column"
#    flask db upgrade


