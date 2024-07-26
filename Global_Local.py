x=3

def sum(a):
    x=4
    print(x+a)

print(x)
sum(2)   

# To change the global variable inside functio.

def add(r):
    global x
    x=7
    print(x+r)

add(3)
print(x)    