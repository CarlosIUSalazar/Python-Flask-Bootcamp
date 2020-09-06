d = {'key1':'value1','key2':'value2'}
print(d)
print(d['key1'])        #en vez de d.key1

salaries = {'John':20,'Sally':30,'Sammy':15}
salaries['Cindy'] = 100     #Adds Cindy to the dictionary
salaries['John'] = salaries['John'] + 40        #John salary increases by 40
print(salaries['John'])     #Prints 60


people = {'John':[1,2,3],'Sally':[40,10,30]}
print(people['Sally'][0])       #prints 40

dudes = {'John':{'salary':10,'age':30}}
print(dudes['John']['salary'])  #Prints 10

d = {'k1':10,'k2':20,'k3':30}
print(d.keys())     #print keys
print(d.values())   #print values
print(d.items())    #prints key value pairs (tuples)
