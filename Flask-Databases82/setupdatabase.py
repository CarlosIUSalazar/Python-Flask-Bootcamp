#In here we setup the database
#This file needs to be in the same location than basic.py
from basic import db, Puppy #basic is basic.py

#creates all the tables - > Transform model class to a database tables
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

#None We should see None before creatring the DB first
#None
print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])

#db.session.add(sam)  --> To add them manually instead of add_all
#db.session.add(frank)

db.session.commit()

