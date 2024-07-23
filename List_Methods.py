# All changes are done on original list
# Therefore, as a fresher try to use copy() 
# l=m this m is refering to same address of l.

l=[45,78,97,67,90,100,20,34]

print(l)

l.append(70)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(100))
print(l.count(1))

# m=l X

m=l.copy()

m.append(300)
m.append(400)
m.append(500)
print(m)

n=[800,12,38]
l.extend(n)
print(l)

p=[499,300,23]
q=[23,98,409]

u=p+q
print(u)