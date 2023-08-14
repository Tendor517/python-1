#To check if the number entered is an palindrome or not?
#for example 23432 and 232 and 454 are palindrome's
#while 3435 and 8687 are not palindrome.
a=0
def fun():
    global a
    a=input("1.enter the number or the word=")
    return a
while 1==1:
    u=fun()
    if len(u)%2==0:
        g=u[0:len(u)//2]
        k=u[-1:(-len(u)//2)-(1):-1]
        count=0
        for i in g:
            if i==k[count]:
                count+=1
                if i==g[-1]:
                    print(a,"is an palindrome")
                    e=input("thanks, if you want to try again then type yes else no:")
                    if e=="yes" or e=="Yes" or e=="YES":
                        continue
                    else:
                        break
                    
            else:
                print(a,"is not an palindrome")
                e=input("thanks, if you want to try again then type yes else no:")
                if e=="yes" or e=="Yes" or e=="YES":
                    continue
                else:
                    break
    if len(u)%2!=0:
        g=u[0:len(u)//2]
        k=u[-1:(-len(u)//2):-1]
        count=0
        for i in g:
            if i==k[count]:
                count+=1
                if i==g[-1]:
                    print(a,"is an palindrome")
                    e=input("thanks, if you want to try again then type yes else no:")
                    if e=="yes" or e=="Yes" or e=="YES":
                        continue
                    else:
                        break
            else:
                print(a,"is not an palindrome")
                e=input("thanks, if you want to try again then type yes else no:")
                if e=="yes" or e=="Yes" or e=="YES":
                    continue
                else:
                    break
print("thank You")
'''#A short program to check whether the input is an palindrome or not.
a=input("1.enter a string or number to check whether it's a palindrome or not:")
def doit():
    a=input("1.enter a string or number to check whether it's a palindrome or not:")
while True:
    if len(a)==0:
        print("plz enter again")
        doit()
    if a==a[::-1]:
        print(a,"is a palindrome")
    else:
        print(a,"is not a palindrome")
'''

        
    
        
    
        
    


