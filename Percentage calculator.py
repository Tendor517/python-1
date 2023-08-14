'''to create a program that will calculate your percentage
of an commercial producct or your school annual result'''
a=["School","Product"]
print(a)
b=input("Choose what kind of percentage you want:")
if b==a[0]:
    marks=float(input("Whats your total marks in all the subjects:"))
    out=int(input("Whats the total or out how much marks:"))
    per=(marks/out)*100
    print("Your percentage is=",per)
if b.lower()==a[1]:
    price=float(input("Enter the actual price of the product:"))
    reduced=float(input("Enter the offer price:"))
    offper=(reduced/price)*100
    print("The percenteage offer on this product is=",offper,"%")
print("PROGRAM OVER")
