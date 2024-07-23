a=int(input("Enter your age:"))
if(a>18):
    print("You are eligible to vote")
else:
    print("Go to your home child!")


num1=int(input("Enter the number:"))

if(num1<-5):
    print("Your number is negative.")
elif(num1>0):
    print("Your number is positive just like you.")
elif(num1==0):
    print("This number is neutral.")
else:
    print("You are special.")  


# Good Morning Sir

import time

timestramp=time.strftime('%H:%M:%S')

print(timestramp)

hours=int(time.strftime('%H'))

if(hours>12 and hours<16 ):
    print("Good afternoon")
elif(hours<12 and hours>=1):
    print("Good morning")
elif(hours>=16 and hours<=19):
    print("Good evening") 
else:
    print("Good night") 