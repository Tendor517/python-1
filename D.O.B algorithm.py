#To calculate the day of your date of birth..29/5/2021(developed).
mon={1:6,2:2,3:2,4:5,5:0,6:3,7:5,8:1,9:4,10:6,11:2,12:4}
year={1900:1,1910:6,1920:5,1930:3,1940:2,1950:0,1960:6,1970:4,1980:3,1990:1,2000:0,2010:5}
even={0:1,1:0,2:0,3:0,4:0,5:1,6:1,7:1,8:1,9:2}
odd={0:0,1:0,2:0,3:1,4:1,5:1,6:1,7:1,8:2,9:2}
name=input("1.Your Name:")
Year=int(input("2.enter the year of your birth:"))
month=int(input("3.enter the month of your birth in numbers;"))
date=int(input("4.enter the date of your birth in numbers:"))
def find(x,y,z):     #x=date, y=month, z=year
    c=x+mon[y]
    e,g=str(z),str(z)
    g=int(g)-int(g[-1])
    c=c+year[g]
    c=c+int(e[-1])
    if int(e[-2])%2==0:
        c+=even[int(e[-1])]
        w=c//7
        w*=7
        c-=w
    else:
        c+=odd[int(e[-1])]
        w=c//7
        w*=7
        c-=w
    if z%4==0:
        if z%100==0:
            if z%400==0:
                print("it is  leap year")
                c-=1
            else:
                print("it is not a leap year")
        elif z%100!=0:
            print("it is a leap year")
            c-=1
    else:
        print("#it is not a leap year")
    return c
a=find(date,month,Year)
days={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
print("5.The day of your's date  of birth is=",days[int(a)])
        
    
