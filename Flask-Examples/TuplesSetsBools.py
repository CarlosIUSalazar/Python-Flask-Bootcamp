# Tuples are the same as lists but they are immutable. Once an element is
# inside a tuple it cannot be reasigned.

#Sets ar eunordered collections of unique elements. There can only be one representative of the same object

#Booleans True or False

#tuples
t = (1,2,3)
mylist = [1,2,3]
mylist[0] = 'NEW'
#t[0] = 'NEW'    #Returns an error.  Eg calendar dates don't change etc.
print(t)
print(t[0])

#Sets
x = set()
print(x)
x.add(1)
print(x)
x.add(2)
x.add(3)
print(x)
x.add(3)
x.add(3)
print(x)    #Doesnt return an error just {1,2,3}. So you can get individual values of a set easily.

#E.G. use case
mylist5 = [1,54,3,3,45,5,3,1,3,3,3,4,1,3,3,55,3,3,1,3,4]
print(set(mylist5)) #Prints {1, 3, 4, 5, 45, 54, 55}


#Booleans
a = True #Capital T must
b = False
c = None #Es como null, place holder for an object you dont want to reassign yet.
print(1>2)
print(1==1)
