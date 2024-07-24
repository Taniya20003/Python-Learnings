# When an error occurs we use try and except blocks to handle the.
# Whatever we thinks can throw the error we try to put them in try except blocks.
# This helps us to not to terminate the program and can run afterwards code easily.
# Except block shows the error or the manually written code.
# We can use multiple except.

try:
    num=int(input("Enter any number:"))
    sum=9+num
    print(sum)
except Exception as e:
    print(e)   

print("Learning try and except")
print("Good day!")    


try:
    num=int(input("Enter any number:"))
    m=9*num
    print(m)
except:
    print("Invalid o/p")   

print("Learning try and except")
print("Good day!")  

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")


# Finally keyword is used that is always executed whatever the condition is returned.
# It is needed like return statements are written then also finally runs but normal print doesn't
# It also helps in closing files if written inside the finally block.

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)