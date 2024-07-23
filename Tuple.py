# Tuples are immutable
# if there is one element in the tuple then put a comma is imp

tup=(1,)
print(type(tup),tup)

tup1=(1,2,3,4,5,6,"I","am","a","Student",True)

print(type(tup1),tup1)
print(tup1[6])

# Can't do this
# tup1[4]="Yes"

print(tup1[1:5])