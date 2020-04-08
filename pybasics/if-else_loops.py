#Main goal here is to show how you can work with Python if/else statements and loops

num = 0 #Assign value for 'num' variable

if num  > 0:
    print('Fantastic!')
elif num == 0:
    print('Number equals zero')
else:
    print('Number is negative')

num = [1,2,3,4,5]
sum=0
for var in num:
    sum=sum+var

print('TOTAL IS', sum)

fruits = ['Five apples', 'Three oranges', 'Ten grapes']

print('Lets count all the fruits from our array basket (-:')

for count in fruits:
    print(count)
else:
    print('You ate all the fruits! ^_^')

num = 10
val = 0
x = 1

while x < num:
    val=val+x
    x=x+1
    print(val, x)
print('Final prompt of "val" number when "x" becomes 10 is: ', val)
