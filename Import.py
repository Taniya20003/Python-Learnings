# import in python is the process of using loading the fucntions and variables of that module.

import math
print(math.sqrt(9))

import math as m
print(m.ceil(4.6))

from math import sqrt,pi
print(sqrt(4)*10)

# Not recommended
# from math import *

print(dir(math))