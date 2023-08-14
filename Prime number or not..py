n=int(input("1.enter the numebr:"))
count=0
if n==0 or n==1:
        print("#this number is neither prime nor composite")
for i in range(1,n+1):
    if n%i==0:
        count+=1
    if count>2:
            print("#The number entered is an composite number")
            break
    elif count==2:
            print("#the number entered is an prime number")
            break
