# They are only 2 loops in python for and while.
# do while is not there
# we can use while else loop. The else statement will run after while loop ends
# While loop requires initialisation of variable
# In general, for loop is used but in complex cases the while case is preferable.

name="Taniya"
for i in name:
    print(i)

list1=["Red","Pink","Green","Orange"]
for color in list1:
    print(color)

    for c in color:
        print(c)

# By default 0 value is there in k.
# It will run 1 less so if there is 5 it will run from 0 to 4.
# It increases automatically.

for k in range(5):
    print(k)  

for k in range(5):
    print(k+1)    

for k in range(1,12,3):
    print(k)        


i=1
while(i<=38):
    i=int(input("Enter number:"))
    print(i)
    
print("Loop exit")   

a=1
while(a<=18):
    a=int(input("Enter number:"))
    print(a)
else:
    print("Loop no more. Stay Chill!")   


# This code tells how to convert the while loop into do while by using while, if and break.

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break