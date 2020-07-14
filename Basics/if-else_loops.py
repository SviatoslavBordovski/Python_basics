#Main goal here is to show how you can work with Python if/else statements and loops

num = 0 #Assign value for 'num' variable

#Lets show the manipulation with 'num' variable:
if num  > 0:
    print('Fantastic!')
elif num == 0:
    print('Number equals zero')
else:
    print('Number is negative')

#Continue  manipulation by declaring the array with data:
num = [1,2,3,4,5]
sum = 0
for var in num:
    sum = sum + var

print('TOTAL IS', sum)

#Another count of an array data but with strings:
fruits = ['Five apples', 'Three oranges', 'Ten grapes']

print('Lets count all the fruits from our array basket (-:')

for count in fruits:
    print(count)
else:
    print('You ate all the fruits! ^_

#Finally, trying show how is it possible to count the numbers in loop until the variable achieves the number and loop finishes:
num = 10
val = 0
x = 1

while x < num: #Loop that gives opportunity to run it until some value will achieve the goal
    val = val + x
    x = x + 1
    print(val, x)
print('Final prompt of "val" number when "x" becomes 10 is: ', val)
