# Healthy Programmers Exercise
from pygame import mixer
from _datetime import datetime
from time import sleep
from plyer import notification

print("\nWelcome to \'HEALTHY PROGRAMMER\' by Sachin Dabhade\n")
sleep(1)
name = input("Enter your name: ")
print("Hello " + name.capitalize() + "! Best of Luck for your coding practice!")
sleep(1)
print("\nI will take care of your health...!\n Let's start programming!")


def login(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name.capitalize()} has {msg} on {datetime.now()}\n")


def log_now(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name.capitalize()} has done {msg} on {datetime.now()}\n")


def Notification(*args):
    """
    title (str) – Title of the notification
    message (str) – Message of the notification
    app_name (str) – Name of the app launching this notification
    app_icon (str) – Icon to be displayed along with the message
    """
    notification.notify(
        title=args[0],
        message=args[1],
        app_name=args[2],
        app_icon=args[3],
        timeout=10
    )


def sleep_programme():
    sleep(60*30)


if __name__ == '__main__':
    login("started coding")

    while True:
        sleep_programme()
        print("\n\nEye Exercise Time...")
        Notification("**Eye Exercise Time...`",
                     "Eye exercise is useful to secure our eyes from the computer rays. To prevent from it, we prefer 20-20-20 rule",
                     "Healthy Programmer",
                     "C:\PycharmProjects\sachinfile.py\Image and logos\Itzikgur-My-Seven-Favorities.ico")
        log_now("Eye Exercise")

        sleep_programme()
        print("\n\nWater Drinking Time...")
        Notification("**Drinking Water Notification",
                     "Human needs at least 3 to 4 liters of water every day...! So keep drinking water everyday..! Thanks for your time..!",
                     "Healthy Programmer",
                     "C:\PycharmProjects\sachinfile.py\Image and logos\Julie-Henriksen-Kitchen-Water-Boiler-Electric-Kettle.ico")
        log_now("Water Drink")

        sleep_programme()
        print("\n\nEye Exercise Time...")
        Notification("**Eye Exercise Time...`",
                     "Eye exercise is useful to secure our eyes from the computer rays. To prevent from it, we prefer 20-20-20 rule",
                     "Healthy Programmer",
                     "C:\PycharmProjects\sachinfile.py\Image and logos\Itzikgur-My-Seven-Favorities.ico")
        log_now("Eye Exercise")

        sleep_programme()
        print("\n\nPhysical Exercise Time...")
        Notification("**physical Exercise Notification",
                     "Physical activity and exercise can have immediate and long-term health benefits. Most importantly, regular activity can improve your quality of life.",
                     "Healthy Programmer",
                     "C:\PycharmProjects\sachinfile.py\Image and logos\Sportsbettingspot-Summer-Olympics-Weightlifting.ico")
        log_now("Physical Exercise")
        continue