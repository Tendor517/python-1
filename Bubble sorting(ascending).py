#bubble sorting(ascending) list or array logic, developed on 5/8/2021.
while 1==1:
    a=[]
    size=int(input("1.enter the size of the list"))
    for i in range (0,size):
        val=int(input("enter the elements="))
        a.append(val)
    print("2.the list you entered is=",a)
#logic to sort in ascending order as below:
    for j in range(size):
        for k in range(size-1):
            if a[k]>a[k+1]:
                t=a[k+1]
                a[k+1]=a[k]
                a[k]=t
            print("stepwise increment",a)
    print("3.finally the sorted(ascending) array or list is=",a)
    ans=input("4.Do you want to try this again?(y/n)=")
    if ans=="Y" or ans=="y":
        continue
    else:
        break
print("See you soon again")
