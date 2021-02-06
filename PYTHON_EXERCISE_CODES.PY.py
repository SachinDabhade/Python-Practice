#  Python exercise no 1:
# This is a snake, water, gun game...
from _datetime import datetime
import random
import time
print("\nWelcome to SNAKE, WATER and GUN game by Sachin Dabhade\n")
name = input("Enter your name: \n")
print("Hello " + name.capitalize() + "! Best of Luck!\n")
time.sleep(3)
print("The game is about to start!\n Let's play and win!\n\n")
time.sleep(2)
def human_input():
    if x == "s":
        return "Snake"
    elif x == "w":
        return "Water"
    else:
        return "Gun"
def computer_input():
    if e == "s":
        return "Snake"
    elif e == "w":
        return "Water"
    else:
        return "Gun"
def body():
    print(f"Your guess is {human_input()} and computer guess is {computer_input()}")
    print("Congratulation.. You Won")
    print(f"Your points are {human_points} and computer points are {computer_points}")
def body_2():
    print(f"Your guess is {human_input()} and computer guess is {computer_input()}")
    print("Sorry.. Computer Won")
    print(f"Computer points are {computer_points} and human points are {human_points}")
def record():
    with open("record.txt", "a") as f:
        f.write(f"The SNAKE, WATER and GUN game is played by {name} on {datetime.now()}\n")
# This is the main programme...
if __name__ == '__main__':
    elements = ("s", "w", "g")
    print("\t\t\t\t\tSnake, Water and Gun Game...\nS for snake, W for water and G for gun...\n")
    # users necessary elements
    no_of_choises = 10
    choises = 0
    human_points = 0
    computer_points = 0
    while choises < no_of_choises:
        inp = input("Please.. Enter your choise :  ")
        e = random.choice(elements)
        x = inp.lower()
        if x == e:
            print("This is draw because of same choises...Please try again..")
            print(f"Your guess is {human_input()} and computer guess is {computer_input()}")
            print(f"Your points are {human_points} and computer points are {computer_points}")
        elif x == "s" and e == "w":
            human_points = human_points + 1
            body()
        elif x == "w" and e == "g":
            human_points = human_points + 1
            body()
        elif x == "g" and e == "s":
            human_points = human_points + 1
            body()
        elif x == "s" and e == "g":
            computer_points = computer_points + 1
            body_2()
        elif x == "g" and e == "w":
            computer_points = computer_points + 1
            body_2()
        elif x == "w" and e == "s":
            computer_points = computer_points + 1
            body_2()
        else:
            print("Invalid input\nPlease check your input")
        choises = choises + 1
        print(f"{no_of_choises - choises} chances is left out off {no_of_choises} \n\n")
    print("Game Over...")
    if computer_points > human_points:
        print(f"Sorry You have lost the game by {computer_points - human_points} points")
    elif computer_points < human_points:
        print(f"Congratulation You have Won the game by {human_points - computer_points} points")
    else:
        print("Sorry...Both have same points...So this is a tie match")
    record()










# Python exercise no 2:
# Healthy Programmers Exercise
from pygame import mixer
from _datetime import datetime
from time import sleep
print("\nWelcome to HEALTHY PROGRAMME by Sachin Dabhade\n")
sleep(2)
name = input("Enter your name: ")
print("Hello " + name.capitalize() + "! Best of Luck for your coding practice!")
sleep(3)
print("\nI will take care of your health...!\n Let's start programming!")
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
def login(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name.capitalize()} has {msg} on {datetime.now()}\n")
def log_now(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name} has done {msg} on {datetime.now()}\n")
def sleep_programme():
    sleep(60 * 30)
if __name__ == '__main__':
    login("started coding")
    while True:
        sleep_programme()
        print("\n\nEye Exercise Time...")
        musiconloop("C:\\Water.mp3", "Quit")
        log_now("Eye Exercise")
        sleep_programme()
        print("\n\nWater Drinking Time...")
        musiconloop('C:\\Water.mp3', 'Quit')
        log_now("Water Drink")
        sleep_programme()
        print("\n\nEye Exercise Time...")
        musiconloop("C:\\Water.mp3", "Quit")
        log_now("Eye Exercise")
        sleep_programme()
        print("\n\nPhysical Exercise Time...")
        musiconloop("C:\\Water.mp3", "Quit")
        log_now("Physical Exercise")
        continue










# Python exercise no 3:
# This is the exercise of animal guessing game which we can play anywhere
import random
import time
from datetime import datetime
# Initial Steps to invite in the game:
print("\nWelcome to ANIMAL GUESSING game by Sachin Dabhade\n")
name = input("Enter your name: ")
print("Hello " + name.capitalize() + "! Best of Luck!")
time.sleep(2)
print("\nThe game is about to start!\n Let's play and win!\n\n")
time.sleep(3)
def record():
    with open("record.txt", "a") as f:
        f.write(f"The ANIMAL GUESSING game is played by {name} on {datetime.now()}\n")
if __name__ == '__main__':
    chance = 5
    score = 0
    attempt = 0
    animal_list = ("Tiger", "Lion", "Giraffe", "Cheeta", "Rabbit")
    print(f"\t\tANIMAL GUESSING GAME\n\n\t\t !...GOOD LUCK...!")
    while chance > attempt:
        animal = random.choice(animal_list)
        attempt = attempt + 1
        print(f"\nYou need at least 2 score to won the game")
        x = input("Guess the animal (Tiger, Lion, Giraffe, Cheeta, Rabbit):")
        if x.capitalize() == animal:
            score = score + 1
            print("Congratulation... Your guess is absolutely correct...!")
        elif x.capitalize() in animal_list:
            print("Sorry but you can do it! Keep trying...!")
        else:
            print("Invalid input...!")
        print(f"The computer guess is {animal} and your guess is {x.capitalize()}")
        print(f"Your score is {score} and you have {chance - attempt} attempt remaining.")
        continue
print("Thanks For Playing!\nWe expect you will back again and enjoy our game...!\n")
record()











# python exercise no 4:
                             # Welcome to SACHIN DABHADAE Game:
from _datetime import datetime
import random
import time
# Initial Steps to invite in the game:
print("\nWelcome to MONTH GUESSING game by Sachin Dabhade\n")
name = input("Enter your name: ")
print("\nHello " + name.capitalize() + "! Best of Luck!")
time.sleep(2)
print("\nThe game is about to start!\n Let's play and win!\n\n")
time.sleep(3)
def record():
    with open("record.txt", "a") as f:
        f.write(f"The MONTH GUESSING game is played by {name.upper()} on {datetime.now()}\n")
record()
def win():
    print("\nCongratulation...! You won...!")
    print("You are lucky that you did not hanged to the hanger")
    print("   _____ \n"
          "  |     |\n"
          "  |     |\n"
          "  |      \n"
          "  |     O \n"
          "  |    /|\ \n"
          "  |    / \ \n"
          "__|__ -----\n")
    print(
        "\nThanks for playing with us..! We expect you have enjoy our game...!\nSee you again.. Till then take care...!")
    exit()
