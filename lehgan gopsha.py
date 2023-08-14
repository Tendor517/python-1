import random
c=int(input("Enter the number of works"))
num=int(input("Enter the number of workers"))
workname=[]
names=[]
for h in range (num):
    ming=input("Enter the name of the worker:")
    names.append(ming)
for i in range (c):
    name=input("Enter the name of the work:")
    workname.append(name)
amount=int(input("Enter the number of workers in each work:"))
l=[]
final={}
for j in workname:
    for k in range(amount):
        ran=random.choice(names)
        l.append(ran)
        names.remove(ran)
        if k==(amount-1):
            print(j,"has these workers=",l)
            l.clear()
            break

    
    
    
    


    
    
    
