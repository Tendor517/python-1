#fibonacci sequence developed on 1/8/2021.
def fib (a):
    l=[]
    l.append(a)
    #print(l)
    l.append(a+1)
    #print(l)
    count=0
    for i in range (1,num-1):
        d=int(l[count])
        e=int(l[count+1])
        g=d+e
        l.append(g)
        count+=1
    return l
while 1==1:
    a=int(input("1.enter the number from where you want to start the sequence="))
    num=int(input("2.how many number you want in the fibonacci sequence starting from the number you have just chosen before="))
    ans=fib(a)
    print("3.finally our fibonacci sequence is",tuple(ans))
    print("4.there are exactly",len(ans),"numbers in the sequence")
    print("5.sum of all the numbers in this sequencee is",sum(ans))
    say=input("6.Do you want to do this again(y/n)")
    if say=="Y" or say=="y":
        print("okay let's do this again")
        continue
    else:
        print("*********************************************I hope you learned something about fibonacci sequence, Have a nice day*****************************************")
        break




    
