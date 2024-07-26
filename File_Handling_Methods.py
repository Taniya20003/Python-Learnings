# readline() method helps to read the lines of the file sequencially until the iterator comes to an end

# The specialty of Python readlines() function is that it reads all the contents from the given file and saves the output in a list.

f=open('myfile2.txt','r')
# l=print(f.readlines())
# print(l) ['56,45,62\n', '12,13,14\n', '1,2,3']
# Therefore, there is no extra line in the last iteration.

i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]

    print(f"Marks of student {i} in maths:",m1)
    print(f"Marks of student {i} in Eng:",m2)
    print(f"Marks of student {i} in SST:",m3)
    print(line)

f.close()


# writelines()

f=open('myfile1.txt','w')
l=['list 1\n','list 2\n','list 3\n']
f.writelines(l)
f.close()

# If want to add a lot of \n in the string then we have to use loop

f=open('myfile1.txt','w')

# having too much data to be written in a file
lines=['line 1', 'line 2','line 3']

for i in lines:
    f.write(i,'\n')

f.close() 

