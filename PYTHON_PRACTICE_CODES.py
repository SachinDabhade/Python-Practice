list1 = [['sachin', 3], ['vaibhav', 32], ['nikhil', 212]]
print(list1)
print("Enter what do you wanna to add in it:")
add1 = input()
add2 = input()
print('this is you added:', add1, add2)
list1.insert(2, [add1, add2])
for items in list1:
    print(items)
    print(list1)
list3 = ['sanjay', 'ajay', 'digvijay', 'saurab', 'sheetal', 45, 46, 3456, 74, 3, 36, 534, 235, 3, 8, 3, 2, 7, 278, 167,
         2, 82, 2523]
for item in list3:
    if str(item).isnumeric() and item >= 8:
        print(item)
if x is int:
    print(x)
print(x)
for items in x:
    print(x)







i = 0

while (i < 53):
    print(i)
    i = i + 1
i = 2









while (i < 12138120):
    print(i)
    i = i + 3472357

    i = i + 1










i = 0
while (True):
    print(i + 2)
    if (i == 2094):
        break
    i = i + 1










print("Enter the random number:\n")

while (True):
    x = int(input())
    if x < 100:
        print("invalid input:please try again")
        continue
    else:
        print("congractulation, you have entered a valid input")
        break










# with a perticular input
n = 28
print('guess the number which is hidden in programme:\n')
while (True):
    x = int(input())
    if x > n:
        print('you entered greater digit than the hidden one...')
        continue
    elif x < n:
        print('you entered lesser digit than the hidden one...')
        continue
    else:
        print('you have entered right number, congratulation')
        break












def function1(a, b):
    """This sentence shows that you have entered in a function and now you are ready to edit this one"""
    print("congratulation, you are in function1")
    sam = a + b
    return sam
a = int(input())
b = int(input())

v = function1(a, b)
print(v)

print(function1.__doc__)

print("Enter the num1:")
num1 = input()
print("Enter the num2:")
num2 = input()
try:
    print('The sum of these two numbers is:', num1 + num2)
except Exception as e:
    print(e)

print("This statement is very important..")














# File IO basics
def func():
    """this is a comment"""
    print("hello world")
    # "r" - Open file for reading(default mode)
    # "w" - Open file for writing
    # "x" - (Exclusive creation) - Create a file that doesnt exist
    # "a" - (append mode) - add more content to a file end
    # "t" - (text mode) - add text to a file(default mode)
    # "b" - (binary mode) - binary form
    # "+" - read as well as write mode
print(func.__doc__)
print(func.__doc__)
print(func.__doc__)
print(func.__doc__)
print(func.__doc__)







f = open("tute8.py", "rt")
for line in f:
    print(line)
f.close()







x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
print(x + y)







f = open("tute8.py", "r+")
print(f.read)
f.append("sachin is the best guy in the world")
f.close()







# Exercise no 4 for harry
print("Enter the number:")
x = int(input())
print("Enter your opinion, True(1) or False(0): \n (1) for true\n(0) for false")
y = int(input())

print("you have entered this number:")

if y == 1:
    print("true")
elif y == 0:
    print("false")
else:
    print("Invalid input...! Please try again....")









# This is seek and tell function for files
f = open("tute8.py")
print(f.readline())
f.seek(0)
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(0)
print(f.readline())
print(f.tell())








# Open any file with with blocks

with open("tute8.py") as f:
    print(f.read())

# This is a programme of stars and boolean variables...

# This project is for the args and the kwargs...sooo keep watching
thelistis = ["sachin", "vaibhav", "Dhiraj", "Nikhik", "sakshi", "manisha", "Jagruti", "XYZ"]
thelistis[1] = "theblackholder"
# print(thelistis)
thelistis.clear()
for i in thelistis:
    print(i)

print(thelistis)
lis = ["sachin", "vaibhav", "Dhiraj", "Nikhik"]
list = {"Nikhil"}
print("Nikhil" in list)
print(lis.index("vaibhav"))
print(lis)









#list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))








import time

initial_time = time.time()
print(initial_time)

if __name__ == '__main__':

    i = 1
    while i < 1500:
        list1 = ["sachin", "vaibhav", "Dhiraj", "Nikhik", "sakshi", "manisha", "Jagruti", "XYZ"]

        x = 1
        for item in list1:
            if x % 2 is not 0:
                print(f"Edith...Please call {item}")
            x += 1
        print("This is the time required for the project:")
        final_time = time.time()
        print(final_time)
        print(final_time - initial_time)

        i = i + 1
        continue









#This is the join function for joining the sentences....with a specific word of symbol...
list1 = ["John", "Cena", "Khali", "Jinder Mahal"]
print(", ".join(list1),end=" ")
print("and other WWE superstars...")
list1 = ["Sachin", "Vaibhav", "Dhiraj", "Nikhil", "Shubham", "Sarvesh", "Rudra", "Princy"]
a = " and ".join(list1)
print(a, "are the family members")








# This is the practice session for map function...
list12 = ["34", "48", "38", "32", "10", "14"]
list1 = list(map(int, list12))
print(list1)
# --------------------------
def funcsquare(x):
    return x * x


num = [2, 1, 3, 3, 3, 563, 25, 2, 53, 4, 1, 53, 24, 4124, 3]
square = list(map(funcsquare, num))
print(num, "and their squares are...", end=" ")
print(square)
# -----------------------
num = [2, 1, 3, 3, 3, 563, 25, 2, 53, 4, 1, 53, 24, 4124, 3]
square = list(map(lambda x:x*x, num))
print(num, "and their squares are...", end=" ")
print(square)
# -------------------------------------------------
def square(a):
    return a * a


def cube(a):
    return a * a * a


func = [square, cube]
for i in range(10):
    a = list(map(lambda x: x(i), func))
    print(a)









# This is the practice for filter function..
def num(num):
    return num >= 5


number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num_greater_than = list(filter(num, number_list))
print(num_greater_than)









# This is the practice for reduce function..
from functools import reduce

A_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
reduce = reduce(lambda x, y: x + y, A_list)
print(reduce)









# This is a practice of decorators function...
def function1():
    print("Subscribe now")
func2=function1
del function1
func2()
# ------------------------------
def funcret(num):
    if num == 0:
        return sum
    if num == 1:
        return print
