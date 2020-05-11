# File where classes would be called from time to time in my unit tests as OOP practice

class Burito:

    def add(self,x,y): #declare a function that simply adds two variables
        return x + y

    def sub(self,x,y): #declare a function that subtracts one variable value from another one
        return x - y

    def notSimilar(self,x,y): #declare a function that checks difference between two numbers
        return x is not y
    
    def falseValue(self,x,y): #declare a function that checks the false equality of values
        return x == y
