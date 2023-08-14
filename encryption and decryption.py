while 1==1:
    def encrypt(pwd):
        a=input("do you want to set the encryption key your self(yes/no)?=")
        if a=="no" or a=="No" or a=="NO":
            key="12#6&@45)0cvyffdjsdb"
            return key.join(pwd),key
        else:
            key=input("enter the encryption key you want?:")
            return yourkey.join(pwd),key
    def decrypt(enpassed,enkey):
        return enpassed.split(enkey)
    password=input("enter your password:")
    enpass=encrypt(password)
    x,y=enpass
    print("Your encrypted password is:",x)
    ask=input("do you want to see your actual password(yes/no):")
    if ask=="yes" or ans=="Yes" or ans=="YES":
        depass=decrypt(x,y)
        depass2="".join(depass)
        print("The password you entered is=",depass2)
    rep=input("do you want to try this again:(y/n):")
    if rep=="n" or rep=="N":
        break
    else:
        continue




        
    
