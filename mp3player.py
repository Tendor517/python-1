#actually thougt of to creat an mp3 player but mp3 was showing some error, so i chosed .wav sound files.
from playsound import playsound
rep=int(input("Enter how many times you want to repeat the music:"))
for i in range(rep):
    playsound("sound.wav")
print("Bye bye it's over now")
