#A mini project on the practical mentioned on class 11 textbook at the Page before the context, modified on 3/8/2021...
#similar but second one.
a=int(input("enter the number of terms you want?"))
b=int(input("enter the base number"))
c=0
c+=1
print(c)
for i in range (1,a+1):
    if i%2==0:
        c=c+(b**i)
        print(c)
    if i%2!=0:
        c=c-(b**i)
        print(c)
print("the final result is",c)
#2 similar to this but the third ne

a=int(input("enter the number of terms you want?"))
b=int(input("enter the base number"))
e=0
e+=b
print(e)
for i in range (2,a+1):
    if i%2==0:
        e+=(b**i)/i
    if i%2!=0:
        e-=(b**i)/i
print("the final result is",e)
#3 similar to before but with factorial at denominator(the fourth one)
a=int(input("enter the number of terms you want?"))
b=int(input("enter the base number"))
k=0
k+=b
fact=1
R=1
for i in range (2,a+1):
    R*=fact*i
    if i%2==0:
        k+=(b**i)/R
    if i%2!=0:
        k-=(b**i)/R
print("the final result is",k)