print(funcret(0))
# -------------------------------
def executor(func):
    func("This is Sachin Dabhade")
executor(print)
# -------------------------------------
def dec1(func1):
    def executor():
        print("Executing now")
        func1()
        print("Executed")
    return executor
def sachin():
    print("Sachin is a goog boy")
sachin=dec1(sachin)
sachin()
# ----------------------------------------
def dec1(func1):
    def executor():
        print("Executing now")
        func1()
        print("Executed")
    return executor
@dec1
def sachin():
    print("Sachin is a goog boy")
sachin()













# --------------------------------------OOPS start----------------------------------------------





# This is the practice for the class (Object oriented proframming)(OOPS)
class student:
    pass

sachin = student()
vaibhav = student()

sachin.name = "Sachin"
sachin.standard = 12
sachin.age = 17
sachin.roll_no = 46
sachin.subjects = ["Maths","Physics","Chemistry"]
vaibhav.name = "Vaibhav"
vaibhav.standard = 16
vaibhav.age = 23
vaibhav.roll_no = "x"
vaibhav.subjects = ["Maths","Physics","Chemistry"]
student()










# This practice is for the class instance variable
class Employee:
    no_of_employee = 1234567890
    pass

sachin = employee()
vaibhav = employee()
sachin.name = "Sachin"
sachin.salary = 2823
sachin.age = 17
sachin.roll_no = 46
sachin.work = "Instructor"
vaibhav.name = "Vaibhav"
vaibhav.salary = 24527
vaibhav.age = 23
vaibhav.roll_no = "Not available"
vaibhav.work = "Technician"

print(employee.no_of_employee)
employee.no_of_employee = 2020
print(employee.no_of_employee)






# This is the practice for the object oriented programming
class employee:
    no_of_employee = 1234567890

    def __init__(self, name, salary, age, roll_no, work):
        self.name = name
        self.salary = salary
        self.age = age
        self.roll_no = roll_no
        self.work = work

sachin = employee("Sachin", 2834, 17, 46, "Instructor")
print(sachin.salary)

vaibhav = employee("Vaibhav", 214789, 23, "none", "Technician")
print(vaibhav.work)









class Employee:
    no_of_employee = 1234567890
    def details(self):
        return f"My name is {self.name}. Salary is {self.salary}. Age is {self.age}. Roll no is {self.roll_no} and work is {self.work}. "
sachin = employee()
vaibhav = employee()

sachin.name = "Sachin"
sachin.salary = 2823
sachin.age = 17
sachin.roll_no = 46
sachin.work = "Instructor"

vaibhav.name = "Vaibhav"
vaibhav.salary = 24527
vaibhav.age = 23
vaibhav.roll_no = "Not available"
vaibhav.work = "Technician"
print(vaibhav.details())











# This video is about calss method and their uses
class Employee:
    no_of_employee = 1234567890


    @classmethod
    def change_employee(cls, newemployee):
        cls.no_of_employee = newemployee

employee.change_employee(200)
print(employee.no_of_employee)








# This method is alternative method used in @classmethod
class employee:
    no_of_employee = 2020

    def __init__(self, aname, asalary, aage, aroll_no, awork):
        self.name = aname
        self.salary = asalary
        self.age = aage
        self.roll_no = aroll_no
        self.work = awork

    def details(self):
        return f"My name is {self.name}.\nSalary is {self.salary}.\nAge is {self.age}.\nRoll no is {self.roll_no} and work is {self.work}. "

    @classmethod
    def from_dash(cls, string):
        ram = string.split("-")
        return cls(ram[0], ram[1], ram[2], ram[3], ram[4])

    @classmethod
    def dash(cls, string):
        return cls(*string.split("-"))

    @classmethod
    def change_employee(cls, newemployee):
        cls.no_of_employee = newemployee

sachin = employee("sachin", 2000, 17, 46, "supervisor")
vaibhav = employee("vaibhav", 5000, 23, "not available", "Engineer")
dhiraj = employee.dash("dhiraj-3000-22-not available-Instructor")

sachin.change_employee(1922)
print(sachin.no_of_employee)

print(dhiraj.details())









# This is the practice on OOPs on @staticmethod
class employee:
    no_of_employee = 2020

    def __init__(self, aname, asalary, aage, aroll_no, awork):
        self.name = aname
        self.salary = asalary
        self.age = aage
        self.roll_no = aroll_no
        self.work = awork

    def details(self):
        return f"My name is {self.name}.\nSalary is {self.salary}.\nAge is {self.age}.\nRoll no is {self.roll_no} and work is {self.work}. "

    @classmethod
    def dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def good(string):
        print("This is good" + string)


sachin = employee("sachin", 2000, 17, 46, "supervisor")
vaibhav = employee("vaibhav", 5000, 23, "not available", "Engineer")
dhiraj = employee.dash("dhiraj-3000-22-not available-Instructor")
dhiraj.good(" vaibhav")










# This is practice for the single inheritance from class:
class programmer(employee):
    holidays = 65

    def __init__(self, aname, asalary, aage, aroll_no, awork, language):
        self.name = aname
        self.salary = asalary
        self.age = aage
        self.roll_no = aroll_no
        self.work = awork
        self.language = language


    def mydetails(self):
        return f"My name is {self.name},salary is {self.salary} and language are {self.language}"

sai = programmer("vaibhav", 5000, 23, "not available", "Engineer",["python", "C++"])
print(sai.mydetails())











# This is practice for the multiple inheritance in class
class employee:
    no_of_employee = 2020

    def __init__(self, aname, asalary, aage, aroll_no, awork):
        self.name = aname
        self.salary = asalary
        self.age = aage
        self.roll_no = aroll_no
        self.work = awork

    def details(self):
        return f"My name is {self.name}.\nSalary is {self.salary}.\nAge is {self.age}.\nRoll no is {self.roll_no} and work is {self.work}. "

    @classmethod
    def dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def good(string):
        print("This is good" + string)

class player:

    def game_details(self):
        return f"The player name is {self.name} and age is {self.age}"

class programmer(employee, player):

    def det_prog(self):
        return f'Programmer\'s name is {self.name} and work as a {self.work}'

