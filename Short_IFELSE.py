# This checks from left to right
# In complex, it firstly checks if condition, if not matched then move to else, else part will be printed if the next if condition meets otherwise else runs

a=7
b=7

print("Hello") if a<b else " "

print ("Yes") if a>b else print("No") if a==b else print("Nottt")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 330
b = 3305
print("A") if a > b else print("=") if a == b else print("B")