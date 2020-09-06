seq = [1,2,3,4,5]
mystring = 'hello'
salaries = {'John':10,'Sally':20,'Lisa':50}

for jellyfish in seq:   #jellyfish can be any word (num, item etc)
    #print(item**2)
    print('hello')

seq2 = 'hello'

for char in mystring:
    print(char)

for employee in salaries:
    #print(employee)            #print names
    print(salaries[employee])   #print salaries


for employee in salaries:
    print(employee)
    print("has salary of:")
    print(salaries[employee])
    print(' ')


#TUPLE UNPACKING
mypairs = [('a',1),('b',2),('c',3)]
for (letter,number) in mypairs:          #unpacking the tuple
    print(letter)
    print(number)


#WHILE LOOPS
i = 1
while i < 5:
    print(f"i is currently: {i}")
    i = i+1


#RANGE FUNCTION
for x in range(0,11,2):     #(start,end,step) can leave step out.
    print(x)

result = list(range(0,11,2))
print(result)               #Prints [0, 2, 4, 6, 8, 10]


#Is letter s in this string?
print('s' in 'lkjhlkjhasdlfkjh')        #Prints True
print(1 in [1,2,3])                   #True