sachin = employee("sachin", 2000, 17, 46, "supervisor")
vaibhav = employee("vaibhav", 5000, 23, "not available", "Engineer")
# sai = player("Sai", 2300, 15, "not available", "player")
dhis = programmer("dhis", 2000, 17, 46, "supervisor")
print(dhis.det_prog())










# This is the practice for multilevel inheritance
class Dad:
    name = "Kalpesh"
    tabla = "visharad"
    harmonium = "intermediate"
    flute = "beginer"
    def art(self):
        return f"My name is {self.name} I am a tabla {self.tabla}, harmonium {self.harmonium} as well as a flute {self.flute} player"

class Son(Dad):
    name = "Swalpesh"
    tabla = "pandit"
    harmonium = "visharad"
    flute = "intermediate"
    def art(self):
        return f"My name is {self.name} I am a tabla {self.tabla}, harmonium {self.harmonium} as well as a flute {self.flute} player"

class Grandson(Son):
    name = "Kiran"
    tabla = "pandit"
    harmonium = "pandit"
    flute = "pandit"
    def art(self):
        return f"My name is {self.name} I am a tabla {self.tabla}, harmonium {self.harmonium} as well as a flute {self.flute} player"


Kalpesh = Dad()
Swalpesh = Son()
Kiran = Grandson()

print(Kiran.art())













# This is a practice for public, protected and private variables
class Employee:
    sachin = 1234567890             # This is a public variable
    _sachin = 2020                  # This is a protected variable
    __sachin = 2010                 # This is a private variable

    def __init__(self, aname, asalary, aage, aroll_no, awork):
        self.name = aname
        self.salary = asalary
        self.age = aage
        self.roll_no = aroll_no
        self.work = awork


    def employee(self):
        pass

sai=Employee("sachin",23,234,23,"xyz")
print(sai._Employee__sachin) # We get access of private variable in this manner












# This is practice of polyorphism in python
# polymorphism is the ability to take various form in same inheritated class
for e.g
print(5+)
print("5" + "6")
# In the above example, the "+" sign takes the polymorphism which takes various forms in various situation







# This is a practice about the super and overridin g in python
class A:
    classvar11 = "I am a class variable in class A"
    def __init__(self):
        self.classvar11 = "I am a instance variable in constructor of class A"
        self.variable = "special"
class B(A):
    classvar11 = "I am a class variable in class B"
    def __init__(self):
        self.classvar11 = "I am a instance variable in constructor of class B"
        self.var2 = "special B"
        super().__init__()
        print(super().classvar11)
a = A()
b = B()
print(b.classvar11)










# This is a problem which programmer face in their programme while using multiple inheritance or multilevel inheritance. This problem we face when we work in different language...!
for e.g
class A:
    def met(self):
        return "This is the funcion in class A"
class B(A):
    def met(self):
        return "This is the funcion in class B"
class C(A):
    def met(self):
        return "This is the funcion in class C"
class D(B,C):
    def met(self):
        return "This is the funcion in class D"
a = A()
b = B()
c = C()
d = D()
print(d.met())










# This is the practice of coding on OOPs on operator overloading and dunder method
class employee:
    no_of_employee = 2020
    def __init__(self, aname, asalary, aage, aroll_no, awork):
        self.name = aname
        self.salary = asalary
        self.age = aage
        self.roll_no = aroll_no
        self.work = awork
    def details(self):
        return f"My name is {self.name}.\nSalary is {self.salary}.\nAge is {self.age}.\nRoll no is {self.roll_no} and work is {self.work}. "
    @classmethod
    def dash(cls, string):
        return cls(*string.split("-"))
    @staticmethod
    def good(string):
        print("This is good" + string)
    def __repr__(self):
        return f"This programme have alogrithm like (\"name\", salary, age, roll_no, \"work\")"
    def __str__(self):
        return f"This is the practice of coding and programming."
    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
emp1 = employee("Vaibhav", 4000, 17, 4, "Cleaner")
emp2 = employee("Sachin", 40, 17, 46, "Instructor")
print((emp1))










# This is the practice of abstract base class on OOPs programming
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def shape(self):
        return "SHAPE"

class employee(Shape):
    no_of_employee = 2020
    def __init__(self, aname, asalary, aage, aroll_no, awork):
        self.name = aname
        self.salary = asalary
        self.age = aage
        self.roll_no = aroll_no
        self.work = awork
    def details(self):
        return f"My name is {self.name}.\nSalary is {self.salary}.\nAge is {self.age}.\nRoll no is {self.roll_no} and work is {self.work}. "
    @classmethod
    def dash(cls, string):
        return cls(*string.split("-"))
    @staticmethod
    def good(string):
        print("This is good " + string)
    def __repr__(self):
        return f"This programme have alogrithm like (\"name\", salary, age, roll_no, \"work\")"
    def __str__(self):
        return f"This is the practice of coding and programming."
    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def shape(self):
        print(f"Sachin Vinayak Dabhade is the brother of Vaibhav Vinayak Dabhade")
emp1 = employee("Vaibhav", 4000, 17, 4, "Cleaner")
emp2 = employee("Sachin", 40, 17, 46, "Instructor")
emp1.shape()









