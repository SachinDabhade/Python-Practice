# Exercise no 7:
# This is News API
# from win32com.client import Dispatch
import json
import requests
from datetime import datetime

import pyttsx3

"""The main speaking engine is here"""
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)


def speak(audio):
    """It is used to speak the audio output"""
    engine.say(audio)
    engine.runAndWait()


def loop(msg):
    for i in msg:
        print(i, end=", ")


# def speak(msg):
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(msg)
def login(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name.capitalize()} has {msg} on {datetime.now()}\n")


if __name__ == '__main__':
    print("\nWelcome to News API made by Sachin Dabhade\n")
    name = input("Enter your name: ")
    print("\nHello " + name.capitalize() + "! Best of Luck!")
    print("\nThe News API is starting...!\n Let's Enjoy the programme...!\n\n")
    login("started News API")
    while True:
        countrys = {'Argentina': 'ar', 'Australia': 'au', 'Austria': 'at', 'Belgium': 'be', 'Brazil': 'br',
                    'Bulgaria': 'bg', 'Canada': 'ca', 'China': 'cn', 'Colombia': 'co',
                    'Cuba': 'cu', 'Czech republic': 'cz', 'Egypt': 'eg', 'France': 'fr', 'Germany': 'de',
                    'Greece': 'gr',
                    'Hong kong': 'hk', 'Hungary': 'hu', 'India': 'in',
                    'Indonesia': 'id', 'Ireland': 'ie', 'Israel': 'il', 'Italy': 'it', 'Japan': 'jp', 'Latvia': 'lv',
                    'Lithuania': 'it', 'Malaysia': 'my', 'Mexico': 'mx',
                    'Morocco': 'ma', 'Netherlands': 'nl', 'New zealand': 'nz', 'Nigeria': 'ng', 'Norway': 'no',
                    'Philippines': 'ph', 'Poland': 'pl', 'Portugal': 'pt',
                    'Romania': 'ro', 'Russia': 'ru', 'Saudi arabia': 'sa', 'Serbia': 'rs', 'Singapore': 'sg',
                    'Slovakia': 'sk', 'Slovenia': 'si', 'South africa': 'za',
                    'South korea': 'kr', 'Sweden': 'se', 'Switzerland': 'ch', 'Taiwan': 'tw', 'Thailand': 'th',
                    'Turkey': 'tr', 'Uae': 'ae', 'Ukraine': 'ua',
                    'United kingdom': 'gb', 'United states': 'us', 'Venuzuela': 've'}
        loop(countrys)
        country = input("\nEnter the Country (EX. India):")
        if country.capitalize() not in countrys.keys():
            print('\nNews for this country is not available...!')
            continue
        country1 = countrys.get(country.capitalize())
        categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
        loop(categories)
        category = input("\n\nEnter the category (EX. Science):")
        if category not in categories:
            print("\nThis category is not available...!")
            continue
        url = (
            f'https://newsapi.org/v2/top-headlines?country={country1.lower()}&category={category.lower()}&apiKey=2114b271bda54165b23a311b1d1e3c49')
        try:
            response = requests.get(url).text
            news = json.loads(response)
            print(news)
            print(news["articles"])
            articles = news["articles"]
        except Exception:
            print("\nSomething wents wrong...! Please try again...!")
            speak("Sorry...! Something wents wrong...! Please try again...!")
            continue
        else:
            if news["totalResults"] == 0:
                print("Sorry, there is no news on this topic...!")
                continue
            number = news["totalResults"]
            print(f"\nThere were {number} results found by API..!")
            try:
                int = int(input("How many news you want to listen (Ex. 1,2,3...):"))
            except ValueError:
                print("Only integers are allowed...!")
                continue
        variable = 1
        for article in articles:
            print(variable)
            print(article["title"])
            speak(article["title"])
            speak("The news description is ....!")
            print(article["description"])
            description = article["description"]
            speak(description)
            if variable == int:
                speak("Thanks for Listening us, Meet soon...!")
                break
            speak("The next news is.....!")
            variable = variable + 1
        continue
