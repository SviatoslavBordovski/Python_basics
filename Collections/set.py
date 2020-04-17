# Set {} unordered | unindexed |

set_1 = {'Toyota', 'Honda', 'Nissan'}
#print(set_1[1]) - would throw a traceback since it is unindexed and unordered

for x in set_1:
    print(x)
    
#Verify that Honda exists in set:
print('Honda' in set_1) #output is True or False

set_1.add('Subaru') #added single element, always randomly
print(set_1)
set_1.update(['Mazda', 'Suzuki', 'Daihatsu']) #added multiple elements, always randomly
print(set_1)

#Count the values in set:
print(len(set_1))

#Remove something added:
set_1.remove('Suzuki') #removes the selected value of set
print(set_1)
set_1.discard('Nissmo') #removes the selected value of set (reusable)
print(set_1)
set_1.discard('Suzuki') #use instead of 'remove' if you you are not sure it was deleted or not to avoid errors

#del set_1

print(set_1) #traceback thrown if 27th row is not commented

set_2 = {'Apples', 24, 37, (3,4,5)}
print(set_2)
