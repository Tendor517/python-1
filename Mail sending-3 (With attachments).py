#developed on 16th of December 2021.
# a Program to send mail to anyone through gmail with proper body (with indentation in the body) and attachments options. Using the SSL port number of Gmail.
#here we have used glob module.
import smtplib
import glob
from email.message import EmailMessage
mes=EmailMessage()
sub=input("Enter the subject of your mail=")
From=input("Enter the name or association of the sender=")
recid=input("Enter the email-id of the receiver=")
mes["Subject"]=sub
mes["From"]=From
mes["To"]=recid
with open("email body.txt") as body: #you can open the file without with statement but in that case you need to close the file separately.
    data=body.read()
    mes.set_content(data)
for files in glob.glob("*.JPG"):  #it takes all the jpg files in the current working directory of this program.
    with open(files,"rb") as f:
        fdat=f.read()
        print("File name is ",f.name)
        mes.add_attachment(fdat,maintype="application",subtype="JPG")
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("tendorjee517@gmail.com","tendorjee")
server.send_message(mes)
server.quit()
print("Mail had been sent")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
