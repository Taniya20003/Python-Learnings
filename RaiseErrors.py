# Raise errors are raised manually
# If a developer knows that user can mistake then raise errors are used.

num=int(input("Enter any number:"))

if(num<5 or num>9):
    raise ValueError("Not in b/w 5 and 9!")