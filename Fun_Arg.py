# There are 4 types of fucntions arguement we can pass
# Default, Required, Keyword, Variable length arguements

# 1. Default Arg

def Yourname(fname="John", mname="Annie",lname="Kaju"):
    print(fname+" "+mname+" "+lname)

Yourname("ABC","XYZ")   

# 2. Keyword Arg

def Game(fname="John", mname="Annie",lname="Kaju"):
    print(fname," ",mname," ",lname)

Game(fname="YES",lname="No",mname="Go")

# 3. Required Arg

def name(fname, mname, lname="123"):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")

# 4. Variable length Arg

