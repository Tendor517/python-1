#Multiplication of one to eleven.

a=int(input("1.multiplication table of?(1 to 11):"))
for i in range(1,11) :
    for c in range(1,a+1):
        print(c,"x",i,"=",c*i,end="  ")
        if c==a:
            print()
            
        
