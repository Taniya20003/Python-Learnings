# open() -> to open the file and read it
# read ('r') is by default
# write() -> to write inside the file, if the file is not created then it creates. If we write inside the existing written file then it erases first then writes.
# Therefore, it is recommended to use append()
# Always close the opened file
# Alternative is also there which closes the file automatically.

f=open("myfile1.txt",'r')
print(f.read())

f1=open("myfile2.txt",'w')
f1.write("No way!")

f2=open('myfile1.txt','w')
f2.write("Stay Calm, Stay Happy!")
f2.close()

f1=open('myfile1.txt')
print(f1.read())

f1=open('myfile1.txt','a')
f1.write(" Okay! Move on.")

f1=open('myfile1.txt')
print(f1.read())

f1.close()

with open("myfile1.txt",'r') as f:
    print("_______________")
    print(f.read())
