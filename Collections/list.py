# List [] ordered | indexed | changeable | duplicates

list_of_cities = ['Tokyo', 'London', 'New York']

print(list_of_cities) #List is fully printed
print(list_of_cities[2]) #London is an output

#Lets change the New York to Kiev:
list_of_cities[2] = 'Kiev'
print(list_of_cities)

#You can show the data without any brackets by simple loop run:
for val in list_of_cities:
    print(val)
    
print(len(list_of_cities)) #Count the number of values in the list

list_of_cities.append('Boston') #added Boston at the end
list_of_cities.insert(2, 'Vienna') #inserted city in the array in order that you need
list_of_cities.remove('Tokyo') #removed Tokyo from the list
list_of_cities.pop() #removes the last element by default
list_of_cities.pop(1) #removes the exact value that is selected
del list_of_cities[0] #removes first city in the list (London)
list_of_cities.clear() #makes the list of array totally clear

#Execute the list after changes:
print(list_of_cities)

#Declare a list of fruits in array:
fruits = ['apples', 'oranges', 'cherry']
print(fruits)
fruits.reverse()
print(fruits)

#Declare different types of lists in the arrays:
random_list_2019 = ['vegetables', 1, 2, 3.0]
random_list_2020 = ['vegetables', [1, 2, 3], ['x', 'y', 'z']]
print(random_list_2020[1][2]) #access to the second statement list and third value which is 3
