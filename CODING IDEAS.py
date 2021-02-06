# CODING IDEAS #

# practice programme
# programme exercise
# Mega projects


# This is the code for loop exit and restart
def play_quit():
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")

    if play_game.capitalize() == "Q":
        print(
            "Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
        exit()
    else:
        print("Enjoy the programme...!\n")








# This is the starting part of almost every programme
print("\nWelcome to MONTH GUESSING game by Sachin Dabhade\n")
name = input("Enter your name: ")
print("\nHello " + name.capitalize() + "! Best of Luck!")
print("\nThe game is about to start!\n Let's play and win!\n\n")









# This is the login form
from _datetime import datetime
def login(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name.capitalize()} has {msg} on {datetime.now()}\n")








# This is the record of almost every programme
from _datetime import datetime
name = input("Enter your name: ")
def record():
    global name
    name = " "
    with open("record.txt", "a") as f:
        f.write(f"The \'Magic words\' game is played by {name.upper()} on {datetime.now()}\n")
record()





# This is the music playing function of pygame module
from pygame import mixer
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        a = input("\nPress any key to stop the alarm:\nEnter \"Quit\" to stop the programme:")
        if a.capitalize() == stopper:
            quit()
        else:
            mixer.music.stop()
        break
musiconloop("C:\\Water.mp3", "Quit")  # This is how musiconloop works for playing music







# Tricks for python comprehension
# Long tricks for python for loops
ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)
print(ls)
# Short trick for forloops.
ls = [i for i in range(100) if i % 3 == 0]
print(ls)
# Short trick for dictionary.
list = {i: f"item{i}" for i in range(1, 10001)}
print(list)
# Short trick for reversing dictionary
list1 = {i:f"item{i}" for i in range(1,10)}
list1 = {value:key for key, value in list1.items()}
print(list1)








# This is a trick for the python speech recognition model that can be use on many occasional codes
from win32com.client import Dispatch
def speak(msg):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(msg)







# The Google Translator
from googletrans import Translator
translator = Translator()
Str = translator.translate('My brother is very good boy', src='en', dest='hi')
Str = Str.text
print(Str)







# The loop ender
variable = 1
if variable >= int:
    speak("Thanks for Listening us, Meet soon...!")
    break
variable = variable + 1







# The image to text converter
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\VAIBHAV\AppData\Local\Tesseract-OCR\tesseract.exe'
img = Image.open('')
text = pytesseract.image_to_string(img)
print(text







# This is the request for downloading data form the online source
import json
import requests
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = requests.get(url).text
print(data)  # We can also use json (java script object notation) for further process which we can't read directly for this
a = json.loads(data)
print(a)









# This is the regular experession for finding the special data in the big data
import re
pattern = re.compile(r'\w+@gmail.com')
matches = pattern.finditer(data)
for match in matches:
    print(match)










# This is the error handling of Value errors where str input is not acceptable
try:
    no_apple = int(input("\nEnter the number of apples: "))
    minimum = int(input("Enter the minimum number in range: "))
    maximum = int(input("Enter the maximum number in range: "))
except Exception as e:
    print("Enter Integers only...!")
    continue



# ---------------------------------* Here I Have finished the python course *----------------------------


# ---------------------------------* Here I Have started python projects *----------------------------

# This is the python speak function from pyttsx3 module
import pyttsx3
"""The main speaking engine is here"""
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
def speak(audio):
    """It is used to speak the audio output"""
    engine.say(audio)
    engine.runAndWait()







# This is the function which get command from microphones and give output as text
import speech_recognition as sr
def Take_Command():
    """It simply take command from the user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Please speak clearly...")
        speak("Please speak clearly...")
        return "None"
    return query


# --------------------------------****--------------------------------------



# This is the notification system for windows machines
from plyer import notification
def Notification(*args):
    """
    title (str) – Title of the notification
    message (str) – Message of the notification
    app_name (str) – Name of the app launching this notification
    app_icon (str) – Icon to be displayed along with the message
    timeout (int) – time to display the message for, defaults to 10
    ticker (str) – text to display on status bar as the notification arrives
    toast (bool) – simple Android message instead of full notification
    """
    notification.notify(
        title=args[0],
        message=args[1],
        app_name=args[2],
        app_icon=args[3],
        timeout=10,
        ticker=args[4],
        toast=True
    )
    Notification("here you have to put only five arguments in string format")

# Another method to get desktop notification
from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast("Email Sent!",
                     f"Today is {name}'s birthday. E-mail is sent.",
                     threaded=True,
                     icon_path=None,
                     duration=6)
while toast.notification_active():
    time.sleep(0.1)







