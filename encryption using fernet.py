#A program to encrypt and decrypt messages.
#developed on 22/12/2021
from cryptography.fernet import Fernet
message=input("enter the message to be encrypted=")
key=Fernet.generate_key()
fernet=Fernet(key)
encmessage=fernet.encrypt(message.encode())
print("The original message:",message)
print("The encrypted message is:",encmessage)
decmessage=fernet.decrypt(encmessage).decode()
print("The decrypted message=",decmessage)
