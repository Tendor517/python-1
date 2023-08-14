#developed on 16th of December 2021.
# a Program to send an instant mail to anyone through gmail. Using the SSL port number of Gmail.
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("tendorjee517@gmail.com","tendorjee")
rec=input("Enter the email-Id of the receiver=")
message=input("Enter the message you want to send")
server.sendmail("tendorjee517@gmail.com",rec,message)
server.close()
print("Mail had been sent")
