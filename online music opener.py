#this program uses pywhatkit modulue to open the music on youtube.
#but strangely we also require the flask module too for opening the music video on youtube.
import pywhatkit
command=input("Enter your song:")
pywhatkit.playonyt(command)   # yt means youtube.

