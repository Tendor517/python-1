#Bubble sorting(descending) list or logic, developed on 7/8/2021.
while 1==1:
    a=[]
    size=int(input("1.enter the size of the list:"))
    for i in range (0,size):
        val=int(input("enter the number:"))
        a.append(val)
    print("2. the list of marks you  entered is=")
#logic to sort in descending order as below:
    for i in range (size):
        for k in range(-1,-size,-1):
            if a[k]>a[k-1]:
                t=a[k-1]
                a[k-1]=a[k]
                a[k]=t
            print("stepwise decrement",a)
    print("finally the sorted(descending) array or list",a)
    ans=input("4.Do you want to try this again?(y/n)=")
    if ans=="Y" or ans=="y":
        continue
    else:
        break
print("See you soon!")

    
