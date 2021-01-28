# List [] ordered | indexed | changeable | duplicates

list_of_cities = ['Tokyo', 'London', 'New York']

print(list_of_cities) #List is printed
print(list_of_cities[2]) #London is an output

#Lets change 'New York' to 'Kiev':
list_of_cities[2] = 'Kiev'
print(list_of_cities)

#You can show data without any brackets by simple loop run:
for val in list_of_cities:
    print(val)
    
print(len(list_of_cities)) #Count number of values in the specified list

list_of_cities.append('Boston') #added Boston at the end
list_of_cities.insert(2, 'Vienna') #inserted city in an array in needed order
list_of_cities.remove('Tokyo') #removed Tokyo from the list
list_of_cities.pop() #removes last element by default
list_of_cities.pop(1) #removes exact value that is selected
del list_of_cities[0] #removes first city in the list (London)
list_of_cities.clear() #makes list of array totally clear

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