# This is the practice of setters and property in OOPs of python
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def detail(self):
        return f"The employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "The email is not set.. Please set it by using setter"
        return f"{self.fname}.{self.lname}@codewithsachin.com"

    @email.setter
    def email(self, string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

obj = Employee("Sachin", "Dabhade")
print(obj.email)
obj.email = "this.that@codewithharry.com"
print(obj.email)
del obj.email
print(obj.email)









# This is the practice of introspection in python and inspect module in python
import  inspect
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def detail(self):
        return f"The employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "The email is not set.. Please set it by using setter"
        return f"{self.fname}.{self.lname}@codewithsachin.com"

    @email.setter
    def email(self, string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

obj = Employee("Sachin", "Dabhade")
print(type(obj))
print(id(obj))
print(dir(obj))
print(inspect.getmembers(obj))
# ----------------------------------------------OOPS finish----------------------------------------------












# This is the practice for the iterables, iterators and iteration and generators
iterable - __iter__() or __getitem__() runs
iterator - __next__() function runs
iteration - process in which we iterate the iterable is called iteration
# This is the general method in which memory space become decrease
for i in range(1000001):
    print(i)
# This is the memory saving way for forloop
def generator(n): # It generate the value on the ply to save the memory space
    for i in range(n):
        yield i
g = generator(1000)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
for i in g:
    print(i)








# This is the code of python comprehensions for absolutely begineers Python list comprehension

We generally write code like this

ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)
print(ls)

This is the short tricks for the code of python list comprehension
ls = [i for i in range(100) if i % 3 == 0]
print(ls)








# Dictionary comprehension

# This is the long tricks for writing code of list

list = {1:"itemi", 2:"item2"}
print(list)

# This is the short trick for python list comprehension

list = {i:f"item{i}" for i in range(1,10001)}
print(list)

# This is the short tricks for writing code of reversing list

list1 = {i:f"item{i}" for i in range(1,10)}
list1 = {value:key for key, value in list1.items()}
print(list1)









# This practice is all about using else with the for loop
subjects = ["Marathi", "English", "Hindi", "Algebra", "Geometry", "Science"]
for items in subjects:
    if items in subjects:
        print(items, end = ", ")
    else:
        print("You have to take the right path")
        break
else:
    print("\nThe loop is run successfully...")








# This is the practice of lru cacheing decorators for python.
import time
from functools import lru_cache
@lru_cache(maxsize=5)
def some_work(n):
     time.sleep(n)
     print("Work is done...")

if __name__ == '__main__':
    print("Hey, I am doing some work...")
    some_work(3)
    some_work(3)
    some_work(3)
    some_work(3)
    print("Hey, work finished...")








# This practice goes for the try, except Exception as e:
f = open("mylogs.txt", "a")
try:
    f2 = open("Harry.txt","a")
except Exception as e:   # We can use the multiple exception in our code
    print(e)
else:
    print("This will run when except doesnt run")
finally:       # This will definately run although the error found or not
    print("Imp")
    f.close()
    try:
        f2.close()
    except Exception as e:
        print(e)








# This is the practice of coroutine in python that allows you to save the run time of code
import time
def searcher():
    """This is the programme of coroutine which saves the execution time of the programme"""
    book = "This is the python basics book in your library"
    time.sleep(4)
    while True:
        text = (yield )
        if text in book:
            print("Hey, \"you are in loop\"")
        else:
            print("Sorry, you are not in loop")
search = searcher()
next(search)
search.send("python")
input("Enter any key...")
search.send("basics")
search.close()    # after closing the search coroutine in python it doesnt accept any coroutine values
search.send("programme")     # this will give an error...










# This is the practice of Operating system (OS) which is a builtin modules
import os
a = (dir(os))
print(len(a))
print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())   # While we change the directory it finding the mylogs.txt in new directory where it is not available and thats why it gives an error
f = open("mylogs.txt")  # So it doesn't open
print(os.listdir())
print(os.listdir("C:\\"))
# os.mkdir("Sachin")
# # os.makedirs("This/that")
# os.rename("Sachin", "sac")
print(os.environ.get("Path"))
print(os.path.exists("C://"))
print(os.path.isdir("C://"))












# Operating System practice
"""Practice for operating system to change the names and series of the
folders and the png which harry says in their exercise,
but i dont know about that perticular topic so i only practice that session"""
import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")
    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1]==format:
            os.rename(file,f"{i}{format}")
            i = i+1
if __name__ == '__main__':
    soldier(r"D:\Sachin folder",
            r"D:\Sachin folder\Mobile\folder",
            ".png")









# This is the practice  pickel module in python
import pickle
list = ["Audi", "Alto", "Maruti Suzuki", "Karisma", "Dukati", "BMW", "Lamorgini"]
file = "cars.pkl"
fileobj = open(file, "wb")
pickle.dump(list, fileobj)
fileobj.close()
file = "cars.pkl"
files = open(file, "rb")
fileobj = pickle.load(files)
print(fileobj)
print(type(fileobj))









var1=23
var2=934
print("enter any random number:")
var3=int(input())
if var3>var2>var1:
    print("its greater number")
elif var3==var2>var1:
    print("var3 and var2 are equal but var1 is lesser")
elif var2>var3>var1:
    print("var3 is greater than var1 but less than  var2")
elif var2>var1>var3:
    print("var3 is lesser than both var1 and var2")
elif var1==var3<var2:
    print('var3 is equal to var1')
else:
    print("its lesser number")
l = [3,5,52,2,23,52,23,425,52,213]
print("enter the number you want to find in the list:")
x = int(input())
print(x in l)
if x in l:
    print("yes, its in list")
else:
    print("its not in list")








# List comprehension for python
dict = {}
for n in range(21):
    dict[n] = n**2
print(dict)
dict1 = {n:n*2 for n in range(10)}
print(dict1)









# Difference between "equal to (==)" and "is" in python
a = [3,123,2,4]
b = a
c = a
print(c == a)
print(c is a)
c = a[:]
print(c is a)
# task
a = [4,5,"53"]
b = [4,5,"53"]
print(a is b)
print(b is a)










# This is the python command line utility
import sys
import argparse
def cal(args):
    if args.o == "addition":
        return args.x + args.y
    if args.o == "subtraction":
        return args.x - args.y
    elif args.o == "multiplication":
        return args.x * args.y
    elif args.o == "raise to ":
        return args.x ** args.y
    elif args.o == "divide":
        return args.x / args.y
    elif args.o == "root":
        return args.x // args.y
    else:
        return "Invalid Error....!"
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=1.0, help="Enter the first number:")
    parser.add_argument("--y", type=float, default=3.0, help="Enter the second number:")
    parser.add_argument("--o", type=str, default="sum", help="Enter the operation:")
    args = parser.parse_args()
    sys.stdout.write(str(cal(args)))






# This is the python practice unsuccesfully solved problem
import random
def splitNames():
    i = 1
    for item in list:
        item.strip().split(" ")
        if i == 1:
            split_1.append(item)
        elif i ==2:
            split_2.append(item)
        elif i == 3:
            split_3.append(item)
        elif i == 4:
            split_4.append(item)
        elif i == 5:
            split_5.append(item)
        else:
            print("Sorry..! Number of names is exceed in a perticular name...!")
        i += 1
    list.clear()
