# Set {} unordered | unindexed | no duplicates

set_1 = {'Toyota', 'Honda', 'Nissan'}
#print(set_1[1]) - would throw a traceback since it is unindexed and unordered

for x in set_1:
    print(x)
    
#Verify that 'Honda' value exists in set:
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
set_1.discard('Suzuki') #use it instead of 'remove' if you are not sure it was deleted or not to avoid errors

#del set_1

print(set_1) #traceback thrown if 27th row is not commented

#Try to make something interesting with a new set:
set_2 = {'Apples', 24, 37, (3,4,5)}
print(set_2)

#Convert the declared list to a set:
list_1 = [1,2,3,'Vienna','London','Kiev']
print(list_1)
set_3 = set(list_1)
print(set_3)

#Intersting manipulations with sets:
# UNION | INTERSECTION | DIFF | SYMMETRIC DIFF
A = {'A', 'B', 1,2,3}
B = {'B', 'C', 3,4,5}

print(A.union(B)) #All the declared sets are united and same values are merged
print(A | B) #Result of the output is the same

print(A.intersection(B)) #output the values that are the same in both sets
print(A & B) #output the values that are the same in both sets

print(A.difference(B)) #output the values that are different in those sets
print(A - B) #output the values that are different in those sets

print(A.symmetric_difference(B)) #output different values that exist in both sets
print(A ^ B) #output different values that exist in both sets
