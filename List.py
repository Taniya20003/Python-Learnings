# List are just like arrays in cpp with some differences
# In Python, list is dynamic.
# Indexing is same as array.
# It can store values of different datatypes and a list can contain another list inside it.
# We can do slicing here.
# [] brackets are used here.
# List is changeable. Everything happens on original until the copy is made manually.

marks=[20,30,40,50,60]

print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

list1=["Hello","Taniya","How","are","you","?",1,2,3,4,5,6]

print(list1[1:8])
print(list1[:])
print(list1[1:-6])
# 1:len(list1)-6= 1:12-6=[1:6]


if 1 in list1:
    print("Yes")
else:
    print("No")  

if "Ta" in "ATTA":
    print("Right!")

# We can jump by number in list using slicing

print(list1[1:6])
print(list1[2:9])
print(list1[2:9:2]) 

# List Comprehension: Making new list by iterating the existing list
# We start from last and comes to the start

lst=[i+i for i in list1]
print(lst)
# ['HelloHello', 'TaniyaTaniya', 'HowHow', 'areare', 'youyou', '??', 2, 4, 6, 8, 10, 12]
# i+i is the operation we do on the i elements

lst1=[i*i for i in range(10)]
print(lst1)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

lst2=[i*i for i in range(10) if i%2==0]
print(lst2)
[0, 4, 16, 36, 64]
