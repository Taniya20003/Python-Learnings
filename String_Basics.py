# Strings are the collections of characters like a, b, c,d so on.
# We fetch the characters from the String just like an array.
# It's an array containing the characters collection.
# Use single or double quotes as per the requirement, language is flexible here.

a="Hello"
b="Hey"
anothername="London"
Another="India"

c='''Hey! I am Taniya Sharma. 
I am student of University. 
I am pursuing my post graduate degree.'''

print(c)

d="Hello everyone there! This is Taniya's Laptop. The brand of the laptop is \"DELL\"."

e="Hello everyone there! This is Taniya's Laptop. The brand of the laptop is 'DELL'."

print(e)

print(d)

print(a[0])
print(b[2])

for characters in anothername:
    print(characters)


# Slicing in string is taking out the required part
# string_variable[start:end] 
# if end is not specified it takes len of the string value.
# If start is not specified it takes 0 (by default)
# if negative values are given then subtract the given val from len.

p="Happy Sunday"

plen=len(p)

print(plen)
print(p[0:5])
print(p[0:])
print(p[:10])
print(p[-1:-7])
#12-1=11 and 12-7=5 therefore p[11,5] which is not valid and no o/p will be generated. The blank line will come.

print(p[-7:-1])
# 12-7=5 and 12-1=11 therefore p[5,11]

