#Dice game.
import random
player=int(input("1.enter the number of players"))
a=[1,2,3,4,5,6]
while 1==1:
    for i in range(player):
        c=random.choices(a)
        print("#player number",i,"=",c)
    e=input("***want to roll again?(y/n)=")
    if e=="y" or e=="Y":
        continue
    else:
        break  
print("See you soon,have fun")
