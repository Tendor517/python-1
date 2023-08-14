#Addition only calculator.like=1+2+3..so on..dveloped on 11/6/2021.
def fun():
    a=0
    a=input("1.enter the numbers you want to add=")
    return a
while 1==1:
    a=fun()
    g=a.split("+")
    c=0
    for i in g:
        c+=int(i)
    print("2.the sum of",a,"is=",c)
    e=input("Want to try it one more time?; Yes or no =")
    if e=="yes" or e=="Yes" or e=="YES":
            continue
    else:
        print("okay then have a wonderful day, Bye")
        break
