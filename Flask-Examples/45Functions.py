#Functions

def name_of_function(name):  #by convention names sjhould be lowercase
    '''
    Docstring explains function
    '''
    print("Hello " + name)

name_of_function("Jose")


def report_person():
    print("reporting person!")


report_person()

def report_person2(name='BLANK'):#Blank is default parameter
    print("reporting " + name)

report_person2()


#FUNCTIONS PART 2 VIDEO 46
#Max and Min

max((2,3))  #returns 3
print(max([3,5,4,3,6,7,8,6,54,4,4,5,6]))
print(min([3,4,5,56,6,5,4,4,3]))

#ENUMERATE
mylist = ['a','b','c'];
for letter in mylist:
    print(letter)


index = 0
for letter in mylist:
    print(letter)
    print('is at index: {}'.format(index))
    index = index + 1;

#OR you can use ennumerate      #prints (0, 'a') (1, 'b') (2, 'c')
for item in enumerate(mylist):
    print(item)

for index,item in enumerate(mylist):  #This unpacks the tuple.
    print(item)
    print(f"is at index {index}")
    print(' ')


#JOIN
mylist = ['a','b','c','d']
print(''.join(mylist))          #prints abcd
print('--'.join(mylist))        #prints a--b--c--d
print('-x-'.join(mylist))       #prints a-x-b-x-c-x-d


#PROBELM :  Wite a function tha returns a boolean indicating if the word secret is in a strings
def secret_check(mystring):
    if 'secret' in mystring:
        return True
    else:
        return False

#OR
def secret_check2(mystring):
    return 'secret' in mystring

print(secret_check('simple'))       #returns False
print(secret_check('this is a secret')) #returns true


#PROBLE 2
#Create a code maker function. This function will take in a string name and replace any vowels with the letter x.
def code_maker(mystring):

    output = list(mystring)
    print(output)
    for index,letter in enumerate(mystring):
        for vowel in 'aeiou':
            if letter.lower()==vowel:
                print(letter)
                output[index] = 'x'

    output = ''.join(output)
    return output


print(code_maker('Sammy'))


#THE SUM FUNCTION
print(sum([1,2,3,4]))      #returns 10