if __name__ == '__main__':
    list = []
    split_1 = []
    split_2 = []
    split_3 = []
    split_4 = []
    split_5 = []
    while True:
        try:
            num = int(input("Enter the number of friends:\n"))
        except Exception as e:
            print("Only Integers are allowed...!\n")
            continue
        for item in range(num):
            f_names = input("Enter the names of friends:")
            list.append(f_names)
        splitNames()
        split_1.sort()
        split_2.sort()
        split_3.sort()
        split_4.sort()
        split_5.sort()
        continue



# ---------------------------------* Here I Have finished the python course *----------------------------


# ------------------------------* This is the Intermediate / Advanced python tutorial for absolute begineer *--------------

# Tutorial no 1
# This is the advance tutorial for { if __name__=="__main__" }

# This is demo.py file
import os
def veryIMPfunction():
    print("Sachin want to be coder...!")
# a = os.listdir("/")
# print(a)
# veryIMPfunction()
# To avoid the useless part other than the function, we uses the if (__name__=="__main__")
print(f"This is coming from {__name__} file")
if __name__ == '__main__':
    print(os.listdir("/"))
    veryIMPfunction()

# This is Demo.py file
"""We are importing the file from the sachinfile.py and file name is demo.py and this file name is Demo.py"""
import demo as at
at.veryIMPfunction()
print("This is giving me the two print statements of function..")









# Tutorial no 2
# This is the advance tutorial for *args and **kwargs

"""In *args and **kwargs the name args and kwargs doesnt matter the programme"""
# This is the normal method to use the function
def func_1(name, age, roll_no):
    print(f"The name of student is {name}\n"
          f"The age of student is {age}\n"
          f"The roll no of student is {roll_no}")
def func_2(*args):
    # Remember that the type of *args is "tuple"
    print(type(args))
    for i in range(1):
        if len(args) == 3:
            print(f"The name of student is {args[i]}, age of student is {args[i + 1]} and roll no of student is {args[i + 2]}")
        elif len(args) == 2:
            print(f"The name of student is {args[i]} and age of student is {args[i + 1]}")
        elif len(args) == 1:
            print(f"The name of student is {args[i]}")
        else:
            print("Limit is exceed than three arguments...!")
        break
def func_3(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"The marks of {key} is {value}")
def func_2_duplicate(*args):
    # Remember that the type of *args is "tuple"
    print(type(args))
    for args in duplicate_args_list:
        for i in range(1):
            if len(args) == 3:
                print(f"The name of student is {args[i]}, age of student is {args[i + 1]} and roll no of student is {args[i + 2]}")
            elif len(args) == 2:
                print(f"The name of student is {args[i]} and age of student is {args[i + 1]}")
            elif len(args) == 1:
                print(f"The name of student is {args[i]}")
            else:
                print("Limit is exceed than three arguments...!")
            break
def master(normal, *args, **kwargs):
    print(normal)
    for i in range(1):
        if len(args) == 3:
            print(f"The name of student is {args[i]}, age of student is {args[i + 1]} and roll no of student is {args[i + 2]}")
        elif len(args) == 2:
            print(f"The name of student is {args[i]} and age of student is {args[i + 1]}")
        elif len(args) == 1:
            print(f"The name of student is {args[i]}")
        else:
            print("Limit is exceed than three arguments...!")
        break
    for key, value in kwargs.items():
        print(f"The marks of {key} is {value}")

if __name__ == '__main__':
    list_kwargs = {"Sachin": 100, "Vaibhav": 97}
    # func_1("Sachin", 18, 46) # Normal method
    # func_2("Sachin", 18, 46) # *args method
    # func_3(**list_kwargs)
    """We can also use these instances in the list form.."""
    list_args = ["Vaibhav", 18, 46]
    # func_2(*list_args)
    """We can also load list of list in the *args section"""
    duplicate_args_list = [["Sachin", 18, 46], ["Vaibhav", 28, 96], ["Ujjwal", 19, 74],["Divya", 17]]
    # func_2_duplicate(*duplicate_args_list)
    """We can also execute the all three arguments in the same function"""
    master("This is my normal argument which perform normal tasks on daily basis", *list_args, **list_kwargs)
    """Harry bhai, this is soo good lecture on args and kwargs, thankful to you"""










# Tutorial no 3
# This is the advance python tutorial for the try, except, else, finally commands

try:
    file = open("this.txt", "r")
except ValueError as e:
    print("Sorry...! Give the appropriate value...!")
except IndexError as e:
    print("Sorry...! Please make sure that the range is correct or not...!")
else:
    print("This will run if the exception is not occur")
finally:
    print("This block will permanently run")






# Tutorial no 4
# This is the advanced python tutorial on virtual environment
"""
error_solution = change the execution policy by writing - "set-executionpolicy remotesigned"
1. open the specific folder for the virtual Environment in windows powershell or command prompt as an admin
2. To activate virtual environment, we have to import the 'virtualenv' module in this specific folder
3. Write the name of virtual environment by writing 'virtualenv sachin' - it will make sure the first step of virtual environment
4. To activate the virtual environment, write the path and write scripts/activate. Ex ('virtualenv_folder_name/scripts/activate')
5. And this is done, Congratulation, your virtual environment is created...!
6. Its ok to make the virtual environment, but whenever you have to share the virtual environment file to the other person then...!
   I will recommend you to make the requirements.txt file for the best user experience Ex. (Just you have to write - "pip freeze > requirements.txt") 
7. To get out from the virtual environment we have to write - "deactivate" in our IDE
8. If we want to make the virtual environment that can use the main python packages then use the command out of the virtual environment /
   while making the virtual environment - "virtualenv --system-site-packages (name of the folder/file)"
9. To delete the virtual environment - 1. deactivate the environment 2. write - "del (name of the folder/file)"
10. To install requirements.txt files write - "pip install -r requirements.txt"
"""








# Tutorial no 5
# This is the advance python tutorial on iterator, iterable and iteration
"""
1. Iterable - The object which define "__iter()__" or "__getitem()__" method
2. Iterator - The object which define "next()" method
3. Iteration - Process in which we iterate the iterables is known as iteration
4. Generators - The generator are those who generates the number on the fly
"""
def generator(num):
    for item in range(num):
        yield item
