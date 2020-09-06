print(len("hello"))

mystring = "hello world"

print(mystring[-1])

#Slicing
mystring2 = "abcdefghij"

print(mystring2[0:3])

print(mystring2[4:7])

print(mystring2[0:7:3])

print(mystring2[:5])  #lo mismo que[0:5]
print(mystring2[3:])  #lo mismo que 3 en adelante.
print(mystring2[::2])   #Go all the way from beginning to end with step 2
print(mystring2[::])    #print all
print(mystring2[::-1])  #Print the reverse of string

#Concatenate strings
print("hello " + "carlos")

#String methods
print(mystring2.upper())   #To uppercase
print(mystring2.lower())   #To lowercase

print(mystring.split())  #separa espacios en array
print(mystring.split('w')) #separa espacios en la letra w en array (list)

username = "Sammy"
color = "blue"

print("The {} favorite is {}".format(username,color))  #String interpolation?

#Python 3.6 and above:
# f string literals
print(f"The {username} chose {color}")   #f String literals (interpolation) 
