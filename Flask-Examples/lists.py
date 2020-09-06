mylist = ['a','b','c','d','e','f']
mylist2 = [100,"Hey",3.3]
mylista = [0,1,2]
mylistb = [3,4,5]
mylistc = [6,7,8]

print(len(mylist))

print(mylist[1])
mylist.append('z')      #.append is like .push

mylist.insert(0,'X')    #inserts X at 0 position

print(mylist)

mylist.pop(0)       #Pop item at index 0.  It returns the popped item. pop() pop the end of the list by default.

print(mylist)

mega_list = [mylista,mylistb,mylistc]  #Nested list

print(mega_list[2][1])  #Prints 7. Stacked indexing with a nested list
