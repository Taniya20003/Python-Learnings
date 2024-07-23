# We can't directlt make any change in the tuple
# We can do this thing indirectly
# Firstly, we have to change the tuple into the list and make the changes and assign the list to that tuple.

tup=(1,2,3,4,5,6,78,9,10,5,5,5,8)
l=list(tup)
l.append(55)
l.pop(4) # 4 is idx
tup=l

print(tup)
print(len(tup))

print(tup.index(78)) # index takes value and returns idx of that element

print(tup.count(5))

# index(element,start,end)

print(tup.index(10,5,8))