if __name__ == '__main__':
    print(generator(100))
    for item in generator(100000):
        print(item)
    gen = generator(100)
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    """We can also use this method to generate the numbers"""
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    number = 1000
    str = "sachin"
    for i in number: # This will not be iterable the number coz int object is not iterable
        print(i)
    for i in str: # This will iterable coz str is iterable
        print(i)
    iterable = iter(str)
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))








# Tutorial no 6
# This is the advance python tutorial on comprehension of list, dictionary, set and generator
"""
Basically, python is the very simple yet readable language in among the other language. If we dont use the python as it is popular for then its totally waste
The comprehensions make it better and fast to write. Firstly we have to understand their syntax. These is simple to write.
"""

# 1. List Comprehension
list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# This is the simple method we use daily
divide_3 = []
for i in list_1:
    if i%3 == 0:
        divide_3.append(i)
print(divide_3)

# This is the list comprehension method
divide_1_3 = []
print([i for i in list_1 if i%3 == 0])
# 2. Dictionary Comprehension
dict_1 = {'sachin': 45, 'vaibhav': 50, 'SACHIN': 5}
print("This is the dictionary comprehension", {k.lower():dict_1.get(k.lower(), 0) + dict_1.get(k.upper(), 0) for k in dict_1.keys()})

# This is the set comprehension
square = {x**2 for x in [1,1,2,3,3,3,4,4,5,6,7,8,9,9,9]}
print(square)

# This is the generator comprehension
gen = (i for i in range(56) if i%3 == 0)
for i in gen:
    print(i, end=" ")








# Tutorial no 7
# This is the advanced python tutorial on map, filter and reduce function
# Map Function
"""
1. Map function runs like a for loop
2. We can iterate the elements of list, set, tuple etc
3. Syntax - map(Function/lambda without braces, list,set,tuple,etc)
4. Lambda function make the map function slow than the for loop
5. Map function is better for other than lambda function
6. We have to type-caste it in the form of list, tuple, set coz it make only objects not the list, set, tuple, etc
7. While using the map function we do not have to call the function only write the function name
"""
def square(n):
    return n**2
def cube(n):
    return n**3
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
map_list = tuple(map(square, list))
print(map_list)
map_2_list = tuple(map(cube, list))
print(map_2_list)
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

# Filter Function
"""
1. The filter object is of the iterable type. It retains those elements which the function passed by returning True.
2. Filter filters the list, tuple, set, dict, etc and return the true value
3. Syntax - filter(function/lambda, iterables)
4. Filter is mainly use for the true returning values 
5. We have to type-caste this filter objects in the list, tuple, set, dict, etc
6. Do not call the function in syntax, we have to write only function name. 
7. It mainly filter the true returning values
"""
def Great_2(n):
    if n > 4:
        return True
    else:
        return False
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
greater_than_4 = list(filter(Great_2, list))
print(greater_than_4)

# Reduce Function
"""
1. We have to import the reduce function from functools
2. Mainly reduce function is apply on total iterables like list, tuple, set, etc
3. It apply on all elements one by one 
4. mainly it reduces the size of list by applying the function
5. Unlike map and reduce function we do not have to typecast the reduce function
6. Syntax - reduce(function/lambda, iterable)
"""
from functools import reduce
def sum(a, b):
    return a+b
def mult(a, b):
    return a*b
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
reduce_list = reduce(sum, list)
print(reduce_list)
reduce_list_2 = reduce(mult, list)
print(reduce_list_2)









# Tutorial no 8
# This is the advanced python tutorial on Lambda function
"""
Lambda are the one line function
It require less time to write
Syntax = argument : manipulate(argument)
"""
sum = lambda a, b : a + b
print(sum(8, 9))
mult = lambda a, b : a * b
print(mult(8, 7))sum = lambda a, b : a + b
print(sum(8, 9))
mult = lambda a, b : a * b
print(mult(7, 6))
greater = lambda a, b : a > b
print(greater(7, 8))
sort = [(2,13), (1,23), (73,2)]
sort.sort(key=lambda x: x[0])
print(sort)
lkj = [(23, 43), (234,524), (324, 923), (1, 0)]
lkj.sort(key=lambda d:d[0])
print(lkj)








# Tutorial no 9
# This is the advanced python tutorial on advance list slicing
"""
1. List slicing is the very inportant yet easy step in python
2. The reversing of list is good one in python
"""
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(List[0:16])
print(List[1:14])
print(List[1:10:2])
print(List[1:10:4])
print(List[3:0:-2])
print(List[15:0:-3])
print(List[10:0]) # This will not work properly
print(List[10:0:-1]) # This will work properly
print(List[0:-3])
print(List[-2:-10]) # This will not run properly
print(List[-2:-10:-1])
print(List[-9:-1])







# Tutorial no 10
# This is the advanced python tutorial on bisect modules
"""
We can use bisect module for getting the index number to insert at appropriate place
"""
import bisect
num = 45
list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
print(bisect.bisect(list, num))
bisect.insort(list, num)
print(list)
list = [1, 21, 3, 4, 55, 5, 6, 7, 8, 9, 10]
bisect.insort(list, num) # This shows thet the bisect module assume that your list is sorted
print(list)






# Tutorial no 11
# This is the advanced tutorial on Enumerate function
channel = ['Codewithharry', 'Sachin', 'advance', 'geography']
i = 0
# Without enumerate function
for item in channel:
    i += 1
    if i % 2 == 0:
        print(item)
# With enumerate function
for i, item in enumerate(channel):
    if (i + 1) % 2 == 0:
        print(i, item)







# Tutorial no 12
# This is the advance python tutorial on format function
"""
The format function gives the sent of c++ or java programming
"""
users = ['Sachin', 'Vaibhav', 'Nikhil', 'Neha', 'Shubham']
computer = ['Kali linux', 'Linux', 'Windows', 'AMD', 'Intel']
for item in range(len(users)):
    # Various types to write this programme
    print(f'The computer used by {users[item]} is {computer[item]}')
    print('The computer used by' + users[item] + 'is' + computer[item])
    tempelate = "The computer used by {} is {}"
    print(tempelate.format(users[item], computer[item]))







# Tutorial no 13
# This is the advanced python tutorial on join function
"""
1. In join function, we have to parsed a list in this function
2. syntax - 'item'.join(parsed list)
3. Remember that the first argument have to item have to join and then the join function and then parsed the list we have to apply on it
"""
users = ['Sachin', 'Vaibhav', 'Nikhil', 'Neha', 'Shubham']
print(' and '.join(users))