if __name__ == '__main__':
    # The parameters we require to execute the game:
    words_to_guess = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                      "november", "december"]
    word = random.choice(words_to_guess)
    length = len(word)
    display = '_ ' * length
    limit = 5
    attempt = 0
    score = 0
    while limit > attempt:
        guess = input("You have to guess the month of year:" + display + " Enter your guess: \n")
        if guess.lower() == word:
            score = score + 1
            win()
        else:
            attempt += 1
            print('\n')
            if attempt == 1:
                print("You are going to die...!\n")
                print("  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif attempt == 2:
                print("You are on the way to die...!\n")
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif attempt == 3:
                print("You are few step away to die...!\n")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif attempt == 4:
                print("You are just in front of hanger...!\n")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif attempt == 5:
                print("You are hanged on and you are dead...!\n")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
                print("Wrong guess. You are hanged!!!\n")
                print("The word was:", word)
        print(f"your score is {score} and you have {limit - attempt} chances remaining..!\n\n")
        continue











# Python exercise no 5:
# -----------------------------------------library made by SACHIN DABHADE--------------------------------------------------
from _datetime import datetime
class Library:
    """ This class is mainly work as a library which can be give us books from the library which we add here. Also this is efficient library code as per me...! """
    def __init__(self, library_name, booklist):
        self.username = library_name
        self.booklist = booklist
        self.lend = {}
    def details(self):
        print(f"The name of library is {self.username} and the books are {self.booklist}")
    def display_books(self):
        print(f"\nWe have the following books in the library: {self.username} \n")
        for books in self.booklist:
            print(books)
    def lend_book(self):
        a = input("Hello Sir...! Please enter your name:")
        b = input("Please enter the book that you want to lend:")
        if b.capitalize() not in self.booklist:
            print("Sorry... The book is not available at this movement...")
        elif b.capitalize() not in self.lend.values():
            self.lend.update({a.capitalize(): b.capitalize()})
            print(f"The book {b.capitalize()} is successfully given to {a.capitalize()}...!")
            with open("record.txt", "a") as f:
                f.write(f"The book: {b.capitalize()} is added by {a.capitalize()} on {datetime.now()}\n")
        else:
            print(f"The books are already using by {self.lend}")
    def return_book(self):
        a = input("Hello Sir...! Please enter your name:")
        b = input("Please enter the book that you want to return:")
        if b.capitalize() not in self.booklist:
            print("Invalid input...!")
        elif b.capitalize() in self.lend.values():
            self.lend.clear()
            print(f"Thanks You..! Your book: {b.capitalize()} is successfully returned to the database of {self.username} ")
            with open("record.txt", "a") as f:
                f.write(f"The book: {b.capitalize()} is added by {a.capitalize()} on {datetime.now()}\n")
        else:
            print(f"Sorry... The book: {b.capitalize()} is not given to any of the user...! please try again...!")
    def add_book(self):
        a = input("Hello Sir...! Please enter your name:")
        book = input(f"Enter the book you want to add in {x.capitalize()}'s' library:")
        if book.capitalize() not in self.booklist:
            self.booklist.append(book.capitalize())
            print(f"The Book: {book.capitalize()} is successfully added to the database of {self.username}'s")
            with open("record.txt", "a") as f:
                f.write(f"The book: {book.capitalize()} is added by {a.capitalize()} on {datetime.now()}\n")
        else:
            print(f"Sorry...! The book already in the Library: {self.username}")
    def play_loop():
        play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
        while True:
            if play_game.capitalize() == "Q":
                print("Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
                exit()
            break
if __name__ == '__main__':
    # Add library here..
    Sachin = Library("Sachin", ["Python", "C++", "Java", "Javascript", "C#"])
    Vaibhav = Library("Vaibhav", ["Javascript", "C#"])
    print(
        "\n\n---------------------------------Welcome to the book library made by Sachin Dabhade---------------------------------\n")
    # Add library here..
    library = ["Sachin", "Vaibhav"]
    print(f"The library's are:{library}")
    while True:
        # edit int for new function
        int = ["1", "2", "3", "4", "Q"]
        order = input("\n\n1:Display book \n2:Lend book \n3:Return book \n4:Add book \n\nEnter your choice:")
        if order.capitalize() in int:
            x = input("Hello Sir...! Please enter the library name:")
            if order == "1":  # Required elif statement for new library
                if x.capitalize() == "Sachin":
                    Sachin.display_books()
                elif x.capitalize() == "Vaibhav":
                    Vaibhav.display_books()
                else:
                    print("Invalid input...! Please enter a valid option...!")
            elif order == "2":  # Required elif statement for new library
                if x.capitalize() == "Vaibhav":
                    Vaibhav.lend_book()
                elif x.capitalize() == "Sachin":
                    Sachin.lend_book()
                else:
                    print("Invalid input...! Please enter a valid option...!")
            elif order == "3":  # Required elif statement for new library
                if x.capitalize() == "Vaibhav":
                    Vaibhav.return_book()
                elif x.capitalize() == "Sachin":
                    Sachin.return_book()
                else:
                    print("Invalid input...! Please enter a valid option...!")
            elif order == "4":  # Required elif statement for new library
                if x.capitalize() == "Vaibhav":
                    Vaibhav.add_book()
                elif x.capitalize() == "Sachin":
                    Sachin.add_book()
                else:
                    print("Invalid input...! Please enter a valid option...!")
        else:
            print("Invalid input...! Please enter a valid option...!")
        Library.play_loop()
        continue












# Exercise no 6:
#python 3.7.1
#All credits go to Ramaneffect
#he wrote this code in cpp, i rewrote it in python
# correction made by Sachin Dabhade
from _datetime import datetime
def record(ime):
    with open("record.txt", "a") as f:
        f.write(f"The \'Magic words\' game is played by {ime.capitalize()} on {datetime.now()}\n")
def play_quit():
    global ime
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
    while True:
        if play_game.capitalize() == "Q":
            print(
                "Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
            exit()
        break
if __name__ == '__main__':
    while True:
        ime = input("\n\nEnter your name: \n\n")
        for c in ime:
            c = c.upper()
            if (c == "A"):
                print("..######..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
            elif (c == "B"):
                print("..######..\n..#....#..\n..#####...\n..#....#..\n..######..\n\n")
            elif (c == "C"):
                print("..######..\n..#.......\n..#.......\n..#.......\n..######..\n\n")
            elif (c == "D"):
                print("..#####...\n..#....#..\n..#....#..\n..#....#..\n..#####...\n\n")
            elif (c == "E"):
                print("..######..\n..#.......\n..#####...\n..#.......\n..######..\n\n")
            elif (c == "F"):
                print("..######..\n..#.......\n..#####...\n..#.......\n..#.......\n\n")
            elif (c == "G"):
                print("..######..\n..#.......\n..#####...\n..#....#..\n..#####...\n\n")
            elif (c == "H"):
                print("..#....#..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
            elif (c == "I"):
                print("..######..\n....##....\n....##....\n....##....\n..######..\n\n")
            elif (c == "J"):
                print("..######..\n....##....\n....##....\n..#.##....\n..####....\n\n")
            elif (c == "K"):
                print("..#...#...\n..#..#....\n..##......\n..#..#....\n..#...#...\n\n")
            elif (c == "L"):
                print("..#.......\n..#.......\n..#.......\n..#.......\n..######..\n\n")
            elif (c == "M"):
                print("..#....#..\n..##..##..\n..#.##.#..\n..#....#..\n..#....#..\n\n")
            elif (c == "N"):
                print("..#....#..\n..##...#..\n..#.#..#..\n..#..#.#..\n..#...##..\n\n")
            elif (c == "O"):
                print("..######..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
            elif (c == "P"):
                print("..######..\n..#....#..\n..######..\n..#.......\n..#.......\n\n")
            elif (c == "Q"):
                print("..######..\n..#....#..\n..#.#..#..\n..#..#.#..\n..######..\n\n")
            elif (c == "R"):
                print("..######..\n..#....#..\n..#.##...\n..#...#...\n..#....#..\n\n")
            elif (c == "S"):
                print("..######..\n..#.......\n..######..\n.......#..\n..######..\n\n")
            elif (c == "T"):
                print("..######..\n....##....\n....##....\n....##....\n....##....\n\n")
            elif (c == "U"):
                print("..#....#..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
            elif (c == "V"):
                print("..#....#..\n..#....#..\n..#....#..\n...#..#...\n....##....\n\n")
            elif (c == "W"):
                print("..#....#..\n..#....#..\n..#.##.#..\n..##..##..\n..#....#..\n\n")
            elif (c == "X"):
                print("..#....#..\n...#..#...\n....##....\n...#..#...\n..#....#..\n\n")
            elif (c == "Y"):
                print("..#....#..\n...#..#...\n....##....\n....##....\n....##....\n\n")
            elif (c == "Z"):
                print("..######..\n......#...\n.....#....\n....#.....\n..######..\n\n")
            elif (c == " "):
                print("..........\n..........\n..........\n..........\n\n")
            elif (c == "."):
                print("----..----\n\n")
        print("Thanks for playing with us...")
        record(ime)
        play_quit()










# Exercise no 7:
# This is News API
from win32com.client import Dispatch
from datetime import datetime
import json
import requests
def loop(msg):
    for i in msg:
        print(i, end=", ")
def speak(msg):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(msg)
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
    countrys = {'Argentina': 'ar', 'Australia': 'au', 'Austria': 'at', 'Belgium': 'be', 'Brazil': 'br',
                'Bulgaria': 'bg', 'Canada': 'ca', 'China': 'cn', 'Colombia': 'co',
                'Cuba': 'cu', 'Czech Republic': 'cz', 'Egypt': 'eg', 'France': 'fr', 'Germany': 'de', 'Greece': 'gr',
                'Hong Kong': 'hk', 'Hungary': 'hu', 'India': 'in',
                'Indonesia': 'id', 'Ireland': 'ie', 'Israel': 'il', 'Italy': 'it', 'Japan': 'jp', 'Latvia': 'lv',
                'Lithuania': 'it', 'Malaysia': 'my', 'Mexico': 'mx',
                'Morocco': 'ma', 'Netherlands': 'nl', 'New Zealand': 'nz', 'Nigeria': 'ng', 'Norway': 'no',
                'Philippines': 'ph', 'Poland': 'pl', 'Portugal': 'pt',
                'Romania': 'ro', 'Russia': 'ru', 'Saudi Arabia': 'sa', 'Serbia': 'rs', 'Singapore': 'sg',
                'Slovakia': 'sk', 'Slovenia': 'si', 'South Africa': 'za',
                'South Korea': 'kr', 'Sweden': 'se', 'Switzerland': 'ch', 'Taiwan': 'tw', 'Thailand': 'th',
                'Turkey': 'tr', 'UAE': 'ae', 'Ukraine': 'ua',
                'United Kingdom': 'gb', 'United States': 'us', 'Venuzuela': 've'}
    loop(countrys)
    country = input("\n\nEnter the Country (EX. India):")
    country1 = countrys.get(country.capitalize())
    categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
    loop(categories)
    category = input("\n\nEnter the category (EX. Science):")
    if category not in categories:
        print("Invalid input....! Please try again....!")
        speak("Invalid input....! Please try again....!")
        exit()
    url = (
        f'https://newsapi.org/v2/top-headlines?country={country1.lower()}&category={category.lower()}&apiKey=2114b271bda54165b23a311b1d1e3c49')
    response = requests.get(url).text
    news = json.loads(response)
    print(news)
    print(news["articles"])
    articles = news["articles"]
    if news["totalResults"] == 0:
        speak("Sorry, there is no news on this topic...!")
        exit()
    int = int(input("\nHow many news you want to listen (Ex. 1,2,3...):"))
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










# exercise no 8:
# This is the pickel exercise
import pickle
import requests
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = requests.get(url).text
datalist = []
a = data.split("\n")
for item in a:
    if len(item) != 0:
        a = item.split(", ")
        datalist.append(a)
# # This methed we can use by list comprehension
# b = [item.split(",") for item in a if len(item) != 0]
# print(b)
with open("data.pkl", "wb") as f:
    pickle.dump(datalist, f)
with open("data.pkl", "rb") as f:
    a = pickle.load(f)
    print(a)










# exercise no 9:
# This is image to text converter
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\VAIBHAV\AppData\Local\Tesseract-OCR\tesseract.exe'
img = Image.open('img.jpg')
text = pytesseract.image_to_string(img)
print(text)












# Exercis no 10:
# This is the regular experession for finding the special data in the big data
data = """Skip to main content
View All Resources
Search
Search form
TUFTS.EDU
You are here
HomeCareer CenterNetworkProfessional Email Etiquette
Professional Email Etiquette
A Quick Guide to College Email Etiquette
You’ve probably written countless emails in your life by now and can post, text, and tweet with the best of them. But professional correspondence is a whole new ball game. Here are some pointers to keep in mind:
Use a Professional Email Address
You may prefer to be known by a witty screen name, but at best you won’t be taken seriously and at worst, your email will land in a spam folder. We recommend either using your official university email address or creating a professional email address with your first and last name.
Use a Formal Salutation
Professional correspondence should have a certain level of formality including a standard greeting. Unless you are invited to use a first name, it is best to address your recipient by his or her title, such as Dear Mr., Ms. or Professor. Hint: If you don’t know a recipient’s gender, a quick Google search will usually help clarify if you are addressing a Mr. or Ms.
Lead With a Clear Subject Line
A concise and specific subject line will help your reader know exactly what to expect. If you are writing to a networking contact, you may use the subject: Career Question from Tufts Senior. If you are writing to a professor, consider including your class department and number. For example, a question about midterm might have the subject: SPN 0003-B Midterm Question.
Be Clear, Polite, and Succinct
Emails to networking contacts should be requests for advice or career information, rather than a job/internship. Emails to professors should reference the course, and if appropriate, the name of the assignment. If your question relates to your academic record, include your student ID number.
Before sending, review your copy and make sure that it meets these criteria:
It is written in complete, coherent sentences
There are no spelling errors
No part of it is written in all caps
Sign Off with a Thank You
It is common courtesy to thank someone for his or her time and help. End your email with a “thank you” or “best” and your full name. Staff and professors are often keeping track of thousands of students, so clearly identifying yourself is the easiest way to ensure you get an answer.
Boost Your Image with a Strong Email Signature
There is no exact template you have to follow, but your ultimate goal should be to clearly state who you are and how to easily contact you.
We recommend following these guidelines:
Include essential information such as your name, major, school (Tufts) and expected graduation year.
Limit your signature to 3 or 4 lines. Use colons or pipes to separate.
Include your preferred email address and phone number.
Include links to your social media accounts such LinkedIn and Twitter. Make sure these are accounts with a professional message.
Avoid fancy fonts, colors, graphics, and inspirational quotes.
Example:
Jane Jumbo │ International Relations Major, Tufts University 20XX
Jane.Jumbo@Tufts.edu │(617) 627 -2000
http://twitter.com/janejumbo│http://www.linkedin.com/janejumbo
A Few Final Thoughts
Emails Are Forever
You cannot take back what gets sent, and without a clear tone of voice, it can be easy to sound offensive. Read your message before you send it and keep in mind that some issues are better discussed in person. If it can’t be wrapped up in a short paragraph, consider making an appointment or visiting office hours.
Patience Is a Virtue
We all like instant gratification, but everyone is busy and sometimes a reply takes more time than you’d hope. If your question or concern is time sensitive it may be appropriate to write a follow-up email, but be realistic about your expectations.
Practice Common Courtesy
If you expect timely, helpful replies, you should do the same for others. Check your email regularly, and respond as soon as you are able.
Tufts students walking outside.
Explore Career Options
Campus Maps
Medford/Somerville
Boston
Grafton
 sachindabhade1922@gmail.com
 vaibhavdabhade97@gmail.com
 sachindabhade254@gmail.com
Privacy
European Economic Area (EEA) Privacy Statement for Students
Upcoming Student Life Events
Administrative Contacts
Dean of Student Affairs
Deans of Academic Advising and Undergraduate Studies
Student Services Center
Looking for a different Tufts student resource?
A-Z Resource Listing
Undergraduate Admissions
Graduate Admissions
School of Arts and Sciences
School of Engineering
Fletcher School Students
Medical School Students
Graduate Biomedical Sciences Students
Dental School Students
Friedman School Students
Cummings School Students
© 2020 Tufts University
"""
# rules for regular expression
"""Meta Characters
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string
\A:         the resultant is a match if the input characters are at the beginning of the string
\b          the resultant is a match whether the input characters are at the beginning or the end of a word
\d          the resultant is a match if the string contains any digits
\s           the resultant is a match if the string contains a white space character
There are many metacharacters supported by the re module. Some characters with their working are the following:
'.': Matches any single character except newline
'$': Anchors a match at the end of a string
' *': Matches zero or more repetitions
'+':Matches one or more repetitions
'{}':Matches an explicitly specified number of repetitions
'[]':Specifies a character class"""
if __name__ == '__main__':
    import re
    data_list = []
    pattern = re.compile(r'\w+@gmail.com')
    matches = pattern.finditer(data)
    for match in matches:
        data_list.append(match)
    print(data_list)











# Exercise no 11:
# This is the practice problem for python given by harry bhai
from datetime import datetime
def login(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name.capitalize()} has {msg} on {datetime.now()}\n")
def age():
    future_age = 2020 - int(age_birth) + user_input
    print(f"You will be {user_input} year old in the year {str(future_age)}")
def birth():
    row = age_birth[-4:]
    if int(row) < 2021 and int (row) >= 1900:
        if int(age_birth[0:2]) < 32 and int(age_birth[2:4]) < 13:
            future_age = int(row) + user_input
            print(f"You will be {user_input} year old on {age_birth[0:2]}/{age_birth[2:4]}/{str(future_age)}")
        else:
            print("Sorry...! Invalid birth date Input Occur...! Please try again...!")
    else:
        print("Sorry ...! Your age can't be greater than 150 and lesser than and 0...!")
        exit()
if __name__ == '__main__':
    name = str(input("\nEnter your name:"))
    age_birth = str(input("\nEnter your age (EX. 18) or date of birth (19092002):"))
    user_input = int(input("Enter the years to see your birth date in future (EX. 100):"))
    if len(age_birth) <= 3:
        if int(age_birth) > 0 and int(age_birth) < 150:
            age()
        else:
            print("Sorry ...! Your age can't be greater than 150 and lesser than and 0...!")
            exit()
    elif len(age_birth) == 8:
        birth()
    else:
        print("Invalid input...! Please try again with a valid input...!")
    login("Login in the age finder software")











# Exercise no 12
# This is the Practice problem of apple distribution between the students and harry bhai
if __name__ == '__main__':
    while True:
        try:
            no_apple = int(input("\nEnter the number of apples: "))
            minimum = int(input("Enter the minimum number in range: "))
            maximum = int(input("Enter the maximum number in range: "))
        except ValueError:
            print("Enter Integers only...!")
            exit()
        if minimum >= maximum:
            print("This is not a range...!")
        for item in range(minimum, maximum + 1):
            if no_apple % item == 0:
                print(f"{item} is divisor of {no_apple}")
            else:
                print(f"{item} is not divisor of {no_apple}")
        continue









# Exercise no 13:
# This is the practice problem of reversing list by three method
def play_quit():
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
    if play_game.capitalize() == "Q":
        print(
            "Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
        exit()
    else:
        print("Enjoy the programme...!\n")
def reverse_1():
    reverse_1 = list[:]
    reverse_1.reverse()
    print(f"The user list is sorted by builtin method is {reverse_1}")
def reverse_2():
    print(f"The user list is sorted by list slicing method is {list[::-1]}")
def reverse_3():
    for i in range(list_len//2):
        list[i], list[list_len-i-1] = list[list_len-i-1], list[i]
    print(f"The user list is sorted by swapping elements method is {list}")
if __name__ == '__main__':
    list = []
    while True:
        try:
            list_len = int(input("Enter the length of list:\n"))
            for item in range(list_len):
                list.append(int(input("Enter the list elements one by one:")))
        except ValueError:
            print("Invalid Input...!")
            exit()
        print(f"Your list is {list}\n")
        reverse_1()
        reverse_2()
        reverse_3()
        play_quit()









# Ecercise no 14
# This is the number palindrome practice problem given by harry (424,646,292)
def play_quit():
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
    if play_game.capitalize() == "Q":
        print(
            "Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
        exit()
    else:
        print("Enjoy the programme...!\n")
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def next_palindrome(n):
    while not is_palindrome(n):
        n += 1
    return n
if __name__ == '__main__':
    while True:
        try:
            raw_input = int(input("Enter the turns of number:\n"))
            list = []
            for item in range(raw_input):
                palin = int(input("Enter the element:"))
                list.append(palin)
        except Exception as e:
            print("Invalid input occurs...! Please try again...! The Error is:",e)
            exit()
        for item in range(len(list)):
            print(f"The next palindrome of {list[item]} is {next_palindrome(list[item])}")
        play_quit()
        continue









# Exercise no 15:
# This is the practice problem given by harry (Palindromelity list)
def play_quit():
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
    if play_game.capitalize() == "Q":
        print("Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
        exit()
    else:
        print("Enjoy the programme...!\n")
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def next_palindrome(n):
    while not is_palindrome(n):
        n += 1
    data.pop(i)
    data.insert(i,n)
if __name__ == '__main__':
    while True:
        try:
            chance = int(input("Enter the length of list:\n"))
            data = []
            for i in range(chance):
                list_item = int(input("Enter the items of list:"))
                data.append(list_item)
        except Exception as e:
            print("Invalid input/...! Please try again...!")
            continue
        for i in range(chance):
            if data[i] > 10:
                next_palindrome(data[i])
        print(data)
        play_quit()








# Exercise no 16:
# This is a practice problem of multiplayer number guessing game given by harry bhai
import random
from datetime import datetime
def number():
    chances = 1
    while True:
        print("\nAttempt number:", chances)
        get = int(input(f"\nGuess the number between {a} and {b}:"))
        if get >= a and get <= b:
            if get == num:
                print("Congratulation...! You guess the correct number...!")
                print(f"You took {chances} chances to guess the correct number...")
                points.append(chances)
                break
            elif get < num:
                print(f"Wrong guess...! Please enter greater number.")
            else:
                print(f"Wrong guess...! Please enter smaller number.")
        else:
            print("Invalid Input...! Please enter the valid input..!")
            continue
        chances += 1
        continue
def check_points():
    if points[0] < points[1]:
        print(f"\n{name_1} is win by {points[1] - points[0]} points..")
    elif points[0] > points[1]:
        print(f"\n{name_2} is win by {points[0] - points[1]} points..")
    else:
        print("\nThis is draw because of same points..!")
def play_quit():
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
    if play_game.capitalize() == "Q":
        print("Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
        exit()
    else:
        print("Enjoy the programme...!\n")
def login(msg):
    global name_1
    global name_2
    with open("record.txt", "a") as f:
        f.write(f"{name_1.capitalize()} and {name_2.capitalize()} are {msg} on {datetime.now()}\n")
if __name__ == '__main__':
    print("\nWelcome to Multi-player NUMBER GUESSING game made by Sachin Dabhade\n")
    name_1 = input("Enter first player name: ")
    name_2 = input("Enter second player name: ")
    print("\nHello " + name_1.capitalize() + " and " + name_2.capitalize() + "! Best of Luck!")
    print("\nThe game is about to start!\n Let's play and win!\n\n")
    login("Playing the multiplayer number guessing game")
    try:
        a = int(input("Enter the first number in range: "))
        b = int(input("Enter the second number in range: "))
        if a < b:
            if a>100 or a<-100 or b>100 or b<-100:
                print("Number should be lesser than 100 and greater than -100..")
                exit()
        else:
            print("first number should be lesser than the second one...!")
            exit()
    except Exception as e:
        print("Invalid Input...!\n")
        exit()
    points = []
    play = 1
    while True:
        if play % 2 != 0:
            num = random.randint(a, b)
            print("\nThis is first inning...!")
            print(f"{name_1} will guess the number..")
            number()
            play += 1
        if play % 2 == 0:
            num = random.randint(a, b)
            print("\nThis is second inning...!")
            print(f"{name_2} will guess the number..")
            number()
        else:
            print("Something wents wrong...!\n")
            exit()
        check_points()
        points.clear()
        play_quit()









# Exercise no 17:
# This is the search engine like google which gives us search results
def matchingWords(sentence1, sentence2,):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score = score + 1
    return score
if __name__ == '__main__':
    while True:
        sentences = ["Sachin is a good boy", "vaibhav is my brother", "Vinayak vasant dabhade is my father", "mandakin dabhade is is is my mother"]
        query = input("\nSearch Engine is ready to work:")
        scores = [matchingWords(query, sentence) for sentence in sentences]
        sortedSentScored = [sentScore for sentScore in sorted(zip(scores, sentences), reverse = True) if sentScore[0] != 0] # This is list comprehension.
        print(f"\n{len(sortedSentScored)} results found...!\n")
        for score, items in sortedSentScored:
            print(f"\"{items}\": with a source of {score}")
        continue










# Exercise no 18
# This is the rohan das fraud multiplication table
import random
def table(num):
    for i in range(1, 11):
        table_1.append(num*i)
def defect_table(num):
    choice = random.randint(1, 11)
    for i in range(1, 11):
        if i == choice:
            table_2.append((num*i) + choice)
        else:
            table_2.append(num*i)
    print(table_2)
def defect_found():
    for i in range(0, 10):
        if table_1[i] != table_2[i]:
            print(f"Defect is found in step {i + 1} : {table_2[i]} has to {table_1[i]} in list...!")
            print("Rohan Das is a fraud and he cheated with the class guys..!")
if __name__ == '__main__':
    while True:
        a = table_1 = []
        b = table_2 = []
        try:
            num = int(input("\nEnter the number:"))
        except Exception as e:
            print("Invalid input..!")
            continue
        table(num)
        defect_table(num)
        defect_found()
        continue


# ---------------------------------* Here I Have finished the python course *----------------------------



# --------------------------------****--------------------------------------



# ---------------------------------* Here i have started the python practice course *-----------------------------------

# Practice problem 1
# Write the python programme which will add the number input given by user
""" This function will simply make the receipt bill """

bill_rec = []
def receipt_bill(name, bill):
    print("\nStore name: Shubham Grocery shop.")
    print(f"Costumer name: {name}")
    for i, item in enumerate(bill_rec):
        print(f"{i + 1}. {name} has buy item of rupees {item}")
    print(f"Your bill is {bill}. Thanks shopping with us...!")

name = input("Enter your name:")
bill = 0
while True:
    try:
        user_input = str(input("\nEnter the price:"))
    except Exception as e:
        print("Please enter the your name.")
        continue
    if user_input != 'q':
        try:
            bill = bill + int(user_input)
            bill_rec.append(bill)
            print("Order total so far is ", bill)
        except Exception as e:
            print("Sorry something went wrong...!")
    elif user_input == 'q':
        for i in bill_rec:
            a = 0
            a = a + i
        receipt_bill(name, a)
        quit()


# Pracitice problem 2
# find the factorial of the number n also number of trailing zeroes in that factorial
def factorial_1(number):
    """ This will find the factorial number of the input"""
    factor = 1
    for i in range(1, number + 1):
        factor = factor * i
    return factor


# another method to find factorial is
def factorial_2(number):
    """ This will find the factorial number of the input"""
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial_2(number=number - 1)


# Finding trailing(continuously) zeroes
def TrailingZeroes(number):
    """This will gives us the number of zeroes in the following factorial"""
    Count = 0
    i = 5
    while number // i != 0:
        Count = Count + int(number // i)
        i = i * 5
    return Count


if __name__ == '__main__':
    while True:
        try:
            number = int(input("Enter the number:"))
        except ValueError as Value:
            print("Sorry...! Only integers are allowed...!")
            continue
        else:
            print(f'The factorial of {number} is {factorial_1(number=number)} from function 1')
            print(f'The factorial of {number} is {factorial_2(number=number)} from function 2')
            print(f'The Trailing zeroes in the factorial is {TrailingZeroes(number=number)}')




# Practice problem 3
# This is the python programme to make the currency converter








# Practice problem 4
# This is the python programme to make the small server in python instead of locak html file or any big server
""" How to make servers into the python programmes to run websites """
"""
1. We recommend you to use sublime text for web development 
2. Open the folder in sublime text and make the html file
3. same folder or file open in power-shell and run the command - 'python -m http.server --bind=localhost' or 'python -m http.server' amd open chrome and search for localhost:8000
4. That's done from you...!
Is it html or http
"""






# Practice problem 5
# This is the python clutter used by the users who want to make their directories systematic and clean
"""
This programme is not here because it can damage my files systematic arrangement so i prefer it to run in virtual environment name as clutter.
If you want to run this file in your computer then please go to the virtual environment projects and lets see the work
"""






# Practice problem 6
# This is the python notification system for python users who spend most of their time on computer
# Python practice programme to get notification on our windows

import time
from plyer import notification

"""
title (str) – Title of the notification
message (str) – Message of the notification
app_name (str) – Name of the app launching this notification
app_icon (str) – Icon to be displayed along with the message
timeout (int) – time to display the message for, defaults to 10
ticker (str) – text to display on status bar as the notification arrives
toast (bool) – simple Android message instead of full notification
"""

if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Drinking Water Notification",
            message="Human needs at least 3 to 4 liters of water every day...! So keep drinking water everyday..! Thanks for your time..!",
            app_name="Healthy Programmer",
            app_icon="C:\PycharmProjects\sachinfile.py\Image and logos\Julie-Henriksen-Kitchen-Water-Boiler-Electric-Kettle.ico",
            ticker="Drinking water notification...",
            toast=True
        )
        time.sleep(6)
        # time.sleep(60*60)
        continue






# Practice programme 7
# This is the python practice on making the password generator
""" While making the password we have to make strong password """

import string
import random
import pickle

if __name__ == '__main__':
    while True:
        purpose = input("Reason Behind your password:")
        final_set = []
        set_1 = string.ascii_letters
        set_2 = string.digits
        set_3 = string.punctuation
        final_set.extend(set_1)
        final_set.extend(set_2)
        final_set.extend(set_3)
        random.shuffle(final_set)
        try:
            P_len = int(input("Enter your password length:"))
        except Exception as E:
            print("Please enter integers only...!")
            continue
        Password = final_set[0:P_len]
        Pass_dict = {purpose: ''.join(Password)}
        with open("Pass.pkl", "ab") as f:
            pickle.dump(Pass_dict, f)
        # with open("Pass.pkl", "rb") as f:
        #     a = pickle.load(f)
        #     print(a)
        continue







# Practice problem 8
# This is the practic problem on automating the birthday wishing programme made on python
# import required packages
import pandas as pd
import datetime
import smtplib
import time
import requests
from win10toast import ToastNotifier
import os
os.chdir(r"C:\PycharmProjects\Virtual_Environment\Birthday")
# your gmail credentials here
GMAIL_ID = 'sachin1922dabhade1998@gmail.com'
GMAIL_PWD = 'dabhade@12'
# for desktop notification
toast = ToastNotifier()
# define a function for sending email
def sendEmail(to, sub, msg, name):
    # conncection to gmail
    gmail_obj = smtplib.SMTP('smtp.gmail.com', 587)
    # starting the session
    gmail_obj.starttls()
    # login using credentials
    gmail_obj.login(GMAIL_ID, GMAIL_PWD)
    # sending email
    gmail_obj.sendmail(GMAIL_ID, to,
                       f"Subject : {sub}\n\n{msg}")
    # quit the session
    gmail_obj.quit()
    print("Email sent to " + str(to) + " with subject "
          + str(sub) + " and message :" + str(msg))
    toast.show_toast("Email Sent!",
                     f"Today is {name}'s birthday. E-mail is sent.",
                     threaded=True,
                     icon_path=None,
                     duration=6)
    while toast.notification_active():
        time.sleep(0.1)
    # define a funtion for sending sms
def sendsms(to, msg, name, sub):
    url = "https://www.fast2sms.com/dev/bulk"
    payload = f"sender_id=FSTSMS&message={msg}&language=english&route=p&numbers={to}"
    headers = {
        'authorization': "7ypEadrM43gBoV8zbeXKxH2CkAftYJTljL65huSGsvPcO0WiRUNOgM31FdYVBsKDrLiZqIS9lEQ4Hj6n",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response_obj = requests.request("POST", url,
                                    data=payload,
                                    headers=headers)
    print(response_obj.text)
    print("SMS sent to " + str(to) + " with subject :" +
          str(sub) + " and message :" + str(msg))
    toast.show_toast("SMS Sent!",
                     f"Today is {name}'s birthday. Message is sent.",
                     threaded=True,
                     icon_path=None,
                     duration=6)
    while toast.notification_active():
        time.sleep(0.1)

    # driver code
if __name__ == "__main__":
    # read the excel sheet having all the details
    dataframe = pd.read_excel("data.xlsx")
    # today date in format : DD-MM
    today = datetime.datetime.now().strftime("%d-%m")
    # current year in format : YY
    yearNow = datetime.datetime.now().strftime("%Y")
    # writeindex list
    writeInd = []
    for index, item in dataframe.iterrows():
        msg = "Many Many Happy Returns of the day dear " + str(item['NAME'])
        # stripping the birthday in excel
        # sheet as : DD-MM
        bday = item['Birthday'].strftime("%d-%m")
        # condition checking
        if (today == bday) and yearNow not in str(item['Year']):
            # calling the sendEmail function
            sendEmail(item['Email'], "Happy Birthday",
                      msg, item['NAME'])
            # calling the sendsms function
            sendsms(item['Contact'], msg, item['NAME'],
                    "Happy Birthday")
            writeInd.append(index)
    for i in writeInd:
        yr = dataframe.loc[i, 'Year']
        # this will record the years in which
        # email has been sent
        dataframe.loc[i, 'Year'] = str(yr) + ',' + str(yearNow)
    dataframe.to_excel('data.xlsx',
                       index=False)










# Practice problem 9
# This video is about securing and making the strong password using the exiting password with the help of your python programme

def strongPass(password):
    for a, b in StrongList:
        if a in password:
            password = password.replace(a, b)
    return password
if __name__ == '__main__':
    StrongList = (
    ('a', '@'), ('and', '&'), ('s', '$'), ('h', '#'), ('i', '!'), ('o', '0'), ('t', '|-'), ('son', '*'), ('sun', '*'),
    ('c', '<'), ('d', '|>'), ('l', '|'), ('9', '?'))

    password = input("Enter Your Password:")
    password = password.lower()
    Pass = strongPass(password)
    print(Pass)

# Python program to check validation of password
# Module of regular expression is used with search()
import re


def Check_1():
    # Function one to check the password strength get by user
    while len(Password) >= 8:
        if not re.search(r"[a-z]", Password):
            return "Not a Strong Password...!"
        elif not re.search(r"[A-Z]", Password):
            return "Not a Strong Password...!"
        elif not re.search(r"[0-9]", Password):
            return "Not a Strong Password...!"
        elif not re.search(r"[_@$]", Password):
            return "Not a Strong Password...!"
        else:
            return "Strong Password...!"
    else:
        return "Password is too short...!"


if __name__ == '__main__':

    while True:
        try:
            # User input for check password
            Password = input("Enter the Password: ")
            # This is the method 1 to check the password strength
            print(Check_1())
        except Exception as E:
            print(E)
        continue








# Practice problem 10
# This video is not in  my playlist so we will get it soon





# Practice problem 11
# This is the practice problem on how to find amstorong numbers in the python programme
def Armstrong_1(number):
    output = 0
    for num in str(number):
        Num = int(num) ** len(str(number))
        output = Num + output

    if number == output:
        print("This is the Armstrong number...!")
    else:
        print("This is not the Armstrong number...!")


if __name__ == '__main__':
    while True:
        try:
            number = int(input("Enter the number: "))
        except ValueError as E:
            print("Only Integers are allowed...!")
        else:
            Armstrong_1(number)
        continue

# This programme is made by harry's video
# Practice problem 11
# This function will give me the anstrong number output
def Armstrong_2(number):
    copyNum = number
    order = len(str(number))
    output = 0
    while number > 0:
        digit = number % 10
        output += digit ** order
        number = number // 10
    if copyNum == output:
        print("This is the Armstrong...!")
    else:
        print("This is not the Armstrong...!")


if __name__ == '__main__':
    while True:
        try:
            number = int(input("Enter the number: "))
        except Exception as E:
            print("Only integers are allowed...!")
        else:
            Armstrong_2(number)
        continue







# Practice problem 12
# This is the problem solving on how to make the rest APIs on pyhton
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/armstrong/<string:number>')
def Armstrong_1(number):
    output = 0
    for num in str(number):
        Num = int(num) ** len(str(number))
        output = Num + output
        print(output)

    if int(number) == output:
        print(f"{number} is the Armstrong number...!")
        results = {
            "number": number,
            "IP": "112.232.254.25",
            "Armstrong": True,
            "Results": number + " is a Armstrong number"
        }
    else:
        print(f"{number} is not the Armstrong number...!")
        results = {
            "number": number,
            "IP": "112.232.254.25",
            "Armstrong": False,
            "Results": number + " is not a Armstrong number"
        }
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)






# Practice problem 13
# This is the practice problem on how to write fibonacci series in python

def Fibonacci_Self(number):
    PN = 0
    CN = 1
    if number == 0:
        return 0
    for i in range(1, number):
        PPN = PN
        PN = CN
        CN = PPN + PN
    return CN

if __name__ == '__main__':
    while True:
        try:
            number = int(input("Enter the number: "))
        except Exception as E:
            print("Only integers are allowed...!")
            continue
        else:
            print(f'The fibonacci series for {number} number is {Fibonacci_Self(number=number)}')
        continue







# Practice Problem 14
# This is the Practice problem to solve the following problem statement

"""
20 random cards are placed in a row all faces down. A turn consists of taking two adjacent
card where the left 1 is faced up and the right one can be faced up or faced down and flipping
them both. Show that this process can be terminate.(With all the cards facing up)
"""

def transform(data):
    for i in range(len(data) - 1):
        if data[i] == '0' or data[i] == '1':
            if data[i] == '1':
                data[i] = '0'
                if data[i + 1] == '1':
                    data[i + 1] = '0'
                else:
                    data[i + 1] = '1'
        else:
            return "none"
    return str(data)

if __name__ == '__main__':
    while True:
        try:
            data = list(input("Enter the number ( Only 1 and 0 are acceptable) : "))
        except Exception as E:
            print("Something went wrong...!")
        else:
            if transform(data=data) != "none":
                print(f"This is the processed number: {transform(data=data)}")
            else:
                print("Only 1 and 0 numbers are allowed..!")
        continue






# Practice problem 15
# This is the practice problem on how to add two matrix in python

def Take_Matrix(row, column):
    matrix = []
    for i in range(row):
        print(f"This is row {i + 1}...!")
        raw_row = []
        for j in range(column):
            number = int(input(f"Enter the number {j + 1}: "))
            raw_row.append(number)
        matrix.append(raw_row)
    return matrix

def Add_Matrix(A, B):
    Matrix = []
    for i in range(row):
        Row = []
        for j in range(column):
            number = A[i][j] + B[i][j]
            Row.append(number)
        Matrix.append(Row)
    return Matrix

if __name__ == '__main__':
    while True:
        choice = 0
        try:
            row = int(input("How many rows do you want in your matrix: "))
            column = int(input("How many column do you want in your matrix: "))
        except Exception as e:
            print('Only integers are allowed...!')
        else:
            print("\nMatrix A: \n")
            A = Take_Matrix(row, column)
            print(f"This is the A matrix: {A}")

            print("\nMatrix B: \n")
            B = Take_Matrix(row, column)
            print(f"This is the B matrix: {B}")

            print("\nAdding the Matrices...!\n")
            print(f"Addition of the matrices is {Add_Matrix(A, B)}")
            print("\nThis is done...!\n")
        continue





# practice problem 16
# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


if __name__ == '__main__':
    while True:
        try:
            num1 = int(input("Enter the Number 1: "))
            num2 = int(input("Enter the Number 2: "))
        except Exception as E:
            print("Only integers are allowed...!")
        else:
            try:
                print("The L.C.M. is", compute_lcm(num1, num2))
            except Exception as E:
                print(f"Can't Find LCM of {num1} and {num2}")
        continue






# Practicie problem 17
# This is the practice problem to find the HCF or GCD hy using python

def HCF(a, b):
    if a < b:
        lesser = a
    else:
        lesser = b
    for i in range(1, lesser + 1):
        if a%i==0 and b%i==0:
            HCF = i
    return HCF


if __name__ == '__main__':
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except Exception as E:
            print("Only integers are allowed...!\n")
        else:
            try:
                print(f"\nThe Highest Common Factorial (HCF) of {num1} and {num2} is {HCF(num1, num2)}")
            except Exception as E:
                print("Something went wrong...!")
            else:
                print("This is done...!\n")
            finally:
                print("** Thanks for your valuable time **\n")







# Practice Problem 18
# This is the practice on how to multiply two matrices by using python
"""
This programme will give us the multiplication of any length of matrix if possible..!
"""

def Take_Matrix(row, column):
    matrix = []
    for i in range(row):
        print(f"This is row {i + 1}...!")
        raw_row = []
        for j in range(column):
            number = int(input(f"Enter the number {j + 1}: "))
            raw_row.append(number)
        matrix.append(raw_row)
    for m in matrix:
        print(m)
    return matrix

def Multiply_Matrix(A, B):
    Matrix = []
    for i in range(len(A)):
        Row = []
        for j in range(len(B[0])):
            number = 0
            for k in range(len(B)):
                number = number + A[i][k]*B[k][j]
            Row.append(number)
        Matrix.append(Row)
    for M in Matrix:
        print(M)


if __name__ == '__main__':
    choice = 0
    while True:
        try:
            row = int(input("\nEnter the number of rows you want in your matrix: "))
            column = int(input("Enter the number of columns you want in your matrix: "))
        except Exception as E:
            print("Only integers are allowed...!")
        else:
            try:
                if choice % 2 == 0:
                    A_column = column
                    print("\nMatrix A: \n")
                    print(f"\nThis is the A matrix:\n")
                    A = Take_Matrix(row, column)
                    choice += 1
                    continue
                else:
                    B_row = row
                    print("\nMatrix B: \n")
                    print(f"\nThis is the B matrix:\n")
                    B = Take_Matrix(row, column)
                    choice += 1
            except Exception as E:
                print("Invalid Input...!")
            else:
                try:
                    if (A_column != B_row):
                        print("\nNumber of column of A matrix must be equal to row of B matrix")
                        continue
                    else:
                        print('\nMultiplying Two Matrices...')
                        print(f"Multiplication of two matrices:")
                        Multiply = {Multiply_Matrix(A, B)}
                except Exception as E:
                    print("\nMultiplication does not occur...! Something Went Wrong...!")
                else:
                    print("\nMultiplication is done...!\n")
                finally:
                    print("\n ** Thanks for your valuable time ** \n")
        continue






# Practice problem 119
# This is the practice problem on how to read and extract text in pdf

"""
With the help of this module we will play with pdfs and much more
"""

import PyPDF2


def Text(PDF):
    # printing number of pages in pdf file
    print(PDF.numPages)
    # creating a page object
    for i in range(PDF.getNumPages()):
        pageObj = PDF.getPage(i)
        print(i+1)
        # extracting text from page
        print(pageObj.extractText())


if __name__ == '__main__':
    Dict_PDF = {'1': 'PDF Information', '2': 'Content Page Number', '3': 'PDF Fields', '4': 'Text Fields in PDF',
                '5': 'Text Destination', '6': 'Total PDF Pages', '7': 'PDF Outline', '8': 'Get Page Number',
                '9': 'PDF Layout', '10': 'PDF Mode', '11': 'PDF Decodeness', '12': "PDF Text Extraction"}
    while True:
        try:
            pdf_file = input("Enter the path of PDF file: ")
            pdf_File = open(pdf_file, 'rb')
            PDF = PyPDF2.PdfFileReader(pdf_File)
        except Exception as E:
            print("\nplease give the correct PDF path...!")
        else:
            try:
                for i, item in enumerate(Dict_PDF.values()):
                    print(i + 1, item)
                choice = input("\nEnter the option number (Ex. 1, 2, 3...) : ")
                if choice in Dict_PDF.keys():
                    if choice == '1':  # the document information of this PDF file
                        print(f"\nPDF information: {PDF.getDocumentInfo()}")
                    elif choice == '2':
                        try:  # Retrieve page number of a given Destination object
                            destination = input("Enter the Destination(content): ")
                            print(f"\nPDF Destination Page Number: {PDF.getDestinationPageNumber(destination)}")
                        except Exception:
                            print("\nData not found...!")
                        else:
                            print(f"Page found successfully...!")
                    elif choice == '3':  # Extracts field data if this PDF contains interactive form fields. The tree and retval parameters are for recursive use.
                        print(f"\nFields in PDF are: {PDF.getFields()}")
                    elif choice == '4':  # Retrieves form fields from the document with textual data (inputs, dropdowns)
                        print(f'\nText fields in PDF are: {PDF.getFormTextFields()}')
                    elif choice == '5':  # Retrieves the named destinations present in the document.
                        print(f"\nName Destination Present in PDF: {PDF.getNamedDestinations()}")
                    elif choice == '6':  # Calculates the number of pages in this PDF file.
                        print(f"\nTotal Pages in PDF: {PDF.getNumPages()}")
                    elif choice == '7':  # Retrieves the document outline present in the document.
                        print(f"\nThe Outlines in the PDF: {PDF.getOutlines()}")
                    elif choice == '8':  # Retrieves a page by number from this PDF file.
                        pageNo = int(
                            input("Enter the page number: "))  # The page number to retrieve (pages begin at zero)
                        print(f"\n{pageNoD:\Sachin folder\Sachin\programming\programming pdfs\Python pdfs\Beginning-Python.pdf} page from PDF: {PDF.getPage(pageNo + 1)}")
                    elif choice == '9':  # Page layout currently being used
                        print(f"\nPage layout of PDF: {PDF.getPageLayout()}")
                    elif choice == '10':  # Page mode currently being used.
                        print(f"\nPage Mode of PDF: {PDF.getPageMode()}")
                    elif choice == '11':  # Read-only boolean property showing whether this PDF file is encrypted
                        print(f"\nPDF Decodeness: {PDF.isEncrypted()}")
                    elif choice == '12':
                        print(f"\nText in the PDF: ")
                        Text(PDF)
                    else:
                        print("\nSomething went wrong...!")
                else:
                    print("Command not in Dict_PDF...!")
            except Exception as E:
                print(f"\nError Occur: {E}")
        finally:
            pdf_File.close()
            print(" \n** Thanks for your valuable time ** \n")
        continue

# 2, 3, 4, 5, 9,
# Not working functions are:
