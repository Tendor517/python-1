a={}
num=int(input("1.enter the number of students to be counted in the marksheet:"))
for i in range(1,num+1):
    name=input("enter the name of the student:")
    mark=int(input("enter the marks:"))
    a[name]=mark
l=list(a.values())
#print(l)
for i in range (len(l)):
    for k in range(-1,-len(l),-1):
        if l[k]>l[k-1]:
            t=l[k-1]
            l[k-1]=l[k]
            l[k]=t
#print(l)
z={}
for i in l:
    for k in list(a.keys()):
        if a[k]==i:
            z[k]=i
        else:
            continue
pos=z.items()
count=1
print("*****Students academia 2021-2022*****")
for key,val in pos:
    if count<4:
        print(count,".",key,"=",val,end="           #")
        print(count,"position",key,"=",val,"marks")
        count+=1
    else:
        print(count,".",key,"=",val,"marks")
        count+=1
        
            