computer = ['Kali linux', 'Linux', 'Windows', 'AMD', 'Intel']
print('We have the computers like', end=' ')
print(' and '.join(computer))



# ----------------------------------* Here I have finished the advance python tutorial *-----------------------------


# ----------------------------------* Here I have basic python tutorial *-----------------------------


# Tutorial no 1
# How to find the execution time of any python programme
"""
1. Import the time module or import time from time
2. take the initial time and final time
3. minus the initial time by the final time
"""
import time
initial = time.time()
list = []
for item in range(10000):
    list.append(item)
print(list)
final = time.time()
print("The execution time of the above python programme is:", final - initial)






# Tutorial no 2
# This is the basic python tutorial on finding the palindrome of a number
while True:
    num = input("Enter the number:")
    for i in range(1):
        rev_num = num[::-1]
        if num == rev_num:
            print("This number is palindrome...!")
        else:
            print("This is not a palindrome...!")
    continue








# Tutorial no 3
# This is the basic python tutorial on calculating factorial
from time import time
def factorial(number):
    if number < 0:
        output = "not possible...!"
    elif number == 0:
        output = 1
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial = factorial * i
        print(len(str(factorial)))
        output =  factorial
    return "The factorial of " + str(number) + " is " + str(output)
if __name__ == '__main__':
    while True:
        number = int(input("Enter the number:"))
        init = time()
        print(factorial(number))
        final = time() - init
        print(final)
        continue






# Tutorial no 4
# This is the basic python tutorial on converting the python(py) file into the executive(exe) file
"""
1. As same as making the virtual environment it also have to install a module - name - pyinstaller
2. Then simply open the folder which you want to convert into executable file in any IDE or in prwershell or in command prompt
3. Simply write - "pyinstaller (folder name/py. file name) and run it
4. It may take some time, so make sure you have completed the whole process
5. If you want to get all files into one file then give the command - "pyinstaller --onefile (folder name/py. file name)" and thats it. 
"""



# --------------------------------* Here i have completed basic python programming course *-----------------------------


# ---------------------------------****--------------------------------------


# --------------------------------* Here i have Started Object Oriented programming course *-----------------------------




# Tutorial no 1:
# This is the OOPs Tutorial Explaining about OOPs

class Employee:
    def __init__(self, name, age, salary, work):
        self.name = name
        self.age = age
        self.salary = salary
        self.work = work

rohan = Employee("Rohan", 22, 40000, "Developer")
harry = Employee("Harry", 22, 40000, "Hacker")

# rohan.name = "Rohan"
# rohan.age = 22
# rohan.salary = 40000
# rohan.work = "Developer"
#
# harry.name = "Harry"
# harry.age = 22
# harry.salary = 40000
# harry.work = "Hacker"

