from basic import db, Puppy

# CREATES ALL THE TABLES Model--> Db Table
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])  #or add individually with db.session.add(sam)

db.session.commit()

print(sam.id)
print(frank.id)
