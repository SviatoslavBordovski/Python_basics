# Dictionary {K:V} unordered | changeable | indexed | no duplicates

#Declare a test dictionary:
dict_1 = {
          'class': 'Golf',
          'name': 'Volkswagen',
          'trim': '1.6 TDI Variant'
         }

print(dict_1) #execute the declared dictionary
print(dict_1['name']) #get the chosen value from dictionary
print(dict_1.get('name')) #get the chosen value from dictionary
print(dict_1.values()) #dictionary values are executed only

#How to execute a name of the value in dictionary:
for x in dict_1:
    print(x)
    
#How to execute the values in dictionary with a loop:
for x in dict_1:
    print(dict_1[x])
    
#Execute the dictionary fully:
for x,y in dict_1.items():
    print(x,y)

#Change the existing value in dictionary:
dict_1['name'] = 'Mercedes'
print(dict_1)

#Add a new value to the dictionary:
dict_1['color'] = 'Yellow'
print(dict_1)

#Remove previously added to the dictionary color:
dict_1.pop('color')
print(dict_1)

#Remove the last item/value (trim) in the dictionary:
dict_1.popitem()
print(dict_1)

#Remove the particular value that you want:
del dict_1['class']
print(dict_1)

#Remove all the values in the dictionary, so the program returns an empty dictionary:
dict_1.clear()
print(dict_1)

#Delete the dictionary fully:
del(dict_1)
print(dict_1) #returns a traceback since it was deleted/not defined
