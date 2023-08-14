#to Check if the entered alphabet is an vowel or not?..
def fun():
   k=input("1.enter the alphabet:")
   return k
while 1==1:
   a=fun()
   if len(a)==1:
      if a in['a','e','i','o','u'] or a in ['A','E','I','O','U']:
         print("2.yes it's an vowel")
         e=input("3.do you want to try again?; yes or no =")
         if e=="yes" or e=="Yes" or e=="YES":
            continue
         else:
            print("#okay then have a nice day, Bye")
            break
      else:
         print("the alphabet entered is an not an vowel")
         e=input("3.do you want to try again?; yes or no =")
         if e=="yes" or e=="Yes" or e=="YES":
            continue
         else:
            print("okay then have a nice day, Bye")
            break
   
   elif len(a)==0:
      print("!!you must alleast enter one alphabet")
      e=input("3.do you want to try again?; yes or no =")
      if e.lower()=="yes":
         continue
      else:
         print("**************okay then have a nice day,Bye****************")
         break
print()
   
  
