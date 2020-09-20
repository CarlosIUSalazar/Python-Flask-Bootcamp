#MODELS.PY
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db) #esta linea es diferente que el tutorial necesitas poner migrate = 

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    #ONE TO MANY
    #Puppy to Many Toys...  backref means also related to puppy.  Lazy specified how items should be loading.  There's also other parameters like: select, immediate, join, subquery etc.
    toys = db.relationship('Toy',backref='puppy',lazy='dynamic')
    # ONE TO ONE
    # ONE PUPPY ---> ONE OWNER
    owner = db.relationship('Owner',backref='puppy',uselist=False) #uselist is true by default which makes sense for one to many relationship. but here its just one to one so we dont need a list of owners so we put false.

    def __init__(self,name)
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet!"
    
    def report_toys(self):
        print("Here are my toys:")
        for you in self.toys:   #because uselist by default is true and gives a list
            print(toy.item_name)  #item_name is an attribute of Toy class



class Toy(db.Model):
    
    __tablename__ = 'toys'

    id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))  #puppies.id viene de linea 19 and 21

    def __init__(self,item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    #one to one
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id