#encrypting messages using rsa library, which uses encryption key and decryption key both, whereasa fernet library only uses one key.
#developed on 23/12/2021.
import rsa
pub,pri=rsa.newkeys(512)
message=input("Enter the message to be encrypted and decrypted=")
encmessage=rsa.encrypt(message.encode(),pub)
print("The encrypted the message is=",encmessage)
decmessage=rsa.decrypt(encmessage,pri).decode()
print("The decrypted message is=",decmessage)

