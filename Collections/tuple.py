# Tuple () ordered | indexed | unchangeable | duplicates

#Tuple manipulations:
tuple_1 = ('Apples', 'Bananas', 'Grapes')
print(tuple_1)
print(tuple_1[1]) #Executed second in the list of tuple_1
print(tuple_1[-1]) #Executed first from the end
print(tuple_1[0:2]) #Executed selected data range of the tuple_1

#It is easy to execute the tuple using loop:
for fruit in tuple_1:
    print(fruit)

print(len(tuple_1)) #Count of data values in the tuple

#It is time to walk through the new tuple and change something there:
tuple_2 = ('Oranges', (1,5,10), ['Ford', 'Toyota', 'Honda'])
print(tuple_2)
print(tuple_2[2][0]) #Executed 'Ford' value

tuple_2[2][0] = 'Nissan' #We are replacing Ford in the tuple_2
print(tuple_2)

print('Bananas' in tuple_1) #output would give us True
print('Cherry' in tuple_1) #output would give us False

#Errors or limitations of tuple:
tuple_1[3] = 'Cherry' #it is not possible to add/assign new value to tuple
del tuple_1[2] #impossible to delete particular value from the tuple
del tuple_1 #however, it is allowed to delete the existing tuple fully
