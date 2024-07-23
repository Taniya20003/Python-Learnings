for i in range(20):
    if(i==5 or i==10 or i==15):
        print("This is not included")
        continue

    print(i)

a=0
while True:

    if(a==100):
        break  
    
    print(a)    
    a=a+1  