print(rohan.name, harry.name





# Tutorial no 2
# This is the OOPs tutorial on use of oOPs in python

class Employee:
    increnment = 1.5
    no_of_employee = 0
    def __init__(self, name, age, salary, work):
        self.name = name
        self.age = age
        self.salary = salary
        self.work = work
        self.increnment = 2
        Employee.no_of_employee += 1

    def Increase(self):
        # self.salary = int(self.salary * Employee.increnment)
        self.salary = int(self.salary *  self.increnment)


print(Employee.no_of_employee)
rohan = Employee("Rohan", 22, 40000, "Developer")
print(Employee.no_of_employee)
harry = Employee("Harry", 22, 40000, "Hacker")
print(Employee.no_of_employee)

# rohan.name = "Rohan"
# rohan.age = 22
# rohan.salary = 40000
# rohan.work = "Developer"
#
# harry.name = "Harry"
# harry.age = 22
# harry.salary = 40000
# harry.work = "Hacker"

# print(rohan.salary, harry.salary)

print(harry.salary)
harry.Increase()
print(harry.salary)
print(harry.__dict__)

"""
We can see all the instance variable of the class by using the argument - "print(harry.__dict__)"
"""





# Tutorial no 3
# This is the OOPs tutorial on how to use the class method in python OOPS

class Employee:
    increnment = 1.5
    no_of_employee = 0
    def __init__(self, name, age, salary, work):
        self.name = name
        self.age = age
        self.salary = salary
        self.work = work
        self.increnment = 2
        Employee.no_of_employee += 1

    def Increase(self):
        self.salary = int(self.salary * Employee.increnment)
        # self.salary = int(self.salary *  self.increnment)

    @classmethod
    def change_Increnment(cls, amount):
        cls.increnment =  amount




print(Employee.no_of_employee)
rohan = Employee("Rohan", 22, 40000, "Developer")
print(Employee.no_of_employee)
harry = Employee("Harry", 22, 40000, "Hacker")
print(Employee.no_of_employee)

# rohan.name = "Rohan"
# rohan.age = 22
# rohan.salary = 40000
# rohan.work = "Developer"
#
# harry.name = "Harry"
# harry.age = 22
# harry.salary = 40000
# harry.work = "Hacker"

# print(rohan.salary, harry.salary)

# print(harry.salary)
# harry.Increase()
# print(harry.salary)
# print(harry.__dict__)

"""
We can see all the instance variable of the class by using the argument - "print(harry.__dict__)"
"""


print(harry.salary)
Employee.change_Increnment(4)
harry.Increase()
print(harry.salary)








# Tutorial no 4
# This is the OOPs tutorial on how to use the classmethod for getting diffferent types of instance variable by user

class Employee:
    increnment = 1.5
    no_of_employee = 0
    def __init__(self, name, age, salary, work):
        self.name = name
        self.age = age
        self.salary = salary
        self.work = work
        self.increnment = 2
        Employee.no_of_employee += 1

    def Increase(self):
        self.salary = int(self.salary * Employee.increnment)
        # self.salary = int(self.salary *  self.increnment)

    @classmethod
    def change_Increnment(cls, amount):
        cls.increnment =  amount

    @classmethod
    def from_str(cls, emp_string):
        name, age, salary, work = emp_string.split("-")
        return cls(name, age, salary, work)



print(Employee.no_of_employee)
rohan = Employee("Rohan", 22, 40000, "Developer")
print(Employee.no_of_employee)
harry = Employee("Harry", 22, 40000, "Hacker")
print(Employee.no_of_employee)
lovish = Employee.from_str("lovish-22-40000-Developer")
print(lovish.name, lovish.age, lovish.salary, lovish.work)
# rohan.name = "Rohan"
# rohan.age = 22
# rohan.salary = 40000
# rohan.work = "Developer"
#
# harry.name = "Harry"
# harry.age = 22
# harry.salary = 40000
# harry.work = "Hacker"

# print(rohan.salary, harry.salary)

# print(harry.salary)
# harry.Increase()
# print(harry.salary)
# print(harry.__dict__)

"""
We can see all the instance variable of the class by using the argument - "print(harry.__dict__)"
"""


# print(harry.salary)
# Employee.change_Increnment(4)
# harry.Increase()
# print(harry.salary)







# Tutorial no 5
# This is the OOPs tutorial on how to use the staticethod for making the separate function which didn't use the any type of instance

class Employee:
    increnment = 1.5
    no_of_employee = 0
    def __init__(self, name, age, salary, work):
        self.name = name
        self.age = age
        self.salary = salary
        self.work = work
        self.increnment = 2
        Employee.no_of_employee += 1

    def Increase(self):
        self.salary = int(self.salary * Employee.increnment)
        # self.salary = int(self.salary *  self.increnment)

    @classmethod
    def change_Increnment(cls, amount):
        cls.increnment =  amount

    @classmethod
    def from_str(cls, emp_string):
        name, age, salary, work = emp_string.split("-")
        return cls(name, age, salary, work)

    @staticmethod
    def isOpen(day):
        if day.lower() == 'sunday':
            return 'Your office is closed'
        else:
            return 'Your office is open'



# print(Employee.no_of_employee)
# rohan = Employee("Rohan", 22, 40000, "Developer")
# print(Employee.no_of_employee)
# harry = Employee("Harry", 22, 40000, "Hacker")
# print(Employee.no_of_employee)
# lovish = Employee.from_str("lovish-22-40000-Developer")
# print(lovish.name, lovish.age, lovish.salary, lovish.work)

# rohan.name = "Rohan"
# rohan.age = 22
# rohan.salary = 40000
# rohan.work = "Developer"
#
# harry.name = "Harry"
# harry.age = 22
# harry.salary = 40000
# harry.work = "Hacker"

# print(rohan.salary, harry.salary)

# print(harry.salary)
# harry.Increase()
# print(harry.salary)
# print(harry.__dict__)

"""
We can see all the instance variable of the class by using the argument - "print(harry.__dict__)"
"""

print(Employee.isOpen('sunday'))
print(Employee.isOpen('monday'))







# Tutorial no 6
# This is the OOPs tutorial on how to use the inheritance to make code reusable and how inheritance work

class Employee:
    increnment = 1.5
    no_of_employee = 0
    def __init__(self, name, age, salary, work):
        self.name = name
        self.age = age
        self.salary = salary
        self.work = work
        self.increnment = 2
        Employee.no_of_employee += 1

    def Increase(self):
        self.salary = int(self.salary * Employee.increnment)
        # self.salary = int(self.salary *  self.increnment)

    @classmethod
    def change_Increnment(cls, amount):
        cls.increnment =  amount

    @classmethod
    def from_str(cls, emp_string):
        name, age, salary, work = emp_string.split("-")
        return cls(name, age, salary, work)

    @staticmethod
    def isOpen(day):
        if day.lower() == 'sunday':
            return 'Your office is closed'
        else:
            return 'Your office is open'

class Programmer(Employee):
    def __init__(self, name, age, salary, work, language, experience):
        super().__init__(name, age, salary, work)
        self.language = language
        self.experience = experience

sachin = Programmer("Sachin", 18, 000000, "Programmer", "Python", "Fresher")
print(sachin.work)
help(Programmer)
help(Employee)

"""
We have the help function in classes to get know about what we have done till now
command is - help(Programmer)
"""

# print(Employee.no_of_employee)
# rohan = Employee("Rohan", 22, 40000, "Developer")
# print(Employee.no_of_employee)
# harry = Employee("Harry", 22, 40000, "Hacker")
# print(Employee.no_of_employee)
# lovish = Employee.from_str("lovish-22-40000-Developer")
# print(lovish.name, lovish.age, lovish.salary, lovish.work)

# rohan.name = "Rohan"
# rohan.age = 22
# rohan.salary = 40000
# rohan.work = "Developer"
#
# harry.name = "Harry"
# harry.age = 22
# harry.salary = 40000
# harry.work = "Hacker"

# print(rohan.salary, harry.salary)

# print(harry.salary)
# harry.Increase()
# print(harry.salary)
# print(harry.__dict__)

"""
We can see all the instance variable of the class by using the argument - "print(harry.__dict__)"
"""

# print(Employee.isOpen('sunday'))
# print(Employee.isOpen('monday'))







# Tutorial no 7
# This is the OOPs tutorial on how to use dunder(maguc) methods in pythonk
"""
Double Underscore represent the dunder methods in python
They are the magical methods and we can edit them using python
"""
class Employee:
    increnment = 1.5
    no_of_employee = 0
    def __init__(self, name, age, salary, work):
        self.name = name
        self.age = age
        self.salary = salary
        self.work = work
        self.increnment = 2
        Employee.no_of_employee += 1

    def Increase(self):
        self.salary = int(self.salary * Employee.increnment)
        # self.salary = int(self.salary *  self.increnment)

    @classmethod
    def change_Increnment(cls, amount):
        cls.increnment =  amount

    @classmethod
    def from_str(cls, emp_string):
        name, age, salary, work = emp_string.split("-")
        return cls(name, age, salary, work)

    @staticmethod
    def isOpen(day):
        if day.lower() == 'sunday':
            return 'Your office is closed'
        else:
            return 'Your office is open'

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.salary}, {self.work}"

    def __str__(self):
        return "The name of worker is {}".format(self.name)


harry = Employee("Harry", 22, 40000, "Developer")
Sachin = Employee("Sachin", 20, 1100, "Hacker")

print(harry.__add__(Sachin))
print(harry)
print(repr(harry))  
print(harry)
print(str(harry))
