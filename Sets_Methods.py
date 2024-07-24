s1={3,4,2}
s2={9,8,7}

# Union returns a new set

print(s1.union(s2))
s1.update(s2)
print(s1)

# Intersection returns a new set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)

# Symmmetric_Difference returns new set.
# It keeps those items in the set that are not common in both the sets.

c1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
c2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
c3 = c1.symmetric_difference(c2)
print(c3)

cc1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cc2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cc1.symmetric_difference_update(cc2)
print(cc1)

# Difference returns new set.
# It is just like subtraction

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities.difference_update(cities2)
print(cities)

# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

# Nothing match = True otherwise False

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo2"}
print(cities.isdisjoint(cities2))

# issuperset()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi","Kabul"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid","Kabul"}
print(cities.issuperset(cities3))

# issubset()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# remove() and discard()

# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Tokyo")
print(cities)

# pop()
# We generally don't use because it popped the last item from the set. And we don't have any idea about the last item as set is unordered.
# But we can store the pop item in a variable

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del
# del is not a method, rather it is a keyword which deletes the set entirely.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)

# clear()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

