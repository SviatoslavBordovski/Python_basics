class UnoMomento:
    ''' Methods are functions defined inside the body of a class. They are used to define the behaviors of an object. '''
    #This is an example of the object description that is named "UnoMomento".
    
    realname = 'Sviatoslav'
    
    #Class functions that begins with double underscore (__) are called special functions as they have special meaning:
    def __init__(self, nickname, age): #This type of function is also called 'constructors' in OOP. We normally use it to initialize all the variables.
        self.nickname = nickname
        self.age = age

    def sum(self, x, y):
        print(x + y)

#Manipulations using the defined data with functions inside of class:
Kyle = UnoMomento('Billy', 33)
realage = str(20) #convert to a string to make the value of the same type with a text
passage = str(Kyle.age) #once again the same operation
print(type(realage)) #type of the 'realage' variable
print(type(passage)) #type of the 'realage' variable
print("Kyle's real name is " + Kyle.realname)
print("Kyle's nickname is " + Kyle.nickname)
print("Kyle's Passport age is " + passage)
print("Application age of Kyle is " + realage)

Kyle.sum(20,9) #access the function inside of the class

#Function remove from the 'UnoMomemto' object:
del UnoMomento.sum
print(UnoMomento.sum) #Traceback: class UnoMomento has no attribute 'sum'
