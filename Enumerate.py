# Enumerate is in-built function
# It helps to apply the loop over sequence data structures like list, tuple etc
# It gets the index and value at same time
# The index starts from 0 but we can change as per requirements.
# Always write index first then data structure

marks=[10,20,30,40,50,60,41,34,97]

for index,m in enumerate(marks):
    print(index," ",m)

for index,m in enumerate(marks,start=1):
    print(index," ",m)    

for index,m in enumerate(marks):
    if(index==2):
        print("Its 30!")
    else:
        print(m)    