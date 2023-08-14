#developed on 16th of December 2021.
# a Program to send mail to anyone through gmail. Using the SSL port number of Gmail.
import smtplib
from email.message import EmailMessage
mes=EmailMessage()
sub=input("Enter the subject of your mail=")
From=input("Enter the name or association of the sender=")
recid=input("Enter the email-id of the receiver=")
mes["Subject"]=sub
mes["From"]=From
mes["To"]=recid
simplecontent=input("Enter the content of your mail=")
mes.set_content(simplecontent)
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("tendorjee517@gmail.com","tendorjee")
server.send_message(mes)
server.quit()
print("Mail had been sent")
print("-----------------------------------------------------------------------------------------------------------------------------------------------")
