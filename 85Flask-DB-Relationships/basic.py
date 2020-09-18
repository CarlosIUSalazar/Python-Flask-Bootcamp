#BASIC.PY
# CREATE ENTRIES INTO THE TABLES

from models import db,Puppy,Owner,Toy

#  CREATING 2 PUPPIES
rufus = Puppy('Rufus')
fido = Puppy('Fido')

#Add Puppies to DB
db.session.add_all([rufus,fido])
db.session.commit()

# Check!
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()   #or .all()  or .all()[0]
print(rufus)
#CREATE OWNER OBJECT
jose = Owner('Jose',rufus.id)  #rufus.id is rufus created in line 17 with which is the puppy created in line 7

#GIVE RUFUS SOME TOYS
toy1 = Toy('Crew Toy',rufus.id)
toy2 = Toy('Ball',rufus.id)

#commit changes
db.session.add_all([jose,toy1,toy2])
db.session.commit()

#GRAB RUFUS AFTER THOSE ADDITIONS
rufus = Puppy.query.filter_by(name='Rugus').first()
print(rufus)

rufus.report_toys()
