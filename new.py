# Tutorial no 7
# This is the OOPs tutorial on property decorator
"""

"""


class Employee:
    increnment = 1.5
    no_of_employee = 0

    def __init__(self, name, lname, age, salary, work):
        self.name = name
        self.lname = lname
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
        cls.increnment = amount

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

    @property
    def email(self):
        if self.name == None or self.lname == None:
            return "Email not set"
        else:
            return self.name + "." + self.lname + '@gmail.com'

    @email.setter
    def email(self, Email):
        list_email = Email.split('@')[0].split('.')
        self.name = list_email[0]
        self.lname = list_email[1]

    @email.deleter
    def email(self):
        self.name = None
        self.lname = None

harry = Employee("Harry", 'potter', 22, 40000, "Developer")
Sachin = Employee("Sachin", 'Dabhade', 20, 1100, "Hacker")
print(Sachin.email)
Sachin.email = "Dabhade.Sachin@gmail.com"
print(Sachin.email)
print(Sachin.name)
del Sachin.email
print(Sachin.email)