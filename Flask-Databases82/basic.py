import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

## Create a SQLite DB ##
basedir = os.path.abspath(os.path.dirname(__file__))  #This file variable is set to the name of the actual file.  Is set to basic.py essentially.  And then we want to get the directory name of basic.py   And then you want the absolute path of this file and directory name.
print(basedir)  #in this case is /Users/Carlos/Dropbox/CODECHRYSALIS/zPOST BOOTCAMP PROJECTS/UDEMY/Python and Flask Bootcamp/Python-Flask-Bootcamp/Flask-Databases82

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sq')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
## End Creation of DB

#### DB Model Description ###
class Puppy(db.Model):

    __tablename__ = 'puppies' #this overrides the default table name to puppies

    id = db.Column(db.Integer,primary_key=True)  #is is a column that is primary key as well.
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):     #Id is auto passed so no need to type it in here
        self.name = name
        self.age = age

    def __repr__(self):  #Gives you the string representation of the object, so you can print it out.
        return f"Puppy {self.name} is {self.age} years old"




