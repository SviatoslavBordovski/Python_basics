def learn(a,b):
    print(a+b)

x = learn(30,30) #We have a value stored to 'x' but it is defined as 'None'

#On this stage x = 'None', let's handle that thing :)

#Quick workaround to make it interactive in the terminal
if x == None:
    x = 60
    print('Good job, "x" is 60 now!')
else:
    print('Never mind')

print('Looks like it is still', x) #Can we double check the value 'x'? Yes, we can!

#Now let's define the values for different variables and see the type of each one
x=70
y=85.0
z=100j

print(type(x)) #returns 'integer' class
print(type(y)) #returns 'float' class
print(type(z)) #returns 'complex' class

#Manipulation with 'x' variable:
x = '   Python is one love   '
print(x[3]) #returns second character of the 'x' string
print(x[3:10]) #returns 6 characters of the first word
print(len(x)) #returns length (number of the charactets) in 'x' string
print(x.lower()) #fully transforms 'x' string to the lowercase characters
print(x.upper()) #fully transforms 'x' string to the uppercase characters
print(x.strip()) #all the manioulations with case sensitivity and spaces are removed
print(x.replace('P', 'Iron P')) #replace characters of the string
print(x.split(',')) #splits words in the string and creates several strings (make sure that you added comma to the string as well)

#Finally, introduce yourself:
print('Enter your name: ')
x=input()
print('Welcome to the Python club, '+x+'!')
