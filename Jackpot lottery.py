#interactive Lottery Game, Developed on 13/6/2021.
import random
import json
print("************Welcome to JACKPOT ZONE.","In this lottery game ,only three person wins! $10000************")
win=0
players=int(input("1.enter the number of players:"))
b={}
for i in range(1,players+1):
    print("player number",i)
    age=int(input("What is your age:"))
    you=input("Enter your name:")
    if age<18:
        print("!!!!!!Below 18 cannot play!!!!!!")
        continue
    d=int(input("choose a number from 0 to 100="))
    b[you]=d
print(json.dumps(b,indent=2))
count=0
for f in range(1,players+1):
    if win==3:
        print("Winnners of the jacpot lottery",json.dumps(l,indent=2))
        print("Game over.","Please Do Visit again,Thank You")
    num=random.randrange(0,100)
    print("Player number",f,"gets",num)
    if num in list(b.values()):
        l={}
        name=list(b.keys())
        if b[count]==num:
            print("Congratulations!",name[count],"you have won $10000!!")
            win+=1
            l[name[count]]=b[name[count]]
    else:
        print("sorry your number didn't matched, Better luck next time")
    
    count+=1
print("Game over, Please do visit again at JACPOT ZONE")
    


    
    
        

